import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Temporary Player Rectangle
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        # Player Movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.75
        self.jump_height = -20

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_height

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else: 
            self.direction.x = 0

        if keys[pygame.K_w]:
            self.jump()

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
        self.apply_gravity()
        