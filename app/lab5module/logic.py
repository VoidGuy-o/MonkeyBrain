import random


# XOR function
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

    
def encrypt(message: str, rounds: int = 1, debug=False):
    # convering the str input into binary str, slicing into two halves
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    half = int(len(binary_message)/2)
    left = binary_message[:half]
    right = binary_message[half:]

    # generating the list of keys based on the rounds number
    key_list = [[str(random.getrandbits(1)) for nuphin in range(half)] for nuphin in range(rounds)]
    for i in range(rounds):
        key_list[i] = "".join(key_list[i])

    
    if debug == True:
        print(f"left_before: {left} \nright_before:{right}\n")

    # processing the rounds (that zig-zag thingy)
    for num in range(rounds):
        right_tmp = left
        left = XOR(lefts=XOR(lefts=left, rights=key_list[num]), rights=right)
        right = right_tmp

    # combining halves
    final_message = left + right
    final_message_str = ''

    # converting binary back into str of unicode chars
    for i in range(0, len(final_message), 8):
        final_message_str += chr(int(final_message[i:i+8], 2))

    if debug == True:
        print(f"left_after:  {left} \nright_after: {right}\nbinary_message_input:{binary_message}\n")
        
    return final_message_str



if __name__ == "__main__":
    print(encrypt("Hello", debug=True))