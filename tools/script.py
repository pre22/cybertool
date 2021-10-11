import smtplib
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
        self.body = str(body)
        self.password_user = password_user
    

    def run(self):
        body_txt = open(self.body, "r")
        body_content = body_txt.read()
        body_txt.close()

        text_content = open(self.receiver_input, "r")
        receiver_list = text_content.readlines()
        text_content.close()
        for user in receiver_list:
            sender = self.sender_input
            receivers = user
            body_of_email = body_content
            msg = MIMEText(body_of_email, "html")
            msg['Subject'] = self.subject
            msg['From'] = sender
            msg['To'] = user

            try:
                s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
                s.login(user=sender, password=self.password_user)
                s.sendmail(sender, receivers, msg.as_string())
                s.quit()
                print("Sent to {}".format(user))
            except smtplib.SMTPException:
                continue

        print("Ran Successful")



