alphabet_en = {
    " ": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26

}
alphabet_en_reversed ={
    0: ' ',
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}
alphabet_ua = {
    " ": 0,
    "а": 1,
    "б": 2,
    "в": 3,
    "г": 4,
    "ґ": 5,
    "д": 6,
    "е": 7,
    "є": 8,
    "ж": 9,
    "з": 10,
    "и": 11,
    "і": 12,
    "ї": 13,
    "й": 14,
    "к": 15,
    "л": 16,
    "м": 17,
    "н": 18,
    "о": 19,
    "п": 20,
    "р": 21,
    "с": 22,
    "т": 23,
    "у": 24,
    "ф": 25,
    "х": 26,
    "ц": 27,
    "ч": 28,
    "ш": 29,
    "щ": 30,
    "ь": 31,
    "ю": 32,
    "я": 33
}
alphabet_ua_reversed = {
    0: ' ',
    1: 'а',
    2: 'б',
    3: 'в',
    4: 'г',
    5: 'ґ',
    6: 'д',
    7: 'е',
    8: 'є',
    9: 'ж',
    10: 'з',
    11: 'и',
    12: 'і',
    13: 'ї',
    14: 'й',
    15: 'к',
    16: 'л',
    17: 'м',
    18: 'н',
    19: 'о',
    20: 'п',
    21: 'р',
    22: 'с',
    23: 'т',
    24: 'у',
    25: 'ф',
    26: 'х',
    27: 'ц',
    28: 'ч',
    29: 'ш',
    30: 'щ',
    31: 'ь',
    32: 'ю',
    33: 'я'
}

def encode(text, shift=1):
    text = text.casefold()
    text = text.replace("\n", "")
    int_list = []
    alphabet = None
    alphabet_r = None

    a_size = None
    
    if text[0] in alphabet_ua:
        alphabet = alphabet_ua
        alphabet_r = alphabet_ua_reversed
        a_size = 34
    elif text[0] in alphabet_en:
        alphabet = alphabet_en
        alphabet_r = alphabet_en_reversed
        a_size = 27
    #for letter in text:
        #print(letter)
    for letter in text:
        int_list.append((alphabet[letter] + shift) % a_size)
    #print(int_list)
    for i in range(0, len(int_list)):
        int_list[i] = alphabet_r[int_list[i]]
    #print(str(int_list))
    res = "".join(int_list)
    return res

def decode(text, shift=1):
    text = text.casefold()
    text = text.replace("\n", "")
    int_list = []
    alphabet = None
    alphabet_r = None

    a_size = None
    
    if text[0] in alphabet_ua:
        alphabet = alphabet_ua
        alphabet_r = alphabet_ua_reversed
        a_size = 34
    elif text[0] in alphabet_en:
        alphabet = alphabet_en
        alphabet_r = alphabet_en_reversed
        a_size = 27
    
    #for letter in text:
        #print(letter)
    for letter in text:
        int_list.append((alphabet[letter] - shift) % a_size)
    #print(int_list)
    for i in range(0, len(int_list)):
        int_list[i] = alphabet_r[int_list[i]]
    #print(str(int_list))
    res = "".join(int_list)
    return res

if __name__ == "__main__":
    #print(display(int_=''))
    #print(display(int_='10'))
    print(int("10"))
    print(type(int("10")))
    #print(display(int_='10'))