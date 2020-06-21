from abc import ABC, abstractmethod
import json, random
from colorama import init

init(autoreset = True)
from colorama import Fore, Back, Style

class Crypto(ABC):
    @abstractmethod
    def encrypt(self, text_way):
        pass

    @abstractmethod
    def key(self):
        pass

    @abstractmethod
    def decrypt(self, text_way):
        pass


class Zamena(Crypto):
    def encrypt(self, text_way):
        key = self.__get_key()
        encrypt_text = 'Zamena\n'
        with open(text_way, 'r', encoding='utf-8') as file:
            text = file.read()
            for i in range(len(text)):
                flag = False
                for j in key:
                    if text[i] == j:
                        encrypt_text += key[j]
                        flag = True
                        break
                if flag == False:
                    encrypt_text += text[i]
        text_way += '.encrypt'
        with open(text_way, 'w', encoding="utf-8") as file:
            file.write(encrypt_text)

    def key(self):
        while True:
            alph_way = file_check('alph', "алфавитом", 'r')
            if information_from_json(alph_way):
                with open(alph_way, 'r', encoding='utf-8') as file:
                    alph = json.load(file)
                check = alph_check(alph)
                if check:
                    break
                else:
                    print(Fore.RED + "•Повторение в алфавите")
        key = []
        for i in range(len(alph)):
            key.append(alph[i])
        random.shuffle(key)
        dict = {}
        for i in range(len(alph)):
            dict[alph[i]] = key[i]
        while True:
            choice = input("•Напечатать ключить Yes or No: ")
            if choice.lower() == 'yes':
                for key in dict:
                    print(key, '= ', dict[key])
                break
            elif choice.lower() == 'no':
                break
            else:
                print(Fore.RED + "•Неправильная команда")
        key_way = file_check('key', 'ключом (куда его сохранить)', 'w')
        key_ready = ['Zamena', dict]
        with open(key_way, 'w') as file:
            json.dump(key_ready, file, ensure_ascii=False)

    def decrypt(self, text_way):
        key = self.__get_key()
        decrypt_text = ''
        with open(text_way, 'r', encoding='utf-8') as file:
            flag = False
            for line in file:
                if line == 'Zamena\n':
                    flag = True
                    break
            if flag == True:

                text = file.read()
                for i in range(len(text)):
                    flag = False
                    for j in key:
                        if text[i] == key[j]:
                            decrypt_text += j
                            flag = True
                            break
                    if flag == False:
                        decrypt_text += text[i]
                text_way += '.txt'
                with open(text_way, 'w')as file:
                    file.write(decrypt_text)
            else:
                print(Fore.RED + '•Неправильный текст')

    def __get_key(self):
        while True:
            key_way = file_check('key', 'ключом', 'r')
            if information_from_json(key_way):
                with open(key_way, 'r') as file:
                    dirty_key = json.load(file)
                if dirty_key[0] == 'Zamena':
                    return dirty_key[1]
                else:
                    print(Fore.RED + '•Неправильный ключ')


