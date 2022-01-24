import pickle


class Adress_Book():

    def read_abook(self):  # функция загрузки адрессной книги из файла
        # файл для храниения данных адрессной книги
        adressbookfile = 'adressbookfile.data'
        # Считываем из хранилища
        f = open(adressbookfile, 'rb')
        stored_abook = pickle.load(f)  # загружаем объект из файла
        return stored_abook

    def update_abook(self, stored_abook):  # функция записи адрессной книги в файл
        # файл для храниения данных адрессной книги
        adressbookfile = 'adressbookfile.data'
        # запись в  файл
        f = open(adressbookfile, 'wb')
        pickle.dump(stored_abook, f)  # помещаем объект в файл
        f.close()

    def insert(self):  # функция внесения новой записи в адрессную книгу
        print('Введите данные для записи в адрессную книгу.\n')
        name = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        adress = input('Введите адресс: ')

        # файл для храниения данных адрессной книги
        adressbookfile = 'adressbookfile.data'
        # Считываем из хранилища
        f = open(adressbookfile, 'rb')
        stored_abook = pickle.load(f)  # загружаем объект из файла
        if len(stored_abook) < 1:
            stored_abook = dict()

        stored_abook[name] = [phone, adress]
        print(f'Вы успешно добавили запись в адрессную книгу -->  \n \
            Имя: {name}, телефон: {phone}, город: {adress}')
        # запись в  файл
        f = open(adressbookfile, 'wb')
        pickle.dump(stored_abook, f)  # помещаем объект в файл
        f.close()
        del stored_abook  # уничтожаем переменную

    def update(self):  # функция изменения записи в адрессной книге
        # файл для храниения данных адрессной книги
        adressbookfile = 'adressbookfile.data'
        # Считываем из хранилища
        f = open(adressbookfile, 'rb')
        stored_abook = pickle.load(f)  # загружаем объект из файла

        # запрашиваем по какому ключу искать данные в адрессной книге
        action = input('Введите имя, данные по которому вы хотите изменить: ')

        # извлекаем из адресной книги запись с введенным ключем
        update_key = stored_abook.get(action)

        # проверяем есть ли такой ключ в адрессной книге
        if update_key != None:
            # выбираем что хотим изменить
            update_val = input('Выберите какие данные вы хотите изменить: \n \
                                a - адресс \n \
                                p - телефон \n \
                                e - выход, я передумал(а) \n')
            # меняем адресс
            if update_val == 'a':
                new_adress = input('Введите новый адресс: ')
                stored_abook[action][1] = new_adress
            # меняем телефон
            elif update_val == 'p':
                new_phone = input('Введите новый номер телефона: ')
                stored_abook[action][0] = new_phone
            elif update_val == 'e':
                return print('Вы вышли из программы.')
            else:
                print('Вы ввели не корректную команду')

            # записываем в адрессную книгу обновленный словарь
            # запись в  файл
            f = open(adressbookfile, 'wb')
            pickle.dump(stored_abook, f)  # помещаем объект в файл
            f.close()
            del stored_abook  # уничтожаем переменную

        else:
            print('Такой записи нет')

    def delete(self):  # функция удаления записи в адрессной книге
        # файл для храниения данных адрессной книги
        adressbookfile = 'adressbookfile.data'
        action = input('Выберите действие для удаления данных из адресной книги.\n \
            d - очитсить адрессную книгу полностью \n \
            c - очистить запись по имени \n')
        # Считываем из хранилища
        f = open(adressbookfile, 'rb')
        stored_abook = pickle.load(f)  # загружаем объект из файла
        if len(stored_abook) < 1:
            print('Адрессная книга пуста.')
        else:
            if action == 'd':
                stored_abook.clear()
                # запись в  файл
                f = open(adressbookfile, 'wb')
                pickle.dump(stored_abook, f)  # помещаем объект в файл
                f.close()
                del stored_abook  # уничтожаем переменную
            elif action == 'c':
                del_item = input(
                    'Введите имя, данные по которому нужно удалить: ')
                # удаляем запись в адрессной книге и проверяем наличие записи по данному ключу
                deleted = stored_abook.pop(del_item, False)
                if deleted == False:
                    print('Записи с таким именем не существует')
                else:
                    # загружаем обновленную адрессную книгу в файл и выводим сообщение об удачном удалении записи
                    # запись в  файл
                    print(
                        f'Вы удалили запись "{del_item} - т. {deleted[0]}, г. {deleted[1]}" из адрессной книги')
                    f = open(adressbookfile, 'wb')
                    pickle.dump(stored_abook, f)  # помещаем объект в файл
                    f.close()
                    del stored_abook  # уничтожаем переменную
                    del deleted  # уничтожаем переменную

            else:
                print('Вы ввели не корректную команду')

    def filter(self):  # функция поиска записи в адрессной книге

        # файл для храниения данных адрессной книги
        adressbookfile = 'adressbookfile.data'
        # Считываем из хранилища
        f = open(adressbookfile, 'rb')
        stored_abook = pickle.load(f)  # загружаем объект из файла

        action = input('Выберите действие для отображения данных из адресной книги.\n \
                a - показать адрессную книгу полностью \n \
                f - найти и показать запись по имени \n')
        if action == 'a':
            # выводим данные из адрессной книги
            for row in stored_abook:
                print(
                    f'Имя: {row}, телефон: {stored_abook[row][0]}, город: {stored_abook[row][1]}')
        elif action == 'f':
            find_item = input('Введите имя, данные по которому нужно найти: ')
            if stored_abook.get(find_item) != None:
                print(
                    f'Имя: {find_item}, телефон: {stored_abook[find_item][0]}, город: {stored_abook[find_item][1]}')
            else:
                print('Такой записи не существует')
        else:
            print('Вы ввели не корректную команду')


action = input('Что вы хотите сделать? \n \
            i - внести запись в адрессную книгу \n \
            u - изменить запись в адрессной книге \n \
            d - удалить запись из адрессной книги \n \
            f - вывести записи в адрессной книге \n')


a = Adress_Book()
if action == 'i':
    a.insert()
elif action == 'u':
    a.update()
elif action == 'd':
    a.delete()
elif action == 'f':
    a.filter()
else:
    print('Вы ввели не корректную команду')
