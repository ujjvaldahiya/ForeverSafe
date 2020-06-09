import random
from datetime import datetime

def generate():
    random.seed(datetime.now())
    return random.randrange(100000, 999999)