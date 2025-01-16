"""
Program for adding titles to a note.
The user can enter as many titles as needed and finish input with an empty string.
Duplicate titles are not allowed.
"""

titles = []  # List to store the titles

while True:
    # Prompt the user to enter a title
    title = input(
        "Enter the title of the note "
        "(leave blank and press Enter to finish): "
    )

    # Check if the user wants to finish input
    if not title:
        break

    # Check for duplicate titles to ensure uniqueness
    if title in titles:
        print("Note with the same title already exists.")
        continue

    # Add the title to the list
    titles.append(title)

# Display all added titles
print("Note titles:")
for title in titles:
    print(f"    -{title}")