# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import shutil


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def use_os_module():
    print(os.getuid())


def use_shutil_module():
    shutil.copyfile('./data/data.db', 'sauvegarde.db')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   use_shutil_module()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
