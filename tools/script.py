import smtplib, ssl
from email.mime.text import MIMEText
from tools.forms import ToolsForm

class Script(ToolsForm):

    def __init__(self, sender_input=ToolsForm.declared_fields['sender_input'],
                 receiver_input=ToolsForm.declared_fields['receiver_input'],
                 subject=ToolsForm.declared_fields['subject'], body=ToolsForm.declared_fields['body'],
                 password_user=ToolsForm.declared_fields['password_user']):
        self.sender_input = sender_input
        self.receiver_input = receiver_input
        self.subject = subject
        self.body = body
        self.password_user = password_user

    def run(self):
        # Converting fields to str format
        s_sender = str(ToolsForm.declared_fields['sender_input'])
        s_receiver = str(ToolsForm.declared_fields['receiver_input'])
        s_subject = str(ToolsForm.declared_fields['subject'])
        sbody = str(ToolsForm.declared_fields['body'])
        s_password_user = str(ToolsForm.declared_fields['password_user'])

        # Saving Form content to a file
        saveBodyFile = open('bodytext.txt', "w")
        saveBodyFile.write(sbody)
        saveBodyFile.close()

        saveRecieverInput = open('content.txt', "w")
        saveRecieverInput.write(s_receiver)
        saveRecieverInput.close()

        # Carries out the remain tasks
        body_txt = open('bodytext.txt', "r")
        body_content = body_txt.read()
        body_txt.close()

        text_content = open('content.txt', "r")
        receiver_list = text_content.readlines()
        text_content.close()
        for user in receiver_list:
            sender = s_sender
            receivers = user
            body_of_email = body_content
            msg = MIMEText(body_of_email, "html")
            msg['Subject'] = self.subject
            msg['From'] = sender
            msg['To'] = user

            # Create a secure SSL Certificate
            context = ssl.create_default_context()

            try:
                s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context)
                s.login(user=sender, password=s_password_user)
                s.sendmail(sender, receivers, msg.as_string())
                s.quit()
                print("Sent to {}".format(user))
            except smtplib.SMTPException:
                continue

        print("Script is running smoothly")



