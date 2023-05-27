import subprocess
from time import sleep
import sys


def install_wifi_driver():
    print("After Installing Your Machine is Going to REBOOT")
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", f"linux-image-{subprocess.check_output(['uname', '-r']).decode().strip().split('-')[0]}", f"linux-headers-{subprocess.check_output(['uname', '-r']).decode().strip().split('-')[0]}", "broadcom-sta-dkms"])
    subprocess.run(["modprobe", "-r", "b44", "b43", "b43legacy", "ssb", "brcmsmac", "bcma"])
    subprocess.run(["modprobe", "wl"])

    # Check if system was updated
    if not is_updated() or not any_changes_made():
        return

    reboot_system()

def show_commands():
    print("apt-get update")
    kernel_version = subprocess.check_output(['uname', '-r']).decode().strip().split('-')[0]
    print(f"apt-get install linux-image-{kernel_version} linux-headers-{kernel_version} broadcom-sta-dkms")
    print("modprobe -r b44 b43 b43legacy ssb brcmsmac bcma")
    print("modprobe wl")

def is_updated():
    process = subprocess.run(["apt-get", "upgrade", "--dry-run"], capture_output=True, text=True)
    return "The following packages will be upgraded" in process.stdout

def any_changes_made():
    process = subprocess.run(["apt-get", "autoremove", "--dry-run"], capture_output=True, text=True)
    return "The following packages will be REMOVED" in process.stdout

def reboot_system():
    subprocess.run(["reboot"])

def main():
    print("""
    #######################################################
    #############################


#   __          __  _    __   _             __   _        
#   \ \        / / (_)  / _| (_)           / _| (_)       
#    \ \  /\  / /   _  | |_   _           | |_   _  __  __
#     \ \/  \/ /   | | |  _| | |          |  _| | | \ \/ /
#      \  /\  /    | | | |   | |          | |   | |  >  < 
#       \/  \/     |_| |_|   |_|          |_|   |_| /_/\_\


     Installer Version 2023
     Created By Alva
    #######################################################
    ############################
    """)

    while True:
        print("Please enter your choice:")
        print("1. Install Wifi Driver")
        print("2. Show Commands")
        print("3. Quit")
        choice = input("Choice: ")

        if choice == "1":
            install_wifi_driver()
            break
        elif choice == "2":
            show_commands()
        elif choice == "3":
            print("Thanks for Using")
            sys.exit(0)
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

