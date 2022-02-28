# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import http.client
import imaplib
import os
import re
import shutil
import sys
import time


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

def use_http_client_web(host):
    connection = http.client.HTTPConnection(host,80)
    return connection

def read_mail_from_imap_server(email, password):
    mail_box = imaplib.IMAP4("smtp.utopios.net")
    mail_box.login(email,password)
    mail_box.select('inbox')
    status, data = mail_box.search(None, 'ALL')

def use_timer_module():
    #print(time.perf_counter())
    start = time.perf_counter()
    # le temps pour afficher le 'hello world'
    print("hello world")
    end = time.perf_counter()
    print(f"le temps de l'action est {end-start:0.10f} secondes")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    use_timer_module()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
