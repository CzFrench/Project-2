def encrypt(text: str, key: int) ->str:
    """
    The purpose of this function is to move the letters down in the alphabet determined how many places by the key.
    :param text: String of only alpha chars that user inputted and wants encrypted.
    :param key: The key is a int that represents how far each letter in string should move up the alphabet.
    :return: Encrypted text that has had each char in the string moved up however many letters the key was.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A' if char.isupper() else 'a') + key) % 26 + ord('A' if char.isupper() else 'a'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text: str, key: int) -> str:
    """
     The purpose of this function is to move the letters down in the alphabet determined how many places by the key.
    :param text: String of alpha chars that user inputted and wants decrypted.
    :param key: The key is an int that represent how far each letter in a string should move down the alphabet.
    :return: decrypted text that has had each char in the string moved down however many letters the key was.
    """
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A' if char.isupper() else 'a') - key) % 26 + ord('A' if char.isupper() else 'a'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


def append_to_file(filename: str, text: str):
    """
    The purpose of this function is to open the correct txt file in append mode and appends text to the txt file.
    :param filename: determines which file to append to. If decrypt radio button is selected it would move the text to decrypted.txt and vice versa.
    :param text: The text you wish to append to file so already decrypted or encrypted.
    :return:
    """
    with open(filename, 'a') as file:
        file.write(text)
