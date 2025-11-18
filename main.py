#Nicholas Derby & Johnathan Mondragon
# classroom hall monitor challenge
#1
students = ["Fred", "Jimbo","Earl", "Melanie", "Bethany"]
time_gone = ['2', '1', '5', '7', '11']

#2
for i in range(len(students)):
    name = students[i]
    minutes = time_gone[i]
    if minutes > 10:
        status = 'flagged'
    elif minutes >= 6 and <= 10:
        status = 'warning'
    else:
        status = 'ok'
print(name, '>', status)




# #prints of students and time spend
# print(students)
# print(time_gone)

# # #input student and time gone
# # print(students[-1])
# # #For
# # for time_gone in range(1, 12):
# #     if time_gone < 5:
# #         print('Nice and on time!')
# #     else:
# #         if time_gone <10:
# #             print('Your on thin ice')
# #         else:
# #             print('OVER TEN MINUTES?!, flagged')


# #while
# # while not time_gone > 10:
# #     print("You have come back under 10 minutes.")

# # print("You have been flagged because you have taken more than 10 minutes. If this was a mistake, or if you have a reasonable excuse, send me an email.")