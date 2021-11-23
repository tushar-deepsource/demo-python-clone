file_names = get_file_names()
for file_name in file_names:
    if file_name.endswith('.py'):
        print('Python file found!')
        break
else:
    print('No Python file found :(')

