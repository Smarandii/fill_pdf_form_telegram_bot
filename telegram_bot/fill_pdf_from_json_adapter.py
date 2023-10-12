import os
import PyPDF2
import pdfkit
import subprocess
from dotenv import load_dotenv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from jinja2 import Environment, FileSystemLoader


class FillPdfFromJsonAdapter:
    forms_identifier_to_pdf_files_mapping = {"AR-11": "../pdf_inputs/ar-11-unlocked.pdf",
                                             "I-589": "../pdf_inputs/i-589-unlocked.pdf",
                                             "I-765": "../pdf_inputs/i-765-unlocked.pdf",
                                             "I-485": "../pdf_inputs/i-485-unlocked.pdf",
                                             "I-131": "../pdf_inputs/i-131-unlocked.pdf"}
    forms_identifier_to_html_templates_mapping = {
        "I-131": "../static/templates/form-i-131/"
    }

    def __init__(self, data, form_identifier, user_id, timestamp):
        self.pdf_output_folder_path = r"../pdf_outputs/"
        self.user_id = user_id
        self.data = data
        self.form_identifier = form_identifier
        self.pdf_input_file_path = FillPdfFromJsonAdapter.forms_identifier_to_pdf_files_mapping[form_identifier]
        self.json_input_file_path = rf"../json_inputs/{user_id}-{form_identifier}-{timestamp}.json"
        self.pdf_output_file_path = rf"{self.pdf_output_folder_path}{form_identifier}-{user_id}.pdf"

    def render_html(self, template_name, context):
        env = Environment(
            loader=FileSystemLoader(
                self.forms_identifier_to_html_templates_mapping[self.form_identifier]
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

        complete_pdf_name = self.generate_additional_page_for_i_131(
            self.pdf_output_file_path,
            data,
            f'Вы собираетесь вернуться в страну, от которой вы запрашивали убежище по причине: '
            f'\n{self.data["IntendToComeBackExplanation"]}',
            f"{self.pdf_output_folder_path}{self.user_id}-IntendToComeBackExplanation.pdf",
            1)

        complete_pdf_name = self.generate_additional_page_for_i_131(
            complete_pdf_name,
            data,
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы возвращались в '
            f'страну, от которой вы'
            f'запрашивали убежище по причине: '
            f'{self.data["ReasonOfComeBackExplanation"]}',
            f"{self.pdf_output_folder_path}{self.user_id}-ReasonOfComeBackExplanation.pdf",
            2
        )

        complete_pdf_name = self.generate_additional_page_for_i_131(
            complete_pdf_name,
            data,
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы подавали заявку на '
            f'получение или получали национальный паспорт, подавали заявку на обновление или обновляли имеющийся '
            f'паспорт, подавали заявку или получали разрешение на въезд в страну, от которой вы'
            f'запрашивали убежище по причине: '
            f'{self.data["ReasonOfIssuedPassport"]}',
            f"{self.pdf_output_folder_path}{self.user_id}-ReasonOfIssuedPassport.pdf",
            3
        )

        complete_pdf_name = self.generate_additional_page_for_i_131(
            complete_pdf_name,
            data,
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы подавали заявку на '
            f'получение или получали какие-либо выплаты или пособия в стране, от которой вы'
            f'запрашивали убежище по причине: '
            f'{self.data["TellAboutHelpFromGovernment"]}',
            f"{self.pdf_output_folder_path}{self.user_id}-TellAboutHelpFromGovernment.pdf",
            4
        )

        complete_pdf_name = self.generate_additional_page_for_i_131(
            complete_pdf_name,
            data,
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы восстанавливали '
            f'гражданство в стране, от которой вы'
            f'запрашивали убежище по причине: '
            f'{self.data["RestoredCitizenshipOfLeftCountryReason"]}',
            f"{self.pdf_output_folder_path}{self.user_id}-RestoredCitizenshipOfLeftCountryReason.pdf",
            5
        )

        complete_pdf_name = self.generate_additional_page_for_i_131(
            complete_pdf_name,
            data,
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы приобрели новое '
            f'гражданство по причине: '
            f'{self.data["GotNewCitizenshipReason"]}',
            f"{self.pdf_output_folder_path}{self.user_id}-GotNewCitizenshipReason.pdf",
            6
        )

        complete_pdf_name = self.generate_additional_page_for_i_131(
            complete_pdf_name,
            data,
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вам был предоставлен '
            f'статус беженца или лица, получившего убежище, в любой другой стране по причине: '
            f'{self.data["GotRefugeeStatusElsewhereReason"]}',
            f"{self.pdf_output_folder_path}{self.user_id}-GotRefugeeStatusElsewhereReason.pdf",
            7
        )

        return complete_pdf_name

    def save_json(self):
        import json

        serializable_data = {key: value for key, value in self.data.items()}
        json_str = json.dumps(serializable_data, ensure_ascii=False, indent=4)

        json_str = json_str.replace('/', '//')
        json_str = json_str.replace('\\', '//')

        with open(self.json_input_file_path, 'w', encoding="utf-8") as f:
            f.write(json_str)

    def fill_pdf(self):
        load_dotenv()
        executable_path = os.getenv("EXECUTABLE_PATH")
        pdf_input_file_path = self.pdf_input_file_path
        json_input_file_path = self.json_input_file_path
        pdf_output_file_path = self.pdf_output_file_path

        subprocess.run([executable_path, pdf_input_file_path, json_input_file_path, pdf_output_file_path])
        if self.data['form_identifier'] == "I-131":
            return self.fill_additional_page_for_i_131_form()

        return pdf_output_file_path
