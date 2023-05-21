import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(subject, body, attachment_path, sender_email, sender_password, receiver_email):
    # Setup the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    if attachment_path:
        # Attach the invoice file
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        filename = os.path.basename(attachment_path)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        message.attach(part)

    # Connect to the SMTP server
    smtp_server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server and port
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Send the email
    smtp_server.send_message(message)
    smtp_server.quit()

def generate_invoice():
    # Logic to generate the invoice
    # Replace this with your actual invoice generation code
    invoice_data = {
        'customer_name': 'Camille Molliex',
        'invoice_number': 'INV-2023-06',
        'amount': 1000.00,
        'due_date': '2023-06-01',
    }

    # Generate the invoice file (e.g., PDF, CSV, etc.)
    # Save the file to a location
    invoice_file_path = '/Users/camillemolliex/practice/invoice.pdf'

    return invoice_data, invoice_file_path

def main():
    # Email configuration
    sender_email = 'cuentas.molliex@gmail.com'
    sender_password = '011235813Cm.'
    receiver_email = 'camillemolliex@gmail.com'

    # Generate the invoice
    invoice_data, invoice_file_path = generate_invoice()

    # Compose the email
    subject = f"Invoice {invoice_data['invoice_number']}"
    body = f"Dear {invoice_data['customer_name']},\n\nPlease find attached the invoice for the amount of {invoice_data['amount']}.\n\nDue Date: {invoice_data['due_date']}\n\nBest regards,\nYour Company"

    # Send the email with the invoice attachment
    send_email(subject, body, invoice_file_path, sender_email, sender_password, receiver_email)
    print("Invoice sent successfully!")

if __name__ == '__main__':
    main()