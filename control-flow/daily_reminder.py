task = input("Enter your task: ")   
priority_input = input("Priority (high/medium/low): ")
time_input = input("Is it time-bound? (yes/no): ")

# Convert to lowercase for consistent matching
priority = priority_input.lower()
time = time_input.lower()

# Now use match with the converted variable
match priority:
    case "high" if time == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "high":
        print(f"Reminder: '{task}' is a high priority task that needs your attention soon.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task. Schedule time for it this week.")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")