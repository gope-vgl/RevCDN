import json
from exceptions import FailedToOpenFile

def json_load(path: str) -> dict[str, str]:
    try:
        with open(path) as file:
            return json.load(file)
    except FileNotFound as file_error:
        raise FailedToOpenFile(path=path, message=file_error.strerror)
    except json.JSONDecodeError as decode_error:
        raise FailedToOpenFile(path=path, message=decode_error.msg)
