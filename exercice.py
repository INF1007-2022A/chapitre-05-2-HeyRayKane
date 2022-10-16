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
	sous_total = round(sous_total,2)
	taxes = round(sous_total * 0.15,2)
	total = round(sous_total + taxes,2)
	bill = name
	c = len("SOUS TOTAL")+len(str(total)) + 5
	donnees = {"SOUS TOTAL": sous_total, "TAXES": taxes, "TOTAL": total}
	for a,b in donnees.items():
		bill += chr(10) + a + chr(32)*(c-len(a)-len(str(b))) + f"{b} $"
	return bill


"""def format_number(number, num_decimal_digits):
	return ""

def get_triangle(num_rows):
	return ""
"""

if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	#print(format_number(-12345.678, 2))

	#print(get_triangle(2))
	#print(get_triangle(5))
