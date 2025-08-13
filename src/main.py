from config import *
from sprites import Player


class Game:
    """Main game class."""

    def __init__(self):
        init_window(WIDTH, HEIGHT, TITLE)
        self.import_assets()

        self.player = Player(self.assets["player"], Vector2(WIDTH // 2, HEIGHT // 2))

    def import_assets(self):
        self.assets = {
            "player": load_texture(join("assets", "sprites", "spaceship", "001.png"))
        }

    def run(self):
        while not window_should_close():
            dt = get_frame_time()

            self.player.update(dt)

            begin_drawing()
            clear_background(BG_COLOR)
            end_drawing()
        close_window()


if __name__ == "__main__":
    game = Game()
    game.run()
