# Michael L. Kelley Jr.
# 9/11/12
# GradYear.py
# A Python script to calculate the year a child should graduate high school

# Prompt the user to enter the child's current grade in integer form

CurrentGrade = int(input("Please enter current grade in integer form (Ex: 5). Grade: "))

# Prompt the user for the current year in integer form

CurrentYear = int(input("Enter the year when the child will finish their current grade (Ex: 2012). Year: "))

# Subtract the current grade from the number 12

CalulatedNumber = 12 - CurrentGrade

# Add the CalculatedNumber to the current year.
# This produces the estimated graduation year.

GradYear = CurrentYear + CalculatedNumber

# Output the year the estimated year the child would graduate

print(GradYear)














                  
