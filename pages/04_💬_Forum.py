import streamlit as st
import pandas as pd

# 1. Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# 2. Σύνδεση με τα δεδομένα (Απευθείας Link)
sheet_url = "https://google.com"

st.title("💬 Forum Τεχνικής Υποστήριξης")
st.markdown("---")

# 3. Περιοχή Επισκέπτη
with st.expander("➕ Πώς να κάνετε μια ερώτηση"):
    st.info("Για να υποβάλετε μια νέα ερώτηση, επικοινωνήστε απευθείας με τον Νεκτάριο.")

st.subheader("Πρόσφατες Συζητήσεις")

# 4. Διάβασμα και Εμφάνιση Δεδομένων
try:
    df = pd.read_csv(sheet_url)
    df.columns = df.columns.str.strip() # Καθαρισμός κενών στις στήλες
    
    if not df.empty:
        # Φιλτράρουμε τις άδειες γραμμές
        df = df.dropna(subset=['Ερώτηση'])
        
        for index, row in df.iterrows():
            with st.container():
                st.markdown(f"**👤 {row.get('Όνομα', 'Επισκέπτης')}** | 📅 {row.get('Ημερομηνία', '-')}")
                st.info(f"❓ {row.get('Ερώτηση', '')}")
                
                apantisi = row.get('Απάντηση')
                if pd.notna(apantisi) and str(apantisi).strip() != "":
                    st.success(f"✅ **Απάντηση:** {apantisi}")
                else:
                    st.warning("🕒 *Αναμένεται απάντηση...*")
                st.write("---")
    else:
        st.write("Δεν υπάρχουν ακόμα συζητήσεις.")
except Exception as e:
    st.error("⚠️ Η σύνδεση με το Google Sheets καθυστερεί. Παρακαλώ κάντε Refresh στη σελίδα.")

# 5. ΚΡΥΦΗ ΠΕΡΙΟΧΗ ΔΙΑΧΕΙΡΙΣΗΣ (Sidebar)
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")

if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες Νεκτάριε!")
    # Το σωστό link για να ανοίγει το Excel σου
    direct_link = "https://google.com"
    st.sidebar.markdown(f"[👉 ΑΝΟΙΓΜΑ GOOGLE SHEET]({direct_link})")
