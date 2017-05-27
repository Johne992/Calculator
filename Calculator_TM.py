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
		try:
			a = 1 /x
		except ZeroDivisionError:
			print '*'*30
			print "\n\nInvalid input cannot divide by 0.\n\n"
			print '*'*30
			continue
		
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
				twoint(menu)
		
			elif menu in range(5,7):
				oneint(menu,a)
				
			else:
				pass
				
	def twoint(m)
		a = int(raw_input("Enter your first number: \t"))
		b = int(raw_input("Enter  your second number: \t"))
		
		if m == 1:
			print "%d + %d = %d" %(a,b,c.add(a,b))
		
		elif m == 2:
			print "%d - %d = %d" %(a,b,c.subtract(a,b))
		
		elif m == 3:
			print "%d * %d = %d" %(a,b,c.multiply(a,b))
		
		elif m == 4:
			print "%d / %d = %d" %(a,b,c.divide(a,b))
		
	def oneint(m)
		a = int(raw_input("Enter your number: \t"))
		
		if m == 5:
			print "%d ^ 2 = %d" %(a,c.square(a)) 
				
		elif m == 6:		
			print "%Square root of %d = %d" %(a,sqrt(a))
		
		else:
			print "Reciprocal of %d = %d" %(a,c.multinv(a))

			
	
begin = Engine()
begin.start()
