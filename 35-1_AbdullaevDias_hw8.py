import sqlite3


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)


connection = create_connection('hw_8_1.db')

cursor = connection.cursor()
if connection:
    cicle = True
    while cicle:
        print('\nВы можете отобразить список сотрудников по выбранному id города '
              '\nиз перечня городов ниже, для выхода из программы введите 0: ')
        print("Список городов и id города: \n1.New_York\n2.Chicago\n3.Los Angeles"
              "\n4.Bishkek\n5.Issyk_Kul\n6.Moscow\n7.Kazan")
        try:
            choice = int(input('\nВведите id города: '))
        except ValueError:
            print('Введите только число!')
            continue
        cursor.execute('''
            SELECT employees.first_name, employees.last_name, countries.title, cities.title, cities.area
            FROM employees
            INNER JOIN cities ON employees.city_id = c_id
            INNER JOIN countries ON cities.id_country = id
            WHERE c_id = ?
        ''', (choice,))
        results = cursor.fetchall()
        if results:
            for row in results:
                first_name, last_name, country, city, area = row
                print(f"|Имя: {first_name},\tФамилия: {last_name},\tСтрана: {country},"
                      f"\tГород проживания: {city},\tПлощадь города: {area}|")
        elif choice == 0:
            print('Exiting...')
            cicle = False
        else:
            print("Нет сотрудников, проживающих в выбранном городе.\n")
    connection.commit()
    connection.close()





