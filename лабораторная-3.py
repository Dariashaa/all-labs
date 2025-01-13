############
def reader(file, mode):
    if mode == 'all':
        with open(file, 'r') as f:
            content = f.read()
            print(content)
    if mode == 'line':
        with open(file, "r") as f:
            for line in f:
                print(line)
    else:
        print('Выберете режим all или line')

reader('example.txt','all')

####################

def new_file(content):
    with open('user_input.txt','a+') as file:
        file.write(content + '\n')
        file.seek(0)
        print(file.read())

new_file(input('напиши текст: '))

########################3
def reader(file, mode):
    try:
        if mode == 'all':
            with open(file, 'r') as f:
                content = f.read()
                print(content)
        elif mode == 'line':
            with open(file, "r") as f:
                for line in f:
                    print(line)
        else:
            print('Выберете режим all или line')
    except FileNotFoundError:
        print('Такого файла не существует. ')


reader('exampl.txt','all')
