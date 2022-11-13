import ctypes
user32 = ctypes.windll.user32

DEFAULT_SCREEN_WIDTH = user32.GetSystemMetrics(0)
DEFAULT_SCREEN_HEIGHT = user32.GetSystemMetrics(1)
TITLE = "Pysar"

SPRITE_PATH = "Assets/sprites/C3/"

DEFAULT_FPS = 1/60

SPRITE_SCALING = 1
SCALE_MIN = SPRITE_SCALING / 2
SCALE_MAX = 1.5 * SPRITE_SCALING
TILE_COUNT = 40
