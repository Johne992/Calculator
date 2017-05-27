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
	#Square one integer	
	def square(x):
		return x * x;
	#Multiplicative Inverse of one integer
	def multinv(x):
		return 1 / x;

	
	
	

class Engine:
	
	c = Calculator()
	
	def start(self):
		While True:
			print"\n\n\n"
			print '-'*30
			print"Welcome to Calculator.py! Select your operation. \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n"
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
			
			if not menu in range(1,8)
				print '*'*30
				print "\n\nInvalid input please enter a number between 1 & 8.\n\n"
				print '*'*30
				continue
			
			elif menu == 8:
				print "\n\n Good Bye! \n\n"
				sys.exit()
			
			elif menu in range(1,4):
				a = int(raw_input("Enter your first number: \t"))
				b = int(raw_input("Enter  your second number: \t"))
				twoint(a,b)
		
			elif:
				a = int(raw_input("Enter your first number: \t"))
				b = int(raw_input("Enter  your second number: \t"))
				oneint(a)
				
			#resume here
			
			if menu == 1:
				print "%d + %d = %d" %(a,b,c.add(a,b))
		
			elif menu == 2:
				print "%d - %d = %d" %(a,b,c.subtract(a,b))
		
			elif menu == 3:
				print "%d * %d = %d" %(a,b,c.multiply(a,b))
		
			elif menu == 4:
				print "%d / %d = %d" %(a,b,c.divide(a,b))
				
			elif menu == 5:
				print
				
			elif menu == 6: 
				print

			
	
begin = Engine()
begin.start()
