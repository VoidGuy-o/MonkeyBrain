from tkinter import ttk, filedialog as fd
import json
import imageio.v3 as iio



def encode(message: str, BMPfilepath: str, IsTen = True, debug = False) -> any:
    if IsTen == True:
          encode_number = 10
    else:
          encode_number = 100

    # opening image file and preparing text message for encoding
    message = message.lower()
    imagebitmap_ndarray = iio.imread(BMPfilepath)
    with open(r"app\lab4module\dictionary_table.json", mode = "r", encoding = "utf-8") as dictionary_table:
        convertion_table = json.load(dictionary_table)

    # transforming text message to the array of ints (whether it is one-digit or two-digit)
    if IsTen == True:
        message_array = [convertion_table[letter] for letter in message if letter != "\n"]
        message_array = [str(letter) for letter in message_array]
        message_array = "".join(message_array)
        message_array_final = [int(symbol) for symbol in message_array]
    else:
        message_array_final = [convertion_table[letter] for letter in message if letter != "\n"]

    # modifying the pixel valuel
    letter_num = 0
    for item_a in imagebitmap_ndarray:
        if letter_num == len(message_array_final):
                        break
        for item_b in item_a:
            if letter_num == len(message_array_final):
                break
            while (item_b[0] + item_b[1] + item_b[2]) % encode_number != message_array_final[letter_num]:
                item_b[0] +=1
            letter_num += 1

    # Debug section
    if debug == True:  
        print(f"convertion table dict: {convertion_table}")
        print(f"message converted to list of ints: {message_array}")
        print(f"look: {imagebitmap_ndarray[0][0]}")
        print(message)
        print(BMPfilepath)
        print(imagebitmap_ndarray)
        print(f"image type: {type(imagebitmap_ndarray)}")
        print(f"image size/shape: {imagebitmap_ndarray.shape}")

    #Writing encoded BitMap
    iio.imwrite(r"C:\Users\voidg\Downloads\1-bmp-sample-10_ENCODED.bmp", imagebitmap_ndarray) # insert your own path/URI
    print("Encoding successful")




# To see if function works
if __name__ == "__main__":
    test_message: str = "Hello world"
    filepath: str =r"" #insert your own path/URI
    encode(test_message, filepath, debug=True)