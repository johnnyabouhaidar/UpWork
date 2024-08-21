import smtplib, ssl

class email_class:
    def __init__(self,email,password):
        self.email=email
        self.password=password

    def send_email(self,subject,content,receiver):
        port = 587  # For starttls
        smtp_server = "smtp.office365.com"
        context = ssl.create_default_context()
        message="""\
Subject: {0}

{1}""".format(subject,content)
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.email,self.password)
            server.sendmail(self.email, receiver, message)        
