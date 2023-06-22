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

public class Item
{
    public string S1_MiddleName { get; set; }
    public string S1_GivenName { get; set; }
    public string S1_FamilyName { get; set; }
    public string S1_DateOfBirth { get; set; }
    public string S2B_State { get; set; }
    public string S2B_ZipCode { get; set; }
    public bool S2B_Unit0 { get; set; }
    public bool S2B_Unit1 { get; set; }
    public bool S2B_Unit2 { get; set; }
    public string S2B_AptSteFlrNumber { get; set; }
    public string S2B_StreetNumberName { get; set; }
    public string S2B_CityOrTown { get; set; }
    public string S2C_State { get; set; }
    public string S2C_ZipCode { get; set; }
    public bool S2C_Unit0 { get; set; }
    public bool S2C_Unit1 { get; set; }
    public bool S2C_Unit2 { get; set; }
    public string S2C_AptSteFlrNumber { get; set; }
    public string S2C_StreetNumberName { get; set; }
    public string S2C_CityOrTown { get; set; }
    public string AlienNumber { get; set; }
    public string S3_SignatureApplicant { get; set; }
    public string S3_DateofSignature { get; set; }
    public string S2A_State { get; set; }
    public string S2A_ZipCode { get; set; }
    public bool S2A_Unit0 { get; set; }
    public bool S2A_Unit1 { get; set; }
    public bool S2A_Unit2 { get; set; }
    public string S2A_AptSteFlrNumber { get; set; }
    public string S2A_StreetNumberName { get; set; }
    public string S2A_CityOrTown { get; set; }
}


class PdfFormFiller
{
    private static string XFAFilePathInput = @"";
    private static string JsonFileInput = @"";
    private static string XFAFilePathOutput = @"";
    
    static void Main(string[] args)
    {
        Console.WriteLine(args[0] + args[1] + args[2]);
        XFAFilePathInput = args[0];
        JsonFileInput = args[1];
        XFAFilePathOutput = args[2];
        Console.ReadKey();
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
