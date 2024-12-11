### Genshin Impact 5.2 Shadow PC BSOD Bypass
### Disclaimer: This script is intended solely to enable gameplay on a Shadow PC virtual machine.
###             I do not support or endorse cheating, tampering, or violating the terms of service of any game.
###             Please be aware that using this method carries a risk of account bans or other consequences.
###             Use at your own risk. I am not responsible for any bans, penalties, or other outcomes resulting from its use.

import os
import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Please specify the game executable to run this bypass.")
        input("Press Enter to exit...")
        return

    game_executable = sys.argv[1]

    if not os.path.isfile(game_executable):
        print(f"The file {game_executable} does not exist.")
        input("Press Enter to exit...")
        return

    game_dir = os.path.dirname(os.path.abspath(game_executable))
    driver_file = os.path.join(os.path.abspath(game_dir), "HoYoKProtect.sys")
    temp_driver_file = os.path.join(os.path.abspath(game_dir),"HoYoKProtect.sys.orig")

    if not os.path.isfile(driver_file):
        print(f"Driver file {driver_file} not found in the current directory.")
        input("Press Enter to exit...")
        return

    try:
        os.rename(driver_file, temp_driver_file)
        print(f"Renamed {driver_file} to {temp_driver_file}. Launching the game...")

        subprocess.Popen([game_executable], shell=True)

        input("Press Enter when you are in the title screen...")

        print(f"Restoring {temp_driver_file} to {driver_file}...")

        os.rename(temp_driver_file, driver_file)
        print("Driver file restored.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.isfile(temp_driver_file):
            os.rename(temp_driver_file, driver_file)

if __name__ == "__main__":
    main()
