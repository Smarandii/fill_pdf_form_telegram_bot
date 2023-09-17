class FillPdfFromJsonAdapter:
    forms_identifier_to_pdf_files_mapping = {"AR-11": "../pdf_inputs/ar-11-unlocked.pdf",
                                             "I-589": "../pdf_inputs/i-589-unlocked.pdf",
                                             "I-765": "../pdf_inputs/i-765-unlocked.pdf"}

    def __init__(self, data, form_identifier, user_id, timestamp):
        self.data = data
        self.pdf_input_file_path = FillPdfFromJsonAdapter.forms_identifier_to_pdf_files_mapping[form_identifier]
        self.json_input_file_path = rf"../json_inputs/{user_id}-{form_identifier}-{timestamp}.json"
        self.pdf_output_file_path = rf"../pdf_outputs/{form_identifier}-{user_id}.pdf"

    def save_json(self):
        import json

        serializable_data = {key: value for key, value in self.data.items()}
        json_str = json.dumps(serializable_data, ensure_ascii=False, indent=4)

        json_str = json_str.replace('/', '//')
        json_str = json_str.replace('\\', '//')

        with open(self.json_input_file_path, 'w', encoding="utf-8") as f:
            f.write(json_str)

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
