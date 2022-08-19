class Garden:
    student_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                    "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

    plant_dict = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}

    def __init__(self, diagram, students = student_list):
        self.diagram = diagram
        self.stu = [list(p) for p in diagram.split("\n")]
        self.plant_stu = [[self.plant_dict[count] for count in p] for p in self.stu]
        self.students = sorted(students)

    def plants(self, student):
        return self.index_of_plant(self.students.index(student))

    def index_of_plant(self, s):
        return [self.plant_stu[0][s * 2],
                self.plant_stu[0][(s * 2) + 1],
                self.plant_stu[1][s * 2],
                self.plant_stu[1][(s * 2) + 1]]

