import streamlit as st
import pandas as pd

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# Το link σου για απευθείας ανάγνωση (CSV format)
# ΠΡΟΣΟΧΗ: Αυτό το link δουλεύει μόνο αν το Sheet είναι "Οποιοσδήποτε διαθέτει τον σύνδεσμο"
sheet_id = "1d0Nr5QNiwq3OUbUN9sgieNy519CXv5Ui9Sqla_niYIU"
sheet_url = "https://google.com"


st.title("💬 Forum Τεχνικής Υποστήριξης")
st.write("---")

# Φόρμα Ερώτησης (Μήνυμα προς τον χρήστη)
with st.expander("➕ Κάντε μια ερώτηση στον Νεκτάριο"):
    st.info("Για να υποβάλετε ερώτηση, επικοινωνήστε απευθείας ή περιμένετε την ενεργοποίηση της αυτόματης φόρμας.")
    st.write("Προς το παρόν, μπορείτε να βλέπετε τις απαντήσεις στις συχνές ερωτήσεις παρακάτω.")

st.subheader("Πρόσφατες Συζητήσεις")

# Προσπάθεια ανάγνωσης των δεδομένων
try:
    # Προσθέτουμε ένα τυχαίο νούμερο στο τέλος για να μην "κολλάει" σε παλιά δεδομένα (cache)
    df = pd.read_csv(sheet_url)
    
    if not df.empty:
        for index, row in df.iterrows():
            # Έλεγχος αν η γραμμή έχει ερώτηση (να μην είναι άδεια)
            if pd.notna(row['Ερώτηση']):
                with st.container():
                    st.markdown(f"**👤 {row['Όνομα']}** | 📅 {row['Ημερομηνία']}")
                    st.info(f"❓ {row['Ερώτηση']}")
                    if pd.notna(row['Απάντηση']):
                        st.success(f"✅ **Απάντηση:** {row['Απάντηση']}")
                    else:
                        st.warning("🕒 *Αναμένεται απάντηση από τον Νεκτάριο...*")
                    st.write("---")
    else:
        st.write("Δεν υπάρχουν ακόμα συζητήσεις.")
except Exception as e:
    st.error("Σύνδεση σε αναμονή... Βεβαιωθείτε ότι έχετε προσθέσει τουλάχιστον μία ερώτηση στο Google Sheet.")

# Διαχείριση (Sidebar)
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")
if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες!")
    st.sidebar.link_button("📝 Διαχείριση Ερωτήσεων (Google Sheets)", "https://google.com1d0Nr5QNiwq3OUbUN9sgieNy519CXv5Ui9Sqla_niYIU/edit")
