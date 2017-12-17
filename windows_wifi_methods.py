from subprocess import check_output


def get_ssid_name():
    interface_info = check_output("netsh wlan show interfaces")
    
