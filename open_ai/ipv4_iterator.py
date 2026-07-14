
DEFAULT_MASK = 2 ** 32 - 1

def convert_to_int(address):
    result = 0
    for octet in address.split("."):
        result = result * 256 + int(octet)
    return result

def convert_to_string(address):
    result = []
    for _ in range(4):
        result.append(str(address % 256))
        address //= 256
    return ".".join(result[::-1])

def next(address):
    split_addr = address.split("/")

    int_address = convert_to_int(split_addr[0])

    if len(split_addr) == 1:
        return convert_to_string(int_address + 1)

    block_size = int(split_addr[1])
    mask = (DEFAULT_MASK << (32 - block_size)) & DEFAULT_MASK

    return convert_to_string((int_address | ~mask) & DEFAULT_MASK)
    

def prev(address):
    pass


if __name__ == "__main__":
    address1 = "192.168.1.0"
    result1 = next(address1)
    assert result1 == "192.168.1.1"

    address2 = "192.168.1.0/24"
    result2 = prev(address2)
    assert result2 == "192.168.1.1" # TODO

    print("All test cases passed")



