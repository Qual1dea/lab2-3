import time

buffer_len = 1
number, digit = "", ""
index_count = 0
index, sequence_num, digits_num = [], [], []
start = time.time()

with open("text.txt", "r") as file:
    buffer = file.read(buffer_len)                     # читаем первый блок
    while buffer:
        while (buffer < '0' or buffer > '9') and buffer:
            buffer = file.read(buffer_len)             # читаем очередной блок
        if not buffer:
            print("\nФайл text.txt в директории проекта пустой или его нет.")
        while (buffer >= '0' and buffer <= '9' or buffer == " " or buffer == "." or buffer < '0' or buffer > '9') and buffer:
            if (buffer >= '0' and buffer <= '9' or buffer == ".") and buffer:
                number += buffer
            else:
                number += " "
            digit += number
            buffer = file.read(buffer_len)             # читаем очередной блок
            number = ""
    text = digit.split()

    for value in text:
        try:
            try:
                value = int(value)
            except ValueError:
                value = float(value)
        except ValueError:
            print("Измените входной файл и перезапустите программу!")
            quit()
        digits_num.append(len(str(abs(value)).replace(".", "")))
        sequence_num.append(value)
        index.append(index_count)                # подсчёт номера символа, с которого начинается число
        index_count = index_count + len(str(abs(value)).replace(".", "")) + 1
    for x in range(len(text))[::-1]:
        try:
            text[x] = int(text[x])
        except ValueError:
            text[x] = float(text[x])
        if not (x % 2 and not text[x] % 2):
            del (text[x], sequence_num[x], index[x], digits_num[x])
    if len(text) > 0:
        for i in range(len(text)):
            print("Число:", sequence_num[i])
            print("Количество цифр:", digits_num[i])
            print("Номер символа, с которого начинается число:", index[i])
            print("")
    else:
        print("В файле отсутствуют числа или нет подходщих к условию.")
print(f"Programm time: {time.time() - start}")