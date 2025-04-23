import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)

DB_NAME = "students.db"

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                course TEXT,
                department TEXT
            )
        """)
        conn.commit()


class StudentDBApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Database Manager")
        self.setGeometry(100, 100, 800, 500)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Input fields
        form_layout = QHBoxLayout()
        self.id_input = QLineEdit()
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.course_input = QLineEdit()
        self.dept_input = QLineEdit()

        form_layout.addWidget(QLabel("ID:"))
        form_layout.addWidget(self.id_input)
        form_layout.addWidget(QLabel("Name:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Age:"))
        form_layout.addWidget(self.age_input)
        form_layout.addWidget(QLabel("Course:"))
        form_layout.addWidget(self.course_input)
        form_layout.addWidget(QLabel("Dept:"))
        form_layout.addWidget(self.dept_input)

        layout.addLayout(form_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add")
        view_btn = QPushButton("View All")
        search_btn = QPushButton("Search")
        update_btn = QPushButton("Update")
        delete_btn = QPushButton("Delete")

        add_btn.clicked.connect(self.add_student)
        view_btn.clicked.connect(self.view_students)
        search_btn.clicked.connect(self.search_student)
        update_btn.clicked.connect(self.update_student)
        delete_btn.clicked.connect(self.delete_student)

        for btn in [add_btn, view_btn, search_btn, update_btn, delete_btn]:
            btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Age", "Course", "Department"])
        layout.addWidget(self.table)

        central_widget.setLayout(layout)
    

    def add_student(self):
        try:
            student = (
                int(self.id_input.text().strip()),
                self.name_input.text().strip(),
                int(self.age_input.text().strip()),
                self.course_input.text().strip(),
                self.dept_input.text().strip(),
            )
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", student)
                conn.commit()
            QMessageBox.information(self, "Success", "Student added successfully!")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not add student:\n{e}")
        

    def view_students(self):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
        self.load_table(rows)
        

    def search_student(self):
        query = self.name_input.text().strip() or self.id_input.text().strip()
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            if query.isdigit():
                cursor.execute("SELECT * FROM students WHERE CAST(student_id AS TEXT) LIKE ?", ('%' + query + '%',))
            else:
                cursor.execute("SELECT * FROM students WHERE LOWER(name) LIKE ?", ('%' + query.lower() + '%',))
            rows = cursor.fetchall()

        self.load_table(rows)


        query = input("Enter Student Roll Number or Name to search: ").strip()

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            if query.isdigit():
                cursor.execute("SELECT * FROM students WHERE CAST(student_id AS TEXT) LIKE ?", ('%' + query + '%',))
            else:
                cursor.execute("SELECT * FROM students WHERE LOWER(name) LIKE ?", ('%' + query.lower() + '%',))

            results = cursor.fetchall()

            if not results:
                print("No matching student found.")
                return

            print("\nMatching Student(s):")
            print("{:<12} {:<15} {:<5} {:<15} {:<15}".format("Roll Number", "Name", "Age", "Course", "Department"))
            for student in results:
                student_id, name, age, course, department = student
                print("{:<12} {:<15} {:<5} {:<15} {:<15}".format(student_id, name, age, course, department))


    def update_student():
        student_id = input("Enter Student Roll Number to update: ").strip()

        if not student_id.isdigit():
            print("Invalid Roll Number!")
            return
        
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students WHERE student_id = ?", (int(student_id,)))
            student = cursor.fetchone()

            if not student:
                print("Student not found.")
                return
            
            _, name, age, course, department = student

            new_name = input(f"Enter New Name ({name}): ").strip()
            if new_name and not new_name.isalpha():
                print("Invalid Name! Name should contain only alphabets.")
                return
            new_name = new_name or name

            new_age = input(f"Enter New Age ({age}): ").strip()
            if new_age and (not new_age.isdigit() or not (1 <= int(new_age) <= 100)):
                print("Invalid Age! Age should be a number between 1 and 100.")
                return
            new_age = new_age or age

            new_course = input(f"Enter New Course ({course}): ").strip() or course
            new_department = input(f"Enter New Department ({department}): ").strip() or department

            cursor.execute("""
                UPDATE students
                SET name = ?, age = ?, course = ?, department = ?
                WHERE student_id = ?
            """, (new_name, int(new_age), new_course, new_department, int(student_id)))

            conn.commit()
            print("Student record updated successfully!")


    def delete_student():
        student_id = input("Enter Student Roll Number to delete: ").strip()

        if not student_id.isdigit():
            print("Invalid Roll Number!")
            return
        
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students WHERE student_id = ?", (int(student_id),))
            if not cursor.fetchone():
                print("Student not found.")
                return
            
            cursor.execute("DELETE FROM students WHERE student_id = ?", (int(student_id),))
            conn.commit()
            print("Student record deleted successfully!")

    def load_table(self, rows):
        self.table.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))


if __name__ == "__main__":
    create_table()
    app = QApplication(sys.argv)
    window = StudentDBApp()
    window.show()
    sys.exit(app.exec_())