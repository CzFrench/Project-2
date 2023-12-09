from PyQt5 import QtWidgets
from caeser_cipher_gui import Ui_MainWindow
from logic import encrypt, decrypt, append_to_file
import sys

class CaesarCipherApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(CaesarCipherApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radio_encrypt.setChecked(True)

        self.ui.button_encrypt_append.clicked.connect(self.handle_append)
        self.ui.button_reset_file.clicked.connect(self.handle_reset_file)

        self.ui.radio_encrypt.clicked.connect(self.handle_radio_buttons)
        self.ui.radio_decrypt.clicked.connect(self.handle_radio_buttons)
    def handle_append(self):
        """
        This function calls either the encrypt or decrypt function according to what the user chose.
        It also raises error exceptions. If the input text isn't all letters, and if the key isn't a number
        between 1-26 these error will raised.
        This function is called by __init__

        :return:
        """

        try:
            input_text = self.ui.input_text_data.toPlainText()
            key = int(self.ui.input_line_key.text())

            if not input_text.isalpha():
                raise ValueError("Input text should only be letters!")

            if not (1 <= key <= 26):
                raise ValueError("Key should be an int between 1-26!")

            if self.ui.radio_encrypt.isChecked():
                encrypted_text = encrypt(input_text, key)
                append_to_file('encrypted.txt', f"Encrypted Text: {encrypted_text}")
                self.ui.label_output.setText(f"Encrypted Text: {encrypted_text}")
            else:
                decrypted_text = decrypt(input_text, key)
                append_to_file('decrypted.txt', f"Decrypted Text: {decrypted_text}")
                self.ui.label_output.setText(f"Decrypted Text: {decrypted_text}")
        except ValueError as e:
            self.ui.label_output.setText(f"Error: {e}")

    def handle_reset_file(self):
        """
        The purpose of this function is clear the txt file of whatever radio button is chosen.
        As well as the input fields.
        This function is called by the __init__ function when the rest button is pressed.
        :return:
        """
        filename = 'encrypted.txt' if self.ui.radio_encrypt.isChecked() else 'decrypted.txt'
        with open(filename, 'w') as file:
            file.truncate()

        self.ui.input_text_data.clear()
        self.ui.input_line_key.clear()

    def handle_radio_buttons(self):
        """
        This functions purpose is to alter the gui headers and label in accordance to which radio button is chosen.
        :return:
        """
        if self.ui.radio_decrypt.isChecked():
            self.ui.label_title.setText("Caesar Cipher Decrypter")
            self.ui.label_input_header.setText("Enter text to be decrypted:")
            self.ui.button_encrypt_append.setText("Decrypt And Append")
        else:
            self.ui.label_title.setText("Caesar Cipher Encrypter")
            self.ui.label_input_header.setText("Enter text to be encrypted:")
            self.ui.button_encrypt_append.setText("Encrypt and Append")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CaesarCipherApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()