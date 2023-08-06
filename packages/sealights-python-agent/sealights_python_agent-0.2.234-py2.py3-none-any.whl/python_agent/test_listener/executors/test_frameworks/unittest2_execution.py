import logging
import os
import sys

from python_agent.test_listener.executors.test_frameworks.agent_execution import AgentExecution

if sys.version_info >= (2, 7):
    from python_agent.test_listener.integrations.unittest_helper import main as unittest_main
else:
    from python_agent.test_listener.integrations.unittest_26_helper import main as unittest_main

log = logging.getLogger(__name__)


class Unittest2AgentExecution(AgentExecution):

    def __init__(self, config_data, labid, test_stage, cov_report, per_test, interval, args):
        super(Unittest2AgentExecution, self).__init__(config_data, labid, test_stage=test_stage, cov_report=cov_report, per_test=per_test, interval=interval)
        self.args = args

    def execute(self):
        # we're appending the current working directory for customers running unittest using: "python -m unit2"
        # since running it like that adds current working directory to sys.path
        sys.path.insert(0, os.getcwd())
        unittest_main(["unit2"] + list(self.args))
