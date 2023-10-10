import os
import PyPDF2
import subprocess
from dotenv import load_dotenv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class FillPdfFromJsonAdapter:
    forms_identifier_to_pdf_files_mapping = {"AR-11": "../pdf_inputs/ar-11-unlocked.pdf",
                                             "I-589": "../pdf_inputs/i-589-unlocked.pdf",
                                             "I-765": "../pdf_inputs/i-765-unlocked.pdf",
                                             "I-485": "../pdf_inputs/i-485-unlocked.pdf",
                                             "I-131": "../pdf_inputs/i-131-unlocked.pdf"}

    def __init__(self, data, form_identifier, user_id, timestamp):
        self.user_id = user_id
        self.data = data
        self.pdf_input_file_path = FillPdfFromJsonAdapter.forms_identifier_to_pdf_files_mapping[form_identifier]
        self.json_input_file_path = rf"../json_inputs/{user_id}-{form_identifier}-{timestamp}.json"
        self.pdf_output_file_path = rf"../pdf_outputs/{form_identifier}-{user_id}.pdf"

    def create_additional_text_page_for_i_131_form(self, output_filename, custom_text):
        try:
            c = canvas.Canvas(output_filename, pagesize=letter)
            width, height = letter
            c.drawString(100, height - 100, f'Full name: {self.data["[0].Line1a_FamilyName[0]"]} '
                                            f'{self.data["[0].Line1b_GivenName[0]"]} '
                                            f'{self.data["[0].Line1c_MiddleName[0]"]}')
            c.drawString(100, height - 130, f'Alien Number: {self.data["[0].#area[1].Line3_AlienNumber[0]"]}')

            number_of_lines = len(custom_text) // 52
            for n in range(number_of_lines):
                line = ""
                counter = 0
                for symbol in custom_text:
                    line += symbol
                    counter += 1
                    if counter >= 52:
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

    def fill_additional_pages_for_i_131_form(self, pdf_output_file_path):
        complete_pdf_name = pdf_output_file_path.replace(".pdf", "") + "-with-additional-pages.pdf"
        additional_pages = f"{self.user_id}-{self.data['form_identifier']}-additional-pages.pdf"

        custom_text_for_IntendToComeBackExplanation = (f'Вы собираетесь вернуться в страну, от которой вы '
                                                       f'запрашивали убежище по причине:\n'
                                                       f'{self.data["IntendToComeBackExplanation"]}')
        self.create_additional_text_page_for_i_131_form(additional_pages,
                                                        custom_text_for_IntendToComeBackExplanation)
        self.merge_pdfs([complete_pdf_name, additional_pages], "1 " + complete_pdf_name)
        complete_pdf_name = "1 " + complete_pdf_name

        custom_text_for_ReasonOfComeBackExplanation = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы возвращались в '
            f'страну, от которой вы'
            f'запрашивали убежище по причине:\n'
            f'{self.data["ReasonOfComeBackExplanation"]}')
        self.create_additional_text_page_for_i_131_form(additional_pages,
                                                        custom_text_for_ReasonOfComeBackExplanation)
        self.merge_pdfs([complete_pdf_name, additional_pages], "2 " + complete_pdf_name)
        complete_pdf_name = "2 " + complete_pdf_name

        custom_text_for_ReasonOfIssuedPassport = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы подавали заявку на '
            f'получение или получали национальный паспорт, подавали заявку на обновление или обновляли имеющийся '
            f'паспорт, подавали заявку или получали разрешение на въезд в страну, от которой вы'
            f'запрашивали убежище по причине:\n'
            f'{self.data["ReasonOfIssuedPassport"]}')
        self.create_additional_text_page_for_i_131_form(additional_pages,
                                                        custom_text_for_ReasonOfIssuedPassport)
        self.merge_pdfs([pdf_output_file_path, additional_pages], "3 " + complete_pdf_name)
        complete_pdf_name = "3 " + complete_pdf_name

        custom_text_for_TellAboutHelpFromGovernment = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы подавали заявку на '
            f'получение или получали какие-либо выплаты или пособия в стране, от которой вы'
            f'запрашивали убежище по причине:\n'
            f'{self.data["TellAboutHelpFromGovernment"]}')
        self.create_additional_text_page_for_i_131_form(additional_pages,
                                                        custom_text_for_TellAboutHelpFromGovernment)
        self.merge_pdfs([pdf_output_file_path, additional_pages], "4 " + complete_pdf_name)
        complete_pdf_name = "4 " + complete_pdf_name

        custom_text_for_RestoredCitizenshipOfLeftCountryReason = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы восстанавливали '
            f'гражданство в стране, от которой вы'
            f'запрашивали убежище по причине:\n'
            f'{self.data["RestoredCitizenshipOfLeftCountryReason"]}')
        self.create_additional_text_page_for_i_131_form(additional_pages,
                                                        custom_text_for_RestoredCitizenshipOfLeftCountryReason)
        self.merge_pdfs([pdf_output_file_path, additional_pages], "5 " + complete_pdf_name)
        complete_pdf_name = "5 " + complete_pdf_name

        custom_text_for_GotNewCitizenshipReason = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вы приобрели новое '
            f'гражданство по причине:\n'
            f'{self.data["GotNewCitizenshipReason"]}')
        self.create_additional_text_page_for_i_131_form(additional_pages,
                                                        custom_text_for_GotNewCitizenshipReason)
        self.merge_pdfs([pdf_output_file_path, additional_pages], "6 " + complete_pdf_name)
        complete_pdf_name = "6 " + complete_pdf_name

        custom_text_for_GotRefugeeStatusElsewhereReason = (
            f'После того как вам был предоставлен статус беженца/лица, получившего убежище, вам был предоставлен '
            f'статус беженца или лица, получившего убежище, в любой другой стране по причине:\n'
            f'{self.data["GotRefugeeStatusElsewhereReason"]}')
        self.create_additional_text_page_for_i_131_form(additional_pages,
                                                        custom_text_for_GotRefugeeStatusElsewhereReason)
        self.merge_pdfs([pdf_output_file_path, additional_pages], "7 " + complete_pdf_name)
        complete_pdf_name = "7 " + complete_pdf_name

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
            return self.fill_additional_pages_for_i_131_form(pdf_output_file_path)

        return pdf_output_file_path
