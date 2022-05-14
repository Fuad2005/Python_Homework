#1)
# n1= 15
# n2= 13

# print('%s + %s = %s' %(n1,n2,n1+n2)) 


#2)
# userData = [
#     {
#         'debt': 12543,
#         'payed': 341.346742,
#         'payed_percent': 0.027214122777644904,
#         'card_number': '5326-6644-1234-6432',
#         'first_name': 'Akif',
#         'last_name': 'Serifov',
#         'father_name': 'Elekber',
#     }
# ]
# print('''
# Hormetli {first_name:.1}. {father_name:.1}. {last_name} sizin {card_number:*<19.10} nomreli
# kredit kartiniza {payed:.2f} odenis edildi.
# Umumi {debt:,}AZN teskil eden borcunuzdan {payed_percent:.2%} borc silinmisdir!
# '''.format_map(userData[0]))


#3)
#???


# #4)
# animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
# farm = ['inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek']
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

# text = f"""
# Axtarilan Heyvan: {animal}
# {animal}
# Fermadaki {animal} sayi:  {farm.count(animal)}
# Diger heyvanlara olan faizi: {(farm.count(animal)/len(farm)):.2%}
# {animal} umumi qiymeti: {qiymetler[animal]*farm.count(animal)} AZN
# """

# print(text)