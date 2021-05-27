from random import random
from .core import LOWER_CASE_LETTERS,\
    UPPER_CASE_LETTERS, MIXED_CASE_LETTERS,\
        DIGITS, DEFAULT_STR_LEN, \
            check_string_length, generate_random_sample


def get_alphanumeric_string(str_len):
    """
    Generates a random string containing digits along with mixed case
    letters eg. 46sjf7HGSDF0F8
    """

    str_len = check_string_length(str_len)
    return generate_random_sample(MIXED_CASE_LETTERS+DIGITS, str_len)


def get_lowercase_string(str_len):
    """
    Generates a random lower case string eg. ingvlancvhqoez
    """

    str_len = check_string_length(str_len)
    return generate_random_sample(LOWER_CASE_LETTERS, str_len)


def get_mixedcase_string(str_len):
    """
    Generates a random mixed case string eg. kdjfIASJDjfdmT
    """

    str_len = check_string_length(str_len)
    return generate_random_sample(MIXED_CASE_LETTERS, str_len)


def get_uppercase_string(str_len):
    """
    Generates a random upper case string eg. BHJBVYDFOWEKLS 
    """

    str_len = check_string_length(str_len)
    return generate_random_sample(UPPER_CASE_LETTERS, str_len)


__all__ = [
    'get_alphanumeric_string',
    'get_lowercase_string',
    'get_mixedcase_string',
    'get_uppercase_string'
]
