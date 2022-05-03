#1)
# ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']
#a
# print(ferma.index('keci'))
#b
# ferma.sort()
# print(ferma)
#c
# ferma.remove('at')
# ferma.append('toyug')
# print(ferma)
#d
# ferma.insert(0,'keci')
# print(ferma)
#e
# new_list= ferma[:len(ferma)//2]
# print(new_list)
#f
# ferma.extend(['at', 'qoyun', 'inek', 'inek', 'qoyun'])
# print(ferma)
#g
# print(ferma*3)
#h
# ferma.reverse()
# print(ferma)
#i
# cow_count=ferma.count('inek')
# print(str(((cow_count/len(ferma))*100).__round__(1))+'%')
#j
# ferma_2=ferma.copy()
# print(ferma_2)
#k
# ferma.clear()
# print(ferma)


#2)
# result = [0, 0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# counter=0
# total_neg=0
# total_pos=0
# while counter<len(numbers):
#     current_number= numbers[counter]
#     if current_number<0:
#         total_neg=total_neg+current_number
#     elif current_number>0:
#         total_pos=total_pos+current_number
#     result[1]=total_neg
#     result[0]=total_pos
#     counter+=1
# print(result)


#3)
# number_list=[*input('Number: ')]
# number_list.reverse()
# print(number_list)


#4)
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# numbers.sort()
# print('En kicik eded: '+str(numbers[1]),'En boyuk eded: '+str(numbers[-1]),sep='\n')


#5)
# r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
# counter=0
# bad_score=0
# good_score=0
# while counter<len(r):
#     current_student=r[counter]
#     if current_student<51:
#         bad_score+=1
#     elif current_student>80:
#         good_score+=1
#     counter+=1
# print('Telebe sayi: '+ str(len(r)),'Orta Bal: '+ str(sum(r)/len(r)), 'Kesilen telebelerin faizi: '+str((bad_score/len(r))*100)+'%', 'Yuksek netice gosteren telebelerin faizi: '+str((good_score/len(r))*100)+'%',sep='\n')
