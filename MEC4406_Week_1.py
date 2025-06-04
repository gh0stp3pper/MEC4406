# MEC4406 week 1 Python for Quiz 
name = "Benjamin Jones"

# Print name
print(name)

# Print it Backwards
print(name[::-1])

# Count to favourite number squared
favouriteNumber = 7
for i in range(1,favouriteNumber**2+1):
    print(i)

# Class for engineers
class Engineer:
    skill = "Problem Solver"
    def __init__(self, name, type, yearsOfExperience):
        self.name = name
        self.type = type
        self.yearsOfExperience = yearsOfExperience

# Creating two Engineers
Engineer1 = Engineer("Emily", "Electrical", 3)
Engineer2 = Engineer("Mitch", "Mechanical", 18)

# Printing their attributes
print("Engineer 1:")
print("Name:", Engineer1.name)
print("Type:", Engineer1.type)
print("Years of Experience:", Engineer1.yearsOfExperience)
print("Skill:", Engineer1.skill)

print("\nEngineer 2:")
print("Name:", Engineer2.name)
print("Type:", Engineer2.type)
print("Years of Experience:", Engineer2.yearsOfExperience)
print("Skill:", Engineer2.skill)

