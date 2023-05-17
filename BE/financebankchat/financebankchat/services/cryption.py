from datetime import  timedelta
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
import base64
from Crypto.Cipher import PKCS1_OAEP
from django.utils.timezone import datetime


def sign_message(a_message, privatekey):
    digest = SHA256.new()
    digest.update(a_message.encode("utf-8"))
    privatekey = PKCS1_v1_5.new(privatekey)
    sign = base64.b64encode(privatekey.sign(digest))
    return sign

def verify_sign(a_message, signature, publickey):
    digest = SHA256.new()
    digest.update(a_message.encode("utf-8"))
    publickey = PKCS1_v1_5.new(publickey)
    return publickey.verify(digest, base64.b64decode(signature))

def decrypt_message(a_message, privatekey):
    rsa = RSA.importKey(privatekey)
    cipher = PKCS1_OAEP.new(rsa)
    return cipher.decrypt(a_message).decode()

def encrypt_message(a_message, public_key):
    rsa = RSA.importKey(public_key)
    cipher = PKCS1_OAEP.new(rsa)
    return cipher.encrypt(a_message)
    
def generate_keys():
    modulus_length = 2048
    privatekey = RSA.generate(modulus_length)
    publickey = privatekey.publickey()
    return privatekey, publickey


def get_token(minutes=10):
    privatekey, publickey = generate_keys()
    expired_time = datetime.now() + timedelta(minutes=minutes)
    return publickey.export_key().decode(), privatekey.export_key().decode() , expired_time