class Course:
    def __init__(self):
        self.course_name=input('enter course name')
        self.course_number=int(input('entre course number'))
        self.number_of_students=int(input('number of students'))
        self.max_number_of_students=int(input('max number of students'))

    def detiles(self):
        print(f'course name: {self.course_name}, course number: {self.course_number}, number of students: {self.number_of_students}, max number of students:{self.max_number_of_students}')

    def avelable_places(self):
        return self.max_number_of_students-self.number_of_students
Biology_course=Course()
Biology_course.detiles()
print(Biology_course.avelable_places())