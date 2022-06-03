from math import pi
from math import factorial as f
#1)
# radius = input('Radiusu girin: ')
# print('Kure Hecmi =',3/4*pi*int(radius)**3)

# radius = input('Radiusu girin: ')
# height = input('Hundurluyu girin: ')
# print('Koni hecmi =', 1/3*pi*int(radius)**2*int(height))



#2)

# n ,r = input('iki eded girin: ').split(',')
# n = int(n)
# r = int(r)
# if n>r:
#     print('C =', f(n)/f(r)*f(n-r))
    
# else:
#     print('Birinci eded ikinci ededden kicik ola bilmez')


# n ,r = input('iki eded girin: ').split(',')
# n = int(n)
# r = int(r)
# if n>r:
#     print('P =', f(n)/f(n-r))
    
# else:
#     print('Birinci eded ikinci ededden kicik ola bilmez')





import random
#3)

# names = input('Adlari girin\n>>>').split(',')
# for i in range(len(names)):
#     print(random.choice(names))
#     input('')



#4)
# number = random.randrange(1,50)
# print('Komputer beyninde bir reqem tutb, onu tapmaga  calisin\n')
# for i in range(10,-2,-1):
#     user_num = input('Number: ')
#     user_num = int(user_num)
#     if user_num == number:
#         print('You Win')
#         break
#     elif user_num > number:
#         print('Lower')
#         if i<1:
#             print('No Attempts Left\n Correct Answer:', number)
#             break
#         else:
#             print('Attempts Left:',i,'\n')
#     elif user_num < number:
#         print('Higher')
#         if i<1:
#             print('No Attempts Left\n Correct Answer:', number)
#             break
#         else:
#             print('Attempts Left:',i,'\n')




#5)
# ticket = ''
# for i in range(15):
#     if i%5:
#         ticket+=str(random.randint(0,100))
#         ticket+=', '
#     else:
#         ticket+='\n'
#         ticket+=str(random.randint(0,100))
#         ticket+=', '

# print(ticket)


from datetime import timedelta, datetime, date, time
#6)
# hours = 5058000000/90
# print(datetime.now()+ timedelta(hours=hours))


#7)
#????????
# sentence ='Saat 17:00, 4.6.2022 tarixində dərsə gəlin'
# sent_date = 'Saat %X, %x tarixində dərsə gəlin'
# sentence_date = datetime.strptime(sentence, sent_date)
# print(sentence)



#8)
#????????