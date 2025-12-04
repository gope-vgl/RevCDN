import json
from utils import exceptions

class ReportConfig:
    def __init__(self, hosts_path: str, credentials_path: str, report_path: str, *args, **kwargs ) -> None:
        self.hosts_path = hosts_path
        self.credentials_path = credentials_path
        self.report_path = report_path
    @staticmethod
    def load_config(json_path: str) -> ReportConfigDict:
        try:
            with open(json_path) as file:
                return json.load(file)
        except FileNotFoundError as file_error:
            raise FailedToOpenFile(path=json_path, message=file_error.strerror)
