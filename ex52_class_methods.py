# Exercise 52 (Medium) – Classes: More Methods

#   Create a Student class with:
#   - Attributes: name, id, grades (list of grades)
#   - Method add_grade(grade) - adds a grade to the list
#   - Method average() - returns the average of all grades
#   - Method passed() - returns True if average >= 70, False otherwise
#   - Method summary() - returns a string like "Alice (ID: 101) - Average: 85.5 - Passed: True"

#   Then:
#   1. Create 3 students
#   2. Add different grades to each student (use loops to add multiple grades)
#   3. Call summary() on each
#   4. Store all students in a list and print those who passed
#   5. Find and print the student with the highest average

class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.grades=[]
        
    def add_grade(self,grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades)/len(self.grades)
    
    def passed(self):
       # avg=sum(self.grades)/len(self.grades)
        if self.average()>=70: return True
        else: return False

    def summary(self):
        return f"{self.name} (ID: {self.id}) - average: {self.average()} - passed: {self.passed()}"
    
student1=Student("gabriel",101)
student1.add_grade(90)
student1.add_grade(86)
student1.add_grade(66)
student1.add_grade(96)

print(student1.average())
print(student1.passed())
print(student1.summary())