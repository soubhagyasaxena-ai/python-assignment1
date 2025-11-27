# ==========================================
# Daily Calorie Tracker
# For 1st Year 1st Semester B.Tech Students
# ==========================================

print("=== DAILY CALORIE TRACKER ===")

# Ask user for calorie goal
goal = int(input("Enter your daily calorie goal: "))

# Taking input for meals
breakfast = int(input("Enter calories for breakfast: "))
lunch = int(input("Enter calories for lunch: "))
dinner = int(input("Enter calories for dinner: "))
snacks = int(input("Enter calories for snacks: "))

# Calculate total calories consumed
total = breakfast + lunch + dinner + snacks

# Display results
print("\n=== SUMMARY ===")
print("Total calories consumed today:", total, "calories")

# Compare with goal
if total < goal:
    print("You are under your calorie goal by", goal - total, "calories. ✅")
elif total == goal:
    print("You have met your calorie goal exactly! 🎯")
else:
    print("You have exceeded your calorie goal by", total - goal, "calories. ⚠")

print("\nKeep tracking your meals to stay healthy!")
