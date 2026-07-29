from tkinter import ttk, filedialog as fd
import imageio.v3 as iio


def encode(message: str, BMPfilepath: str) -> any:

    imagebitmap_ndarray = iio.imread(BMPfilepath)
    print(f"look: {imagebitmap_ndarray[0][0]}")
    imagebitmap_ndarray[0][0] = [0, 200, 0]
    print(f"look: {imagebitmap_ndarray[0][0]}")
    print(message)
    print(BMPfilepath)
    print(imagebitmap_ndarray)
    print(f"image type: {type(imagebitmap_ndarray)}")
    print(f"image size/shape: {imagebitmap_ndarray.shape}")
    iio.imwrite(r"", imagebitmap_ndarray) # insert your own path/URI





if __name__ == "__main__":
    test_message: str = "Hello world"
    filepath: str =r"" #insert your own path/URI
    encode(test_message, filepath)