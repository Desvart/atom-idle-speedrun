# Atom Idle Speedrun Bot

This project goal is to automate the grinding mechanism of the [Atom Idle game](https://play.google.com/store/apps/details?id=com.AG.atomMerge&hl=en).

## How it works
This scripts take control of the mouse of your computer and manipulates the front-end of the game.
Since the game is a mobile game, a virtual clone of the mobile device is done toward the computer.
Then the bot simply interacts with the virtual clone to automate the grinding mechanism.
The virtual clone is done with [ScrPy](https://scrcpy.org/) and the mouse takeover and image recognition is done with [PyAutoGui](https://pyautogui.readthedocs.io/en/latest/).

## How to setup and use?
* Install pyautogui, PIL and openCV  
```pip install pyautogui pillow opencv-python```
* Install [ScrCpy](https://scrcpy.org/)
* Enable the USB debugging on the mobile device
  * Go to your [build number location](https://developer.android.com/studio/debug/dev-options) and tap 7 times on it
  * Go to settings, `<Dev-options>` and then enable the USB debugging flag
* Plug your mobile device to a USB port of your computer
* In a terminal, launch the virtual clone (accept the notification on your device)   
`scrcpy --turn-screen-off --crop=1440:2975:0:125 --max-size=720 --no-audio --keyboard=disabled`
* Start the game manually and close the offline gain pop-up.
* Then run the script `main.py`

## Known limitations
* Only works with Android devices
* The computer cannot be used during the grinding
* Cannot be executed faster due to the game forced latency between clicks
* Only work with the resolution and crop defined in the above scrcpy command
* The device screen is off, but the computer screen has to stay on
* The computer sleeptime has to be set to "never go to sleep"