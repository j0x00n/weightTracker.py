import csv
from datetime import datetime

# Weight Tracker csv

now = datetime.now().strftime('%d-%m-%Y')
print()
weightValue = float(input("Weight(kgs): "))
print()

fields=[weightValue,now]

with open('weight.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

# Macro shit

bmr = weightValue * 24

# activityLevel = 1.7 for heavy 
# 7 day a week routine/activity

activityLevel = 1.7
calIntake = bmr * activityLevel
minSurplus = calIntake + 200
maxSurplus = calIntake + 400

# Min Surplus

carbsRequiredMin = round((minSurplus * 0.5)/4)
protienRequiredMin = round((minSurplus * 0.25)/4)
fatRequiredMin = round((minSurplus * 0.25)/9)

print("# Min Surplus")

print("Carbs: " + str(carbsRequiredMin) + "(g)")
print("Protein: " + str(protienRequiredMin) + "(g)")
print("Fats: " + str(fatRequiredMin) + "(g)")
print()

# Max Surplus

carbsRequiredMax = round((maxSurplus * 0.5)/4)
protienRequiredMax = round((maxSurplus * 0.25)/4)
fatRequiredMax = round((maxSurplus * 0.25)/9)

print("# Max Surplus")

print("Carbs: " + str(carbsRequiredMax) + "(g)")
print("Protein: " + str(protienRequiredMax) + "(g)")
print("Fats: " + str(fatRequiredMax) + "(g)")

# other shit

print()
print("Recommended protein intake (2g/per kg): " + str(weightValue*2) +"(g)")

# Doesn't need to be specific (in minutes)

waterIntakeInOuncesMin = round((weightValue * 1.66)/33.8140, 2)

print("Minimum water intake: " + str(waterIntakeInOuncesMin) + "(l)")
print()
