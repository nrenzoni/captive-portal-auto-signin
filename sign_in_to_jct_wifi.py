# Nechemia Renzoni, Jul 4, 2017
# written using Python 3.6
# requires requests package installed

from requests import post
from subprocess import check_output
from config import *
from time import sleep
from os import name

wifi_name = 'JCT'

print('Welcome to Auto Wifi Login Tool')

if not name == 'nt':  # checks os name
    print("this tool is designed for windows only")
    quit()

# check connected to specific wifi
# netsh is a windows only command
if not str.encode(wifi_name) in check_output("netsh wlan show interfaces"):
    input('not connected to JCT wifi...')
    quit()

# check config file exits


try:
    config_results = load_config_file()
    username = config_results['username']
    password = config_results['password']
except NoConfig as excep:
    print('First time setup initiating...')
    config_results = gen_config()
    username = config_results['username']
    password = config_results['password']
except MultipleConfig as excep:
    print('Error: make sure there is only one jct config file in ', excep.dir)
    quit()
except InvalidConfig as excep:
    print('Error: {} is not configured properly.\n'
          'Either edit file with a text editor, or delete file and run this script again'.format(excep.file))
    quit()

data = {'username': username, 'password': password}

try:
    r = post('https://captiveportal-login.jct.ac.il/auth/index.html/u', data, timeout=1)
    # print('status code: ', r.status_code)
    # when no exceptions, exit gracefully
    if r.status_code == 200:
	    print('succesfully logged in...')
	    sleep(2)
	    raise SystemExit(0)
    else:
        print('something fishy happened...')
        quit()
except Exception as e:
    print(e.args)
    quit()
