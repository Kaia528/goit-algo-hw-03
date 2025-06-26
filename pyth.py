#name: str = 'Anna'
#age: int = 34
#height: float = 1.67
#is_student: bool = True
#has_high_degree: None = None


#age_one, age_two = 10, 20
#print(age_one, age_two)
#print(name, age, height, is_student, has_high_degree)

#width = 10
#height = 7
#area = width * height
#print(area)

#divide_result = round(7/3, 2)
#print(divide_result)

#text = " let's code together "
#print(text * 2)

#name = 'Anna'
#age = 30

#message = (f"My name is {name} and I am {age*2} years old")
#print(message)

#name = 'Anna'
#age = 30

#message = "My name is {} and I am {} years old".format(name, age)
#print(message)

#message = "My name is %s and I am %d years old"%(name, age)
#print(message)

#message = "My name is " + name + ". and I am " + str(age) + " years old"
#print(message)

#number = 10
#number = number + 15
#print(number)


#age = 25
#weight = 25.0
#room = '25'

#print(type(age), type(weight), type(room))

#age = str(25)
#weight =int(25.0)
#room = float('25')

#print(type(age), type(weight), type(room))
#print(age, weight, room)

#sentence_one = "Hello world!"
#sentence_two = "Hello " + 'world!'
#print(sentence_one, sentence_two, sep='\n')

#sentence_one = "Hello world"
#sentence_two = "Hello " + "world"
# Відображення змінних
#print(sentence_one, sentence_two, sep='\n')

# Перевірка рівності і ідентичності
#print(f'Are sentence equal? {sentence_one == sentence_two}')
#print(f'Are sentence identical? {sentence_one is sentence_two}')

#new_text = sentence_one
#print(sentence_one)

# Перевірка місця збереження у памяті
#print(f'Path of sentence in memory {id(sentence_one)}')
#print(f'Path of sentence in memory {id(sentence_two)}')

#print(45, True, None, sep='\t:\t', end='')
#print(36, False,'apple', sep='\t:\t', end='')

#entertainment = input('Enter your favourite entertainment:')

#print('Your favorite entertainment is {}'.format(entertainment))
#print('Your favourite entertainment is {entertainment}')

#bill_one = 34.34
#bill_two = 12.01
#bill_tree = 17.42
#bill_four = 4.93

#final_bill = bill_one + bill_two + bill_tree + bill_four
#print(final_bill)

#dollars = int(final_bill)
#cents = int((final_bill - int(final_bill)) * 100)

#print(f"Price {final_bill}", f"Dollars {dollars}", f"Cents {cents}", sep='\n')

#FLOORS = 5
#APARTMENTS_PER_FLOOR = 4

#apartment_number = int(input('Enter apartment number:'))

#apartments_per_entrance = FLOORS * APARTMENTS_PER_FLOOR

#entrance_number = (apartment_number -1) // apartments_per_entrance +1
#floor_number = ((apartment_number -1) % apartments_per_entrance) // APARTMENTS_PER_FLOOR + 1
#print(f"Entrance number {entrance_number}, Floor number {floor_number}")

#user = ['Anna', 'Chaika']
#first_name, last_name = user
#print(first_name, last_name, sep='\n')
#print(user[1], user[0])

#my_list = [1, 2, 2, 3, 4, 5, 100, 35.45, -8]
#print(f"Max value in list {max(my_list)},\nMin value in list {min(my_list)}")

#my_list.append(120)
#print(my_list)

#my_list.insert(0, -110)
#print(my_list)

#my_list.pop(1)
#print(my_list)

#my_list.remove((2))
#print(my_list)

#my_list.pop(2)
#print(my_list)
#print(my_list.count(2))
#print(len(my_list))
#new_list = ['loop', 'start']
#print(my_list, new_list, sep='\n')
#my_list.extend(new_list)
#print(my_list)
#my_list.append(new_list)
#print(my_list)
#print(my_list[-1][1])
#my_list.clear()
#print(my_list)
#del my_list
#print(my_list)

#my_list = [1, 2, 2, 3, 4, 5, 100, 35.45, -8]
#print(my_list.index(100))
#my_list.insert(my_list.index(1),55)
#print(my_list)

#my_list[my_list.index(2)] = None
#print(my_list)
#sorted_list = sorted(my_list)
#print(sorted_list)

#my_list[4] = None
#print(my_list)

#length = 2.75
#width = 1.75
#area = length * width
#show = f"The area is {area}"
#print(show)

#my_list = [1, 2, 2, 3, 4, 5, 100, 35.45, -8]
#sorted_list = sorted(my_list)
#my_list.sort(reverse=True)
#print(my_list)

#palindrome = [1, 2, 1]
#print(palindrome == palindrome[::-1])

#my_list = [1, 2, 2, 3, 4, 5, 100, 35.45, -8]

#print(my_list[3:])
#print(my_list[2:4:2])

#person = {'name': 'Oleh', "age": 22, "phone": "38(098)*********", 'student': False, 1243: ['test', 'failed']}
#print(person.keys())
#print(person.values())
#print(person.get('name'))
#print(person.get('name', 'Noname'))

#new_data = {'location': 'Ukraine, Lviv', 'lang': "ukr"}
#person.update(new_data)
#print(person)
#person.pop('student')
#print(person)
#person['age'] = 100
#print(person)
#del person['age']
#print(person)
#person['test'] = 5
#print(person)


