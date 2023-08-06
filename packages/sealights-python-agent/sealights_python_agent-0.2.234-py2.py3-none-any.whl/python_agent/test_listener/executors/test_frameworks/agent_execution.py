from python_agent.common import constants
from python_agent.test_listener.managers.agent_manager import AgentManager


class AgentExecution(object):

    def __init__(self, config_data, labid, test_stage=None, cov_report=None, per_test=True, interval=constants.INTERVAL_IN_MILLISECONDS, init_agent=True):
        self.config_data = config_data
        self.test_stage = test_stage
        self.labid = self.resolve_lab_id(labid)
        self.config_data.covReport = cov_report
        self.config_data.testStage = test_stage or constants.DEFAULT_ENV
        self.config_data.labId = self.labid
        self.config_data.workspacepath = self.config_data.additionalParams.get("workspacepath", constants.DEFAULT_WORKSPACEPATH)
        self.config_data.include = self.config_data.additionalParams.get("include")
        self.config_data.exclude = self.config_data.additionalParams.get("exclude")
        self.config_data.perTest = per_test
        self.config_data.interval = interval
        if init_agent:
            self.init_agent()

    def resolve_lab_id(self, labid):
        return labid or self.config_data.buildSessionId or self.config_data.appName or constants.DEFAULT_LAB_ID

    def init_agent(self):
        AgentManager(config_data=self.config_data)


