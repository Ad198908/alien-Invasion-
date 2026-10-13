import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("Adhanet's Game")
        self.running = True
    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
    

    



