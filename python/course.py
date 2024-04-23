class Course():
    def __init__(self, number_=0,inputname="", credit_hr_=0, grade_=0.0):
        self.number = number_
        self.inputname = inputname
        self.credit_hr = credit_hr_
        self.grade = grade_
        self.next = None

    def name(self) -> str:
        return self.inputname
    
    def number(self) -> int:
        return self.number()
    
    def credit_hr(self) -> int:
        return self.credit_hr

    def grade(self) -> float:
        return self.grade

    def __str__(self):
        return f"{self.number} {self.name} {self.credit_hr} {self.grade}"

c=Course()

print()