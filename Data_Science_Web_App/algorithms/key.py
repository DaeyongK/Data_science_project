import random
import string
def generate_key(length):
    dict = string.ascii_letters + string.digits
    key = ''.join((random.choice(dict) for i in range(length)))
    return key
