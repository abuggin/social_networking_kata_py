from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    action: str
    actor: str
    arg_dependant_on_action: str
