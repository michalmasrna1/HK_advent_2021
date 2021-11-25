from converts import *

HASH_SIZE = 16  # in bytes, if changed, change PADDING size as well
PADDING = 174939381029149250539442622636417864133


def correct_size(number: int, max_size: int = HASH_SIZE) -> int:
    if number < 256 ** (max_size - 1):
        return number ^ PADDING
    if number > 256 ** max_size:
        return number % (256 ** max_size)
    return number


def my_hash(password: str) -> str:
    """
    This function creates a hash of the given string. The size of the hash is 16 bytes.
    Longer inputs are trimmed, shorter inputs are expanded with a constant. The output
    is a hexadecimal string representation of the computed hash.
    """
    psswd_int = ascii_to_int(password)
    psswd_int = correct_size(psswd_int)
    result_int = psswd_int

    while psswd_int > 0:
        psswd_int >>= 4
        result_int ^= psswd_int

    return int_to_hex_string(result_int)
