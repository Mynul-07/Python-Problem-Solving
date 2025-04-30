class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def clg():
        print("ABC College")

    def avg_marks(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("Mynul", [99, 98, 97])
avg = s1.avg_marks()
print(f"Average marks of {s1.name} is: {avg}")
Student.clg()
