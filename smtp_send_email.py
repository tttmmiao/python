import sys
from email.mime.text import MIMEText
import smtplib
def main():
	msg = MIMEText('Everything will be OK...Send by python...','plain','utf-8')
	from_add = input('From:')
	password = input('Password:')
	to_add = input('To:')
	smtp_server = input('SMTP server:')
	server = smtplib.SMTP(smtp_server,25)
	server.set_debuglevel(1)
	server.login(from_add, password)
	server.sendmail(from_add,[to_add],msg.as_string())
	server.quit()
if __name__ == '__main__':
	main()