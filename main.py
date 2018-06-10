import math, random, sys, fileinput

inputs = fileinput.input()

class Main():

	def __init__(self, inputs):	
		stack = []
		quote_queue = []
		open_braces = ["{","["]
		close_braces = ["}","]"]
		quotes = ["\'","\"",":",","]

		floating_point = ['a','b','c']

		for line in inputs:
			print_line = True
			for char in line:
				floating_point[0] = floating_point[1]
				floating_point[1] = floating_point[2]
				floating_point[2] = char
				if floating_point[1] == '.' and floating_point[2].isdigit():
					if not floating_point[0].isdigit():
						sys.stderr.write("------------------\nErr with line\n")
						sys.stderr.write(line)
						sys.stderr.write("\nMissing Lead zero\n------------------\n")
						del stack[len(stack) - 1]
						print_line = False
						break

				if char in open_braces:
					stack.append(char)
				elif char in close_braces:
					if not(len(stack) == 0):
						if (stack[len(stack) - 1] == "[" and char == "]") or (stack[len(stack) - 1] == "{" and char == "}"):
							del stack[len(stack) - 1]
						else:
							sys.stderr.write("------------------\nErr with line\n")
							sys.stderr.write(line)
							sys.stderr.write("\nIncorrect closing parentesis\n------------------\n")
							del stack[len(stack) - 1]
							print_line = False
							break
				elif char in quotes:
					if char == "\'" and len(quote_queue) > 0:
						if quote_queue[len(quote_queue) - 1] == "\'":
							sys.stderr.write("------------------\nErr with line\n")
							sys.stderr.write(line)
							sys.stderr.write("Incorrect quotation marks\n------------------\n")		
							print_line = False
							break

					if char == "\"" and len(quote_queue) > 2:
						if quote_queue[len(quote_queue) - 1] == "\"" and quote_queue[len(quote_queue) - 2] == "\"" and quote_queue[len(quote_queue) - 3] == "\"":
							sys.stderr.write("------------------\nErr with line\n")
							sys.stderr.write(line)
							sys.stderr.write(quote_queue[len(quote_queue) - 1] +" " +quote_queue[len(quote_queue) - 2] + " "+ quote_queue[len(quote_queue) - 3])
							sys.stderr.write("Nested Quotation Marks\n------------------\n")
							print_line = False
							quote_queue.append(":")
							break
					quote_queue.append(char)
			if print_line:
				print(line)


Main(inputs)