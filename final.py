username = input("Enter your username: ")
title1 = input("Enter the name of your 1st task: ")
title2 = input("Enter the name of your 2nd task: ")
title3 = input("Enter the name of your 3rd task: ")
content = input("Enter the content of your task: ")
status = input("Enter the status of your task: ")
created_date = input("Enter the created date in DD-MM format: ")
issue_date = input("Enter the issue date in DD-MM format: ")
titles_list = [title1, title2, title3]
note = [username, content, status, created_date, issue_date, titles_list]

print(note)