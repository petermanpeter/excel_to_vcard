import streamlit as st
import pandas as pd
import math

def excel_to_vcf(df):
    vcf_lines = []
    for _, row in df.iterrows():
        name = row['Contact_Mum_Name']
        if not(pd.isna(row['Mum_phone'])):
            phone = str(int(row['Mum_phone']))
            vcf_lines.append(f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
END:VCARD
""")
        name = row['Contact_Dad_Name']
        if not(pd.isna(row['Dad_phone'])):
            phone = str(int(row['Dad_phone']))
            vcf_lines.append(f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
END:VCARD
""")
    return "\n".join(vcf_lines)

st.title("Excel to vCard Converter")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    vcf_content = excel_to_vcf(df)
    st.download_button("Download vCard file", vcf_content, file_name="contacts.vcf", mime="text/vcard")

