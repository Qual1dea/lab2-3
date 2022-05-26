import time

buffer_len = 1
max_len = 100
number, digit = "", ""
index_count = 0
index, sequence_num, digits_num = [], [], []
start = time.time()

try:
    with open("text.txt", "r") as file:
        buffer = file.read(buffer_len)                                 # читаем первый блок
        while buffer:
            while (buffer < '0' or buffer > '9') and buffer:
                buffer = file.read(buffer_len)                         # читаем очередной блок
            if not buffer:
                print("\nФайл в директории проекта пустой или его нет")
            while ('0' <= buffer <= '9' or buffer in ' .,' or buffer < '0' or buffer > '9') and buffer:
                if '0' <= buffer <= '9' or buffer == '.' or buffer == ',':
                    if len(number) != 0 and (buffer == '.' or buffer == ','):
                        number += buffer
                    elif '0' <= buffer <= '9':
                        number += buffer
                else:
                    if number.find('.') != -1 and number.find('.') == len(number) - 1:
                        number.replace('.', '')
                    if len(number) > 0:
                        number += ' '
                    digit += number
                    number = ""
                buffer = file.read(buffer_len)                          # читаем очередной блок
                if len(number) == max_len:
                    print("Последовательность слишком длинная, измените файл.")
                    break
        text = digit.split()
        for value in text:
            digits_num.append(len(str(value).replace('.', '').replace('-', '')))
            sequence_num.append(value)
            index.append(index_count)                            # подсчёт номера символа, с которого начинается число
            index_count = index_count + len(str(value).replace('.', ' ')) + 1
        for x in range(len(text))[::-1]:
            if not (x % 2 and not float(text[x].replace(',', '.')) % 2):
                del (text[x], sequence_num[x], index[x], digits_num[x])
        if len(text) > 0:
            for i in range(len(text)):
                print("Число:", text[i])
                print("Количество цифр:", digits_num[i])
                print("Номер символа, с которого начинается число:", index[i])
                print("")
        else:
            print("В файле отсутствтуют числа или нет подходящих условию.")
except FileNotFoundError:
    print(
        "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
print(f"Program time: {time.time()-start}")

