import smtplib
from credentail.settings import SENDER_EMAIL, SENDER_PASSWORD
from email.mime.text import MIMEText

def send_email_via_zoho(subject, body, recipient_email):
    """Send an email using the Zoho SMTP server.
    
    Args:
        subject (str): The subject of the email.
        body (str): The body content of the email.
        recipient_email (str): The recipient's email address.
    """

    # Retrieve the sender's email and password from settings
    sender_email = SENDER_EMAIL
    sender_password = SENDER_PASSWORD

    # Create the email message
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    try:
        # Connect to the Zoho SMTP server using SSL
        with smtplib.SMTP_SSL('smtp.zoho.in', 465) as server:
            # Log in to the server using the sender's credentials
            server.login(sender_email, sender_password)
            # Send the email to the recipient
            server.sendmail(sender_email, [recipient_email], message.as_string())
            return True
    except Exception as e:
        # Print an error message if sending the email fails
        print(f"Failed to send email: {e}")
        return False
