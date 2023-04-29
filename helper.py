# def miles(conversion_dictionary):
#   try:
#     user_input = int(conversion_dictionary["number"])
#     if user_input > 0 and conversion_dictionary["unit"] == "kilometers":
#       mile = user_input / 1.61
#       result = round(mile, 2)
#       print(f"The number of miles is {result} miles.")
#     elif user_input > 0 and conversion_dictionary["unit"] == "miles":
#       km = user_input * 1.61
#       result = round(km, 2)
#       print(f"The number of kilometers is {result} kilometers.")
#     elif user_input == 0 or user_input < 0:
#       print("Value must be greater then zero")
#   except ValueError:
#    print("Kindly enter a positive non-decimal non-text value.")

class User:
  def __init__(self, name, age, job, gender):
    self.name = name
    self.age = age
    self.job = job
    self.gender = gender

  def change_age(self, new_age):
   self.age = new_age

  def print_user(self):
   print(f"The users name is {self.name}. {self.name}'s age is {self.age}. During the day {self.name} works as {self.job}. {self.name} is a {self.gender}")
    

