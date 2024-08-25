# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:27:05 2024

@author: Student
"""


dia_chi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = dia_chi.split(", ")
print("Ket qua dap an muc 1: ")
for part in sub_strings:
    print(part)
sub_strings_2 = [part.replace("P. ", "").replace("Q. ", "").replace("Tp. ", "") for part in sub_strings]
print("Ket qua dap an muc 2: ")
for part in sub_strings_2:
    print(part)


