class School:
    student = {}
    adding = []

    def __init__(self):
        self.student = {}
        self.adding = []

    def add_student(self, name, grade):
        if grade not in self.student:
            self.student[grade] = []

        if name not in [name for grade in self.student.keys() for name in
                        self.student[grade]]:
            self.student[grade].append(name)
            self.adding.append(True)

        else:
            self.adding.append(False)

    def added(self):
        return self.adding

    def roster(self):
        return [name for grade in sorted(self.student.keys()) for name in
                sorted(self.student[grade])]

    def grade(self, grade_number):
        if grade_number in self.student:
            return [a for a in sorted(self.student[grade_number])]

        return []