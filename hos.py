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

    # Modified: takes parameters instead of input()
    def add_patient(self, patient_id, name, age, disease):
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

    # Modified: takes parameter
    def search_patient(self, pid):
        for patient in self.patients:
            if patient.patient_id == pid:
                print("\nPatient Found:")
                patient.display()
                return
        print("❌ Patient not found.\n")

    # Modified: takes parameter
    def delete_patient(self, pid):
        for patient in self.patients:
            if patient.patient_id == pid:
                self.patients.remove(patient)
                print("🗑️ Patient deleted successfully!\n")
                return
        print("❌ Patient not found.\n")


# Main Program (AUTO MODE - no input)
if __name__ == "__main__":
    hospital = Hospital()

    print("===== Hospital Management System (Auto Mode) =====")

    # Add patients automatically
    hospital.add_patient("101", "John", "25", "Fever")
    hospital.add_patient("102", "Alice", "30", "Cold")

    # View patients
    hospital.view_patients()

    # Search patient
    hospital.search_patient("101")

    # Delete patient
    hospital.delete_patient("102")

    # Final list
    hospital.view_patients()

    print("✅ Program executed successfully (No input required)")