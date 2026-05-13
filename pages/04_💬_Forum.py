import streamlit as st
import pandas as pd

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# Το δικό σου ID αρχείου από το Google Sheet
SHEET_ID = "1d0Nr5QNiwq3OUbUN9sgieNy519CXv5Ui9Sqla_niYIU"

# Η ΣΩΣΤΗ ΚΑΙ ΠΛΗΡΗΣ ΔΙΕΥΘΥΝΣΗ για τράβηγμα δεδομένων CSV
DATA_URL = f"google.com{SHEET_ID}/export?format=csv"

st.title("💬 Forum Τεχνικής Υποστήριξης")
st.markdown("---")

# Περιοχή Επισκέπτη
with st.expander("➕ Πώς να κάνετε μια ερώτηση"):
    st.info("Για να υποβάλετε μια νέα ερώτηση, πατήστε το κουμπί 'Διαχείριση' στο πλάι για να μπείτε στο Sheet (αν είστε ο Νεκτάριος) ή στείλτε τη μήνυμα.")
    st.write("Οι ερωτήσεις και οι απαντήσεις εμφανίζονται αυτόματα παρακάτω.")

st.subheader("Πρόσφατες Συζητήσεις")

# Διάβασμα και Εμφάνιση Δεδομένων
try:
    # Διαβάζουμε το Sheet με εξαναγκασμένο refresh
    df = pd.read_csv(DATA_URL)
    
    # Καθαρίζουμε τυχόν κενά από τα ονόματα των στηλών
    df.columns = df.columns.str.strip()
    
    if not df.empty:
        # Φιλτράρουμε ώστε να δείχνει μόνο τις γραμμές που έχουν γραμμένη ερώτηση (3η στήλη = index 2)
        df = df.dropna(subset=[df.columns[2]])
        
        for index, row in df.iterrows():
            with st.container():
                # Παίρνουμε τα δεδομένα με βάση τη σειρά των στηλών (0=Ημερομηνία, 1=Όνομα, 2=Ερώτηση, 3=Απάντηση)
                hmerominia = row.iloc[0] if pd.notna(row.iloc[0]) else "-"
                onoma = row.iloc[1] if pd.notna(row.iloc[1]) else "Επισκέπτης"
                erotisi = row.iloc[2]
                apantisi = row.iloc[3] if len(row) > 3 and pd.notna(row.iloc[3]) else None
                
                # Εμφάνιση στην οθόνη
                st.markdown(f"**👤 {onoma}** | 📅 {hmerominia}")
                st.info(f"❓ {erotisi}")
                
                if apantisi and str(apantisi).strip() != "" and str(apantisi).lower() != "nan":
                    st.success(f"✅ **Απάντηση Νεκτάριου:** {apantisi}")
                else:
                    st.warning("🕒 *Αναμένεται απάντηση από τον Νεκτάριο...*")
                st.write("---")
    else:
        st.write("Δεν υπάρχουν ακόμα διαθέσιμες συζητήσεις.")

except Exception as e:
    st.error("⚠️ Η σύνδεση με το Google Sheets ανανεώνεται. Παρακαλώ κάντε ένα Refresh στη σελίδα σας.")

# ΚΡΥΦΗ ΠΕΡΙΟΧΗ ΔΙΑΧΕΙΡΙΣΗΣ (Sidebar)
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")

if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες Νεκτάριε!")
    # Το σωστό link για να ανοίγει το Excel σου απευθείας
    edit_url = f"google.com{SHEET_ID}/edit#gid=0"
    st.sidebar.link_button("📝 Απάντησε / Σβήσε Ερωτήσεις", edit_url)
