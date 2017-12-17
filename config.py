import xml.etree.cElementTree as ET
from xml.dom import minidom
from getpass import getpass
from os import listdir, getcwd
import re
from exceptions import *
from crypto_functions import *



def gen_config():
    root = ET.Element('JCT_Wifi_Login')
    tree_username = ET.SubElement(root, 'username')
    tree_password = ET.SubElement(root, 'password')

    while True:
        username = input("enter username: ")
        password = getpass()
        if username and password:
            break
        else:
            print('username and password cannot not be empty')

    # encrypt username & password
    key = get_uuid()
    encrypted_uname = encrypt(username, key)
    encrypted_pass = encrypt(password, key)

    tree_username.text = str(encrypted_uname)
    tree_password.text = str(encrypted_pass)

    # tree = ET.ElementTree(root)
    # tree.write('jct_wifi_login.config')

    reparsed = minidom.parseString(ET.tostring(root, 'utf-8'))

    with open('jct_wifi_login.config', 'w') as f:
        pass
        f.write(reparsed.toprettyxml())

    return {'username': username, 'password': password}


def load_config_file():
    """
    returns dict of username and password if both file exists and data exists.
    throws exception if username or password is blank or tags don't exists
    throws exception if config file not found (or more than 1 in current directory)
    """
    current_dir_files = listdir()
    pattern = re.compile(r".*config")
    config_files = list(filter(pattern.match, current_dir_files))
    config_file_l = [str for str in config_files if 'jct' in str]

    if len(config_file_l) > 1:
        raise MultipleConfig(getcwd())
    elif len(config_file_l) == 0:
        raise NoConfig()
    # 1 jct config file
    else:
        config = config_file_l[0]
        tree = ET.parse(config)
        root = tree.getroot()
        # check 2 child elements, password and username, and each is not empty
        if len(root) != 2 or not root[0].text or not root[1].text:
            raise InvalidConfig(config)
        else:
            encrypted_uname = (root[0].text)[2:-2].encode() # cuts off b'' then encodes as byte string
            encrypted_pass = (root[1].text)[2:-2].encode()

            # decrypt username & password
            key = get_uuid()
            username = decrypt(encrypted_uname, key)
            password = decrypt(encrypted_pass, key)

            return {'username': username, 'password': password}

