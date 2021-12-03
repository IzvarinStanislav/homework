# модуль призначено для работи з зовнішніми файлами
# читання та виведення для візуального контролю

def get_rates():
    """читання файла курсів валют 'rates'
    та формування списку курсів валют
    повертає список курсів валют
    """


    # накопичення даних файлу у списку
    with open("./data/rate.csv", 'r') as f:
        rates = f.readlines()

    # підготовка даних для подальшої обробки
    rates_splitted = []
    # порізати в циклі строки на окремі елементи
    for rate in rates:
        obj = split_line(rate)
        obj[0] = int(obj[0])
        rates_splitted.append(obj)

    return rates_splitted

def split_line(line):
    """повертає список об'єктів з строки"""
    object = line.split(',')
    return object

# читання файлу найменувань банків 'directories'
def get_directories ():
    """читання файла довідника ринків 'directories'
    та формування списку ринків
    повертає список ринків
    """

    # накопичення даних файлу у списку
    with open("./data/directories.csv", 'r') as f:
        directories = f.readlines()

    # підготовка даних для подальшої обробки
        directories_splitted =[]
        # порізати в циклі строки на окремі елементи
        for directory in directories:
            obj = split_line(directory)
            directories_splitted.append(obj)

    return directories_splitted

# вивід списку найменувань банків
def show_directories(directories):

    # задати інтервал виводу
    directory_code_from = input("З якого кода клієнта?")
    directory_code_to = input("По який кода клієнта?")

    lines_found=0

    for directory in directories:
        if directory_code_from <= directory[0] <= directory_code_to:
            print ("Код банку: {:5} Назва: {:25}".format(*directory))
            lines_found += 1

        if lines_found == 0:
            print ("Банків по Вашому запиту не знайдено")

def show_rates(rates):

    for rate in rates:
        print("Код банку:{:3} Доллари США {:4} Марки ФРН {:4} Рік{:4}".format(rate[1], rate[2], rate[3], rate[4]))


def split_line(line):
    """повертає список об'єктів з строки"""
    object = line.split(',')
    return object

if __name__ == '__main__':
    rates = get_rates
    directories = get_directories
    
    show_directories(directories)
    
    pass
   