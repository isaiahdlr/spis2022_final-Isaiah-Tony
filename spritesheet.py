import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    # Spritesheet Setup
    "Self allows us to select which spritesheet we want to work with"
    "Width and Height outline the size of a single frame in that sheet"
    "Scale resizes the image and Color replaces the background of a sprite with a transparent one"
    
    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
