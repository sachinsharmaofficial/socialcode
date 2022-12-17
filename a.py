import smtplib

server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login('team.socialcode@outlook.com','Ullu_Gang')

server.sendmail('team.socialcode@outlook.com','naman065op',"hello")

print("Hit")


