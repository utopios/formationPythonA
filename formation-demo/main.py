# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import os
import re
import shutil
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def use_os_module():
    print(os.getuid())


def use_shutil_module():
    shutil.copyfile('./data/data.db', 'sauvegarde.db')


def use_module_glob():
    print(glob.glob("./cpp/*.cpp"))


def use_module_sys():
    print(sys.argv)
    sys.stderr.write('Warning possible error\n')


def use_module_regex_find_in():
    print(re.findall(r'\bf[a-z]*', 'wich foot or hand fell fastest'))


def use_module_regex_search(regex, chaine):
    m = re.search(regex, chaine)
    return m.group(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(use_module_regex_search(r'(?<=-)\w+', 'element-test'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
