
from user_model.models import CustomerUser, OtpLog
from random import shuffle, randint
from datetime import datetime
from hashlib import sha224
import math, random

def generate_token(email=''):
    try:
        alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz']
        shuffle(alpha)
        word = ''.join([a for a in alpha if randint(0,1) ==1])
        token = str(sha224(bytes(email + str(datetime.now()) + str(randint(1000,99999)) + word, 'utf-8')).hexdigest())
        return token

    except Exception as e:
        return token


def generate_otp():
    digits = "0123456789"
    OTP = str(randint(0,9))
    
    for i in range(5):
        OTP += str(digits[math.floor(random.random()*10)])
    return OTP


def send_otp_email(email):
    token = None
    otp=None
    try:
        token = generate_token(email=email)
        otp = generate_otp()
        
        create_otp_log(token = token, otp = otp, type=type, email=email)
        
        return {'token': token, 'otp': otp}
    except Exception as e:
        return {'token': token, 'otp': otp}
    
    

def create_otp_log(user=None,email=None,type=None,otp=None,token=None,contact=None):
    OtpLog.objects.filter(email=email).delete()
    otp_log = OtpLog.objects.create(
        user=user,
        email=email,
        token=token,
        type=type,
        otp=otp,
        contact=contact
    )
    return otp_log
