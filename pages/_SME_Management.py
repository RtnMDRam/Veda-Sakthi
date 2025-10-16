import streamlit as st
import pandas as pd
import os

# --- CONFIGURATION ---
CSV_FILE = "SME_Name_Trial.csv"  # Change to your master file name

# --- LOAD DATA ---
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    df = pd.DataFrame(columns=[
        "PrefixSalutation", "SME Name", "Initial", "Email", "WhatsApp",
        "Subject 1", "Subject 2", "Subject 3", "Date of Birth", "Gender", "Photo",
        "Address", "Place", "Pincode", "Taluk", "District", "Block ID", "Block Name",
        "Education", "Experience"
    ])

st.title("Admin: SME Management Panel")

# --- DISPLAY EXISTING SMEs ---
st.subheader("Current SMEs")
st.dataframe(df, use_container_width=True)

with st.expander("➕ Add a new SME"):
    cols = st.columns(3)
    prefix = cols[0].text_input("Prefix/Salutation")
    name = cols[1].text_input("SME Name")
    ini = cols[2].text_input("Initial")
    email = cols[0].text_input("Email")
    whatsapp = cols[1].text_input("WhatsApp")
    subj1 = cols[2].text_input("Subject 1")
    subj2 = cols[0].text_input("Subject 2")
    subj3 = cols[1].text_input("Subject 3")
    dob = cols[2].date_input("Date of Birth")
    gender = cols[0].selectbox("Gender", ["Male", "Female", "Other"])
    photo = cols[1].text_input("Photo (URL)")
    address = cols[2].text_input("Address")
    place = cols[0].text_input("Place")
    pincode = cols[1].text_input("Pincode")
    taluk = cols[2].text_input("Taluk")
    district = cols[0].text_input("District")
    blockid = cols[1].text_input("Block ID")
    blockname = cols[2].text_input("Block Name")
    education = cols[0].text_input("Educational Qualification")
    experience = cols[1].text_input("Experience (years)")

    if st.button("Add SME"):
        new_row = {
            "PrefixSalutation": prefix,
            "SME Name": name,
            "Initial": ini,
            "Email": email,
            "WhatsApp": whatsapp,
            "Subject 1": subj1,
            "Subject 2": subj2,
            "Subject 3": subj3,
            "Date of Birth": dob,
            "Gender": gender,
            "Photo": photo,
            "Address": address,
            "Place": place,
            "Pincode": pincode,
            "Taluk": taluk,
            "District": district,
            "Block ID": blockid,
            "Block Name": blockname,
            "Education": education,
            "Experience": experience
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)
        st.success("Added SME! Refresh page to see in table.")

# --- DOWNLOAD MASTER AS CSV ---
st.download_button(
    label="Download Complete SME Master CSV",
    data=df.to_csv(index=False),
    file_name="SME_Master.csv",
    mime="text/csv"
)
