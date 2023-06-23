class FillPdfFromJsonAdapter:
    forms_identifier_to_pdf_files_mapping = {"ar-11": "../pdf_inputs/ar-11-unlocked.pdf"}

    def __init__(self, data, form_identifier, user_id, timestamp):
        self.pdf_input_file_path = FillPdfFromJsonAdapter.forms_identifier_to_pdf_files_mapping[form_identifier]
        self.json_input_file_path = rf"../json_inputs/{user_id}-{form_identifier}-{timestamp}.json"
        self.pdf_output_file_path = rf"../pdf_outputs/{form_identifier}-{data['S1_FamilyName']}-{data['S1_GivenName']}-{user_id}.pdf"

    def save_json(self, data):
        import json
        serializable_data = {key: value for key, value in data.items()}
        with open(self.json_input_file_path, 'w', encoding="utf-8") as f:
            json.dump(serializable_data, f)

    def fill_pdf(self):
        import subprocess
        from dotenv import load_dotenv
        import os
        load_dotenv()
        executable_path = os.getenv("EXECUTABLE_PATH")
        pdf_input_file_path = self.pdf_input_file_path
        json_input_file_path = self.json_input_file_path
        pdf_output_file_path = self.pdf_output_file_path

        subprocess.run([executable_path, pdf_input_file_path, json_input_file_path, pdf_output_file_path])
        return pdf_output_file_path
