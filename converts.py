def ascii_to_int(string: str) -> int:
    psswd_bytes = bytes(string, encoding='ASCII')
    psswd_int = int.from_bytes(psswd_bytes, byteorder='big')
    return psswd_int


def int_to_ascii(number: int) -> str:
    result = ""

    while number > 0:
        result += chr(number % 256)  # add characters from end to start
        number >>= 8  # 8 bits = 1 character

    return result[::-1]  # return the result in the correct order


def int_to_hex_string(number: int) -> str:
    result_hex = hex(number)  # turn the number into hexadecimal representation
    result = result_hex[2:]  # remove leading 0x
    return result
