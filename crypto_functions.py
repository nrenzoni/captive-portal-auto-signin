from Crypto.Cipher import AES
from subprocess import check_output

encrypt_iv = b'1' * 16


def get_uuid():
    raw_uuid_cmd = check_output('wmic csproduct get uuid')
    start_index = raw_uuid_cmd.find(b"\r\r\n") + 3
    uuid = raw_uuid_cmd[start_index:].replace(b"-", b"")[0:32]
    return uuid  # returns byte object


def encrypt(plaintext, key):
    obj = AES.new(key, AES.MODE_CFB, encrypt_iv)

    str_for_encrypt = plaintext.encode()
    return obj.encrypt(str_for_encrypt) # returns as byte string


def decrypt(byte_str, key):
    obj = AES.new(key, AES.MODE_CFB, encrypt_iv)
    x = obj.decrypt(byte_str)
    return x.decode() # decode to string