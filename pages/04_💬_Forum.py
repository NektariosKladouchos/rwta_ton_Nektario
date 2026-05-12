import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Forum - Geyer", page_icon="💬", layout="wide")

st.title("💬 Forum Ερωτήσεων & Απαντήσεων")
st.write("---")

# Το αρχείο που θα κρατάει τις ερωτήσεις
DB_FILE = "forum_messages.csv"

# Αν δεν υπάρχει το αρχείο, το φτιάχνουμε
if not os.path.exists(DB_FILE):
    df = pd.DataFrame(columns=["Ημερομηνία", "Όνομα", "Ερώτηση", "Απάντηση"])
    df.to_csv(DB_FILE, index=False)

# Φόρμα για τον πελάτη
with st.expander("➕ Κάντε μια ερώτηση στον Νεκτάριο"):
    with st.form("forum_form"):
        user_name = st.text_input("Το όνομά σας:")
        user_question = st.text_area("Η ερώτησή σας:")
        submit = st.form_submit_button("Υποβολή Ερώτησης")
        
        if submit and user_name and user_question:
            new_row = pd.DataFrame([[datetime.now().strftime("%d/%m/%Y"), user_name, user_question, "Αναμένεται απάντηση"]], 
                                    columns=["Ημερομηνία", "Όνομα", "Ερώτηση", "Απάντηση"])
            df_existing = pd.read_csv(DB_FILE)
            df_final = pd.concat([new_row, df_existing], ignore_index=True)
            df_final.to_csv(DB_FILE, index=False)
            st.success("Η ερώτησή σας στάλθηκε! Θα απαντηθεί σύντομα.")
            st.rerun()

# Εμφάνιση των ερωτήσεων
st.subheader("Πρόσφατες Ερωτήσεις")
df_display = pd.read_csv(DB_FILE)

for index, row in df_display.iterrows():
    with st.container():
        st.info(f"👤 **{row['Όνομα']}** | 📅 {row['Ημερομηνία']}")
        st.write(f"❓ {row['Ερώτηση']}")
        st.warning(f"✅ **Απάντηση:** {row['Απάντηση']}")
        st.write("---")
