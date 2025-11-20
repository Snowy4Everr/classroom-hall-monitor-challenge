#Nicholas Derby & Johnathan Mondragon
# classroom hall monitor challenge
#1
students = ["Alex", "Maria", "John", "Alex", "Sasha"]
minutes_out = [3, 7, 12, 4, 9]

#2
statuses = []      # stores OK / WARNING / FLAGGED
notes = []         # stores extra notes

for i in range(len(students)):
    name = students[i]
    minutes = minutes_out[i]
    note = ""   # will add to this if needed

    # Apply hallway rules:
    if 0 <= minutes <= 5:
        status = "OK"
    elif 6 <= minutes <= 10:
        status = "WARNING"
    else:  # > 10
        status = "FLAGGED"


    if students.count(name) > 1:
        status = "FLAGGED"
        note = "duplicate name detected"

    statuses.append(status)
    notes.append(note)


print("=== HALL PASS REPORT ===")
for i in range(len(students)):
    print(f"Student: {students[i]}")
    print(f"Minutes Out: {minutes_out[i]}")
    print(f"Status: {statuses[i]}")
    if notes[i] != "":
        print(f"Notes: {notes[i]}")
    print("------------------------")



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