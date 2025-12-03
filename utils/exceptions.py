class InvalidArguments(Exception):
    """Custom error that is raised when passed system arguments do not match requested parameters"""

    def __init__(self, inv_args: list[str], message: str) -> None:
        self.inv_args: list[str] = inv_args
        self.message = message
        super().__init__(message)


class FailedToOpenFile(Exception):
    """Custom error that is raised when a file fails to open"""

    def __init__(self, path: str, message: str) -> None:
        self.path = path
        self.message = message
        super().__init__(message)


class FailedToLoadData(Exception):
    """Custom error that is raised when a configuration path is not found or incorrect"""

    def __init__(self, path: str, message: str) -> None:
        self.path = path
        self.message = message
        super().__init__(message)
