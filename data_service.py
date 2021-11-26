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
        rates_splitted.append(obj)

    return rates_splitted

def split_line(line):
    """повертає список об'єктів з строки"""
    object = line.split(',')
    return object


# модуль призначено для роботи з зовнішнім файлами
# читання та виведення візуального контролю

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
        object = split_line(directory)
        directories_splitted.append(object)

    return directories_splitted

if __name__ == '__main__':
    rates = get_rates
    directories = get_directories
    pass
    