class Perestanovka(Crypto):
    def encrypt(self, text_way):
        key = self.__get_key()
        encrypt_text = 'Perestanovka\n'
        block = len(key)
        with open(text_way, 'r', encoding='utf-8') as file:
            text = file.read()
            text_size = len(text)
            mod = text_size % block
            if mod != 0:
                for i in range(block - mod):
                    text += 'i'
            for i in range(0, len(text), block):
                perestanovka = list(range(len(key)))
                for j in range(len(key)):
                    perestanovka[key[j] - 1] = text[i + j]
                for j in range(len(key)):
                    encrypt_text += perestanovka[j]
        text_way += '.encrypt'
        with open(text_way, 'w', encoding="utf-8") as file:
            file.write(encrypt_text)

    def key(self):
        while True:
            try:
                len = int(input('•Введите длину ключа: '))
            except ValueError:
                print(Fore.RED + '•Неверный тип данных')
            else:
                if len > 0:
                    break
                else:
                    print(Fore.RED + '•Неверная длина ключа!')
        list_key = []
        for i in range(1, len):
            list_key.append(i)
            random.shuffle(list_key)
        while True:
            choice = input("•Напечатать ключить Yes or No: ")
            if choice.lower() == 'yes':

                print(list_key)
                break
            elif choice.lower() == 'no':
                break
            else:
                print(Fore.RED + "•Неправильная команда")
        key = ['Perestanovka', list_key]
        key_way = file_check('key', 'ключом', 'w')
        with open(key_way, 'w') as file:
            json.dump(key, file, ensure_ascii=False)

    def __get_key(self):
        while True:
            key_way = file_check('key', 'ключом', 'r')
            if information_from_json(key_way):
                with open(key_way, 'r') as file:
                    dirty_key = json.load(file)
                if dirty_key[0] == 'Perestanovka':
                    return dirty_key[1]
                else:
                    print(Fore.RED + '•Неправильный ключ')

    def decrypt(self, text_way):
        key = self.__get_key()
        decrypt_text = 'Perestanovka\n'
        block = len(key)
        with open(text_way, 'r', encoding='utf-8') as file:
            flag = False
            for line in file:
                if line == "Perestanovka\n":
                    flag = True
                break
            if flag == True:
                text = file.read()
                text_size = len(text)
                for i in range(0, len(text), block):
                    perestanovka = list(range(len(key)))
                    for j in range(len(key)):
                        perestanovka[j] = text[i + key[j] - 1]
                    for j in range(len(key)):
                        decrypt_text += perestanovka[j]
                text_way += '.txt'
                with open(text_way, 'w', encoding="utf-8") as file:
                    file.write(decrypt_text)
            else:
                print(Fore.RED + '•Неверный текст')


