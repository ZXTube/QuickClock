import pygame
import time

pygame.font.init()

WIN = pygame.display.set_mode((0, 0))
HEIGHT = WIN.get_height()
WIDTH = WIN.get_width()

GRAY = (30, 30, 30)
CYAN = (0, 230, 230)
WIN.fill(GRAY)

DAYS = {
    '0': 'Monday',
    '1': 'Tuesday',
    '2': 'Wednesday',
    '3': 'Thursday',
    '4': 'Friday',
    '5': 'Saturday',
    '6': 'Sunday'
}


def get_time():
    gmtime = time.gmtime()
    return f'{str(gmtime.tm_hour).zfill(2)}:{str(gmtime.tm_min).zfill(2)}:{str(gmtime.tm_sec).zfill(2)}'


def main():
    clock = pygame.time.Clock()

    time_font = pygame.font.SysFont('comicsans', 150)
    time_size = time_font.render(get_time(), True, CYAN).get_size()
    time_rect = pygame.Rect(WIDTH/2 - time_size[0]/2, HEIGHT/2 - time_size[1]/2, time_size[0], time_size[1])
    time_clearer = pygame.Rect(time_rect.x - 100, time_rect.y, time_rect.width + 200, time_rect.height)

    gmtime = time.gmtime()

    date_font = pygame.font.SysFont('comicsans', 30)
    date_render = date_font.render(f'{gmtime.tm_mday}/{gmtime.tm_mon}/{gmtime.tm_year}', True, CYAN)
    date_pos = (WIDTH/2 - date_render.get_width()/2, HEIGHT - date_render.get_height() - 10)

    day_font = pygame.font.SysFont('comicsans', 20)
    day_render = day_font.render(f'{DAYS[str(gmtime.tm_wday)]}', True, CYAN)
    day_pos = (WIDTH/2 - day_render.get_width()/2, HEIGHT - day_render.get_height() - date_render.get_height() - 10)

    WIN.blit(date_render, date_pos)
    WIN.blit(day_render, day_pos)

    while True:
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        pygame.draw.rect(WIN, GRAY, time_clearer)

        WIN.blit(time_font.render(get_time(), True, CYAN), time_rect)

        pygame.display.update()


if __name__ == "__main__":
    main()
