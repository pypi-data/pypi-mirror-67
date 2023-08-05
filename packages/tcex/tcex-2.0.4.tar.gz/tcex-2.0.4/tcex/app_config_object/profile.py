# -*- coding: utf-8 -*-
"""TcEx testing profile Class."""
import json
import logging
import os
import re
import sys
from random import randint
import math

import colorama as c

try:
    import jmespath
except ImportError:
    # jmespath is only required for local development
    pass

from .install_json import InstallJson
from .layout_json import LayoutJson
from .permutations import Permutations
from ..env_store import EnvStore
from ..utils import Utils

# autoreset colorama
c.init(autoreset=True, strip=False)


class Profile:
    """Testing Profile Class.

    Args:
        feature (str, optional): The feature name. Defaults to None.
        name ([type], optional): The filename of the profile
            in the profile.d director. Defaults to None.
    """

    def __init__(
        self,
        default_args=None,
        feature=None,
        merge_inputs=False,
        merge_outputs=False,
        name=None,
        redis_client=None,
        replace_exit_message=False,
        replace_outputs=False,
        tcex_testing_context=None,
        logger=None,
    ):
        """Initialize Class properties."""
        self._default_args = default_args or {}
        self._feature = feature
        self._name = name
        self.log = logger or logging.getLogger('profile').addHandler(logging.NullHandler())
        self.merge_inputs = merge_inputs
        self.merge_outputs = merge_outputs
        self.replace_exit_message = replace_exit_message
        self.replace_outputs = replace_outputs
        self.tcex_testing_context = tcex_testing_context

        # properties
        self._app_path = os.getcwd()
        self._data = None
        self._output_variables = None
        self._context_tracker = []
        self.env_store = EnvStore(logger=self.log)
        self.ij = InstallJson(logger=self.log)
        self.lj = LayoutJson(logger=self.log)
        self.permutations = Permutations(logger=self.log)
        self.redis_client = redis_client
        self.tc_staged_data = {}

    @property
    def _test_case_data(self):
        """Return partially parsed test case data."""
        return os.getenv('PYTEST_CURRENT_TEST').split(' ')[0].split('::')

    @property
    def _test_case_name(self):
        """Return partially parsed test case data."""
        return self._test_case_data[-1].replace('/', '-').replace('[', '-').replace(']', '')

    def add(self, profile_data=None, profile_name=None, sort_keys=True, permutation_id=None):
        """Add a profile.

        Args:
            profile_data (dict, optional): The profile data.
            profile_name (str, optional): The name of the profile.
            sort_keys (bool, optional): If True the keys will be sorted. Defaults to True.
            permutation_id (int, optional): The index of the permutation id. Defaults to None.
        """
        profile_data = profile_data or {}
        if profile_name is not None:
            # profile_name is only used for profile migrations
            self.name = profile_name

        # get input perutations when a permutation_id is passed
        input_permutations = None
        if permutation_id is not None:
            try:
                input_permutations = self.permutations.input_dict(permutation_id)
            except Exception:
                # catch any error
                print(f'{c.Fore.RED}Invalid permutation id provided.')
                sys.exit(1)

        # this should not hit since tctest also check for duplicates
        if os.path.isfile(self.filename):
            print(f'{c.Fore.RED}A profile with the name already exists.')
            sys.exit(1)

        profile = {
            'outputs': profile_data.get('outputs'),
            'stage': profile_data.get('stage', {'kvstore': {}}),
        }
        if self.ij.runtime_level.lower() in ['triggerservice', 'webhooktriggerservice']:
            profile['configs'] = [
                {
                    'trigger_id': str(randint(1000, 9999)),
                    'config': profile_data.get(
                        'inputs',
                        {
                            'optional': self.ij.params_to_args(
                                input_permutations=input_permutations,
                                required=False,
                                service_config=False,
                            ),
                            'required': self.ij.params_to_args(
                                input_permutations=input_permutations,
                                required=True,
                                service_config=False,
                            ),
                        },
                    ),
                }
            ]
        elif self.ij.runtime_level.lower() in ['organization', 'playbook']:
            profile['exit_codes'] = profile_data.get('exit_codes', [0])
            profile['exit_message'] = None
            profile['inputs'] = profile_data.get(
                'inputs',
                {
                    'optional': self.ij.params_to_args(
                        required=False, input_permutations=input_permutations
                    ),
                    'required': self.ij.params_to_args(
                        required=True, input_permutations=input_permutations
                    ),
                },
            )

        if self.ij.runtime_level.lower() == 'organization':
            profile['stage']['threatconnect'] = {}
            profile['validation_criteria'] = profile_data.get('validation_criteria', {'percent': 5})
            del profile['outputs']
        elif self.ij.runtime_level.lower() == 'triggerservice':
            profile['trigger'] = {}
        elif self.ij.runtime_level.lower() == 'webhooktriggerservice':
            profile['webhook_event'] = {
                'body': '',
                'headers': [],
                'method': 'GET',
                'query_params': [],
                'trigger_id': '',
            }

        with open(self.filename, 'w') as fh:
            json.dump(profile, fh, indent=2, sort_keys=sort_keys)

    def add_context(self, context):
        """Add a context to the context tracker for this profile.

        Args:
            context (str): The context (session_id) for this profile.
        """
        self._context_tracker.append(context)

    def clear_context(self, context):
        """Delete all context data in redis"""
        keys = self.redis_client.hkeys(context)
        if keys:
            return self.redis_client.hdel(context, *keys)
        return 0

    @property
    def context_tracker(self):
        """Return the current context trackers for Service Apps."""
        if not self._context_tracker:
            if self.tcex_testing_context:
                self._context_tracker = json.loads(
                    self.redis_client.hget(self.tcex_testing_context, '_context_tracker') or '[]'
                )
        return self._context_tracker

    @property
    def data(self):
        """Return the Data (dict) from the current profile."""
        if self._data is None:
            try:
                with open(os.path.join(self.filename), 'r') as fh:
                    profile_data = json.load(fh)

                    # replace all variable references
                    profile_data = self.replace_env_variables(profile_data)

                    # replace all staged variable
                    profile_data = self.replace_tc_variables(profile_data)

                    # set updated profile data
                    self._data = profile_data
            except OSError:
                print(f'{c.Fore.RED}Could not open profile {self.filename}.')
        self._data['name'] = self.name
        return self._data

    @data.setter
    def data(self, profile_data):
        """Set profile_data dict."""
        self._data = profile_data

    def delete(self):
        """Delete an existing profile."""
        raise NotImplementedError('The delete method is not currently implemented.')

    @property
    def directory(self):
        """Return fully qualified profile directory."""
        return os.path.join(self._app_path, 'tests', self.feature, 'profiles.d')

    @property
    def feature(self):
        """Return the current feature."""
        if self._feature is None:
            # when called in testing framework get the feature from pytest env var.
            self._feature = self._test_case_data[0].split('/')[1].replace('/', '-')
        return self._feature

    @property
    def feature_directory(self):
        """Return fully qualified feature directory."""
        return os.path.join(self._app_path, 'tests', self.feature)

    @property
    def filename(self):
        """Return profile fully qualified filename."""
        return os.path.join(self.directory, f'{self.name}.json')

    def init(self):
        """Return the Data (dict) from the current profile."""

        # replace all variable references
        profile_data = self.replace_env_variables(self.data)

        # replace all staged variable
        profile_data = self.replace_tc_variables(profile_data)

        # set update profile data
        self._data = profile_data

    def migrate(self):
        """Migrate profile to latest schema and rewrite data."""
        with open(os.path.join(self.filename), 'r+') as fh:
            profile_data = json.load(fh)

            # update all env variables to match latest pattern
            self.migrate_permutation_output_variables(profile_data)

            # update config section of profile for service Apps
            self.migrate_service_config_inputs(profile_data)

            # change for threatconnect staged data
            profile_data = self.migrate_stage_redis_name(profile_data)

            # change for threatconnect staged data
            profile_data = self.migrate_stage_threatconnect_data(profile_data)

            # update all version 1 env variables to match latest pattern
            profile_data = self.migrate_variable_pattern_env_v1(profile_data)

            # update all version 2 env variables to match latest pattern
            profile_data = self.migrate_variable_pattern_env_v2(profile_data)

            # update all tcenv variables to match latest pattern
            profile_data = self.migrate_variable_pattern_tcenv(profile_data)

            # write updated profile
            fh.seek(0)
            json.dump(profile_data, fh, indent=2, sort_keys=True)
            fh.write('\n')  # add required newline
            fh.truncate()

        return profile_data

    @staticmethod
    def migrate_permutation_output_variables(profile_data):
        """Remove permutation_output_variables field.

        Args:
            profile_data (dict): The profile data dict.

        Returns:
            dict: The updated dict.
        """
        try:
            del profile_data['permutation_output_variables']
        except KeyError:
            pass
        return profile_data

    def migrate_service_config_inputs(self, profile_data):
        """Change flat config inputs to include required/options.

        Args:
            profile_data (dict): The profile data dict.

        Returns:
            dict: The updated dict.
        """
        for configs in profile_data.get('configs', []):
            config = configs.get('config', {})

            # handle updated configs
            if config.get('optional') or config.get('required'):
                continue

            # new config schema
            config_inputs = {'optional': {}, 'required': {}}

            # iterate over defined inputs
            for k, v in config.items():
                input_data = self.ij.params_dict.get(k)
                if input_data is not None:
                    input_type = 'optional'
                    if input_data.get('required') is True:
                        input_type = 'required'

                # add value back with appropriate input type
                config_inputs[input_type][k] = v

            # overwrite flattened config
            configs['config'] = config_inputs
        return profile_data

    @staticmethod
    def migrate_stage_redis_name(profile_data):
        """Update staged redis to kvstore

        This change updates the previous value of redis with a
        more generic value of kvstore for staged data.

        Args:
            profile_data (dict): The current profile data dict.

        Returns:
            dict: The update profile dict.
        """
        if profile_data.get('stage') is None:
            return profile_data

        kvstore_data = profile_data['stage'].get('redis', None)
        if kvstore_data is not None:
            del profile_data['stage']['redis']
            profile_data['stage']['kvstore'] = kvstore_data

        return profile_data

    @staticmethod
    def migrate_stage_threatconnect_data(profile_data):
        """Update for staged threatconnect data section of profile

        This change updates the previous list to a dict with a key that
        can be reference as a variable in other sections of the profile.

        Args:
            profile_data (dict): The current profile data dict.

        Returns:
            dict: The update profile dict.
        """
        if 'stage' not in profile_data:
            return profile_data

        stage_tc = profile_data.get('stage').get('threatconnect')

        # check if profile is using old list type
        if isinstance(stage_tc, list):
            profile_data['stage']['threatconnect'] = {}

            counter = 0
            for item in stage_tc:
                profile_data['stage']['threatconnect'][f'item_{counter}'] = item
                counter += 1

        return profile_data

    @staticmethod
    def migrate_variable_pattern_env_v1(profile_data):
        """Update the profile variable to latest pattern

        Args:
            profile_data (dict): The profile data dict.

        Returns:
            dict: The updated dict.
        """
        profile = json.dumps(profile_data)

        for m in re.finditer(r'\"\$(env|envs)\.(\w+)\"', profile):
            try:
                full_match = m.group(0)
                env_type = m.group(1)
                env_key = m.group(2)

                new_variable = f'"${{{env_type}:{env_key}}}"'
                profile = profile.replace(full_match, new_variable)
            except IndexError:
                print(f'{c.Fore.YELLOW}Invalid variable found {full_match}.')
        return json.loads(profile)

    @staticmethod
    def migrate_variable_pattern_env_v2(profile_data):
        """Update the profile variable to latest pattern

        Args:
            profile_data (dict): The profile data dict.

        Returns:
            dict: The updated dict.
        """
        profile = json.dumps(profile_data)

        for m in re.finditer(r'\${(env|envs|local|remote)\.(.*?)}', profile):
            try:
                full_match = m.group(0)
                env_type = m.group(1)  # currently env, envs, local, remote
                env_key = m.group(2)

                new_variable = f'${{{env_type}:{env_key}}}'
                profile = profile.replace(full_match, new_variable)
            except IndexError:
                print(f'{c.Fore.YELLOW}Invalid variable found {full_match}.')
        return json.loads(profile)

    def migrate_variable_pattern_tcenv(self, profile_data):
        """Update the profile variable to latest pattern

        Args:
            profile_data (dict): The profile data dict.

        Returns:
            dict: The updated dict.
        """
        if 'jmespath' not in sys.modules:
            print(
                f'{c.Fore.RED}Missing jmespath module. Try '
                f'installing "pip install tcex[development]"'
            )
            sys.exit(1)

        profile = json.dumps(profile_data)

        for data in self.tc_staged_data:
            key = data.get('key')
            for m in re.finditer(r'\${tcenv\.' + str(key) + r'\.(.*?)}', profile):
                try:
                    full_match = m.group(0)
                    jmespath_expression = m.group(1)

                    new_variable = f'${{tcenv:{key}:{jmespath_expression}}}'
                    profile = profile.replace(full_match, new_variable)
                except IndexError:
                    print(f'{c.Fore.YELLOW}Invalid variable found {full_match}.')
        return json.loads(profile)

    @property
    def name(self):
        """Return partially parsed test case data."""
        if self._name is None:
            name_pattern = r'^test_[a-zA-Z0-9_]+\[(.+)\]$'
            self._name = re.search(name_pattern, self._test_case_data[-1]).group(1)
        return self._name

    @name.setter
    def name(self, name):
        """Set the profile name"""
        self._name = name

    @staticmethod
    def output_data_rule(variable, data):
        """Return the default output data for a given variable"""
        output_data = {'expected_output': data, 'op': 'eq'}
        if variable.endswith('json.raw!String'):
            output_data['exclude'] = []
            output_data['op'] = 'jeq'
            output_data['ignore_order'] = False
        elif variable.endswith('web_link!String') or variable.endswith('web_link!StringArray'):
            output_data['op'] = 'is_url'
        elif variable.endswith('.id!String') or variable.endswith('.id!StringArray'):
            output_data['op'] = 'is_number'
        elif (
            variable.endswith('date_added!String')
            or variable.endswith('date_added!StringArray')
            or variable.endswith('last_modified!String')
            or variable.endswith('last_modified!StringArray')
        ):
            output_data['op'] = 'is_date'
        elif variable.endswith('StringArray'):
            output_data['op'] = 'dd'
            output_data['ignore_order'] = False
        elif variable.endswith('TCEntity') or variable.endswith('TCEntityArray'):
            output_data['exclude'] = ['id']
            output_data['op'] = 'jeq'
            output_data['ignore_order'] = False
        return output_data

    def profile_inputs(self):
        """Return the appropriate inputs (config) for the current App type.

        Service App use config and others use inputs.

        "inputs": {
            "optional": {}
            "required": {}
        }
        """
        if self.ij.runtime_level.lower() in ['triggerservice', 'webhooktriggerservice']:
            for config_data in self.configs:
                yield config_data.get('config')
        else:
            yield self.inputs

    def replace_env_variables(self, profile_data):
        """Replace any env vars.

        Args:
            profile_data (dict): The profile data dict.

        Returns:
            dict: The updated dict.
        """
        profile = json.dumps(profile_data)

        for m in re.finditer(r'\${(env|envs|local|remote):(.*?)}', profile):
            try:
                full_match = m.group(0)
                env_type = m.group(1)  # currently env, envs, local, or remote
                env_key = m.group(2)

                env_value = self.env_store.getenv(env_key, env_type)
                if env_value is not None:
                    profile = profile.replace(full_match, env_value)
            except IndexError:
                print(f'{c.Fore.YELLOW}Could not replace variable {full_match}).')
        return json.loads(profile)

    def replace_tc_variables(self, profile_data):
        """Replace all of the TC output variables in the profile with their correct value.

        Args:
            profile_data (dict): The profile data dict.

        Returns:
            dict: The updated dict.
        """
        if 'jmespath' not in sys.modules:
            print(
                f'{c.Fore.RED}Missing jmespath module. Try '
                f'installing "pip install tcex[development]"'
            )
            sys.exit(1)

        profile = json.dumps(profile_data)

        for data in self.tc_staged_data:
            key = data.get('key')
            data_value = data.get('data')

            for m in re.finditer(r'\${tcenv:' + str(key) + r':(.*?)}', profile):
                try:
                    full_match = m.group(0)
                    jmespath_expression = m.group(1)

                    if jmespath_expression:
                        value = jmespath.search(jmespath_expression, data_value)
                        profile = profile.replace(full_match, str(value))
                except IndexError:
                    print(f'{c.Fore.YELLOW}Invalid variable found {full_match}.')
        return json.loads(profile)

    @property
    def test_directory(self):
        """Return fully qualified test directory."""
        return os.path.join(self._app_path, 'tests')

    def update_exit_message(self):
        """Update validation rules from exit_message section of profile."""
        message_tc = ''
        if os.path.isfile(self.message_tc_filename):
            with open(self.message_tc_filename, 'r') as mh:
                message_tc = mh.read()

        with open(self.filename, 'r+') as fh:
            profile_data = json.load(fh)

            if (
                profile_data.get('exit_message') is None
                or isinstance(profile_data.get('exit_message'), str)
                or self.replace_exit_message
            ):
                # update the profile
                profile_data['exit_message'] = {'expected_output': message_tc, 'op': 'eq'}

                # write updated profile
                fh.seek(0)
                json.dump(profile_data, fh, indent=2, sort_keys=True)
                fh.write('\n')  # add required newline
                fh.truncate()

    def update_outputs(self):
        """Update the validation rules for outputs section of a profile.

        By default this method will only update if the current value is null. If the
        flag --replace_outputs is passed to pytest (e.g., pytest --replace_outputs)
        the outputs will replaced regardless of their current value. If the flag
        --merge_outputs is passed to pytest (e.g., pytest --merge_outputs) any new
        outputs will be added and any outputs that are not longer valid will be
        removed.
        """
        if self.redis_client is None:
            # redis_client is only available for children of TestCasePlaybookCommon
            print(f'{c.Fore.RED}An instance of redis_client is not set.')
            sys.exit(1)

        outputs = {}
        trigger_id = None
        for context in self.context_tracker:
            # get all current keys in current context
            redis_data = self.redis_client.hgetall(context)
            trigger_id = self.redis_client.hget(context, '_trigger_id')

            # updated outputs with validation data
            self.update_outputs_variables(outputs, redis_data, trigger_id)

            # cleanup redis
            self.clear_context(context)

        if self.outputs is None or self.replace_outputs:
            # update profile if current profile is not or user specifies --replace_outputs
            with open(self.filename, 'r+') as fh:
                profile_data = json.load(fh)
                profile_data['outputs'] = outputs

                # write updated profile
                fh.seek(0)
                json.dump(profile_data, fh, indent=2, sort_keys=True)
                fh.write('\n')  # add required newline
                fh.truncate()
        elif self.merge_outputs:
            if trigger_id is not None:
                # service Apps have a different structure with id: data
                merged_outputs = {}
                for id_, data in outputs.items():
                    merged_outputs[id_] = {}
                    for key in list(data):
                        if key in self.outputs.get(id_, {}):
                            # use current profile output value if exists
                            merged_outputs[id_][key] = self.outputs[id_][key]
                        else:
                            merged_outputs[id_][key] = outputs[id_][key]
            else:
                # update playbook App profile outputs
                merged_outputs = {}
                for key in list(outputs):
                    if key in self.outputs:
                        # use current profile output value if exists
                        merged_outputs[key] = self.outputs[key]
                    else:
                        merged_outputs[key] = outputs[key]

            # update profile outputs
            with open(self.filename, 'r+') as fh:
                profile_data = json.load(fh)
                profile_data['outputs'] = merged_outputs

                # write updated profile
                fh.seek(0)
                json.dump(profile_data, fh, indent=2, sort_keys=True)
                fh.write('\n')  # add required newline
                fh.truncate()

    def update_outputs_variables(self, outputs, redis_data, trigger_id):
        """Return the outputs section of a profile.

        Args:
            outputs (dict): The dict to add outputs.
            redis_data (dict): The data from KV store for this profile.
            trigger_id (str): The current trigger_id (service Apps).
        """
        for variable in self.tc_playbook_out_variables:
            # get data from redis for current context
            data = redis_data.get(variable.encode('utf-8'))

            # validate redis variables
            if data is None:
                if 1 not in self.exit_codes:
                    # TODO: add feature in testing framework to allow writing null and
                    #       then check if variables exist instead of null value.
                    # log error for missing output data if not a fail test case (exit code of 1)
                    self.log.debug(f'[{self.name}] Missing KV store output for variable {variable}')
            else:
                data = json.loads(data.decode('utf-8'))

            # validate validation variables
            validation_data = (self.outputs or {}).get(variable)
            if trigger_id is None and validation_data is None and self.outputs:
                self.log.error(f'[{self.name}] Missing validations rule: {variable}')

            # make business rules based on data type or content
            output_data = {'expected_output': data, 'op': 'eq'}
            if 1 not in self.exit_codes:
                output_data = self.output_data_rule(variable, data)

            # get trigger id for service Apps
            if trigger_id is not None:
                if isinstance(trigger_id, bytes):
                    trigger_id = trigger_id.decode('utf-8')
                outputs.setdefault(trigger_id, {})
                outputs[trigger_id][variable] = output_data
            else:
                outputs[variable] = output_data

    def validate_required_inputs(self):
        """Update interactive menu to build profile.

        This method will also merge input is --merge_inputs is passed to pytest.
        """

        errors = []
        status = True
        updated_params = []

        # handle non-layout and layout based App appropriately
        for profile_inputs in self.profile_inputs():  # dict with optional, required nested dicts
            profile_inputs_flattened = profile_inputs.get('optional', {})
            profile_inputs_flattened.update(profile_inputs.get('required', {}))

            params = self.ij.params_dict
            if self.lj.has_layout:
                # using inputs from layout.json since they are required to be in order
                # (display field can only use inputs previously defined)
                params = {}
                for name in self.lj.params_dict:
                    # get data from install.json based on name
                    params[name] = self.ij.params_dict.get(name)

                # hidden fields will not be in layout.json so they need to be include manually
                params.update(self.ij.filter_params_dict(hidden=True))

            inputs = {}
            merged_inputs = {
                'optional': {},
                'required': {},
            }
            for name, data, in params.items():
                if data.get('serviceConfig'):
                    # inputs that are serviceConfig are not applicable for profiles
                    continue

                if not data.get('hidden'):
                    # each non hidden input will be checked for permutations if the App has layout
                    if not self.permutations.validate_input_variable(name, inputs):
                        continue

                # get the value from the current profile
                value = profile_inputs_flattened.get(name)

                input_type = 'optional'
                if data.get('required'):
                    input_type = 'required'
                    if value in [None, '']:  # accept value of 0
                        # validation step
                        errors.append(f'- Missing/Invalid value for required arg ({name})')
                        status = False

                # update inputs
                inputs[name] = value
                merged_inputs[input_type][name] = value

            updated_params.append(merged_inputs)

        if self.merge_inputs:
            # update profile outputs
            with open(self.filename, 'r+') as fh:
                profile_data = json.load(fh)
                if self.ij.runtime_level.lower() in ['triggerservice', 'webhooktriggerservice']:
                    for index, config_item in enumerate(profile_data.get('configs', [])):
                        config_item['config'] = updated_params[index]
                else:
                    profile_data['inputs'] = updated_params[0]

                # write updated profile
                fh.seek(0)
                json.dump(profile_data, fh, indent=2, sort_keys=True)
                fh.write('\n')  # add required newline
                fh.truncate()

        errors = '\n'.join(errors)  # convert error to string for assert message
        return status, f'\n{errors}'

    #
    # Properties
    #

    @property
    def args(self):
        """Return combined optional and required args."""
        args = self.inputs_optional
        args.update(self.inputs_required)
        return dict(args)

    @property
    def configs(self):
        """Return environments."""
        return list(self.data.get('configs', []))

    @property
    def environments(self):
        """Return environments."""
        return self.data.get('environments', ['build'])

    @property
    def exit_codes(self):
        """Return exit codes."""
        return self.data.get('exit_codes', [])

    @property
    def exit_message(self):
        """Return exit message dict."""
        return self.data.get('exit_message', {})

    @property
    def inputs(self):
        """Return inputs dict."""
        return self.data.get('inputs', {})

    @property
    def inputs_optional(self):
        """Return required inputs dict."""
        return self.inputs.get('optional', {})

    @property
    def inputs_required(self):
        """Return required inputs dict."""
        return self.inputs.get('required', {})

    @property
    def message_tc_filename(self):
        """Return the fqpn for message_tc file relative to profile."""
        return os.path.join(
            self._default_args.get('tc_out_path'), self.feature, self._test_case_name, 'message.tc'
        )

    @property
    def owner(self):
        """Return the owner value."""
        return (
            self.data.get('required', {}).get('owner')
            or self.data.get('optional', {}).get('owner')
            or self.data.get('owner')
        )

    @property
    def outputs(self):
        """Return outputs dict."""
        return self.data.get('outputs')

    @property
    def stage(self):
        """Return stage dict."""
        return self.data.get('stage', {})

    @property
    def stage_kvstore(self):
        """Return stage kv store dict."""
        return self.stage.get('kvstore', {})

    @property
    def stage_threatconnect(self):
        """Return stage threatconnect dict."""
        return self.stage.get('threatconnect', {})

    @property
    def tc_in_path(self):
        """Return fqpn tc_in_path arg relative to profile."""
        if self.ij.runtime_level.lower() in ['triggerservice', 'webhooktriggerservice']:
            tc_in_path = os.path.join(self._default_args.get('tc_in_path'), self.feature)
        else:
            tc_in_path = os.path.join(
                self._default_args.get('tc_in_path'), self.feature, self._test_case_name
            )
        return tc_in_path

    @property
    def tc_log_path(self):
        """Return fqpn tc_log_path arg relative to profile."""
        if self.ij.runtime_level.lower() in ['triggerservice', 'webhooktriggerservice']:
            tc_log_path = os.path.join(self._default_args.get('tc_log_path'), self.feature)
        else:
            tc_log_path = os.path.join(
                self._default_args.get('tc_log_path'), self.feature, self._test_case_name
            )
        return tc_log_path

    @property
    def tc_out_path(self):
        """Return fqpn tc_out_path arg relative to profile."""
        if self.ij.runtime_level.lower() in ['triggerservice', 'webhooktriggerservice']:
            tc_out_path = os.path.join(self._default_args.get('tc_out_path'), self.feature)
        else:
            tc_out_path = os.path.join(
                self._default_args.get('tc_out_path'), self.feature, self._test_case_name
            )
        return tc_out_path

    @property
    def tc_playbook_out_variables(self):
        """Return calculated output variables.

        * iterate over all inputs:
          * if input key has exposePlaybookKeyAs defined
          * if value a variable
            * lookup value in stage.kvstore data
            * for each key add to output variables
        """
        output_variables = self.ij.tc_playbook_out_variables
        if self.lj.has_layout:
            # if layout based App get valid outputs
            output_variables = self.ij.create_output_variables(
                self.permutations.outputs_by_inputs(self.args)
            )

        for arg, value in self.args.items():
            # get full input data from install.json
            input_data = self.ij.params_dict.get(arg, {})

            # check to see if it support dynamic output variables
            if 'exposePlaybookKeyAs' not in input_data:
                continue

            # get the output variable type from install.json input data
            variable_type = input_data.get('exposePlaybookKeyAs')

            # staged data for this dynamic input must be a KeyValueArray
            for data in self.stage_kvstore.get(value, []):
                # create a variable using key value
                variable = self.ij.create_variable(data.get('key'), variable_type, job_id=9876)
                output_variables.append(variable)

        return output_variables

    @property
    def tc_temp_path(self):
        """Return fqpn tc_temp_path arg relative to profile."""
        if self.ij.runtime_level.lower() in ['triggerservice', 'webhooktriggerservice']:
            tc_temp_path = os.path.join(self._default_args.get('tc_temp_path'), self.feature)
        else:
            tc_temp_path = os.path.join(
                self._default_args.get('tc_temp_path'), self.feature, self._test_case_name
            )
        return tc_temp_path

    @property
    def validation_criteria(self):
        """Return the validation_criteria value."""
        return self.data.get('validation_criteria', {})

    @property
    def webhook_event(self):
        """Return webhook event dict."""
        return self.data.get('webhook_event', {})


