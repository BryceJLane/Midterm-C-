class Professor:
    def __init__(self, Lnumber, first_name, last_name, department):
        self.set_Lnumber(Lnumber)
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    def __str__(self):
        return f"Professor {self.first_name} {self.last_name} (L{self.Lnumber}), Department: {self.department}"

    def set_Lnumber(self, Lnumber):
        if not isinstance(Lnumber, str) or not Lnumber.isdigit():
            raise ValueError("Invalid Lnumber format. It should be a string with digits only.")
        self.Lnumber = Lnumber

    def get_Lnumber(self):
        return self.Lnumber

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_department(self, department):
        self.department = department

    def get_department(self):
        return self.department

if __name__ == "__main__":
    try:
        prof = Professor("12345", "John", "Doe", "Computer Science")
        print(prof)

        prof.set_first_name("Jane")
        prof.set_last_name("Smith")
        prof.set_department("Mathematics")
        prof.set_Lnumber("54321")
        print(prof)

        # Test with an invalid Lnumber
        prof.set_Lnumber("L54321")
    except ValueError as ve:
        print(ve)
