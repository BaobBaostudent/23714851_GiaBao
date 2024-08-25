# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:14:29 2024

@author: Student
"""

a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
Tong = a+b
print("Tinh tong cua hai so la: ", Tong)
Hieu = a-b
print("Tinh hieu cua hai so la: ", Hieu)
Tich = a*b
print("Tinh tich cua hai so la: ", Tich)
Thuong = a/b
LTP = round(Thuong, 2)
print("Tinh thuong cua hai so la: ", LTP)
CLD = a%b
LD = round(CLD, 2)
print("Tinh chia lay so du cua hai so la: ", LD)
CLN = a//b
print("Tinh chia lay so nguyen cua hai so la: ", CLN)