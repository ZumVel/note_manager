"""
Program for updating the status of a note.
The user can write a new status and update the status of the note.
If no input is provided, the program exits without updating the status.
"""

# Initial status of the note
status = "Created"

# Display the current status
print(f"Current status: {status}")

while True:
    # Prompt the user to enter a new status
    new_status = input(
        "Enter a new note status "
        "(leave blank and press Enter to finish): "
    )

    # Check if the user wants to finish without updating
    if not new_status:
        print("The status of the note has not been updated.")
        break

    # Update the status and display the success message
    status = new_status
    print(f"Status updated successfully to: {status}")