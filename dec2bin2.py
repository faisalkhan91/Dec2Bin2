#!/usr/local/bin/python3


def get_intpart(numstring):

	index = 0

	while index < len(numstring) and numstring[index] != ".":
		index += 1

	if index == 10:
		intpart = decimal[:]
	else:
		intpart = decimal[:index]
	
	return intpart


def get_fracpart(numstring):

	index = 0

	while index < len(numstring) and numstring[index] != ".":
		index += 1

	if index == 10:
		fracpart = ""
	else :
		fracpart = decimal[index+1:]

	return fracpart


def convert_intpart(intpart):

	if intpart == "":
		binint = "0"
	else :
		binint = ""
		intpart = int(intpart)
	
		while intpart != 0:
			if intpart % 2 == 0:
				binint = "0" + binint
			else :
				binint = "1" + binint
			intpart //= 2

	return binint


def convert_fracpart(fracpart):

	if fracpart == "":
		fracint = "0"
	else :
		fracint = ""
		fracpart = float(fracpart) / 10 ** len(fracpart)
	
		while fracpart != 0:
			if fracpart * 2 >= 1:
				fracint += "1"
			else:
				fracint += "0"
	
			fracpart = fracpart * 2 - int(fracpart * 2)

	return fracint


decimal = input("Please enter a real number: ")

intpart = get_intpart(decimal)
fracpart = get_fracpart(decimal)
binint = convert_intpart(intpart)
fracint = convert_fracpart(fracpart)

print(decimal, "is equivalent to", binint + "." + fracint)
