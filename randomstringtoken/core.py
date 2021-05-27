import string
from random import sample

LOWER_CASE_LETTERS = string.ascii_lowercase
MIXED_CASE_LETTERS = string.ascii_letters
UPPER_CASE_LETTERS = string.ascii_uppercase
DIGITS = string.digits
DEFAULT_STR_LEN = 79
MAX_STR_LEN = 512

def check_string_length(str_len:int) -> int:
    """
    This function make sure that the length of the string is not too
    large.
    """

    if str_len:
        if str_len < 1:    
            str_len = DEFAULT_STR_LEN
        elif str_len > MAX_STR_LEN:
            str_len = MAX_STR_LEN
    else:
        str_len = DEFAULT_STR_LEN
    return str_len

def generate_random_sample(token:str, str_len:int) -> str:
    """
    Generates a random string sample from the token provided
    """

    token_len = len(token)
    random_sample = ''
    if str_len > token_len:
        while (str_len > 0):
            random_sample = random_sample + ''.join(sample(token, token_len))
            str_len = str_len - token_len
        random_sample = random_sample + ''.join(sample(token, 0 - str_len))
    else:
        random_sample = ''.join(sample(token, str_len))

    return random_sample
