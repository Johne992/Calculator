#This program makes a simple calculator that can add, subtract, multiply and divide

import sys
from math import sqrt

class Calculator:
	
	def __init__(self):
		pass
	
	#Adds two numbers
	def add(self,x, y):
		return x + y;
	
	#Subtract two integers
	def subtract(self,x, y):
		return x - y;
	
	#multiply two integers
	def multiply(self,x, y):
		return x * y;
	
	#Divide two integers
	def divide(self,x, y):
		return x / y;
	#Square one integer	
	def square(self,x):
		return x * x;
	#Multiplicative Inverse of one integer
	def multinv(self,x):
		try:
			a = 1 /x
		except ZeroDivisionError:
			print '*'*30
			print "\n\nInvalid input cannot divide by 0.\n\n"
			print '*'*30
		
		return 1 / x;

	
	
	

class Engine:
	
	
	def twoint(self,m):
		a = int(raw_input("Enter your first number: \t"))
		b = int(raw_input("Enter  your second number: \t"))
		c = Calculator()
	
		if m == 1:
			print "%d + %d = %d" %(a,b,c.add(a,b))
		
		elif m == 2:
			print "%d - %d = %d" %(a,b,c.subtract(a,b))
		
		elif m == 3:
			print "%d * %d = %d" %(a,b,c.multiply(a,b))
		
		elif m == 4:
			print "%d / %d = %d" %(a,b,c.divide(a,b))
		
	def oneint(self,m):
		a = int(raw_input("Enter your number: \t"))
		c = Calculator()
	
		if m == 5:
			print "%d ^ 2 = %d" %(a,c.square(a)) 
				
		elif m == 6:		
			print "Square root of %d = %d" %(a,sqrt(a))
		
		else:
			print "Reciprocal of %d = %d" %(a,c.multinv(a))
	
	
	def start(self):
		while True:
			print"\n\n\n"
			print '-'*30
			print"Welcome to Calculator.py! Select your operation. \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide"
			print" 5. Square \n 6. Squareroot \n 7. Reciprocal \n 8. End \n"
			
			try:
				menu = int(raw_input(">>>"))
			except ValueError:
				print '*'*30
				print "\n\nInvalid input please enter a number between 1 & 8.\n\n"
				print '*'*30
				continue
				
			print '-'*30
			print"\n\n\n"
			
			if menu < 1 or 8 < menu:
				print '*'*30
				print "\n\nInvalid input please enter a number between 1 & 1000.\n\n"
				print '*'*30
				continue
			
			elif menu == 8:
				print "\n\n Good Bye! \n\n"
				sys.exit()
			
			elif  1 <= menu <= 4:
				self.twoint(menu)
		
			elif 5 <= menu <= 7:
				self.oneint(menu)
				
			else:
				pass
				


			
	
begin = Engine()
begin.start()
