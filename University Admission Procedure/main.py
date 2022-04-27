class UniversityAdmissionProcedure:
    def __init__(self):
        self.applicants_data = None
        self.departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
        self.departments_with_students = {key: [] for key in self.departments}
        self.department_exam_index = {
            "Biotech": [3, 2],
            "Chemistry": [3],
            "Engineering": [5, 4],
            "Mathematics": [4],
            "Physics": [2, 4]
        }

    def load_applicants_data(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            file.close()

        self.applicants_data = [line.split() for line in lines]

    def get_mean(self, student, department):
        exam_indexes = self.department_exam_index[department]
        total = 0
        for exam_index in exam_indexes:
            total += float(student[exam_index])
        mean = total / len(exam_indexes)
        admission_exam = float(student[6])
        return max(mean, admission_exam)

    def select_best_applicants_based_on_capacity(self, total_capacity, department, prio):
        wish_index = 6 + prio
        remaining_capacity = total_capacity - len(self.departments_with_students[department])
        sorted_list = sorted(self.applicants_data, key=lambda x: (-self.get_mean(x, department), x[0] + ' ' + x[1]))
        sorted_filtered_list = list(filter(lambda x: x[wish_index] == department, sorted_list))
        selected_students = sorted_filtered_list[:remaining_capacity]

        for selected_student in selected_students:
            students_of_department = self.departments_with_students[department]
            students_of_department.append(selected_student)
            self.applicants_data.remove(selected_student)

    def distribute_students_to_departments(self, total_capacity):
        for prio in range(1, 4):
            for department in self.departments:
                self.select_best_applicants_based_on_capacity(total_capacity, department, prio)

    def print_departments(self):
        for department in self.departments:
            students_of_department = self.departments_with_students[department]
            students_of_department = sorted(students_of_department, key=lambda x: (-self.get_mean(x, department), x[0] + ' ' + x[1]))

            print(department, f"({len(students_of_department)})")
            print(*[f"{student[0]} {student[1]} {self.get_mean(student, department)}" for student in students_of_department], sep="\n")
            print()

    def save_departments(self):
        for department in self.departments:
            students_of_department = self.departments_with_students[department]
            students_of_department = sorted(students_of_department, key=lambda x: (-self.get_mean(x, department), x[0] + ' ' + x[1]))

            with open(f"{department}.txt", "w") as file:
                txt = "".join([f"{student[0]} {student[1]} {self.get_mean(student, department)}\n" for student in students_of_department])
                file.write(txt)
                file.close()

    def main(self):
        total_capacity = int(input())
        self.load_applicants_data("applicants.txt")
        self.distribute_students_to_departments(total_capacity)
        self.print_departments()
        self.save_departments()


if __name__ == "__main__":
    UniversityAdmissionProcedure().main()