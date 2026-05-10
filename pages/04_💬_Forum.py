
import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Forum - Ρώτα τον Νεκτάριο", layout="wide")

st.title("💬 Forum Ερωτήσεων & Απαντήσεων")
st.markdown("---")

# Αρχείο για αποθήκευση των δεδομένων
DB_FILE = "forum_data.csv"

# Συνάρτηση για φόρτωση δεδομένων
def load_data():
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    else:
        return pd.DataFrame(columns=["Ημερομηνία", "Όνομα", "Ερώτηση", "Απάντηση"])

# Φόρμα υποβολής ερώτησης
with st.expander("➕ Κάντε μια νέα ερώτηση"):
    with st.form("question_form"):
        name = st.text_input("Το όνομά σας:")
        question = st.text_area("Η ερώτησή σας:")
        submitted = st.form_submit_button("Υποβολή")
        
        if submitted and name and question:
            new_data = pd.DataFrame([[datetime.now().strftime("%d/%m/%Y %H:%M"), name, question, "Αναμένεται απάντηση..."]], 
                                    columns=["Ημερομηνία", "Όνομα", "Ερώτηση", "Απάντηση"])
            df = load_data()
            df = pd.concat([new_data, df], ignore_index=True)
            df.to_csv(DB_FILE, index=False)
            st.success("Η ερώτησή σας υποβλήθηκε! Ο Νεκτάριος θα απαντήσει σύντομα.")
            st.rerun()

# Εμφάνιση ερωτήσεων
st.subheader("Πρόσφατες Συζητήσεις")
df = load_data()

for index, row in df.iterrows():
    with st.container():
        st.info(f"**{row['Όνομα']}** ({row['Ημερομηνία']})")
        st.write(f"❓ {row['Ερώτηση']}")
        st.warning(f"✅ **Απάντηση Νεκτάριου:** {row['Απάντηση']}")
        st.markdown("---")
