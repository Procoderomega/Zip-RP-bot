import random
from Configs import bot_config

MIN = int(bot_config["Economy"]["MIN_GAIN"])
MAX = int(bot_config["Economy"]["MAX_GAIN"])

def random_earnings(min_amount=MIN, max_amount=MAX):
    return random.randint(min_amount, max_amount)
