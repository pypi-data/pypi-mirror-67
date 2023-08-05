from dataclasses import dataclass
from typing import Iterable, Optional, List

from dacite import from_dict


@dataclass
class Why:
    expected: Optional[List[str]]
    found: Optional[str]
    missing: Optional[Iterable[str]]


@dataclass
class Message:
    where: str
    why: dict
    error_identifier: Optional[str]
    notification: Optional[str]


@dataclass
class KondutoError:
    status: str
    message: Message

    @staticmethod
    def error_from_dict(response_dict: dict):
        return from_dict(data_class=KondutoError, data=response_dict)
