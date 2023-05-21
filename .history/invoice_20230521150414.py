from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_invoice():
    # Generate the invoice data
    invoice_data = {
        'customer_name': 'Camille Molliex',
        'invoice_number': 'INV-2023-06',
        'amount': 1000.00,
        'due_date': '2023-06-01',
    }

    # Create a PDF canvas
    invoice_file_path = '/Users/camillemolliex/practice/invoice.pdf'
    c = canvas.Canvas(invoice_file_path, pagesize=letter)

    # Set up the invoice content
    c.setFont('Helvetica', 12)
    c.drawString(50, 750, f"Customer: {invoice_data['customer_name']}")
    c.drawString(50, 720, f"Invoice Number: {invoice_data['invoice_number']}")
    c.drawString(50, 690, f"Amount: {invoice_data['amount']}")
    c.drawString(50, 660, f"Due Date: {invoice_data['due_date']}")

    # Save the PDF canvas
    c.save()

    return invoice_file_path

# Generate the invoice
invoice_file_path = generate_invoice()
print(f"Invoice generated successfully: {invoice_file_path}")