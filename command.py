from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    WRITE = 1
    DISPLAY_OWN_POSTS = 2


@dataclass(frozen=True)
class Command:
    action: Action
    actor: str
    arg_dependant_on_action: str

