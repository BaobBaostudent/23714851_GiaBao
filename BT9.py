# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:01:52 2024

@author: Student
"""

import math 
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
bt1 = math.sqrt(a)- math.sqrt(b)
bt2 = math.pow(a, 0.25) - math.pow(b, 0.25)
bt3 = math.sqrt(a)+ math.pow(a*b, 0.25)
bt4 = math.pow(a, 0.25) + math.pow(b, 0.25)
ket_qua = (bt1/bt2) - (bt3/bt4)
print("Gia tri bieu thuc la: ", ket_qua)