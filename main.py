from time import sleep, time
import pyautogui
from pyscreeze import Box
from Coord import Coord
import globals as g
from globals import debug

# Mirror phone and control with ScrCpy (CLI)
# scrcpy --turn-screen-off --crop=1440:2975:0:125 --max-size=720 --no-audio --keyboard=disabled


def click_on_neutrino_menu(anchor_coord: Coord) -> None:
    menu_button = anchor_coord.add(Coord(3180-3118, 934-214))
    pyautogui.moveTo(menu_button.left, menu_button.top)
    pyautogui.click()
    sleep(g.WAIT_TIME)

def double_neutrino_gains(anchor_coord: Coord) -> None:
    menu_button = anchor_coord.add(Coord(3217-3118, 735-214))
    pyautogui.moveTo(menu_button.left, menu_button.top)
    pyautogui.click()
    sleep(g.WAIT_TIME)

def pick_up_accumulated_neutrinos(anchor_coord: Coord) -> None:
    menu_button = anchor_coord.add(Coord(3293-3118, 734-214))
    pyautogui.moveTo(menu_button.left, menu_button.top)
    pyautogui.click()
    sleep(g.WAIT_TIME)

def quit_neutrino_menu(anchor_coord: Coord) -> None:
    menu_button = anchor_coord.add(Coord(3445-3118, 773-214))
    pyautogui.moveTo(menu_button.left, menu_button.top)
    pyautogui.click()
    sleep(g.WAIT_TIME)

def grind_neutrinos(anchor_coord: Coord) -> None:
    click_on_neutrino_menu(anchor_coord)
    double_neutrino_gains(anchor_coord)
    pick_up_accumulated_neutrinos(anchor_coord)
    quit_neutrino_menu(anchor_coord)



def open_antimatter_upgrades_menu(anchor_coord: Coord) -> None:
    menu_button = anchor_coord.add(Coord(129-97, 961-277))
    pyautogui.moveTo(menu_button.left, menu_button.top)
    pyautogui.click()
    sleep(g.WAIT_TIME)

def raise_field_superposition_bonus(anchor_coord: Coord) -> None:
    bonus_button = anchor_coord.add(Coord(345-97, 829-277))
    pyautogui.moveTo(bonus_button.left, bonus_button.top)
    pyautogui.click()
    sleep(g.WAIT_TIME)

def quit_antimatter_upgrades_menu(anchor_coord: Coord) -> None:
    quit2_button = anchor_coord.add(Coord(431-97, 916-277))
    pyautogui.moveTo(quit2_button.left, quit2_button.top)
    pyautogui.click()
    sleep(g.WAIT_TIME)

def raise_field_superposition(anchor_coord: Coord) -> None:
    open_antimatter_upgrades_menu(anchor_coord)
    raise_field_superposition_bonus(anchor_coord)
    quit_antimatter_upgrades_menu(anchor_coord)




def create_180_atoms_manually(anchor_coord: Coord) -> None:
    atom_spawner_coord = anchor_coord.add(Coord(175, 705))
    pyautogui.moveTo(atom_spawner_coord.left, atom_spawner_coord.top)
    for _ in range(180):
        pyautogui.click()

def launch_antimatter_minigame(anchor_coord: Coord) -> None:
    minigame_button_coord: Coord = anchor_coord.add(Coord(175, 640))
    pyautogui.moveTo(minigame_button_coord.left, minigame_button_coord.top)
    pyautogui.click()
    sleep(1.5)

def try_antimatter_minigame_quick_resolution(anchor_coord: Coord) -> None:
    minigame_button_coord: Coord = anchor_coord.add(Coord(3149-3118, 428-214))
    pyautogui.moveTo(minigame_button_coord.left, minigame_button_coord.top)
    pyautogui.click()

def resolve_antimatter_minigame(img_path: str, anchor_coord: Coord, win_width: int) -> None:
    white_particle_img_path = f'{img_path}white_particle.png'
    purple_particle_img_path = f'{img_path}purple_particle.png'
    region = (anchor_coord.left - 5, anchor_coord.top + 365, win_width + 5, 195)
    debug(f'region: {region}')

    debug('Minigame: playing start')
    while True:
        try:
            particle_loc = pyautogui.locateOnScreen(purple_particle_img_path, confidence=0.5, region=region)
            if particle_loc:
                pyautogui.moveTo(particle_loc)
                pyautogui.click()
        except pyautogui.ImageNotFoundException:
            try:
                particle_loc = pyautogui.locateOnScreen(white_particle_img_path, confidence=0.5, region=region)
                if particle_loc:
                    pyautogui.moveTo(particle_loc)
                    pyautogui.click()
            except pyautogui.ImageNotFoundException:
                sleep(g.WAIT_TIME)
                debug('Exiting minigame')
                break

def double_antimatter_gains(img_path: str, anchor_coord: Coord, win_width: int) -> None:
    bonus_button_img_path = f'{img_path}x2_button.png'
    region = (anchor_coord.left + 60, anchor_coord.top + 555, win_width + 145-60, 640-555)
    while True:
        try:
            button_loc = pyautogui.locateOnScreen(bonus_button_img_path, confidence=0.4, region=region)
            if button_loc:
                pyautogui.moveTo(button_loc)
                pyautogui.click()
                sleep(g.WAIT_TIME)
                break
        except pyautogui.ImageNotFoundException:
            sleep(g.WAIT_TIME)

def pick_up_generated_antimatter(anchor_coord: Coord) -> None:
    quit_button = anchor_coord.add(Coord(180, 590))
    pyautogui.moveTo(quit_button.left, quit_button.top)
    pyautogui.click()

def grind_antimatter(img_path: str, anchor_coord: Coord, win_width: int) -> None:
    create_180_atoms_manually(anchor_coord)
    launch_antimatter_minigame(anchor_coord)
    try_antimatter_minigame_quick_resolution(anchor_coord)
    resolve_antimatter_minigame(img_path, anchor_coord, win_width)
    double_antimatter_gains(img_path, anchor_coord, win_width)
    pick_up_generated_antimatter(anchor_coord)


def seconds_to_hms(total_seconds: float) -> str:
    total_seconds = int(total_seconds)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"




if __name__ == '__main__':
    IMG_PATH = './img/'

    print('\n=== ATOM IDLE HACK BOT ===\n')
    g.START_TIME = time()

    # Get absolute location of the window
    win_header_box: Box = pyautogui.locateOnScreen(f'{IMG_PATH}mirror-header.png', confidence=0.9)
    win_tl_coord: Coord = Coord(win_header_box.left, win_header_box.top)
    win_w_dim: int = win_header_box.width
    debug(f'Top-left coord.: {win_tl_coord}')
    debug(f'Window dim.: {win_w_dim}; ?')

    print(f'LOOP {0} ({seconds_to_hms(time() - g.START_TIME)}) - Start')
    for i in range(500):
        loop_time = time()

        grind_neutrinos(win_tl_coord)
        raise_field_superposition(win_tl_coord)
        grind_antimatter(IMG_PATH, win_tl_coord, win_w_dim)

        print(f'LOOP {i} ({seconds_to_hms(time() - g.START_TIME)}) - Finished in {time() - loop_time:.2f} s.')

    debug(f'Exec. time: {seconds_to_hms(time() - g.START_TIME)}.')
    print('=== ;P ===')
