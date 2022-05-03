#1)
# number=int(input('Number\n>>> '))
# first_number = number
# result=1
# while number>1 :
#     result=result*number
#     number=number-1
# print(str(first_number) + '! ='+ str(result))


#2)
# sentence= input('sentence\n>>> ')
# vowels='euioa'
# counter=0
# result=0
# while True:
#     letter=sentence[counter]
#     result+=(1 if letter in vowels else 0)
#     counter+=1
#     if counter==len(sentence):
#         break
# print(result)


#3)
# phone_number=input('Nomrenizi yazin\n>>>')

# is_right_prefix=phone_number.startswith('+994')
# is_all_number= phone_number[1:].isdecimal()
# is_correct_length= len(phone_number)==13
# if is_right_prefix:


#     if is_all_number:

#         if is_correct_length:
#             print('nomrenizi duz yazmisiniz')
#         else:
#             print('nomreniz cox qisadir' if len(phone_number)<13 else 'nomreniz cox uzundur')
#     else:
#         print('nomre sadece reqemlerden ibaret olmalidi')
# else:
#     print('nomre +994 ile baslamalidir')    


#4)
# a = '123456789'
# print(*a[::-1], sep=' saniye\n',end=' saniye\nVaxt Bitti!')

#5)
# number = int(input("bir reqem yazin: "))
# counter = 2
# while number!=1:
#     if not number%counter:
#         number//=counter
#         print(counter)
#     else:
#         counter+= 1
        




#6)

# number = int(input("Write number \n"))

# before = 0
# after = 1
# print(0, 1, end=' ')
# while True:
#     before, after = after, before + after
#     if after > number:
#         break
#     print(after, end =" ")