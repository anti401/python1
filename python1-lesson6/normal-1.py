# coding : utf-8

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Human:
    def __init__(self, lastname, firstname, middlename):
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename

    def get_name(self):
        return '{} {}.{}.'.format(self.lastname, self.firstname[0], self.middlename[0])

    def get_full_name(self):
        return '{} {} {}'.format(self.lastname, self.firstname, self.middlename)


class Student(Human):
    def __init__(self, lastname, firstname, middlename, in_class, parents):
        Human.__init__(self, lastname, firstname, middlename)
        self.in_class = in_class
        self.parents = parents

    def call_parents(self):
        return self.parents["mama"].get_full_name(), self.parents["papa"].get_full_name()


class Teacher(Human):
    def __init__(self, lastname, firstname, middlename, discipline, classes):
        Human.__init__(self, lastname, firstname, middlename)
        self.discipline = discipline
        self.classes = classes


teachers = []
teachers.append(Teacher('Иванов', 'Вениамин', 'Мартинович', 'математика', ['5Б', '6Б', '7Б']))
teachers.append(Teacher('Петрова', 'Галина', 'Анатольева', 'русский язык', ['5Б', '6Б', '7Б']))
teachers.append(Teacher('Степанова', 'Лидия', 'Викторовна', 'биология', ['7Б']))
teachers.append(Teacher('Хромой', 'Иван', 'Васильевич', 'физкультура', ['5Б', '6Б']))

students = []
students.append(Student('Черкасов', 'Тимофей', 'Леонович', '5Б',
                {"mama": Human('Черкасова', 'Елена', 'Викторовна'), "papa": Human('Черкасов', 'Леон', 'Иванович')}))
students.append(Student('Суворов', 'Егор', 'Викторович', '5Б',
                {"mama": Human('Суворова', 'Мария', 'Артуровна'), "papa": Human('Суворов', 'Виктор', 'Иванович')}))
students.append(Student('Фролова', 'Полина', 'Артемовна', '6Б',
                {"mama": Human('Фролова', 'Нона', 'Афанасьевна'), "papa": Human('Фролов', 'Артем', 'Сидорович')}))
students.append(Student('Прохоров', 'Григорий', 'Иванович', '6Б',
                {"mama": Human('Прохорова', 'Зинаида', 'Петровна'), "papa": Human('Прохоров', 'Иван', 'Юриевич')}))
students.append(Student('Курочкина', 'Светлана', 'Владимировна', '7Б',
                {"mama": Human('Курочкина', 'Надежда', 'Ефимовна'), "papa": Human('Курочкин', 'Владимир', 'Ильич')}))
students.append(Student('Уткина', 'Вера', 'Данииловна', '7Б',
                {"mama": Human('Уткина', 'Любовь', 'Эдуардовна'), "papa": Human('Уткин', 'Даниил', 'Витальевич')}))

operation = ''
while operation != 'q':
    print('\nДоступные операции:')
    print('1. Получить полный список всех классов школы')
    print('2. Получить список всех учеников в указанном классе')
    print('3. Получить список всех предметов указанного ученика')
    print('4. Узнать ФИО родителей указанного ученика')
    print('5. Получить список всех учителей, преподающих в указанном классе')
    operation = input("Введите номер операции или 'q' для выхода - ")

    if operation == '1':
        all_classes = set()
        for student in students:
            all_classes.add(student.in_class)
        print('Все классы:', ', '.join(all_classes))

    elif operation == '2':
        class_num = input('Номер класса [7Б] - ')
        if not class_num:
            class_num = '7Б'
        print('\nСписок учеников в классе:')
        for student in students:
            if student.in_class == class_num:
                print(student.get_name())

    elif operation == '3':
        student_name = input('Фамилия ученика [Черкасов] - ')
        if not student_name:
            student_name = 'Черкасов'
        for student in students:
            if student.lastname == student_name:
                class_num = student.in_class
                break
        print('\nСписок предметов для класса:')
        for teacher in teachers:
            if class_num in teacher.classes:
                print(teacher.discipline)

    elif operation == '4':
        student_name = input('Фамилия ученика [Фролова] - ')
        if not student_name:
            student_name = 'Фролова'
        print('\nФИО родителей:')
        for student in students:
            if student.lastname == student_name:
                print('\n'.join(student.call_parents()))

    elif operation == '5':
        class_num = input('Номер класса [6Б] - ')
        if not class_num:
            class_num = '6Б'
        print('\nСписок преподающих учителей:')
        for teacher in teachers:
            if class_num in teacher.classes:
                print(teacher.get_full_name())

    else:
        print('Неизвестный номер операции.')
