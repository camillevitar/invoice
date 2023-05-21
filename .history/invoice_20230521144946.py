def generate_invoice():
    # Generate the invoice data
    invoice_data = {
        'customer_name': 'Camille Molliex',
        'invoice_number': 'INV-2023-06',
        'amount': 1000.00,
        'due_date': '2023-06-01',
    }

    # Format the invoice content
    invoice_content = f"Customer: {invoice_data['customer_name']}\n"
    invoice_content += f"Invoice Number: {invoice_data['invoice_number']}\n"
    invoice_content += f"Amount: {invoice_data['amount']}\n"
    invoice_content += f"Due Date: {invoice_data['due_date']}\n"

    # Save the invoice content to a file
    invoice_file_path = '/Users/camillemolliex/practice/invoice.txt'
    with open(invoice_file_path, 'w') as file:
        file.write(invoice_content)

    return invoice_file_path

# Generate the invoice
invoice_file_path = generate_invoice()
print(f"Invoice generated successfully: {invoice_file_path}")