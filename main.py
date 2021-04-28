from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import RPi.GPIO as GPIO
import time

OUTPIN = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUTPIN, GPIO.OUT) 

MORSE_CODE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'
					}

class MyGUI(QMainWindow):
	def __init__(self):
		super(MyGUI, self).__init__()
		self.setGeometry(100, 100, 200, 200)
		self.setWindowTitle("Morse Code Translator")
		self.initGUI()
		
	def initGUI(self):
		self.label1 = QtWidgets.QLabel("Enter a word", self)
		self.label1.move(70,30)
		self.label2 = QtWidgets.QLabel("(12 characters max)", self)
		self.label2.move(50,40)
		self.text = QtWidgets.QLineEdit(self)
		self.text.move(30,70)
		self.text.resize(150,20)
		self.text.text()
		self.btn = QtWidgets.QPushButton(self)
		self.btn.setText("Send")
		self.btn.move(50,100)
		self.btn.clicked.connect(self.morseCode)
		
	def flashMorse(self, letter: str):
		if letter == ".":
			GPIO.output(OUTPIN, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(OUTPIN, GPIO.LOW)
			time.sleep(0.25)
		elif letter == "-":
			GPIO.output(OUTPIN, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(OUTPIN, GPIO.LOW)
			time.sleep(0.25)
		elif letter == " ":
			time.sleep(2)
		else:
			print("letter or number was not sent in")

	
	def morseCode(self):
		string = self.text.text()
		if len([l for l in string]) > 12:
			print("string too long")
			return 0
		print(string)
		try:
			morse_array = [MORSE_CODE[x.upper()] for x in string]
			morse_string = " ".join(morse_array)
			print(morse_string)
			for y in morse_string:
				self.flashMorse(y)
				print(y)
		except KeyError:
			print('a non letter or number was entered')

			
			
def window():
	app = QApplication(sys.argv)
	win = MyGUI()
	win.show()
	sys.exit(app.exec_())
	
	
window()