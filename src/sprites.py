from config import *


class Sprite:
    """Base sprite class."""

    def __init__(self, texture, pos, speed, direction):
        self.texture = texture
        self.pos = pos
        self.speed = speed
        self.direction = direction

    def update(self, dt):
        self.draw()

    def draw(self):
        draw_texture_ex(self.texture, self.pos, 0.0, 5.0, WHITE)

    def move(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt


class Player(Sprite):
    """Player sprite class."""

    def __init__(self, texture, pos):
        super().__init__(texture, pos, PLAYER_SPEED, Vector2())

    def input(self):
        self.direction.x = int(is_key_down(KEY_D)) - int(is_key_down(KEY_A))
        self.direction.y = int(is_key_down(KEY_S)) - int(is_key_down(KEY_W))
        self.direction = Vector2Normalize(self.direction)

        if is_key_pressed(KEY_SPACE):
            print("firee")

    def update(self, dt):
        self.input()
        self.move(dt)
        self.draw()