class ProfileInteractive:
    """Testing Profile Interactive Class.

    Args:
        profile (Profile): The profile object to build interactive inputs.
    """

    def __init__(self, profile):
        """Initialize Class properties."""
        self.profile = profile

        # properties
        self._inputs = {
            'optional': {},
            'required': {},
        }
        self._staging_data = {'kvstore': {}}
        self._user_defaults = None
        self.exit_codes = []
        self.input_type_map = {
            'boolean': self.present_boolean,
            'choice': self.present_choice,
            'keyvaluelist': self.present_key_value_list,
            'multichoice': self.present_multichoice,
            'string': self.present_string,
        }
        self.utils = Utils()
        self.user_defaults_filename = os.path.join('tests', '.user_defaults')

    def _default(self, data):
        """Return the best option for default."""
        if data.get('type').lower() == 'boolean':
            default = str(data.get('default', 'false')).lower()
        elif data.get('type').lower() == 'choice':
            default = 0
            valid_values = self.profile.ij.expand_valid_values(data.get('validValues', []))
            if data.get('name') == 'tc_action':
                for vv in valid_values:
                    if self.profile.feature.lower() == vv.replace(' ', '_').lower():
                        default = vv
                        break
            else:
                default = data.get('default')
        elif data.get('type').lower() == 'multichoice':
            default = data.get('default')
            if default is not None and isinstance(default, str):
                default = default.split('|')
        else:
            default = data.get('default')
            if default is None:
                default = self.user_defaults.get(data.get('name'))
        return default

    @staticmethod
    def _split_list(data):
        """Split a list in two "equal" parts."""
        half = math.ceil(len(data) / 2)
        return data[:half], data[half:]

    def add_input(self, name, data, value):
        """Add an input to inputs."""
        if data.get('required', False):
            self._inputs['required'].setdefault(name, value)
        else:
            self._inputs['optional'].setdefault(name, value)

    @staticmethod
    def choice(option_text):
        """Return the input choice string."""
        return f'{c.Fore.MAGENTA}Choice{c.Fore.RESET}{c.Style.BRIGHT}{option_text}: '

    @property
    def inputs(self):
        """Return inputs dict."""
        return self._inputs

    def present(self):
        """Present interactive menu to build profile."""

        def params_data():
            # handle non-layout and layout based App appropriately
            if self.profile.lj.has_layout:
                # using inputs from layout.json since they are required to be in order
                # (display field can only use inputs previously defined)
                for name in self.profile.lj.params_dict:
                    # get data from install.json based on name
                    data = self.profile.ij.params_dict.get(name)
                    yield name, data

                # hidden fields will not be in layout.json so they need to be include manually
                for name, data in self.profile.ij.filter_params_dict(hidden=True).items():
                    yield name, data
            else:
                for name, data in self.profile.ij.params_dict.items():
                    yield name, data

        inputs = {}
        for name, data in params_data():
            if data.get('serviceConfig'):
                # inputs that are serviceConfig are not applicable for profiles
                continue

            if not data.get('hidden'):
                # each input will be checked for permutations if the App has layout and not hidden
                if not self.profile.permutations.validate_input_variable(name, inputs):
                    continue

            # present the input
            value = self.input_type_map.get(data.get('type').lower())(name, data)

            # update inputs
            inputs[name] = value

        self.present_exit_code()

    def present_exit_code(self):
        """Provide user input for exit code."""

        self.print_header({'label': 'Exit Codes'})
        values = input(self.choice(' [0]')).strip().split(',')

        # add input
        for e in values:
            e = e or 0
            try:
                self.exit_codes.append(int(e))
            except ValueError:
                print(f'{c.Fore.RED}Please provide a integer between 0-3.')
                sys.exit(1)

        # user feedback
        self.print_feedback(self.exit_codes)

    def present_boolean(self, name, data):
        """Build a question for boolean input."""
        default = self._default(data)
        valid_values = ['true', 'false']

        option_default = 'false'
        option_text = ''
        options = []
        for v in valid_values:
            if v.lower() == default.lower():
                option_default = v
                v = f'[{v}]'
            options.append(v)
        option_text = f" {'/'.join(options)}"

        self.print_header(data)
        value = input(self.choice(option_text)).strip()
        if not value:
            value = option_default
        value = self.utils.to_bool(value)

        # user feedback
        self.print_feedback(value)

        # add input
        self.add_input(name, data, value)

        return value

    def present_choice(self, name, data):
        """Build a question for choice input."""
        default = self._default(data)
        valid_values = self.profile.ij.expand_valid_values(data.get('validValues', []))

        # default value needs to be converted to index
        option_index = 0
        if default:
            try:
                option_index = valid_values.index(default)
            except ValueError:
                # if "magic" variable (e.g., ${GROUP_TYPES}) was not expanded then use index 0.
                # there is no way to tell if the default value is be part of the expansion.
                if any([re.match(r'^\${.*}$', v) for v in valid_values]):
                    option_index = 0
                else:
                    print(
                        f'''{c.Fore.RED}Invalid value of ({default}) for {data.get('name')}, '''
                        'check that default value and validValues match in install.json.'
                    )
                    sys.exit()
        option_text = f' [{option_index}]'

        # build options list to display to the user in two columns
        options = []
        for i, v in enumerate(valid_values):
            options.append(f'{i}. {v}')

        # print header information
        self.print_header(data)

        # display options list into two columns
        left, right = self._split_list(options)
        for i, _ in enumerate(left):
            ld = left[i]
            try:
                rd = right[i]
            except IndexError:
                rd = ''
            print(f'{ld:40} {rd:40}')

        # collect user input an process accordingly
        value = input(self.choice(option_text)).strip()
        if not value:
            value = option_index
        else:
            try:
                value = int(value)
            except ValueError:
                print(f'{c.Fore.RED}Please provide a integer between 0-{len(valid_values) - 1}.')
                sys.exit(1)

        # get value from valid value index
        if valid_values:
            try:
                value = valid_values[value]
            except IndexError:
                print(
                    f'{c.Fore.RED}Invalid value of {value} provided. '
                    f'Please provide a integer between 0-{len(valid_values) - 1}'
                )
                sys.exit(1)

        # user feedback
        self.print_feedback(value)

        # add input
        self.add_input(name, data, value)

        return value

    def present_key_value_list(self, name, data):
        """Build a question for key value list input."""
        # add input
        variable = self.profile.ij.create_variable(data.get('name'), 'KeyValueArray')
        self.add_input(name, data, variable)
        self._staging_data['kvstore'].setdefault(
            variable, [{'key': 'placeholder', 'value': 'placeholder'}]
        )

        return variable

    def present_multichoice(self, name, data):
        """Build a question for choice input."""
        default = self._default(data)  # array of default values
        valid_values = self.profile.ij.expand_valid_values(data.get('validValues', []))

        # default values will be return as an array (e.g., one|two -> ['one'. 'two']).
        # using the valid values array we can look up these values to show as default in input.
        option_indexes = [0]
        if default:
            option_indexes = []
            for d in default:
                try:
                    option_indexes.append(valid_values.index(d))
                except ValueError:
                    # if "magic" variable (e.g., ${GROUP_TYPES}) was not expanded then skip value.
                    # there is no way to tell if the default value is be part of the expansion.
                    if any([re.match(r'^\${.*}$', v) for v in valid_values]):
                        continue

                    print(
                        f'''{c.Fore.RED}Invalid value of ({d}) for {data.get('name')}, check '''
                        'that default value(s) and validValues match in install.json.'
                    )
                    sys.exit()
        option_text = f''' [{','.join([str(v) for v in option_indexes])}]'''

        # build options list to display to the user in two columns
        options = []
        for i, v in enumerate(valid_values):
            options.append(f'{i}. {v}')

        # print header information
        self.print_header(data)

        # display options list into two columns
        left, right = self._split_list(options)
        for i, _ in enumerate(left):
            ld = left[i]
            try:
                rd = right[i]
            except IndexError:
                rd = ''
            print(f'{ld:40} {rd:40}')

        # collect user input an process accordingly
        value = input(self.choice(option_text)).strip()
        if not value:
            # use default values from option_index if no value is provided
            value = option_indexes
        else:
            # parse values into index position based on valid value presented to the user
            try:
                value = [int(i) for i in value.strip().split(',')]
            except ValueError:
                print(
                    f'{c.Fore.RED}Please provide one or more integers between '
                    f'0-{len(valid_values) - 1} separated by commas.'
                )
                sys.exit(1)

        # get value from valid value index
        values = []
        for index in value:
            try:
                values.append(valid_values[index])
            except IndexError:
                print(
                    f'{c.Fore.RED}Invalid value of {index} provided. '
                    f'Please provide one or more integers between 0-{len(valid_values) - 1} '
                    'separated by commas.'
                )
                sys.exit(1)

        # values stored in profile are pipe delimeted for multichoice
        delimited_values = '|'.join(values)

        # user feedback
        self.print_feedback(delimited_values)

        # add input
        self.add_input(name, data, delimited_values)

        return delimited_values

    def present_string(self, name, data):
        """Build a question for boolean input."""
        default = self._default(data)  # the default value from install.json or other

        option_text = ''
        if default is not None:
            option_text = f' [{default}]'

        self.print_header(data)
        value = input(self.choice(option_text)).strip()
        if not value:
            value = default

        feedback_value = value
        input_value = value

        # allow a null input
        if input_value == 'null':
            input_value = None
        elif input_value in ['"null"', "'null'"]:
            input_value = 'null'

        # for non-service Apps replace user input with a variable and add to staging data
        if (
            self.profile.ij.runtime_level.lower() not in ['triggerservice', 'webhooktriggerservice']
            and 'String' in data.get('playbookDataType', [])
            and not os.getenv('TCEX_NO_PROFILE_VARIABLE')
        ):  # only stage String Type
            # create variable and staging data
            variable = self.profile.ij.create_variable(data.get('name'), data.get('type'))
            self._staging_data['kvstore'].setdefault(variable, input_value)
            feedback_value = f'"{value}" - ({variable})'
            input_value = variable

        # user feedback
        self.print_feedback(feedback_value)

        # add input
        self.add_input(name, data, input_value)

        # update default
        if default is None:
            self.user_defaults[name] = value

        return value

    @staticmethod
    def print_feedback(feedback_value):
        """Print the value used."""
        print(f'Using value: {c.Fore.GREEN}{feedback_value}\n')

    @staticmethod
    def print_header(data):
        """Enrich the header with metatdata."""

        def _print_metadata(title, value):
            """Print the title and value"""
            print(f'{c.Fore.CYAN}{title!s:<22}: {c.Fore.RESET}{c.Style.BRIGHT}{value}')

        label = data.get('label', 'NO LABEL')
        print(f'\n{c.Fore.GREEN}{label}')

        # type
        _print_metadata('Type', data.get('type'))

        # note
        note = data.get('note', '')[:200]
        if note:
            _print_metadata('Note', note)

        # required
        _print_metadata('Required', str(data.get('required', False)).lower())

        # hidden
        if data.get('hidden'):
            _print_metadata('Hidden', 'true')

        # Input Types
        pbt = ','.join(data.get('playbookDataType', []))
        if pbt:
            _print_metadata('Playbook Data Types', pbt)

        vv = ','.join(data.get('validValues', []))
        if vv:
            _print_metadata('Valid Values', vv)

        print('-' * 50)

    @property
    def staging_data(self):
        """Return staging data dict."""
        return self._staging_data

    @property
    def user_defaults(self):
        """Return user defaults"""
        if self._user_defaults is None:
            self._user_defaults = {}
            if os.path.isfile(self.user_defaults_filename):
                with open(self.user_defaults_filename, 'r') as fh:
                    self._user_defaults = json.load(fh)
        return self._user_defaults
