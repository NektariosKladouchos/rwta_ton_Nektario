import streamlit as st
import pandas as pd
from datetime import datetime

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# Σύνδεση με το Google Sheet
# ΑΝΤΙΚΑΤΑΣΤΑΣΗ: Εδώ βάζουμε το link σου σε μορφή εξαγωγής CSV
sheet_url = "https://google.com"

def load_data():
    return pd.read_csv(sheet_url)

st.title("💬 Forum Τεχνικής Υποστήριξης")
st.markdown("---")

# --- ΠΕΡΙΟΧΗ ΕΠΙΣΚΕΠΤΗ ---
with st.expander("➕ Κάντε μια ερώτηση στον Νεκτάριο"):
    with st.form("public_form"):
        name = st.text_input("Το όνομά σας:")
        question = st.text_area("Η ερώτησή σας:")
        submit = st.form_submit_button("Υποβολή")
        
        if submit and name and question:
            st.warning("⚠️ Η αυτόματη υποβολή απαιτεί σύνδεση Google. Για τώρα, η ερώτησή σας θα εμφανιστεί μόλις την εγκρίνει ο Νεκτάριος.")
            # Εδώ αργότερα θα προσθέσουμε την αυτόματη εγγραφή

# --- ΕΜΦΑΝΙΣΗ ΕΡΩΤΗΣΕΩΝ ---
st.subheader("Πρόσφατες Συζητήσεις")
try:
    df = load_data()
    for index, row in df.iterrows():
        if pd.notna(row['Ερώτηση']):
            with st.container():
                st.info(f"👤 **{row['Όνομα']}** | 📅 {row['Ημερομηνία']}")
                st.write(f"❓ {row['Ερώτηση']}")
                if pd.notna(row['Απάντηση']):
                    st.success(f"✅ **Απάντηση Νεκτάριου:** {row['Απάντηση']}")
                else:
                    st.write("🕒 *Αναμένεται απάντηση...*")
                st.write("---")
except:
    st.error("Δεν ήταν δυνατή η φόρτωση των δεδομένων.")

# --- ΚΡΥΦΗ ΠΕΡΙΟΧΗ ΔΙΑΧΕΙΡΙΣΗΣ ---
st.sidebar.markdown("---")
admin_pass = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")

if admin_pass == "geyer123": # Αυτός είναι ο κωδικός σου
    st.sidebar.success("Καλώς ήρθες Νεκτάριε!")
    st.sidebar.markdown(f"[👉 Πάτα εδώ για να Απαντήσεις ή να Σβήσεις]({sheet_url.replace('/export?format=csv', '/edit')})")
