import smtplib
from email.message import EmailMessage


class Send_Notification():
    user = 'amithtalentplace@gmail.com'
    password = 'app-password' # ? from gmail u can get it..

    def send_email(self, body, subject, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to
        msg['from'] = self.user
        
        server = smtplib.SMTP('smtp.gmail.com', 587) # ? localhost and port for the sending the email..
        server.starttls # ? tls= transport level security, adding security to email message..
        server.login(self.user, self.password)
        server.send_message(msg)
        
        server.quit()
        
    if __name__ == "__main__":
        send_email(body='congratulations on applying for the job..', subject='Applying for Job', to='amithkulkarni99@gmail.com')
         
    