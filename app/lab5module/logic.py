import random


def func(side: str, key: str):
    #side = side.replace("1", "2")
    #side = side.replace("0", "1")
    #side = side.replace("2", "0")
    list_side = list(side)
    random.shuffle(list_side)
    side = "".join(list_side)
    return side
def XOR(lefts, rights):
    result = []
    for i in range(int(len(lefts))):
        if lefts[i] == "1" and rights[i] == "1":
            result.append("0")
        elif lefts[i] == "1" and rights[i] == "0":
            result.append("1")
        elif lefts[i] == "0" and rights[i] == "1":
            result.append("1")
        elif lefts[i] == "0" and rights[i] == "0":
            result.append("0")
    return "".join(result)

    





def encrypt(message: str, rounds: int = 1):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    half = int(len(binary_message)/2)
    left = binary_message[:half]
    right = binary_message[half:]
    k = 1
    print(f"left: {left} \nright:{right}\n")
    for num in range(rounds):
        right_tmp = left
        left = XOR(lefts=func(side=left, key=k), rights=right)
        #left = func(side=left, key=k)
        right = right_tmp

    final_message = left + right
    final_message_str = ''

    for i in range(0, len(final_message), 8):
        final_message_str += chr(int(final_message[i:i+8], 2))
    return f"left: {left} \nright:{right}\nbinary_message:{binary_message}\nresulting message:{final_message_str}"
    #return len(binary_message)



if __name__ == "__main__":
    print(encrypt("Hello"))