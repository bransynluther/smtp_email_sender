import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

# Open the CSV file containing the list of all of the club members
with open('email_list_dulisse.csv', 'r') as email_csv:
    csv_reader = csv.reader(email_csv)
    email_list = list(csv_reader)
    names = ''
    for x in range(len(email_list)):
        names += email_list[x][0] + ';'

# Logon to your IUP email and type the message
print("Please Login")
print("Login: ")
username = input()
print("Password: ")
password = input()
print("Enter Subject: ")
subject = input()
print("Enter Message: ")
message = input()
signature = '''

Thank you,
'''
message += signature

# Establish a connection with the IUP email server
server = smtplib.SMTP('smtp.outlook.com', 587)
server.starttls()
server.login(username, password)

# Send the email to everyone on the emailing list
msg = MIMEMultipart()
msg['From'] = username
msg['Bcc'] = names
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))
body = msg.as_string()
server.sendmail(username, names, body)

server.quit
