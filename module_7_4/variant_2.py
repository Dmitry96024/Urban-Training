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
str4.insert(5, team2_time)
if team2_time%10 == 1:
    str4[6]='секунду'
elif (team2_time%10==2 or team2_time%10==3 or team2_time%10==4):
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

str7=text[6]
summa_zadach = score_1 + score_2
summa_time = team1_time + team2_time
sr_time_na_1_zadacu = summa_time/ summa_zadach
str7.insert(3, summa_zadach)
str7.insert(8, sr_time_na_1_zadacu)
if summa_zadach%10== 1:
    str7[4]='задачу,'
elif (summa_zadach%10==2 or score_2%10==3 or score_2%10==4):
    str7[4]='задачи,'
else:
    str7[4] = 'задач,'
if sr_time_na_1_zadacu%10 == 1:
    str7[9]='секунду'
elif (sr_time_na_1_zadacu%10==2 or sr_time_na_1_zadacu%10==3 or sr_time_na_1_zadacu%10==4):
    str7[9]='секунды'
