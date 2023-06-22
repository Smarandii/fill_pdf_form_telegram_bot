from pdfjinja import PdfJinja

def fill_pdf_form(input_pdf_path, output_pdf_path, data_dict):
    pdfjinja = PdfJinja(input_pdf_path)
    filled_pdf = pdfjinja(data_dict)
    filled_pdf.write(open(output_pdf_path, 'wb'))

data_dict = {
   'Family Name (Last Name)': 'Doe',
   'Given Name (First Name)': 'John',
   'Middle Name (if applicable)': 'Smith',
   'Date of Birth (mm/dd/yyyy)': '01/01/1970',
   'Alien Registration Number (A-Number) (if any)': 'A-12345678',
   'Street Number and Name': '1234 Main St',
   'City or Town': 'Anytown',
   'State': 'AnyState',
   'ZIP Code': '12345',
   'Your Signature': 'John Doe',
   'Date of Signature (mm/dd/yyyy)': '06/20/2023',
}

fill_pdf_form('ar-11 (1).pdf', 'filled_ar-11.pdf', data_dict)
