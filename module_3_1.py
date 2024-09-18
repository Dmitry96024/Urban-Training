calls = 0
# Создаём функцию count_calls и изменяем в ней значение переменной calls.
#Функция count_calls подсчитывающая вызовы остальных функций
def cound_calls ():
    global calls
    calls+=1
#Создаем функцию string_info с параметром string,
# где  string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info (string):
    cound_calls()
    return (len(string), string.upper(), string.lower())
# Создаём функцию is_contains с двумя параметрами string и list_to_search, где
# is_contains принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains (string, list_to_search):
    cound_calls()
    string = string.lower()
    for a in list_to_search:
        if string == a.lower():
            return True
    return False

# Вызываем функцию
result1 = string_info("Capybara")
result2 = string_info("Armageddon")
result3 = is_contains("Urban",["ban", "BaNaN", "urBAN"])
result4 = is_contains("cycle",['recycling', 'cyclic'])

#Выводим результат.

print(result1)
print(result2)
print(result3)
print(result4)
print(calls)
