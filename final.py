username = input("Enter your username: ")
title1 = input("Enter the name of your 1st task: ")
title2 = input("Enter the name of your 2nd task: ")
title3 = input("Enter the name of your 3rd task: ")
content = input("Enter the content of your task: ")
status = input("Enter the status of your task: ")
created_date = input("Enter the created date in DD-MM format: ")
issue_date = input("Enter the issue date in DD-MM format: ")
titles = [title1, title2, title3]
note = {
    "username": username,
    "content": content,
    "status": status,
    "created_date": created_date,
    "issue_date": issue_date,
    "titles": titles
}

print(
    f"Username: {note['username']}", f"Content: {note['content']}",
    f"Status: {note['status']}", f"Created Date: {"-".join(note["created_date"].split("-")[:2])}",
    f"Issue Date: {"-".join(note["issue_date"].split("-")[:2])}", "Titles: ", sep="\n"
)
for i in note["titles"]:
    print(f"   {i}")
