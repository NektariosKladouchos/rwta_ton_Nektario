import streamlit as st
import pandas as pd

# 1. Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# 2. Σύνδεση με το Δημοσιευμένο Google Sheet (CSV format)
sheet_url = "https://google.com"


st.title("💬 Forum Τεχνικής Υποστήριξης")
st.markdown("---")

# 3. Περιοχή Επισκέπτη (Οδηγίες)
with st.expander("➕ Πώς να κάνετε μια ερώτηση"):
    st.info("Για να υποβάλετε μια νέα ερώτηση, επικοινωνήστε απευθείας με τον Νεκτάριο ή περιμένετε την έγκριση της ερώτησής σας στο Sheet.")
    st.write("Οι απαντήσεις εμφανίζονται αυτόματα μόλις καταχωρηθούν από τον διαχειριστή.")

st.subheader("Πρόσφατες Συζητήσεις")

# 4. Διάβασμα και Εμφάνιση Δεδομένων
try:
    # Διάβασμα του CSV από το Google Sheets
    df = pd.read_csv(sheet_url)
    
    # Καθαρισμός των ονομάτων των στηλών από κενά διαστήματα
    df.columns = df.columns.str.strip()
    
    if not df.empty:
        # Επιλέγουμε τη σωστή στήλη για έλεγχο (Ερώτηση)
        # Χρησιμοποιούμε δυναμική αναζήτηση αν υπάρχει ο τόνος ή όχι
        col_q = 'Ερώτηση' if 'Ερώτηση' in df.columns else df.columns[2]
        
        # Αφαιρούμε τις τελείως κενές γραμμές
        df = df.dropna(subset=[col_q])
        
        for index, row in df.iterrows():
            with st.container():
                # Λήψη δεδομένων με ασφάλεια (fallback τιμές αν λείπει κάτι)
                onoma = row.get('Όνομα', 'Επισκέπτης')
                hmer = row.get('Ημερομηνία', '-')
                erotisi = row.get(col_q, '')
                # Αναζήτηση στήλης Απάντηση
                col_a = 'Απάντηση' if 'Απάντηση' in df.columns else df.columns[3]
                apantisi = row.get(col_a, None)
                
                # Εμφάνιση στην οθόνη
                st.markdown(f"**👤 {onoma}** | 📅 {hmer}")
                st.info(f"❓ {erotisi}")
                
                if pd.notna(apantisi) and str(apantisi).strip() != "" and str(apantisi).strip().lower() != "nan":
                    st.success(f"✅ **Απάντηση:** {apantisi}")
                else:
                    st.warning("🕒 *Αναμένεται απάντηση από τον Νεκτάριο...*")
                st.write("---")
    else:
        st.write("Δεν υπάρχουν ακόμα διαθέσιμες συζητήσεις.")

except Exception as e:
    st.error(f"Σύνδεση σε αναμονή... (Τεχνικό Σφάλμα: {e})")

# 5. Κρυφή Περιοχή Διαχείρισης (Sidebar)
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")

if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες Νεκτάριε!")
    # Link που οδηγεί στο αρχείο για επεξεργασία (ΟΧΙ το public link)
    edit_url = "https://google.com"
    st.sidebar.link_button("📝 Απάντησε / Σβήσε Ερωτήσεις", edit_url)
