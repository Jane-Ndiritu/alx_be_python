task = input ("Enter your task:")   
priority = input ("priority (high/medium/low):")
time = input("Is it time-bound? (yes/no): ")
if priority.lower() == "high" and time.lower() == "yes":
    match priority.lower():
        case "high":
            print(f"Reminder: Your high-priority task '{task}' is time-bound. Please address it immediately!")
        case "medium":
            print(f"Reminder: Your medium-priority task '{task}' should be completed in due time.")
        case "low":
            print(f"Reminder: Your low-priority task '{task}' can be done at your convenience.")
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")