#list_data_one = [1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100]
#list_data_two = [11, 1, 21, 31, 15, 8, 13, 21, 7, 15, 101]

#print(list(set(list_data_one) & set(list_data_two))) # in first and in second &(and)
#print(list(set(list_data_one) | set(list_data_two))) # in first or in second |(or)
#print(list(set(list_data_one) - set(list_data_two))) # in first and not in second -(minus)
#print(list(set(list_data_one) ^ set(list_data_two))) # in first and not in second + in second and not in first

#list_data_one = [20, 9, 8, 5, 6]
#list_data_two = [21, 8, 7, 4, 6]
#print(list(set(list_data_one) & set(list_data_two)))
#print(list(set(list_data_one) | set(list_data_two)))
#print(list(set(list_data_one) - set(list_data_two)))
#print(list(set(list_data_one) ^ set(list_data_two)))

#name = 'Lesia'
#age = 22
#has_driver_licence = True

#print(bool(name))
#if name and age >= 18 and has_driver_licence:
 #    print(f"User {name} can rent a car")

#entry_password = input("Enter password: ")

#if entry_password == "2025":
 #   print("Welcome back 2025")
#else:
 #   print("Access denied")

#balance = 0.7 + 0.6
#print(balance)

#if round(balance, 1) == 1.3:
 #   print('Enough')
#else:
 #   print('Not enough')
#print(round(balance, 1))


#value_one = 12
#value_two = 16
#value_three = 15

#if value_one > value_two:
 #   print('Value one is the biggest')
#elif value_two > value_three:
 #   print('Value two is the biggest')
#else:
 #   print('Value three is the biggest')

#value_x = 11

#match value_x:
 #   case 0: print('value is zero')
  #  case 4 if value_x % 2 == 0:
   #     print(f"value_x % 2 == 0 and case is {value_x} is")
    #case _ if value_x < 0:
     #   print('Value is negative')
    #case _:
     #   print(value_x)
        



#value_x, value_y = 8,7
#max_value = value_x if value_x > value_y else value_y
#print(max_value)

#max_value = 'X > Y' if value_x > value_y else 'X < Y' if value_x < value_y else "X = Y"


#if value_x > value_y:
 #   print( 'X > Y')
#else:
 #   if value_x < value_y:
  #      print( 'X < Y')
   # else:
    #    print("X = Y")

#string_input = input('Enter string: ')
#string_to_compere = input('Enter string to compere: ')

#for char in set(string_input):
 #   print(char)
  #  if char in string_to_compere:
   #  print(False)
    # break
#else:
 #   print(True)


#string_one = input('Enter string: ')
#string_two = input('Enter string to compare: ')

#for char in string_one:
 #   if char not in string_two:
  #      print(False)
   #     break
#else:
 #   print(True)


#def foo(value_a, value_b):
 #   return value_a + value_b

#um_value = foo(value_a=4, value_b=8)
#print(sum_value)

#def add(value_one: int, value_two: int) -> int:

 #   sum_of_two_integers = value_one + value_two
  #  return sum_of_two_integers

#sum_value = add(value_one=4, value_two=8)
#print(sum_value)

#def multiply(number_one, number_two, number_three=None):
 #   if number_three is None:
  #      return number_one * number_two
   # else:
    #    return number_one * number_two * number_three

#print(multiply(number_one=4, number_two=8,))
#print(multiply(number_one=4, number_two=8, number_three=5))



#def foo(number):
 #   print(number)
 #   if number < 10:
 #       foo(number+2)

#foo(0)

#def char_counter(sentence):
 #   operator_dict = dict()
  #  for char in sentence:
   #     if char not in operator_dict.keys():
    #        operator_dict[char] = 1
     #   else:
      #      operator_dict[char] += 1
    #return operator_dict

#user_input = input("Enter a sentence: ")
#print(char_counter(user_input))
#print(char_counter(user_input).keys())
#print(char_counter(user_input).values())


"""from collections import Counter

def char_counter(sentence):
    return Counter(sentence)

user_input = input("Enter a sentence: ")
counter = Counter(user_input)

print(counter)
print("Characters:", counter.keys())
print("Counts:", counter.values())

print("Character counts:")
for key, value in counter.items():
    print(f"{key}: {value}")

    from random import randint  # Імпортуємо функцію, для генерування числа


    def predict_number(number):  # створюємо функцію, яка приймає число на вхід для діапазону чисел
        count = 0  # лічильник для спроб вгадування числа
        goal = randint(0, number)  # генеруємо число від 0 до аргументу функції

        while True:  # вічний
            user_input = int(input(
                f"Guess the number form 0 to {number}: "))  # користувач вводить число з підказкою у вигляді діапазону
            count += 1  # При кожному ведені лічилдьник збільшується на один

            if user_input > goal:  # Якщо число введегне є більше за генероване повідомляємо користувача
                print("Smaller")
            elif user_input < goal:  # Якщо число введегне є менше за генероване повідомляємо користувача
                print("Larger")
            else:  # Якщо число введегне рівне генерованому повідомляємо користувача і перериваємо цикл
                print(f"You win! Number of attempts {count}")
                break


    predict_number(10)
