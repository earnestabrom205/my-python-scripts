import pyinputplus as pyip 


class validate_input:
    def __init__(self) -> None:
        pass

    def validate_name(self):
        while True:
            try:
                self.name = pyip.inputStr(prompt="Enter your name: ", allowRegexes=[r'^[A-Za-z]+\s[A-Za-z]+$'], blockRegexes=[r'[^A-Za-z]'])
                break
            except ValueError:
                print("Please enter a valid name")

    def validate_dob(self):
        while True:
            try:
                self.dob = pyip.inputDate(prompt="Enter your date of birth (YYYY-MM-DD): ", formats=["%Y-%m-%d"])
                break
            except ValueError:
                print("Please enter a valid date of birth")

    def validate_address(self):
        while True:
            try:
                self.address = pyip.inputStr(prompt="Enter your address: ", allowRegexes=[r'^\d+\s[A-Za-z]+\s[A-Za-z]+$'])    
                break
            except ValueError:
                print("Please enter a valid address")

    def validate_goals(self):
        while True:
            try:
                self.goals = pyip.inputStr(prompt="Enter your goals: ", allowRegexes=[r'^[A-Za-z]+$'])    
                break
            except ValueError:
                print("Please enter a goal")