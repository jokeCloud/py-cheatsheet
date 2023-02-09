file = open('text.txt', mode='r', encoding=None)

file.seek(0)

file.readline()
file.readlines()

file.write()
file.writelines()


def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()  # or read()


for line in read_line(filename):
    print(line)


def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writer(text)


def append_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
