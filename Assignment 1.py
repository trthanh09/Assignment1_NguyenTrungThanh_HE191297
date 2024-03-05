class Pupil:
    def __init__(self, name, roll_number, English, Maths, Physics, Chemistry, cs):
        self.name = name
        self.roll_number = roll_number
        self.English = English
        self.Maths = Maths
        self.Physics = Physics
        self.Chemistry = Chemistry
        self.cs = cs

class PupilManagementSystem:
    def __init__(self):
        self.pupils = []

    def display_menu(self):
        print("\nMain Menu:")
        print("1. Report")
        print("2. Admin")
        print("3. Exit")

    def display_admin_menu(self):
        print("\nAdmin Menu:")
        print("1. Create pupil record")
        print("2. Display all pupil records")
        print("3. Search pupil record")
        print("4. Modify pupil record")
        print("5. Delete pupil record")
        print("6. Back to main menu")

    def display_report_menu(self):
        print("\nReport Menu:")
        print("1. Class result")
        print("2. Pupil report card")
        print("3. Back to main menu")
    
    def create_pupil_record(self):
        roll_number = input("Enter pupil roll number: ")
        name = input("Enter pupil name: ")
        English = input("Enter Marks in English: ")
        Maths = input("Enter Marks in Maths: ")
        Physics = input("Enter Marks in Physics: ")
        Chemistry = input("Enter Marks in Chemistry: ")
        cs = input("Enter Marks in CS: ")
        pupil = Pupil(roll_number, name, English, Maths, Physics, Chemistry, cs)
        self.pupils.append(pupil)
        print(f"Pupil record created for {name} (Roll No: {roll_number})")

    def display_all_pupil_records(self):
        if not self.pupils:
            print("No pupil records found.")
        else:
            print("\nAll Pupil Records:")
            for pupil in self.pupils:
                print("PUPIL DETAILS..")
                print(f"Roll Number: {pupil.roll_number}")
                print(f"Name: {pupil.name}")
                print(f"English: {pupil.English}")
                print(f"Maths: {pupil.Maths}")
                print(f"Physics: {pupil.Physics}")
                print(f"Chemistry: {pupil.Chemistry}")
                print(f"CS: {pupil.cs}")

    def search_pupil_record(self):
        roll_number = input("Enter pupil roll number to search: ")
        found = False
        for pupil in self.pupils:
            if pupil.roll_number == roll_number:
                print("PUPIL DETAILS..")
                print(f"Roll Number: {pupil.roll_number}")
                print(f"Name: {pupil.name}")
                print(f"English: {pupil.English}")
                print(f"Maths: {pupil.Maths}")
                print(f"Physics: {pupil.Physics}")
                print(f"Chemistry: {pupil.Chemistry}")
                print(f"CS: {pupil.cs}")
                found = True
                break
        if not found:
            print(f"No pupil found with Roll No: {roll_number}")

    def modify_pupil_record(self):
        roll_number = input("Enter pupil roll number to modify: ")
        for pupil in self.pupils:
            if pupil.roll_number == roll_number:
                new_name = input("Enter new name: ")
                pupil.name = new_name
                new_english = input("Enter new marks: ")
                pupil.English = new_english
                new_maths = input("Enter new marks: ")
                pupil.Maths = new_maths
                new_physics = input("Enter new marks: ")
                pupil.Physics = new_physics
                new_chemistry = input("Enter new marks: ")
                pupil.Chemistry = new_chemistry
                new_cs = input("Enter new marks: ")
                pupil.cs = new_cs
                print(f"Pupil record modified for Roll No: {roll_number}")
                break
        else:
            print(f"No pupil found with Roll No: {roll_number}")

    def delete_pupil_record(self):
        roll_number = input("Enter pupil roll number to delete: ")
        for pupil in self.pupils:
            if pupil.roll_number == roll_number:
                self.pupils.remove(pupil)
                print(f"Pupil record deleted for Roll No: {roll_number}")
                break
        else:
            print(f"No pupil found with Roll No: {roll_number}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                while True:
                    self.display_report_menu()
                    report_choice = input("Enter your report choice: ")
                    if report_choice == '1':
                        print("Generating class result report...")
                        self.display_all_pupil_records()
                    elif report_choice == '2':
                        print("Generating pupil report card...")
                        self.search_pupil_record()
                    elif report_choice == '3':
                        break
                    else:
                        print("Invalid report choice. Please try again.")
            elif choice == '2':
                while True:
                    self.display_admin_menu()
                    admin_choice = input("Enter your admin choice: ")
                    if admin_choice == '1':
                        self.create_pupil_record()
                    elif admin_choice == '2':
                        self.display_all_pupil_records()
                    elif admin_choice == '3':
                        self.search_pupil_record()
                    elif admin_choice == '4':
                        self.modify_pupil_record()
                    elif admin_choice == '5':
                        self.delete_pupil_record()
                    elif admin_choice == '6':
                        break
                    else:
                        print("Invalid admin choice. Please try again.")
            elif choice == '3':
                print("Exiting the Pupil Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = PupilManagementSystem()
    system.run()
