from django.core.mail import send_mail
from django.conf import settings as djangoSettings
import threading
from django.utils.html import strip_tags

####################################################################################################

def SendEmailInternal(subject, html_content, recipient_list) :
    try:
        if(subject == None or html_content == None or recipient_list == None):
            return False

        EmailThread(subject, html_content, recipient_list).start()
        print("Send email to " + recipient_list + " success")

        return True
    except Exception as e:
        return False

####################################################################################################

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        send_mail(self.subject,
                self.html_content,
                djangoSettings.EMAIL_SENDER,
                [self.recipient_list],
                html_message = self.html_content,
                fail_silently=False)