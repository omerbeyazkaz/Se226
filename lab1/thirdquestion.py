name=input("What 's your name ?")
labGrade=int(input("Please enter your lab's score"))
midtermGrade=float(input("Pleae enter your midterm's score "))
finalGrade=float(input("Please enter your final's score" ))

lastScore=((labGrade *25)/100 +(midtermGrade * 35)/100+(finalGrade * 40)/100 )


print("Name = " + name)
print("Lab = " + str(labGrade))
print("Midterm = " + str(midtermGrade))
print("Final = " + str(finalGrade))
print("Last score = " + str(lastScore))
