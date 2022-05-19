#1)
# def string_to_abriviation(*args):
#     abriviation=''
#     for word in args:
#         abriviation+=str(word[0]).upper()
#     print(abriviation)

# string_to_abriviation('birlesmis', 'milletler', 'teskilati')



#2)
# def chstr(sentence,**kwarqs):
#     for i in kwarqs:
#         sentence=str(sentence).replace(str(i),kwarqs[i])
#     print(sentence)
# chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen',sehve='sehife', orgen='oyren')



#3)
# def find_percent(old,new):
#     percentage=(new*100)/old
#     if percentage>100:
#         print('qiymet',str((percentage-100))+'%', 'artib')
#     else:
#         print('qiymet',str(percentage)+'%','azalib')


# find_percent(200,60)
# find_percent(100,150)



#4)
#?????????????????????????????????????????????
# def ascii_only(func):
#     ascii_table={
#         'ü':'u',
#         'ş':'s',
#         'ç':'c',
#         'ə':'e',
#         'ı':'i',
#         'ğ':'g',
#         'ö':'o'
#     }
#     def wrapper():
#         sentence=func()
#         for i in ascii_table:
#             sentence=str(sentence).replace(i,ascii_table[i])
#         func()
#     return wrapper
        

# @ascii_only
# def salam_ver(ad, soyad):
# 	return f'Salam hörmətli {ad} {soyad}, necəsiniz?'

# salam_ver('Arif', 'Həsənov')



#5)
# import math
# def differece(list):
#     biggest=-math.inf
#     for b_num in list:
#         if b_num>biggest:
#             biggest=b_num
#     print('Biggest:',biggest)
#     smallest=math.inf
#     for s_num in list:
#         if s_num<smallest:
#             smallest=s_num
#     print('Smallest:',smallest)
#     difference=biggest-smallest
#     print('Difference:',difference)

# differece([6, 3, 8, 9, 2])



#6)
#??????????????????????????????????????????????????
# def num_to_str(number):
#     strings={
#         '1':'bir',
#         '2':'iki',
#         '3':'uc',
#         '4':'dord',
#         '5':'bes',
#         '6':'alti',
#         '7':'yeddi',
#         '8':'sekkiz',
#         '9':'doqquz',
#     }
#     for i in str(number):
#         number=str(number).replace(i,strings[i])
        
#     print(number)
# num_to_str(365)