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

student1 = Student("Spongebob", 2.4)
student2 = Student("Csaba", 3.4)
student3 = Student("Nathan", 0.1)
student4 = Student("Levendulás", 10)

Student.get_count()

for student in (student1, student2, student3, student4):
    print(student)
        


