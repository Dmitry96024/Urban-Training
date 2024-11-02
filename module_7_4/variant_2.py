team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

text = [ ]
with open('file.txt', 'r', encoding='utf-8') as file_text:
    for line in file_text:
      text.append(line.strip().split())

str1 = text[0]
str1.insert(5,team1_num)

str2 = text[1]
str2.insert(5, team1_num)
str2.insert(7,team2_num)

str3 = text[2]
str3.insert(5, score_2)

str4 = text[3]
time = (team2_time/score_2)
str4.insert(5, time)
if time%10 == 1:
    str4[6]='секунду'
elif (time%10==2 or time%10==3 or time%10==4):
    str4[5]='секунды'

str5 = text[4]
str5.insert(2, score_1)
str5.insert(4, score_2)
if score_2%10== 1:
    str5[5]='задачу'
elif (score_2%10==2 or score_2%10==3 or score_2%10==4):
    str5[5]='задачи'

str6 = text[5]
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result= 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
str6.insert(2, challenge_result)


string_list1 = [str(element) for element in str1]
string_list2 = [str(element) for element in str2]
string_list3 = [str(element) for element in str3]
string_list4 = [str(element) for element in str4]
string_list5 = [str(element) for element in str5]
string_list6 = [str(element) for element in str6]
delimiter = " "

print(delimiter.join(string_list1))
print(delimiter.join(string_list2))
print(delimiter.join(string_list3))
print(delimiter.join(string_list4))
print(delimiter.join(string_list5))
print(delimiter.join(string_list6))
