from tkinter import ttk, filedialog as fd
import json
import imageio.v3 as iio



def encode(message: str, BMPfilepath: str) -> any:
    message = message.lower()
    imagebitmap_ndarray = iio.imread(BMPfilepath)
    with open(r"app\lab4module\dictionary_table.json", mode = "r", encoding = "utf-8") as dictionary_table:
        convertion_table = json.load(dictionary_table)
    message_array = [convertion_table[letter] for letter in message if letter != "\n"]
    message_array = [str(letter) for letter in message_array]
    message_array = "".join(message_array)
    message_array_final = [int(symbol) for symbol in message_array]

    letter_num = 0
    for item_a in imagebitmap_ndarray:
        if letter_num == len(message_array):
                        break
        for item_b in item_a:
            if letter_num == len(message_array):
                break
            while (item_b[0] + item_b[1] + item_b[2]) % 10 != message_array_final[letter_num]:
                item_b[0] +=1
            letter_num += 1










    print(f"convertion table dict: {convertion_table}")
    print(f"message converted to list of ints: {message_array}")
    print(f"look: {imagebitmap_ndarray[0][0]}")
    print(f"look: {imagebitmap_ndarray[0][0]}")
    print(message)
    print(BMPfilepath)
    print(imagebitmap_ndarray)
    print(f"image type: {type(imagebitmap_ndarray)}")
    print(f"image size/shape: {imagebitmap_ndarray.shape}")
    iio.imwrite(r"C:\Users\voidg\Downloads\1-bmp-sample-7_ENCODED.bmp", imagebitmap_ndarray) # insert your own path/URI





if __name__ == "__main__":
    test_message: str = "Hello world"
    filepath: str =r"C:\Users\voidg\Downloads\1-bmp-sample-2.bmp" #insert your own path/URI
    encode(test_message, filepath)