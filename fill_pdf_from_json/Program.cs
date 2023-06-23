using System;
using System.IO;
using iText.Kernel.Pdf;
using iText.Forms;
using iText.Forms.Xfa;
using iText.Forms.Fields;
using System.Xml.Linq;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using iText.Layout.Properties;


class PdfFormFiller
{
    private static string XFAFilePathInput = @"";
    private static string JsonFileInput = @"";
    private static string XFAFilePathOutput = @"";
    
    static void Main(string[] args)
    {
        Console.WriteLine("pdf_input: " + args[0] + " json_input " + args[1] + " pdf_output " + args[2]);
        XFAFilePathInput = args[0];
        JsonFileInput = args[1];
        XFAFilePathOutput = args[2];
        FillPdfFieldsWithJsonValues();
    }

    public static string generateJsonKeyForPdfFieldKey(string initialFieldKey)
    {
        Console.WriteLine(initialFieldKey);
        string jsonKey = initialFieldKey.Replace("form1[0].#subform[0]", "");
        jsonKey = jsonKey.Replace("[0]", "");
        jsonKey = jsonKey.Replace("[1]", "_1");
        jsonKey = jsonKey.Replace("[2]", "_2");
        jsonKey = jsonKey.Replace(".", "");
        jsonKey = jsonKey.Replace("__", "_");

        if (jsonKey.Length > 0 || jsonKey != "form" || jsonKey != "form1")
            return jsonKey;
        else
            return "";
    }

    public static JObject getInputJsonValues()
    {
        string jsonString = File.ReadAllText(JsonFileInput);
        JObject inputJsonValues = JObject.Parse(jsonString);
        return inputJsonValues;
    }

    public static int getIndexOfSelectedState(KeyValuePair<string, PdfFormField> pdfField, JObject inputJsonValues, string jsonKey)
    {
        PdfArray options = pdfField.Value.GetOptions();
        int cnt = 0;
        foreach (PdfObject option in options)
        {
            if (option.ToString().Contains(Convert.ToString(inputJsonValues[jsonKey])))
            {
                break;
            }
            cnt++;
        }
        return cnt;
    }

    public static void FillPdfFieldsWithJsonValues()
    {
        using (PdfReader reader = new PdfReader(XFAFilePathInput))
        using (PdfWriter writer = new PdfWriter(XFAFilePathOutput))
        using (PdfDocument pdfDoc = new PdfDocument(reader, writer))
        {
            PdfAcroForm form = PdfAcroForm.GetAcroForm(pdfDoc, true);
            IDictionary<String, PdfFormField> fieldsDictionary = form.GetAllFormFields();

            JObject inputJsonValues = getInputJsonValues();
            foreach (KeyValuePair<string, PdfFormField> pdfField in fieldsDictionary)
            {

                string jsonKey = generateJsonKeyForPdfFieldKey(pdfField.Key);
                if (jsonKey != "")
                {
                    if (jsonKey == "S2B_State" || jsonKey == "S2C_State" || jsonKey == "S2A_State")
                    {
                        PdfChoiceFormField stateChoiceField = (PdfChoiceFormField)pdfField.Value;
                        int indexOfSelectedState = getIndexOfSelectedState(pdfField, inputJsonValues, jsonKey);
                        int[] ListSelected = { indexOfSelectedState };
                        stateChoiceField.SetListSelected(ListSelected);
                    }
                    else
                    {

                        pdfField.Value.SetValue(Convert.ToString(inputJsonValues[jsonKey]));
                    }
                    Console.WriteLine("Field: " + jsonKey);
                }
            }
            pdfDoc.Close();
        }


    }
}
