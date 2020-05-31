
file_name = 'test.py'
#
# file_obj = open(file_name)
#
# print(file_obj)
#
# file_read = file_obj.read()
#
# # print(file_read)
# import pprint
# file_name = 'file_st.py'
#
#
# try:
#     with open(file_name, 'r+', encoding='utf-8') as file_obj:
#         chuck = 4
#         content = ''
#         # print(type(content))
#         file_obj.write('hahahaha')
#         file_obj.write(str(123))
#
#         while True:
#             current = file_obj.readline(4)
#             pprint.pprint(current) #字符
#             content = content + current
#
#             if not current:
#                 break
# except FileNotFoundError:
#         print('file not found')


# file_name = r'C:\Users\Administrator\Desktop\1234.jpg'
# new_name = '1234.jpg'
# with open(file_name, 'rb') as file_obj:
#     with open(new_name, 'wb') as new_obj:
#         chunk = 1024 * 100
#
#         while True:
#             content = file_obj.read(chunk)
#             if not content:
#                 break
#             new_obj.write(content)

# seek() and tell()
file_name = 'file_st.py'
#
# with open(file_name, 'r') as file_obj:
#     file_obj.seek(10)
#     print(file_obj.read(5))
#     print('当前读取到', file_obj.tell())

import os
from pprint import pprint
r = os.listdir()
# r = os.getcwd()
# # os.mkdir('aaa')
# os.rmdir('aaa')


pprint(r)






























