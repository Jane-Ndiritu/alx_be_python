task = input("Enter your task: ")   
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

# Use match case for priority
match priority.lower():
    case "high":
        if time.lower() == "yes":
            print(f"Reminder: Your high-priority task '{task}' is time-bound. Please address it immediately!")
        else:
            print(f"Reminder: Your high-priority task '{task}' needs your attention soon.")
    case "medium":
        print(f"Reminder: Your medium-priority task '{task}' should be completed in due time.")
    case "low":
        print(f"Reminder: Your low-priority task '{task}' can be done at your convenience.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")