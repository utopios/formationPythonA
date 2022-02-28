# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import os
import shutil


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def use_os_module():
    print(os.getuid())


def use_shutil_module():
    shutil.copyfile('./data/data.db', 'sauvegarde.db')

def use_module_glob():
    print(glob.glob("./cpp/*.cpp"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   use_module_glob()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
