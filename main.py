from time import sleep, time
import pyautogui
from pyscreeze import Box
from Coord import Coord
import globals as g
from globals import debug

# Mirror phone and control with ScrCpy (CLI)
# scrcpy --turn-screen-off --crop=1440:2975:0:125 --max-size=720 --no-audio --keyboard=disabled

if __name__ == '__main__':
    IMG_PATH = './img/'


    print('\n=== ATOM IDLE HACK BOT ===\n')

    # Get absolute location of the window
    win_header_box: Box = pyautogui.locateOnScreen(f'{IMG_PATH}mirror-header.png', confidence=0.9)
    win_tl_coord: Coord = Coord(win_header_box.left, win_header_box.top)
    win_w_dim: int = win_header_box.width
    debug(f'Top-left coord.: {win_tl_coord}')
    debug(f'Window dim.: {win_w_dim}; ?')

    for i in range(500):

        g.START_TIME = time()

        # Create 180 atoms
        atom_spawner_coord = win_tl_coord.add(Coord(175, 705))
        pyautogui.moveTo(atom_spawner_coord.left, atom_spawner_coord.top)
        for _ in range(180):
            pyautogui.click()

        # Go into minigame
        minigame_button_coord: Coord = win_tl_coord.add(Coord(175, 640))
        pyautogui.moveTo(minigame_button_coord.left, minigame_button_coord.top)
        pyautogui.click()
        sleep(1)

        # Click on particles
        white_particle_img_path = f'{IMG_PATH}white_particle.png'
        purple_particle_img_path = f'{IMG_PATH}purple_particle.png'
        region = (win_tl_coord.left - 5, win_tl_coord.top + 365, win_w_dim + 5, 195)
        debug(f'region: {region}')

        debug('Minigame: playing start')
        while True:
            try:
                particle_loc = pyautogui.locateOnScreen(purple_particle_img_path, confidence=0.6, region=region)
                if particle_loc:
                    pyautogui.moveTo(particle_loc)
                    pyautogui.click()
            except pyautogui.ImageNotFoundException:
                try:
                    particle_loc = pyautogui.locateOnScreen(white_particle_img_path, confidence=0.6, region=region)
                    if particle_loc:
                        pyautogui.moveTo(particle_loc)
                        pyautogui.click()
                except pyautogui.ImageNotFoundException:
                    sleep(0.25)
                    debug('Exiting minigame')
                    break

        # Double gain
        bonus_button_img_path = f'{IMG_PATH}x2_button.png'
        region = (win_tl_coord.left + 60, win_tl_coord.top + 555, win_w_dim + 145-60, 640-555)

        while True:
            try:
                button_loc = pyautogui.locateOnScreen(bonus_button_img_path, confidence=0.4, region=region)
                if button_loc:
                    pyautogui.moveTo(button_loc)
                    pyautogui.click()
                    sleep(0.1)
                    break
            except pyautogui.ImageNotFoundException:
                sleep(0.01)

        # Quit minigame
        quit_button = win_tl_coord.add(Coord(180, 590))
        pyautogui.moveTo(quit_button.left, quit_button.top)
        pyautogui.click()

        # Open menu
        menu_button = win_tl_coord.add(Coord(129-97, 961-277))
        pyautogui.moveTo(menu_button.left, menu_button.top)
        pyautogui.click()

        bonus_button = win_tl_coord.add(Coord(345-97, 829-277))
        pyautogui.moveTo(bonus_button.left, bonus_button.top)
        pyautogui.click()

        quit2_button = win_tl_coord.add(Coord(431-97, 916-277))
        pyautogui.moveTo(quit2_button.left, quit2_button.top)
        pyautogui.click()

        print(f'End of loop {i} in {time() - g.START_TIME:.2f} seconds.')


    debug(f'Exec. time: {time() - g.START_TIME:.2f} seconds.')
    print('=== ;P ===')