class Gammirovanie(Crypto):
    def __init__(self):
        self.__alph = {}
        self.__module = 0

    def encrypt(self, text_way):

        key = self.__get_key()
        encrypt_text = 'Gammirovanie\n'
        len_gamma = len(key)
        alph = self.__alph
        self.__module = len(alph)
        file = open(text_way, encoding= 'utf-8')
        text = file.read()
        len_text = len(text)
        key_text = []
        for i in range(len_text // len_gamma):
            for simvol in key:
                key_text.append(simvol)
            for i in range(len_text % len_gamma):
                key_text.append(key[i])
        for i in range(len_text):
            flag = False
            for j in self.__alph:
                if j == text[i]:
                    index = (alph[j] + key_text[i]) % self.__module
                    for k in alph:
                        if index == alph[k]:
                            encrypt_text += k
                            break
                    flag = True
                    break
            if flag == False:
                encrypt_text += text[i]
        file.close()
        text_way += '.encrypt'
        with open(text_way, 'w', encoding="utf-8") as file:
            file.write(encrypt_text)

    def key(self):
        while True:
            alph_way = file_check('alph', "алфавитом", 'r')
            if information_from_json(alph_way):
                with open(alph_way, 'r', encoding='utf-8') as file:
                    alph = json.load(file)
                check = alph_check(alph)
                if check:
                    break
                else:
                    print(Fore.RED + "•Повторение в алфавите")
        self.__module = len(alph)

        dict = {}
        for i in range(len(alph)):
            dict[alph[i]] = i + 1
        self.__alph = dict
        while True:
            try:
                gamma_len = int(input('•Введите длину гаммы: '))
            except ValueError:
                print(Fore.RED + '•Неверный тип данных')
            else:
                if gamma_len > 0:
                    break
                else:
                    print(Fore.RED + '•Неверная длина ключа!')
        key = []
        for i in range(gamma_len):
            while True:
                try:
                    gamma_elem = int(input(f'•Введите {i + 1} элемент гаммы: '))
                except ValueError:
                    print(Fore.RED + '•Неверный тип данных!')
                else:
                    if gamma_len > 0:
                        break
                    else:
                        print(Fore.RED + '•Неверная длина ключа!')
            key.append(gamma_elem)
        while True:
            choice = input("•Напечатать ключить Yes or No: ")
            if choice.lower() == 'yes':

                print(key)
                break
            elif choice.lower() == 'no':
                break
            else:
                print(Fore.RED + "•Неправильная команда!")
        crypt_key = ['Gammirovanie']
        crypt_key.append(self.__alph)
        crypt_key.append(key)
        key_way = file_check('key', 'ключом', 'w')
        with open(key_way, 'w',encoding = 'utf-8') as file:
            json.dump(crypt_key, file, ensure_ascii=False)

    def __get_key(self):
        while True:
            key_way = file_check('key', 'ключом', 'r')
            if information_from_json(key_way):
                with open(key_way, 'r', encoding='utf-8') as file:
                    dirty_key = json.load(file)
                if dirty_key[0] == 'Gammirovanie':
                    self.__alph = dirty_key[1]
                    return dirty_key[2]
                else:
                    print(Fore.RED + '•Неправильный ключ!')

    def decrypt(self, text_way):
        key = self.__get_key()
        decrypt_text = ''
        len_gamma = len(key)
        alph = self.__alph
        self.__module = len(alph)
        with open(text_way, 'r', encoding="utf-8") as file:
            flag = False
            for line in file:

                if line == "Gammirovanie\n":
                    flag = True
                break
            if flag == True:
                text = file.read()
                len_text = len(text)
                key_text = []
                for i in range(len_text // len_gamma):
                    for simvol in key:
                        key_text.append(simvol)
                    for i in range(len_text % len_gamma):
                        key_text.append(key[i])
                for i in range(len_text):
                    flag = False
                    for j in self.__alph:
                        if j == text[i]:
                            index = (alph[j] - key_text[i] + self.__module) % self.__module
                            for k in alph:
                                if index == alph[k]:
                                    decrypt_text += k
                                    break
                            flag = True
                            break
                    if flag == False:
                        decrypt_text += text[i]

                text_way += '.txt'
                with open(text_way, 'w', encoding="utf-8") as file:
                    file.write(decrypt_text)
            else:
                print(Fore.RED + '•Неправильный текст!')


def file_check(expension, type, do):
    while True:
        file_way = input(f"Укажите путь к файлу с {type}: ")
        expension_check = way_check(file_way, expension)
        if expension_check:
            if do == 'r':
                if check_file_exist(file_way, do):
                    break
            elif do == 'w':
                if check_file_exist(file_way, do):
                    break
        else:
            print(Fore.RED + "•Неверный путь")
    return file_way


def way_check(file_way, expension):
    way_list = file_way.split(".")
    if way_list[len(way_list) - 1] == expension:
        return True
    return False


def check_file_exist(file_way, do):
    try:
        file = open(file_way, do)
    except FileNotFoundError:
        print(Fore.RED + "•Файл не существует.")
        return False
    else:
        return True


def information_from_json(file_way):
    try:
        with open(file_way, 'r') as file:
            text = json.load(file)
    except json.decoder.JSONDecodeError:
        print(Fore.RED + '•Неправильная информация в файле!')
        return False
    else:
        return True


def alph_check(alph):
    alph_son = []
    for i in range(len(alph)):
        if not (alph[i] in alph_son):
            alph_son.append(alph[i])
        else:
            return False
    return True

prikol = True
while prikol:

    choice = input("•Main menu (◕‿◕)\n" +
                   "•Замена - 1 (ง°ل͜°)ง\n" + "•Перестановка - 2 ᕦ(ò_óˇ)ᕤ\n" +
                   "•Гаммирование - 3 ʕ•ᴥ•ʔ\n" + '•Выход - 0\n' + "•(^_~) Выберите метод шифрования: ")
    if choice == '1':

        choice = Zamena()
        ffff = True

        while ffff == True:
            Choice_na_key = input('•Сгенерировать ключь - Yes or No: ')
            if Choice_na_key.lower() == 'yes':
                choice.key()
                ffff = False
            elif Choice_na_key.lower() == 'no':
                ffff = False
            else:
                print(Fore.RED + "•Неверная команда!")
        while True:
            vibor_encypt_decrypt = input(
                "•Зашифровать текст - 1\n" + "•Расшифровать текст - 2\n" + "•Выход кнопка - 0\n" + "•Ваш выбор: ")
            if vibor_encypt_decrypt == '1':
                File_way = file_check('txt', 'текстом', 'r')
                choice.encrypt(File_way)
                print(Fore.GREEN + "•Текс зашифрован•")
                break
            vibor_encypt_decrypt = input("•Расшифровать текст - 2\n" + "•Выход кнопка - 0\n" + "•Ваш выбор: ")
            if vibor_encypt_decrypt == '2':
                File_way = file_check('encrypt', 'зашифрованным текстом', 'r')
                choice.decrypt(File_way)
                print(Fore.GREEN + "•Текс расшифрован•")
                break
            elif vibor_encypt_decrypt == '0':
                 break
    elif choice == '2':
        choice = Perestanovka()
        ffff = True

        while ffff:
            Choice_na_key = input('•Сгенерировать ключь - Yes or No: ')
            if Choice_na_key.lower() == 'yes':
                choice.key()
                ffff = False
            elif Choice_na_key.lower() == 'no':
                ffff = False
            else:
                print(Fore.RED + "•Неверная команда!")
        while True:
            vibor_encypt_decrypt = input(
                "•Зашифровать текст - 1\n" + "•Расшифровать текст - 2\n" + "•Выход кнопка - 0\n" + "•Ваш выбор: ")
            if vibor_encypt_decrypt == '1':
                File_way = file_check('txt', 'текстом', 'r')
                choice.encrypt(File_way)
                print(Fore.GREEN + "•Текс зашифрован•")
                break
            vibor_encypt_decrypt = input("•Расшифровать текст - 2\n" + "•Выход кнопка - 0\n" + "•Ваш выбор: ")
            if vibor_encypt_decrypt == '2':
                File_way = file_check('encrypt', 'зашифрованным текстом', 'r')
                choice.decrypt(File_way)

                print(Fore.GREEN + "•Текс расшифрован•")
                break
            elif vibor_encypt_decrypt == '0':
                break
    elif choice == '3':
        choice = Gammirovanie()

        ffff = True
        while ffff:
            Choice_na_key = input('•Сгенерировать ключь - Yes or No: ')
            if Choice_na_key.lower() == 'yes':
                choice.key()
                ffff = False
            elif Choice_na_key.lower() == 'no':
                ffff = False
            else:
                print(Fore.RED + "•Неверная команда!")
        while True:
            vibor_encypt_decrypt = input(
                "•Зашифровать текст - 1\n" + "•Расшифровать текст - 2\n" + "•Выход кнопка - 0\n" + "•Ваш выбор: ")
            if vibor_encypt_decrypt == '1':
                File_way = file_check('txt', 'текстом', 'r')
                choice.encrypt(File_way)

                print(Fore.GREEN + "•Текс зашифрован•")
                break
            vibor_encypt_decrypt = input("•Расшифровать текст - 2\n" + "•Выход кнопка - 0\n" + "•Ваш выбор: ")
            if vibor_encypt_decrypt == '2':
                File_way = file_check('encrypt', 'зашифрованным текстом', 'r')
                choice.decrypt(File_way)

                print(Fore.GREEN + "•Текс расшифрован•")
                break
            elif vibor_encypt_decrypt == '0':
                break
    elif choice == '0':
        flag = False
        break
    else:
        print(Fore.RED + '•Неверная команда!')