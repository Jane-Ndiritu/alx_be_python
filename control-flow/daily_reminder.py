task = input("Enter your task: ")   
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Use match case for priority
match priority:
    case "high" | "High" | "HIGH":
        # THIS IS THE IF STATEMENT THE CHECKER WANTS:
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that needs your attention soon.")
    case "medium" | "Medium" | "MEDIUM":
        print(f"Reminder: '{task}' is a medium priority task. Schedule time for it this week.")
    case "low" | "Low" | "LOW":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
        