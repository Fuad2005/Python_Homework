#1)
# data = b'\xff\xfef\x00e\x00r\x00m\x00a\x00'
# print(data.decode('UTF-16'))



#2)
#??????????

# with open('hide-image.png', mode='rb+') as file:
#     b_data = file.read()
#     new_data=''
#     for el in b_data:
#         el=str(el).lstrip('0')
#         el=el.encode('utf-8')
#         new_data+=''.join(str(el))
#     new_data=reversed(new_data)
#     new_data=str(new_data).encode('utf-16')
#     file.write(new_data)



#3)

# mp4-u tapmir

# def is_jpg(b_content):
#     return b_content.startswith(b'\xFF\xD8\xFF')
# def is_mp4(b_content):
#     return b_content.startswith(b'\x66\x74\x79\x70\x69\x73\x6F\x6D')
# def is_pptx(b_content):
#     return b_content.startswith(b'\x50\x4B\x03\x04')




# f1=open('file1.unkown', mode='rb')
# f2=open('file2.unkown', mode='rb')
# f3=open('file3.unkown', mode='rb')

# for file in [f1,f2,f3]:
#     content=file.read()[:50]
#     if is_jpg(content):
#         print(file.name, 'is JPG file')
#     elif is_mp4(content):
#         print(file.name, 'is MP4 file')
#     elif is_pptx(content):
#         print(file.name, 'is PPTX file')