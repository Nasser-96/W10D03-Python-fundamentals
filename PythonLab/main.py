
#-------------------Task1--------------------------------------


# x = int(input("Enter Start Number: "))
# y = int(input("Enter Second Number: "))
#
# for n in range(x ,y+1):
#     for c in range(2,n):
#         if(n%c) == 0:
#             break
#     else:
#         if n==2:
#             pass
#
#         else:print(n)


#-------------------Task2--------------------------------------

# def show_student(name, GPA=0):
#     print("\nYour Name is "+name+" and Your GPA is "+str(GPA))
#
# show_student("Nasser")

#-------------------Task3--------------------------------------

subjects_grades = { 'Physics': 90, 'Math': 100, 'History': 70 }

print("\nMinimum grade "+list(subjects_grades.keys())[list(subjects_grades.values()).index(min(subjects_grades.values()))])
print("And Maximum grade is "+list(subjects_grades.keys())[list(subjects_grades.values()).index(min(subjects_grades.values()))])