# 1)
sentence= input('Bir cumle yazin\n>>>')
new_sentence=''
for i in sentence:
    if i!=' ':
        new_sentence+=(chr(ord(i)+1))
    else:
        new_sentence+=' '
print(new_sentence)


# 2)
sentence= input('Bir cumle yazin: ').lower()
order=''
for i in sentence:
    if i!=' ':
        order+=(str(ord(i)-96)+',')
    else:
        order+=' '
print(order)


# 3)
