from random import choices
import string
from typing import Dict

__author__ = "Anand Kumar Dubey"
__title__ = 'randomstringtoken'
__version__ = '0.1'

LOWER_CASE_LETTERS = string.ascii_lowercase
MIXED_CASE_LETTERS = string.ascii_letters
UPPER_CASE_LETTERS = string.ascii_uppercase
DIGITS = string.digits
DEFAULT_STR_LEN = 79
MAX_STR_LEN = 256


def check_string_length(str_len):
    """
    This function make sure that the length of the string is not too
    large.
    INPUT: String length passed by the user.
    OPERATION: Checks if the desired string length is greater than
                maximum allowed string length.
    OUTPUT: Validated string length.
    """

    if str_len > MAX_STR_LEN or str_len <=0:
        return MAX_STR_LEN
    else:
        return str_len


def get_lowercase_string(str_len=DEFAULT_STR_LEN):
    str_len = check_string_length(str_len)
    return ''.join(choices(LOWER_CASE_LETTERS, k=str_len))


def get_mixedcase_string(str_len=DEFAULT_STR_LEN):
    str_len = check_string_length(str_len)
    return ''.join(choices(MIXED_CASE_LETTERS, k=str_len))


def get_uppercase_string(str_len=DEFAULT_STR_LEN):
    str_len = check_string_length(str_len)
    return ''.join(choices(UPPER_CASE_LETTERS, k=str_len))


def get_alphanumeric_string(str_len=DEFAULT_STR_LEN):
    str_len = check_string_length(str_len)
    return ''.join(choices(UPPER_CASE_LETTERS+LOWER_CASE_LETTERS+DIGITS, k=str_len))