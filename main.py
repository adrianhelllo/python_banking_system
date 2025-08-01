class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    #INSTANCE METHOD
    def student_info(self):
        return f"\nStudent info:\n| Name: {self.name}\n| GPA: {self.gpa}"

    @staticmethod
    def is_failing_grade(gpa):
        if gpa < 1.5:
            print('This GPA would be considered failing.')
        else:
            print("This GPA would be considered passing.")

    @classmethod
    def get_count(cls):
        print(f"Total number of students: {cls.count}")

    def __str__(self):
        return self.student_info()
    
    def __eq__(self, other_student):
        return self.gpa == other_student.gpa
    
    def __lt__(self, other_student):
        return self.gpa < other_student.gpa
    
    def __gt__(self, other_student):
        return self.gpa > other_student.gpa
    
    def __add__(self, other_student):
        return f"{self.name} and {other_student.name} work together on a group project."
    
    def __contains__(self, kw):
        return kw in self.name
    
    def __getitem__(self, k):
        if k == 'name':
            return self.name
        elif k == 'gpa':
            return self.gpa
        else:
            return f'Key \"{k}\" was not found.'

student1 = Student("Spongebob", 2.4)
student2 = Student("Csaba", 3.4)
student3 = Student("Nathan", 0.1)
student4 = Student("Levendulás", 10)

Student.get_count()

for student in (student1, student2, student3, student4):
    print(student)

print(student4 == student3)
print(student4 < student3)
print(student4 > student3)
print(student4 + student3)
print("evendul" in student4)
print(student4['gpa'])
print(student4['fasz'])
        



