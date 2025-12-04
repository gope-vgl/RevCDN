class FailedToOpenFile(Exception):
    """Custom error that is raised when a file fails to open"""

    def __init__(self, path: str, message: str) -> None:
        self.path = path
        self.message = message
        super().__init__(message)
