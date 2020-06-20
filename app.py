from classesObjects import Student

student1 = Student('Aimi','CS',3.8,False)
student2 = Student('Leana','Business',3.9,False)
student3 = Student('Vanessa','CS',3.2,False)
student4 = Student('Michael','CE',4.0,False)


print(student1.name)
print(student3.is_on_probation)
print(student1.on_honor_roll())
if student1.on_honor_roll() == True:
    print(student1.name + ' is on honor roll.')
else:
    print(student1.name + ' is not on honor roll.')
