import smtplib
from email.mime.text import MIMEText

sender_input = str(input("Enter the Senders mail account here: "))
receiver_input = str(input("Enter the link to txt file here: "))
subject = str(input("Enter the subject here: "))
body = str(input("Enter the link to the body_txt file here: "))
password_user = str(input("Enter your password here: "))

body_txt = open(body, "r")
body_content = body_txt.read()
body_txt.close()

text_content = open(receiver_input, "r")
receiver_list = text_content.readlines()
text_content.close()
for user in receiver_list:
    sender = sender_input
    receivers = user
    body_of_email = body_content
    msg = MIMEText(body_of_email, "html")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = user

    try:
        s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        s.login(user=sender, password=password_user)
        s.sendmail(sender, receivers, msg.as_string())
        s.quit()
        print("Sent to {}".format(user))
    except smtplib.SMTPException:
        continue


