# Monkeybrain

## What is this

A little project that was based on my uni assignments from the 3rd year cryptography course.
## What it does

Basically this is 6 parts (5 because 6 was dropped) slapped together and with simple GUI added. The following modules are:

1. Caesar Cipher (en/ua alphabets only)
2. Transposition Cipher
3. Frequency Analysis. Comparing distribution, presense of double and tripple letter combinations.
4.  Steganography on BMP files using my own flavour of RGB-based LSB steganography (made up at 2 AM).
5. Feistel Network. Simple implementation with some XOR.
### MAIN Packages/libs

- Plotly - basic charts generation for module 3
- ImageIO - basic BMP file manipulation for module 4
- NumPy - some ndarray utilisation for ImageIO in module 4 (not explicitly used)
The rest of dependencies (mosly indirect) are all stated in requirements.txt

## How to install
### Executable
There should be a release for the latest version which contains **main** executable. Although it's linux only. I'll probably setup some kind of actions to automate building and attaching executable assets
### Through code editor/IDE (For development)
1) clone the repo

```git clone https://github.com/VoidGuy-o/MonkeyBrain```

2) install dependencies

```pip install -r requirements.txt```

3) run the file

```python main.py```