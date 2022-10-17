#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	sous_total = 0
	for i in data:
		sous_total += i[INDEX_PRICE]*i[INDEX_QUANTITY]
	sous_total = sous_total
	taxes = sous_total * 0.15
	total = sous_total + taxes
	bill = name
	donnees = {"SOUS TOTAL ": sous_total, "TAXES      ": taxes, "TOTAL      ": total}
	for a,b in donnees.items():
		bill += chr(10) + a + f"{b:>10.2f} $"
	return bill


def format_number(number, num_decimal_digits):
	b=abs(round(number, num_decimal_digits))
	a=str(b)
	nombre_f = ""
	n=0

	if (len(a)-num_decimal_digits-1)%3 == 0:
		count = 0
	elif (len(a)-num_decimal_digits-1)%3 == 1:
		count = 2
	elif (len(a)-num_decimal_digits-1)%3 == 2:
		count = 1

	for i in a:
		count+=1
		nombre_f+=i
		n+=1
		if i == ".":
			count2 = 0
			for j in str(b-int(b)):
				count2 += 1
				if count2<=2:
					continue
				if count2>2:
					nombre_f+= j
				if count2 > num_decimal_digits+1:
					break
			break
		elif count%3==0 and a[n]!= ".":
			nombre_f+=chr(32)

	if number<0:
		nombre_f = "-"+nombre_f

	return nombre_f

def get_triangle(num_rows):
	string = "+"*(2*num_rows+1)
	final_string = string
	for a in range(num_rows):
		final_string += "\n+" + chr(32)*(int((len(string)-2-(2*a+1))/2)) + "A"*(2*a+1) + chr(32)*(int((len(string)-2-(2*a+1))/2)) +  "+"
	final_string += "\n" + string
	return final_string


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
