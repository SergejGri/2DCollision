from dataclasses import dataclass, field

@dataclass(frozen=True)
class GameConfigs:
    width: int = 1080
    height: int = 720
    fps: int = 140
    caption: str = "..."
    num_of_circles: int = 2