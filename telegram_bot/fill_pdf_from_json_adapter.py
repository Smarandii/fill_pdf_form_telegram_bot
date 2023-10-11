import os
import PyPDF2
import subprocess
from dotenv import load_dotenv
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont

class FillPdfFromJsonAdapter:
    forms_identifier_to_pdf_files_mapping = {"AR-11": "../pdf_inputs/ar-11-unlocked.pdf",
                                             "I-589": "../pdf_inputs/i-589-unlocked.pdf",
                                             "I-765": "../pdf_inputs/i-765-unlocked.pdf",
                                             "I-485": "../pdf_inputs/i-485-unlocked.pdf",
                                             "I-131": "../pdf_inputs/i-131-unlocked.pdf"}

    def __init__(self, data, form_identifier, user_id, timestamp):
        self.pdf_output_folder_path = r"../pdf_outputs/"
        self.user_id = user_id
        self.data = data
        self.pdf_input_file_path = FillPdfFromJsonAdapter.forms_identifier_to_pdf_files_mapping[form_identifier]
        self.json_input_file_path = rf"../json_inputs/{user_id}-{form_identifier}-{timestamp}.json"
        self.pdf_output_file_path = rf"{self.pdf_output_folder_path}{form_identifier}-{user_id}.pdf"

    def register_cyrilic_font(self, c):
        pdfmetrics.registerFont(TTFont('DejaVuSans', r'../static/fonts/DejaVuSans.ttf'))
        c.setFont('DejaVuSans', 12)
        return c

    def create_additional_text_page_for_i_131_form(self, output_filename, custom_text):
        try:
            c = canvas.Canvas(output_filename, pagesize=letter)
            width, height = letter
            c = self.register_cyrilic_font(c)
            c.drawString(100, height - 100, f'Full name: {self.data["[0].Line1a_FamilyName[0]"]} '
                                            f'{self.data["[0].Line1b_GivenName[0]"]} '
                                            f'{self.data["[0].Line1c_MiddleName[0]"]}')
            c.drawString(100, height - 130, f'Alien Number: {self.data["[0].#area[1].Line3_AlienNumber[0]"]}')

            number_of_lines = len(custom_text) // 62 + custom_text.count("\n")
            cursor_position = 0
            for n in range(number_of_lines):
                line = ""
                counter = 0
                for symbol in custom_text[cursor_position::]:
                    if symbol == "\n":
                        break
                    line += symbol
                    counter += 1
                    cursor_position += 1
                    if counter >= 62:
                        break
                c.drawString(100, height - 200 - (n * 30), line)
            c.save()
        except KeyError:
            c = canvas.Canvas(output_filename, pagesize=letter)
            c.save()

    def merge_pdfs(self, pdf_list, output_filename):
        pdf_merger = PyPDF2.PdfMerger()
        for pdf in pdf_list:
            pdf_merger.append(pdf)
        with open(output_filename, "wb") as output_filehandle:
            pdf_merger.write(output_filehandle)

    def fill_additional_page_for_i_131_form(self):

        complete_pdf_name = self.pdf_output_file_path

        additional_page = f"{self.pdf_output_folder_path}{self.user_id}-IntendToComeBackExplanation.pdf"

        custom_text_for_IntendToComeBackExplanation = (f'Вы собираетесь вернуться в страну, от которой вы '
                                                       f'запрашивали убежище по причине:\n'
                                                       f'{self.data["IntendToComeBackExplanation"]}')
        self.create_additional_text_page_for_i_131_form(additional_page, custom_text_for_IntendToComeBackExplanation)
        tmp_file_name = f"{self.pdf_output_folder_path}1-{self.user_id}-{self.data['form_identifier']}-additional-pages.pdf"
        self.merge_pdfs([complete_pdf_name, additional_page], tmp_file_name)
        complete_pdf_name = tmp_file_name


        additional_page = f"{self.pdf_output_folder_path}{self.user_id}-ReasonOfComeBackExplanation.pdf"

        custom_text_for_ReasonOfComeBackExplanation = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы возвращались в '
            f'страну, от которой вы'
            f'запрашивали убежище по причине:'
            f'{self.data["ReasonOfComeBackExplanation"]}')
        self.create_additional_text_page_for_i_131_form(additional_page, custom_text_for_ReasonOfComeBackExplanation)
        tmp_file_name = f"{self.pdf_output_folder_path}2-{self.user_id}-{self.data['form_identifier']}-additional-pages.pdf"
        self.merge_pdfs([complete_pdf_name, additional_page], tmp_file_name)
        complete_pdf_name = tmp_file_name

        additional_page = f"{self.pdf_output_folder_path}{self.user_id}-ReasonOfIssuedPassport.pdf"
        custom_text_for_ReasonOfIssuedPassport = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы подавали заявку на '
            f'получение или получали национальный паспорт, подавали заявку на обновление или обновляли имеющийся '
            f'паспорт, подавали заявку или получали разрешение на въезд в страну, от которой вы'
            f'запрашивали убежище по причине:'
            f'{self.data["ReasonOfIssuedPassport"]}')
        self.create_additional_text_page_for_i_131_form(additional_page, custom_text_for_ReasonOfIssuedPassport)
        tmp_file_name = (f"{self.pdf_output_folder_path}3-{self.user_id}-"
                         f"{self.data['form_identifier']}-additional-pages.pdf")
        self.merge_pdfs([complete_pdf_name, additional_page], tmp_file_name)
        complete_pdf_name = tmp_file_name

        additional_page = f"{self.pdf_output_folder_path}{self.user_id}-TellAboutHelpFromGovernment.pdf"
        custom_text_for_TellAboutHelpFromGovernment = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы подавали заявку на '
            f'получение или получали какие-либо выплаты или пособия в стране, от которой вы'
            f'запрашивали убежище по причине:'
            f'{self.data["TellAboutHelpFromGovernment"]}')
        self.create_additional_text_page_for_i_131_form(additional_page, custom_text_for_TellAboutHelpFromGovernment)
        tmp_file_name = (f"{self.pdf_output_folder_path}4-{self.user_id}-"
                         f"{self.data['form_identifier']}-additional-pages.pdf")
        self.merge_pdfs([complete_pdf_name, additional_page], tmp_file_name)
        complete_pdf_name = tmp_file_name

        additional_page = f"{self.pdf_output_folder_path}{self.user_id}-RestoredCitizenshipOfLeftCountryReason.pdf"
        custom_text_for_RestoredCitizenshipOfLeftCountryReason = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы восстанавливали '
            f'гражданство в стране, от которой вы'
            f'запрашивали убежище по причине:'
            f'{self.data["RestoredCitizenshipOfLeftCountryReason"]}')
        self.create_additional_text_page_for_i_131_form(additional_page,
                                                        custom_text_for_RestoredCitizenshipOfLeftCountryReason)
        tmp_file_name = (f"{self.pdf_output_folder_path}5-{self.user_id}-"
                         f"{self.data['form_identifier']}-additional-pages.pdf")
        self.merge_pdfs([complete_pdf_name, additional_page], tmp_file_name)
        complete_pdf_name = tmp_file_name

        additional_page = f"{self.pdf_output_folder_path}{self.user_id}-GotNewCitizenshipReason.pdf"
        custom_text_for_GotNewCitizenshipReason = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы приобрели новое '
            f'гражданство по причине:'
            f'{self.data["GotNewCitizenshipReason"]}')
        tmp_file_name = (f"{self.pdf_output_folder_path}6-{self.user_id}-"
                         f"{self.data['form_identifier']}-additional-pages.pdf")
        self.create_additional_text_page_for_i_131_form(additional_page,
                                                        custom_text_for_GotNewCitizenshipReason)
        self.merge_pdfs([complete_pdf_name, additional_page], tmp_file_name)
        complete_pdf_name = tmp_file_name

        additional_page = f"{self.pdf_output_folder_path}{self.user_id}-GotRefugeeStatusElsewhereReason.pdf"
        custom_text_for_GotRefugeeStatusElsewhereReason = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вам был предоставлен '
            f'статус беженца или лица, получившего убежище, в любой другой стране по причине:\n'
            f'{self.data["GotRefugeeStatusElsewhereReason"]}')
        tmp_file_name = (f"{self.pdf_output_folder_path}7-{self.user_id}-"
                         f"{self.data['form_identifier']}-additional-pages.pdf")
        self.create_additional_text_page_for_i_131_form(additional_page,
                                                        custom_text_for_GotRefugeeStatusElsewhereReason)
        self.merge_pdfs([complete_pdf_name, additional_page], tmp_file_name)
        complete_pdf_name = tmp_file_name

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
