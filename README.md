# CipherVault
Collection of various ciphers and other handful of tools


1. Rail Cipher
2. Morse Code
3. Password Generator
4. Password Strength Checker
5. Base32 Encoding/Decoding

## Rail Cipher
The rail cipher is a type of transposition cipher that rearranges the letters of a message to create a new, encrypted message. The function includes two sub-functions: encrypt and decrypt.

## Functions available:
```python
encrypt(input_string: str, key: int) -> str
# The encrypt function takes two parameters: input_string is the original string that will be encrypted and key is an integer that represents the number of rows in the rail cipher grid. The function returns a string that represents the encrypted message.

decrypt(input_string: str, key: int) -> str
# The decrypt function takes two parameters: input_string is the encrypted string that will be decrypted and key is an integer that represents the number of rows in the rail cipher grid. The function returns a string that represents the decrypted message.
```


## Morse Code
Morse code is a system of communication that uses a series of dots and dashes to represent letters and numbers. The function includes two sub-functions: encrypt and decrypt.
```python
encrypt(message: str) -> str
# The encrypt function takes one parameter: message is the original string that will be encrypted using Morse code. The function returns a string that represents the encrypted message.

decrypt(message: str) -> str
# The decrypt function takes one parameter: message is the Morse code message that will be decrypted. The function returns a string that represents the decrypted message.
```


## Password Generator
The password generator function generates a random password of a specified length.
```python
generate_password(length: int) -> str
# The generate_password function takes one parameter: length is an integer that represents the desired length of the password. The function returns a string that represents the generated password.
```


## Password Strength Checker
The password strength checker function checks the strength of a password based on its length and complexity.
```python
password_strength_checker(password: str) -> str
# The password_strength_checker function takes one parameter: password is the password that will be checked for strength. The function returns a string that represents the strength of the password. The possible values are "Weak", "Medium", and "Strong".
```

## Base32 Encoding/Decoding
The Base32 code is an encoding standard described in RFC 4648 in order to facilitate the transmission of binary strings via 32 characters of the ASCII table.
```python
base32_encode(string: str) -> bytes
# This base32_encode function takes one parameter: message is the original string that will be encrypted using base32.

base32_decode(encoded_bytes: bytes) -> str
# This base32_encode function takes one parameter: encrypted_message is the message that will be decrypted using base32.
```

Main Program
The main program includes calls to all four functions.
```
rail_cipher(): Calls the rail cipher function and prints the encrypted and decrypted messages.
morse_code(): Calls the Morse code function and prints the encrypted and decrypted messages.
password_generator(): Calls the password generator function and prints the generated password.
password_strength(): Calls the password strength checker function and prints the strength of a given password.
base32(): Calls the base32 function and prints the encrypted and decrypted messages.
```
