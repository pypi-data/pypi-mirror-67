import json
import os

from python_agent.common import constants
from python_agent.test_listener.executors.test_frameworks.agent_execution import AgentExecution


class Run(AgentExecution):
    def __init__(self, config_data, labid, cov_report, per_test, interval):
        super(Run, self).__init__(config_data, labid, cov_report=cov_report, per_test=per_test, interval=interval, init_agent=False)

    def execute(self, args):
        self.inject_bootstrap_dir_to_python_path()
        program_exe_path = self.find_program_exe_path(args)
        self.save_config_as_env_variable()
        self.run_program(program_exe_path, args)

    def inject_bootstrap_dir_to_python_path(self):
        from python_agent import __file__ as root_directory

        root_directory = os.path.dirname(root_directory)
        boot_directory = os.path.join(root_directory, 'bootstrap')

        python_path = boot_directory

        if 'PYTHONPATH' in os.environ:
            path = os.environ['PYTHONPATH'].split(os.path.pathsep)
            if boot_directory not in path:
                python_path = "%s%s%s" % (boot_directory, os.path.pathsep, os.environ['PYTHONPATH'])

        os.environ['PYTHONPATH'] = python_path

    def find_program_exe_path(self, args):
        program_exe_path = args[0]

        if not os.path.dirname(program_exe_path):
            program_search_path = os.environ.get('PATH', '').split(os.path.pathsep)
            for path in program_search_path:
                path = os.path.join(path, program_exe_path)
                if os.path.exists(path) and os.access(path, os.X_OK):
                    program_exe_path = path
                    break
        self.config_data.program = program_exe_path
        return program_exe_path

    def run_program(self, program_exe_path, args):
        os.execl(program_exe_path, *(list(args)))

    def save_config_as_env_variable(self):
        os.environ[constants.CONFIG_ENV_VARIABLE] = json.dumps(self.config_data, default=lambda m: m.__dict__)
