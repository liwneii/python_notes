# the first lesson

file_name = r'C:\Users\Administrator\Desktop\MySQL 1.png'
new_name = 'MySQL 2.png'
with open(file_name, 'rb') as file_obj:
    with open(new_name, 'wb') as new_obj:
        chunk = 1024 * 100

        while True:
            content = file_obj.read(chunk)
            if not content:
                break
            new_obj.write(content)

