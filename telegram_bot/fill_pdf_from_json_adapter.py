import os
import PyPDF2
import pdfkit
import subprocess
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
import platform
import json
import logging


class FillPdfFromJsonAdapter:
    forms_identifier_to_pdf_files_mapping = {
        "Windows": {
            "AR-11": "../pdf_inputs/ar-11-unlocked.pdf",
            "I-589": "../pdf_inputs/i-589-unlocked.pdf",
            "I-765": "../pdf_inputs/i-765-unlocked.pdf",
            "I-485": "../pdf_inputs/i-485-unlocked.pdf",
            "I-131": "../pdf_inputs/i-131-unlocked.pdf"
        },
        "Linux": {
            "AR-11": "/app/pdf_inputs/ar-11-unlocked.pdf",
            "I-589": "/app/pdf_inputs/i-589-unlocked.pdf",
            "I-765": "/app/pdf_inputs/i-765-unlocked.pdf",
            "I-485": "/app/pdf_inputs/i-485-unlocked.pdf",
            "I-131": "/app/pdf_inputs/i-131-unlocked.pdf"
        }
    }
    forms_identifier_to_html_templates_mapping = {
        "Windows":
            {
                "I-131": "../static/templates/form-i-131/"
            },
        "Linux":
            {
                "I-131": "/app/static/templates/form-i-131/"
            }
    }

    def __init__(self, data, form_identifier, user_id, timestamp):
        load_dotenv()
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        if platform.system() == "Windows":
            self.current_os = "Windows"
            logging.info(f"Setting FillPdf executable path to {os.getenv('EXECUTABLE_PATH_WINDOWS', r'../binaries/windows/fill_pdf_from_json.exe')}")
            self.executable_path = os.getenv("EXECUTABLE_PATH_WINDOWS", r"../binaries/windows/fill_pdf_from_json.exe")
            self.pdf_output_folder_path = r"../pdf_outputs/"
            self.json_input_file_path = rf"../{user_id}-{form_identifier}-{timestamp}.json"
            self.pdf_input_file_path = FillPdfFromJsonAdapter.forms_identifier_to_pdf_files_mapping[self.current_os][form_identifier]
            logging.info(
                f"Setting pdf input file path to {self.pdf_input_file_path}")
        else:  # Assume any non-Windows OS uses the Linux path
            self.current_os = "Linux"
            logging.info(f"Allowing to run FillPdf executable")
            os.system('chmod +x /app/binaries/linux-x64/fill_pdf_from_json')
            logging.info(f"Setting FillPdf executable path to {os.getenv('EXECUTABLE_PATH_LINUX', r'/app/binaries/linux-x64/fill_pdf_from_json')}")
            self.executable_path = os.getenv("EXECUTABLE_PATH_LINUX", r"/app/binaries/linux-x64/fill_pdf_from_json")
            self.pdf_output_folder_path = r"/tmp/pdf_outputs/"
            self.json_input_file_path = rf"/tmp/json_inputs/{user_id}-{form_identifier}-{timestamp}.json"
            self.pdf_input_file_path = FillPdfFromJsonAdapter.forms_identifier_to_pdf_files_mapping[self.current_os][form_identifier]
            logging.info(
                f"Setting pdf input file path to {self.pdf_input_file_path}")

        self.user_id = user_id
        self.data = data
        self.form_identifier = form_identifier
        self.pdf_output_file_path = rf"{self.pdf_output_folder_path}{form_identifier}-{user_id}.pdf"

    def render_html(self, template_name, context):
        env = Environment(
            loader=FileSystemLoader(
                self.forms_identifier_to_html_templates_mapping[self.current_os][self.form_identifier]
            )
        )
        template = env.get_template(template_name)
        return template.render(context)

    def convert_html_to_pdf(self, html, output_filename):
        options = {
            'encoding': 'UTF-8',
        }
        pdfkit.from_string(html, output_filename, options)

    def create_additional_text_page_for_i_131_form(self, output_filename, data):
        html = self.render_html('additional_page_template.html', data)
        self.convert_html_to_pdf(html, output_filename)

    def generate_additional_page_for_i_131(self, complete_pdf_name, data, custom_text, additional_page_name, counter):
        data['text'] = custom_text
        self.create_additional_text_page_for_i_131_form(additional_page_name, data)
        tmp_file_name = f"{self.pdf_output_folder_path}{counter}-{self.user_id}-{self.data['form_identifier']}-additional-pages.pdf"
        self.merge_pdfs([complete_pdf_name, additional_page_name], tmp_file_name)
        complete_pdf_name = tmp_file_name
        return complete_pdf_name

    def merge_pdfs(self, pdf_list, output_filename):
        pdf_merger = PyPDF2.PdfMerger()
        for pdf in pdf_list:
            pdf_merger.append(pdf)
        with open(output_filename, "wb") as output_filehandle:
            pdf_merger.write(output_filehandle)

    def fill_additional_page_for_i_131_form(self):
        data = {
            'family_name': self.data["[0].Line1a_FamilyName[0]"],
            'given_name': self.data["[0].Line1b_GivenName[0]"],
            'middle_name': self.data["[0].Line1c_MiddleName[0]"],
            'alien_number': self.data["[0].#area[1].Line3_AlienNumber[0]"],
            'text': ''
        }

        explanations = [
            {'key': "IntendToComeBackExplanation",
             'text': "Вы собираетесь вернуться в страну, от которой вы запрашивали убежище по причине: "},
            {'key': "ReasonOfComeBackExplanation",
             'text': "После того как вам был предоставлен статус беженца/лица, получившего убежище, вы возвращались в страну, от которой вы запрашивали убежище по причине: "},
            {'key': "ReasonOfIssuedPassport",
             'text': "После того как вам был предоставлен статус беженца/лица, получившего убежище, вы подавали заявку на получение или получали национальный паспорт, подавали заявку на обновление или обновляли имеющийся паспорт, подавали заявку или получали разрешение на въезд в страну, от которой вы запрашивали убежище по причине: "},
            {'key': "TellAboutHelpFromGovernment",
             'text': "После того как вам был предоставлен статус беженца/лица, получившего убежище, вы подавали заявку на получение или получали какие-либо выплаты или пособия в стране, от которой вы запрашивали убежище по причине: "},
            {'key': "RestoredCitizenshipOfLeftCountryReason",
             'text': "После того как вам был предоставлен статус беженца/лица, получившего убежище, вы восстанавливали гражданство в стране, от которой вы запрашивали убежище по причине: "},
            {'key': "GotNewCitizenshipReason",
             'text': "После того как вам был предоставлен статус беженца/лица, получившего убежище, вы приобрели новое гражданство по причине: "},
            {'key': "GotRefugeeStatusElsewhereReason",
             'text': "После того как вам был предоставлен статус беженца/лица, получившего убежище, вам был предоставлен статус беженца или лица, получившего убежище, в любой другой стране по причине: "},
            {'key': "HaveEverFiledFederalIncomeTaxReturnReason",
             'text': "С тех пор как вы стали постоянным жителем Соединенных Штатов, вы подавали декларацию о федеральном подоходном налоге в качестве нерезидента или не подавали декларацию о федеральном подоходном налоге, потому что считали себя нерезидентом по причине: "}
        ]

        complete_pdf_name = self.pdf_output_file_path
        counter = 1

        for explanation in explanations:
            try:
                text_to_add = explanation['text'] + f'\n{self.data[explanation["key"]]}'
                filename_suffix = explanation['key']
                complete_pdf_name = self.generate_additional_page_for_i_131(
                    complete_pdf_name,
                    data,
                    text_to_add,
                    f"{self.pdf_output_folder_path}{self.user_id}-{filename_suffix}.pdf",
                    counter
                )
                counter += 1
            except KeyError:
                if counter != 1:
                    complete_pdf_name = f"{self.pdf_output_folder_path}{counter}-{self.user_id}-{self.data['form_identifier']}-additional-pages.pdf"

        return complete_pdf_name

    def save_json(self):
        try:
            logging.info(f"Current working directory: {os.getcwd()}")
            logging.info(f"Attempting to save JSON to: {self.json_input_file_path}")
            os.makedirs(os.path.dirname(self.json_input_file_path), exist_ok=True)

            serializable_data = {key: value for key, value in self.data.items()}
            json_str = json.dumps(serializable_data, ensure_ascii=False, indent=4)

            json_str = json_str.replace('/', '//')
            json_str = json_str.replace('\\', '//')

            with open(self.json_input_file_path, 'w', encoding="utf-8") as f:
                f.write(json_str)

            # If everything went well
            logging.info("JSON file saved successfully.")

        except Exception as e:
            # Log any exceptions that occur
            logging.error(f"An error occurred: {e}")
            raise

    def fill_pdf(self):
        try:
            logging.info(f"Attempting to use {self.pdf_input_file_path} initial PDF")
            logging.info(f"Attempting to use {self.json_input_file_path} initial JSON")
            logging.info(f"Attempting to process with {self.executable_path} and save resulting PDF to: {self.pdf_output_file_path}")
            pdf_input_file_path = self.pdf_input_file_path
            json_input_file_path = self.json_input_file_path
            pdf_output_file_path = self.pdf_output_file_path
            os.makedirs(os.path.dirname(self.pdf_output_file_path), exist_ok=True)

            subprocess.run([self.executable_path, pdf_input_file_path, json_input_file_path, pdf_output_file_path])
            if self.data['form_identifier'] == "I-131":
                try:
                    return self.fill_additional_page_for_i_131_form()
                except Exception as e:
                    logging.error(f"An error occurred: {e}")

            return pdf_output_file_path
        except Exception as e:
            logging.error(f"An error occurred: {e}")
