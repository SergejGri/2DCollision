from dataclasses import dataclass, field

@dataclass(frozen=True)
class GameConfigs:
    width: int = 1080
    height: int = 720
    fps: int = 140
    caption: str = "..."
    num_of_circles: int = 11
    rho = 0.97
    font = "Arial"
    font_size = 25