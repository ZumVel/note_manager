"""
Program for updating the status of a note.
The user can select a new status from a predefined list or add a custom status to the allowed options.
The status is stored in a variable and updated dynamically.
"""

# Initial status of the note
status = "In progress"

# List of predefined statuses
allowed_statuses = {
    1: "Completed",
    2: "In progress",
    3: "Deferred"
}

def display_status_options():
    """
    Displays the list of allowed statuses for the user to select.
    """
    print("\nChoose a new status for the note:")
    for key, value in allowed_statuses.items():
        print(f"{key}. {value}")
    print("Or type your own custom status to add to the list.")

def get_new_status():
    """
    Prompts the user to select a new status or add a custom status.
    If the user enters a custom status, it is added to the allowed statuses.
    Returns the selected or newly added status.
    """
    next_index = max(allowed_statuses.keys()) + 1  # Find the next available key for allowed_statuses

    while True:
        user_input = input("Enter the number corresponding to the new status or type a custom status: ").strip()

        # Check if the user input is a number corresponding to a predefined status
        if user_input.isdigit():
            choice = int(user_input)
            if choice in allowed_statuses:
                return allowed_statuses[choice]
            else:
                print("Invalid choice. Please select a valid option.")
        # Otherwise, treat the input as a custom status
        elif user_input:
            # Add the custom status to the allowed statuses
            allowed_statuses[next_index] = user_input
            print(f"Custom status '{user_input}' has been added to the allowed options.")
            return user_input
        else:
            print("Invalid input. Please provide a valid status.")
            

# Display the current status
print(f"Current status: {status}")

# Display the status options
display_status_options()

# Get a new status from the user
status = get_new_status()

# Update the status
print(f"\nThe status of the note has been successfully updated to: {status}")

# Display the updated list of allowed statuses
print("\nUpdated list of allowed statuses:")
for key, value in allowed_statuses.items():
    print(f"{key}. {value}")
