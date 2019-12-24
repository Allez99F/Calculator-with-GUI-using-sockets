import socket		 	 
import sys
import math
import select

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 	  		 

host = socket.gethostbyname("localhost")
host = str(host)
port = int(sys.argv[1])


s.bind((host, port)) 			
s.listen(5) 			         

print("Server is up and running")

while True:
	c, addr = s.accept()
	print('Got connection from', addr)
	
	while True:		
		
				
		a=[]
		b=''
		try:
			equation=c.recv(1024).decode()
			if equation == "Q" or equation == "q" or equation == "Quit" or equation == "quit" or equation == "quit()":
				c.send("Quit".encode())
				break
			elif 'sin' in equation:
				print("You gave me the equation:", equation)
				for i in equation:
					if i.isdigit() or i=='.':
						a.append(i)
				for j in a:
					b+=j
				x = math.sin(float(b)*0.01745329)
				result = "{0:.5f}".format(x)
				result = round(float(result),5)
			elif 'cos' in equation:
				print("You gave me the equation:", equation)
				for i in equation:
					if i.isdigit() or i=='.':
						a.append(i)
				for j in a:
					b+=j
				x = math.cos(float(b)*0.01745329)
				result = "{0:.5f}".format(x)
				result = round(float(result),5)
			elif 'tan' in equation:
				print("You gave me the equation:", equation)
				for i in equation:
					if i.isdigit() or i=='.':
						a.append(i)
				for j in a:
					b+=j
				x = math.tan(float(b)*0.01745329)
				result = "{0:.5f}".format(x)
				result = round(float(result),5)
			elif 'log' in equation:
				print("You gave me the equation:", equation)
				for i in equation:
					if i.isdigit():
						a.append(i)
				for j in a:
					b+=j
				result=math.log(float(b))
			elif 'sqrt' in equation:
				print("You gave me the equation:", equation)
				for i in equation:
					if i.isdigit():
						a.append(i)
				for j in a:
					b+=j
				result = math.sqrt(float(b))

			elif 'e' in equation:
				print("You gave me the equation:", equation)
				for i in equation:
					if i.isdigit():
						a.append(i)
				for j in a:
					b+=j
				result = math.exp(float(b))


			elif 'x' in equation:
				print("You gave me the equation:", equation)
				for i in equation:
					if i.isdigit():
						a.append(i)
				for j in a:
					b+=j
				result = float(b)**2
			else:
				if len(equation)!=0:
					print("You gave me the equation:", equation)
				result = eval(equation)
			c.send(str(result).encode())
			
		except (ZeroDivisionError):
			c.send("ZeroDiv".encode())
		except (ArithmeticError):
			c.send("MathError".encode())
		except (SyntaxError):
			try :			
				c.send("SyntaxError".encode())		
			except (BrokenPipeError):
				break	
		except (NameError):
			c.send("NameError".encode())
	print("Connection Closed with Client : ",addr[0])		
	c.close() 				




