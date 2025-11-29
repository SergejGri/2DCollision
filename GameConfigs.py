import sys 

class GameConfigs:
    width: int = 1600
    height: int = 1280
    background_color = (245, 245, 245)
    fps: int = 60
    sub_steps = 8
    caption: str = "..."
    num_of_circles: int = 30
    wall_bounciness = 1.0
    rho = 0.97
    font = "Arial"
    font_size = 25
    PALETTE = [
            (255, 107, 107),  # Soft Red
            (162, 155, 254),  # Soft Purple (Dracula Theme) - KORRIGIERT
            (72, 219, 251),   # Cyan
            (255, 159, 67),   # Orange
            (29, 209, 161),   # Teal / Green
            (84, 160, 255),   # Blue
            (95, 39, 205)     # Deep Purple
    ]