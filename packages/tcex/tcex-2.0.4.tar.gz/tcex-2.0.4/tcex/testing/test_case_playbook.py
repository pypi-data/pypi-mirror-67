# -*- coding: utf-8 -*-
"""TcEx Playbook Test Case module"""
import sys
import traceback

from .test_case_playbook_common import TestCasePlaybookCommon


class TestCasePlaybook(TestCasePlaybookCommon):
    """Playbook TestCase Class"""

    def run(self, args):  # pylint: disable=too-many-return-statements
        """Run the Playbook App.

        Args:
            args (dict): The App CLI args.

        Returns:
            [type]: [description]
        """
        # add requested output variables
        args['tc_playbook_out_variables'] = self.profile.tc_playbook_out_variables

        # safely log all args to tests.log
        self._log_args(args)

        # get a configured instance of the App
        self.app = self.app_init(args)

        # Setup
        exit_code = self.run_app_method(self.app, 'setup')
        if exit_code != 0:
            return exit_code

        # Run
        try:
            if hasattr(self.app.args, 'tc_action') and self.app.args.tc_action is not None:
                tc_action = self.app.args.tc_action
                tc_action_formatted = tc_action.lower().replace(' ', '_')
                tc_action_map = 'tc_action_map'
                if hasattr(self.app, tc_action):
                    getattr(self.app, tc_action)()
                elif hasattr(self.app, tc_action_formatted):
                    getattr(self.app, tc_action_formatted)()
                elif hasattr(self.app, tc_action_map):
                    self.app.tc_action_map.get(
                        self.app.args.tc_action
                    )()  # pylint: disable=no-member
                else:
                    self.log.data(
                        'run',
                        'App failed',
                        f'Action method ({self.app.args.tc_action}) was not found',
                        'error',
                    )
                    self._exit(1)
            else:
                self.app.run()
        except SystemExit as e:
            if e.code != 0 and self.profile and e.code not in self.profile.exit_codes:
                self.log.data(
                    'run', 'App failed', f'App exited with code of {e.code} in method run', 'error'
                )
            return self._exit(e.code)
        except Exception:
            self.log.data(
                'run',
                'App failed',
                f'App encountered except in run() method ({traceback.format_exc()})',
                'error',
            )
            return self._exit(1)

        # Write Output
        exit_code = self.run_app_method(self.app, 'write_output')
        if exit_code != 0:
            return exit_code

        # call write output
        self.app.tcex.playbook.write_output()

        # Teardown
        exit_code = self.run_app_method(self.app, 'teardown')
        if exit_code != 0:
            return exit_code

        try:
            # call exit for message_tc output, but don't exit
            self.app.tcex.playbook.exit(msg=self.app.exit_message)
        except SystemExit:
            pass

        return self._exit(self.app.tcex.exit_code)

    def run_profile(self):
        """Run an App using the profile name."""
        # backup sys.argv
        sys_argv_orig = sys.argv

        # clear sys.argv
        sys.argv = sys.argv[:1]

        # run the App
        exit_code = self.run(self.profile.args)

        # add context for populating output variables
        self.profile.add_context(self.context)

        # restore sys.argv
        sys.argv = sys_argv_orig

        return exit_code

    def setup_method(self):
        """Run before each test method runs."""
        super().setup_method()
        self.stager.redis.from_dict(self.redis_staging_data)

        self.redis_client = self.tcex.redis_client
