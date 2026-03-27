

class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display(self):
        print(f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}")


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        disease = input("Enter Disease: ")

        patient = Patient(patient_id, name, age, disease)
        self.patients.append(patient)

        print("✅ Patient added successfully!\n")

    def view_patients(self):
        if not self.patients:
            print("No patients found.\n")
        else:
            print("\n--- Patient List ---")
            for patient in self.patients:
                patient.display()
            print()

    def search_patient(self):
        pid = input("Enter Patient ID to search: ")
        found = False

        for patient in self.patients:
            if patient.patient_id == pid:
                print("\nPatient Found:")
                patient.display()
                found = True
                break

        if not found:
            print("❌ Patient not found.\n")

    def delete_patient(self):
        pid = input("Enter Patient ID to delete: ")

        for patient in self.patients:
            if patient.patient_id == pid:
                self.patients.remove(patient)
                print("🗑️ Patient deleted successfully!\n")
                return

        print("❌ Patient not found.\n")


# Main Program
hospital = Hospital()

while True:
    print("===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        hospital.add_patient()
    elif choice == '2':
        hospital.view_patients()
    elif choice == '3':
        hospital.search_patient()
    elif choice == '4':
        hospital.delete_patient()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")