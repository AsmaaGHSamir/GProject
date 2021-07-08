from dataclasses import dataclass

#immutable
@dataclass(frozen=True,eq=True)
class Host():
    """The Host class represent an host on the network.
    It is composed by it's name and it's addresses (IP & MAC)."""
    ip: str
    mac: str
    name: str = None
