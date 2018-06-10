import math, random, sys, fileinput

inputs = fileinput.input()
# Main Class
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
				# Detects missing lead zeros
				floating_point[0] = floating_point[1]
				floating_point[1] = floating_point[2]
				floating_point[2] = char
				if floating_point[1] == '.' and floating_point[2].isdigit():
					if not floating_point[0].isdigit():
						self.print_error(line, "Missing lead zero")
						del stack[len(stack) - 1]
						print_line = False
						break

				if char in open_braces:
					stack.append(char)
				elif char in close_braces:
					# Incorrect Closing parentesis
					if not(len(stack) == 0):
						if (stack[len(stack) - 1] == "[" and char == "]") or (stack[len(stack) - 1] == "{" and char == "}"):
							del stack[len(stack) - 1]
						else:
							self.print_error(line, "Incorrect closing parentesis")
							del stack[len(stack) - 1]
							print_line = False
							break
				elif char in quotes:
					# Incorrect Quotations ' instead of "
					if char == "\'" and len(quote_queue) > 0:
						if quote_queue[len(quote_queue) - 1] == "\'":
							self.print_error(line, "Incorrect Quotation Marks")	
							print_line = False
							break
					# Nedted Quotations "string"example""
					if char == "\"" and len(quote_queue) > 2:
						if quote_queue[len(quote_queue) - 1] == "\"" and quote_queue[len(quote_queue) - 2] == "\"" and quote_queue[len(quote_queue) - 3] == "\"":
							quote_queue.append(":")
							self.print_error(line, "Nested Quotation Marks")
							print_line = False
							break

					quote_queue.append(char)
			# Print valid lines
			if print_line:
				print(line)


	# Print error message to stderr
	def print_error(self, line, error_msg):
		sys.stderr.write("------------------\nErr with line\n")
		sys.stderr.write(line)
		sys.stderr.write("\n" + error_msg + "\n------------------\n")

Main(inputs)