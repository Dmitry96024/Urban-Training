# Создаём функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) 
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
def send_email (message, recipient, *, sender = "university.help@gmail.com" ):
# Если же sender и recipient совпадают, то выводим "Нельзя отправить письмо самому себе!"
    if  sender == recipient:
        print("Нельзя отправить письмо самому себе!")
#Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", 
# то выводим на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    elif ("@" and (".com" or ".ru" or ".net")) not in recipient and ("@" and (".com" or ".ru" or ".net")) not in sender:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
#Если же отправитель по умолчанию - university.help@gmail.com, то выводим сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес ", recipient)
#В противном случае выводим сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
    elif sender != "university.help@gmail.com":
        print ("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ. Письмо успешно отправлено с адреса ", sender, "на адрес ", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.studen@tmail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

#Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
#За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

################################################ Исправленное решение ########################################################################


# Создаём функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель)
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
def send_email (message, recipient, *, sender = "university.help@gmail.com" ):
# Если же sender и recipient совпадают, то выводим "Нельзя отправить письмо самому себе!"
    if  sender == recipient:
        print("Нельзя отправить письмо самому себе!")
#Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
# то выводим на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    elif "@" not in recipient or not recipient.endswith((".com",".ru",".net")) and "@" not in sender or not sender.endswith((".com",".ru",".net")):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
#Если же отправитель по умолчанию - university.help@gmail.com, то выводим сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес ", recipient)
#В противном случае выводим сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
    elif sender != "university.help@gmail.com":
        print ("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ. Письмо успешно отправлено с адреса ", sender, "на адрес ", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.studen@tmail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

#Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
#За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.
