import re
#1)

# names = ['Aygun Kazimova', 'fermer Həsən', 'Namiq Qaracuxurlu', 'Rehim Rehimli', 'roya Ayxan', 'Eynulla']

# for name in names:
#     correct = re.match('[A-Z].* [A-Z].*' , name)
#     if correct:
#         print(name)



#2)
#?????



#3)

# text = """Dünyada bir çox saytlar mövcuddur. Bunların bir çoxu fərqli məqsədlərə xidmət edirlər. Müsal üçün http://www.google.com saytı axtarış üçün istifadə olunur. Digər yandan https://facebook.com və http://www.instagram.com saytları sosial şəbəkə kimi fəaliyyət göstərirlər"""

# result = re.findall('[üeuioöaıə]',text)
# print(result)



#4)
#???????
# email = input('Emailinizi daxil edin: ')
# password = input('Sifrenizi daxil edin: ')

# correct_email = re.match('',email)



# phone_numbers = """051-235-642-12, 055-236-642-23, 077-623-234-26, 51-125-646-32, 50-125-542-12, 70-253-644-12, 050-135-346-64"""
# for number in phone_numbers.split(', '):
#     azercell = re.match('^050|50|51|051',number)
#     if azercell:
#         print(number)