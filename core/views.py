
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .secrets import EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_RECIPIENT

def home(request):
    return render(request, "home.html")


def mail(request):
    if request.method == "POST":
        try:
            FROM = request.POST["email"]
            RECIPIENTS = [EMAIL_RECIPIENT]
            msg = MIMEMultipart()
            msg["From"] = FROM
            msg["To"] = ", ".join(RECIPIENTS)
            msg["Subject"] = "New Message from Pulse website"
            body = f"""<b>Sender</b><br>
            {request.POST['name']}<br><br>
            <b>Email</b><br>
            {request.POST['email']}<br><br>
            <b>Message</b><br>
            {request.POST['message']}<br><br>"""
            msg.attach(MIMEText(body, "html"))
            text = msg.as_string()
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login("no.reply.pulse.hack@gmail.com", EMAIL_PASSWORD)
            server.sendmail(
             FROM, RECIPIENTS, text
            )
            server.quit()
            return HttpResponse("Message Sent")
        except:
            return HttpResponse("Message Not Sent", status=500)
