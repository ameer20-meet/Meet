
import tkinter as tk
from tkinter import simpledialog

exam_one = int(simpledialog.askstring(input, "Input exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring(input , "Input exam grade one: ", parent=tk.Tk().withdraw()))

exam_three = int(simpledialog.askstring(input ,"exam grade three: ", parent=tk.Tk().withdraw()))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    print ('letter_grade = "A"')
elif avg >= 80 and avg < 90:
    print('letter_grade = "B"')
elif avg > 69 and avg < 80:
    print('letter_grade = "C"')
elif avg <= 69 and avg >= 65:
    print('letter_grade = "D"')
else:
    print('letter_grade = "F"')

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter-grade is "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
