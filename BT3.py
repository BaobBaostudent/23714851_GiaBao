# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:39:46 2024

@author: Student
"""

a = int(input("Nhap so nguyen duong N co 2 chu so: "))

shc = a // 10
shdv = a % 10
Tong = shc + shdv
if  10 <= a <= 99:
    print("Tong cac chu so cua N la: ", Tong)
else:
    print("So khong hop le")

