#This program makes a simple calculator that can add, subtract, multiply and divide

import sys
import math

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
	
	#squareroot of two integers
	def sqrt(x,y):
		pass
		
	def 	
	
	
	

class Engine(object):
	
	def start(self):
		print"\n\n\n"
		print '-'*30
		print("Welcome to Calculator.py! Select your operation. \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. End \n  ")
		menu = int(raw_input(">>>"))
		print '-'*30
		print"\n\n\n"
		if menu == 5:
			sys.exit()
	
		else:
			a = int(raw_input("Enter your first number: \t"))
			b = int(raw_input("Enter  your second number: \t"))
			c = Calculator()
			
			if menu == 1:
				print "%d + %d = %d" %(a,b,c.add(a,b))
		
			elif menu == 2:
				print "%d - %d = %d" %(a,b,c.subtract(a,b))
		
			elif menu == 3:
				print "%d * %d = %d" %(a,b,c.multiply(a,b))
		
			elif menu == 4:
				print "%d / %d = %d" %(a,b,c.divide(a,b))
			
			else:
				print '-'*10
				print "\n\nInvalid operator\n\n"
				print "-"*10
				start()
			
	
begin = Engine()
begin.start()
