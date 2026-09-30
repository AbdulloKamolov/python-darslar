# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:51:30 2026

@author: user
"""

# car = {'model':'nexia3', 'rang':'oq'}
# print(car['model'])
# print(car['rang'])
# eng_uz = {'apple':'olma', 'apricot':'o‘rik', 'banana':'banan'}
# mevalar = {'olma':10000, 'o‘rik':5000, 'banan':6000}
# print(f"Olma narhi {mevalar['olma']} so‘m ekan")
# print('eng_uz')
# talaba = {'ismi':'Abduillo', 'yoshi':20, 'tug‘ilgan yili':1997}
# print(f"{talaba['ismi'].title()},\
#       {talaba['yoshi']}-yilda tug‘ilgan,\
#       {talaba['tug‘ilgan yili']} yoshda")
# talaba['kurs'] = 4
# talaba['fakultet'] = 'informatika'
# talaba['ismi'] = 'Abdulloh'
# talaba_1 = {}
# talaba_1['ism'] = "abdullo"
# talaba_1['kurs'] = 1
# talaba_1['yoshi'] = 30
# # print(talaba_1)
# # print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# del talaba_1['ism']
telefonlar = {
    'ali':"NOT10",
    'abdullo':'honorx',
    'shagzod':'Iphone',
    'fayzullo':'S3'
    }
phone = telefonlar.get('ali', "Bunday ism mavjud emas")
print(phone)


