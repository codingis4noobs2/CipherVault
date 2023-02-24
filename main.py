import tkinter as tk
import string
import random
import base64

def rail_cipher():
    def encrypt(input_string: str, key: int) -> str:
        temp_grid: list[list[str]] = [[] for _ in range(key)]
        lowest = key - 1
    
        if key <= 0:
            raise ValueError("Height of grid can't be 0 or negative")
        if key == 1 or len(input_string) <= key:
            return input_string
    
        for position, character in enumerate(input_string):
            num = position % (lowest * 2)  # puts it in bounds
            num = min(num, lowest * 2 - num)  # creates zigzag pattern
            temp_grid[num].append(character)
        grid = ["".join(row) for row in temp_grid]
        output_string = "".join(grid)
    
        return output_string
    
    
    def decrypt(input_string: str, key: int) -> str:
        grid = []
        lowest = key - 1
    
        if key <= 0:
            raise ValueError("Height of grid can't be 0 or negative")
        if key == 1:
            return input_string
    
        temp_grid: list[list[str]] = [[] for _ in range(key)]  # generates template
        for position in range(len(input_string)):
            num = position % (lowest * 2)  # puts it in bounds
            num = min(num, lowest * 2 - num)  # creates zigzag pattern
            temp_grid[num].append("*")
    
        counter = 0
        for row in temp_grid:  # fills in the characters
            splice = input_string[counter : counter + len(row)]
            grid.append(list(splice))
            counter += len(row)
    
        output_string = ""  # reads as zigzag
        for position in range(len(input_string)):
            num = position % (lowest * 2)  # puts it in bounds
            num = min(num, lowest * 2 - num)  # creates zigzag pattern
            output_string += grid[num][0]
            grid[num].pop(0)
        return output_string

    input_string = 'Hello'
    key = 4
    print("Rail Cipher")
    print("Encrypted Text: f{encrypt(input_string, key)}")
    print("Decrypted Text: f{decrypt(encrypt(input_string, key), key)}")

def base32():
    def base32_encode(string: str) -> bytes:
        return base64.b32encode(string.encode("utf-8"))
    
    def base32_decode(encoded_bytes: bytes) -> str:
        return base64.b32decode(encoded_bytes).decode("utf-8")

    msg = "hello"
    print(f"Original Msg: {msg}")
    print(f"Encrypted Msg: {base32_encode(msg)}")
    print(f"Decrypted Msg: {base32_decode(base32_encode(msg))}")

def morse_code():
    MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}  
    REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
    
    
    def encrypt(message: str) -> str:
        """
        >>> encrypt("Sos!")
        '... --- ... -.-.--'
        >>> encrypt("SOS!") == encrypt("sos!")
        True
        """
        return " ".join(MORSE_CODE_DICT[char] for char in message.upper())
    
    
    def decrypt(message: str) -> str:
        """
        >>> decrypt('... --- ... -.-.--')
        'SOS!'
        """
        return "".join(REVERSE_DICT[char] for char in message.split())

    msg = "hello"
    print(f"Encrypted Text: {encrypt(msg)}")
    print(f"Decrypted Text: {decrypt(encrypt(msg))}")

def ceaser_cipher():
    def encrypt(text, key):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += char
        return result

    def decrypt(text, key):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) - key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - key - 97) % 26 + 97)
            else:
                result += char
        return result
        
    msg = "hello"
    key = 10
    print(f"Encrypted Text: {encrypt(msg, key)}")
    print(f"Decrypted Text: {decrypt(encrypt(msg, key), key)}")

def onepad_cipher():
    def encrypt(text: str) -> tuple[list[int], list[int]]:
        """Function to encrypt text using pseudo-random numbers"""
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key

    def decrypt(cipher: list[int], key: list[int]) -> str:
        """Function to decrypt text using pseudo-random numbers."""
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - (key[i]) ** 2) / key[i])
            plain.append(chr(p))
        return "".join(plain)

    msg, key = encrypt("hello")
    print(f"Encrypted Text: {msg}")
    print(f"Decrypted Text: {decrypt(msg, key)}")

def calc_gcd():
    def greatest_common_divisor(a: int, b: int) -> int:
        if a < b:
            a, b = b, a
        while a % b != 0:
            a, b = b, a % b
        return b

    a = 10
    b = 5
    print(f"GCD of {a} and {b} is {greatest_common_divisor(a, b)}")    
    
def password_generator():
    def generate_password(length):
        lowercase_chars = string.ascii_lowercase
        uppercase_chars = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation
    
        # Combine the character sets into a single string
        all_chars = lowercase_chars + uppercase_chars + digits + special_chars
    
        # Generate a password of the desired length by randomly selecting characters from the combined set
        password = ''.join(random.choice(all_chars) for i in range(length))
        return password
    l = 10
    print(f"Password Generated: {generate_password(l)}")

def password_strength():
    def password_strength_checker(password):
        if len(password) < 8:
            return "Weak"
        elif any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
            return "Strong"
        else:
            return "Medium"
    password = "Password"
    print(f"Password Strength: {password_strength_checker(password)}")

def select_op():
    print("Please choose one of the options given below")
    
root = tk.Tk()
root.title("CipherVault")

label = tk.Label(root, text="Select a function to execute:")
label.pack()

function_var = tk.StringVar()
function_var.set("")

function_options = ["Select a option", "Password Generator", "Password Strength Checker", "Rail Cipher Encrypt/Decrypt", "Morse Code Encrypt/Decrypt", "Base32 Encrypt/Decrypt", "Ceaser Cipher Encrypt/Decrypt", "Calculate GCD", "Onepad Cipher Encrypt/Decrypt"]

function_dict = {
    "Select a option": select_op,
    "Rail Cipher": rail_cipher,
    "Password Generator": password_generator,
    "Password Strength Checker": password_strength,
    "Morse Code Encrypt/Decrypt": morse_code,
    "Base32 Encrypt/Decrypt": base32,
    "Ceaser Cipher Encrypt/Decrypt": ceaser_cipher,
    "Calculate GCD": calc_gcd,
    "Onepad Cipher Encrypt/Decrypt": onepad_cipher
}

function_menu = tk.OptionMenu(root, function_var, *function_options)
function_menu.pack()

execute_button = tk.Button(root, text="Execute", command=lambda: function_dict[function_var.get()]())
execute_button.pack()

root.mainloop()
