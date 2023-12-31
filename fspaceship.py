import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/friendlies/playerShip1_blue.png")
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.centerx = 300  # Initial x-position at the center of the screen
        self.rect.bottom = 600  # Initial y-position near the bottom
        self.speed = 5
        self.shoot_delay = 500  # Delay between shots (in milliseconds)
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 550:
            self.rect.x = 550

