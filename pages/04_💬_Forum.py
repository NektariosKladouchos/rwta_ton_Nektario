import streamlit as st
import pandas as pd

# 1. Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# 2. Σύνδεση με τα δεδομένα (CSV Export)
# Αυτό το link φέρνει ΜΟΝΟ τα κείμενα από το Sheet σου
sheet_id = "1d0Nr5QNiwq3OUbUN9sgieNy519CXv5Ui9Sqla_niYIU"
sheet_url = f"https://google.com{sheet_id}/export?format=csv"

st.title("💬 Forum Τεχνικής Υποστήριξης")
st.markdown("---")

# 3. Περιοχή Επισκέπτη
with st.expander("➕ Πώς να κάνετε μια ερώτηση"):
    st.info("Για να υποβάλετε μια νέα ερώτηση, επικοινωνήστε απευθείας με τον Νεκτάριο.")
    st.write("Οι απαντήσεις εμφανίζονται αυτόματα μόλις καταχωρηθούν στο σύστημα.")

st.subheader("Πρόσφατες Συζητήσεις")

# 4. Διάβασμα και Εμφάνιση Δεδομένων
try:
    # Διάβασμα του CSV
    df = pd.read_csv(sheet_url)
    
    # Καθαρισμός κενών από τους τίτλους των στηλών
    df.columns = df.columns.str.strip()
    
    if not df.empty:
        # Αναζήτηση της στήλης Ερώτηση (με ή χωρίς τόνο)
        col_q = 'Ερώτηση' if 'Ερώτηση' in df.columns else 'Ερωτηση'
        if col_q not in df.columns: col_q = df.columns[2] # Fallback στην 3η στήλη

        # Αφαίρεση κενών γραμμών
        df = df.dropna(subset=[col_q])
        
        for index, row in df.iterrows():
            with st.container():
                onoma = row.get('Όνομα', 'Επισκέπτης')
                hmer = row.get('Ημερομηνία', '-')
                erotisi = row.get(col_q, '')
                
                # Αναζήτηση στήλης Απάντηση
                col_a = 'Απάντηση' if 'Απάντηση' in df.columns else 'Απαντηση'
                if col_a not in df.columns: col_a = df.columns[3] # Fallback στην 4η στήλη
                apantisi = row.get(col_a, None)
                
                st.markdown(f"**👤 {onoma}** | 📅 {hmer}")
                st.info(f"❓ {erotisi}")
                
                if pd.notna(apantisi) and str(apantisi).strip() != "" and str(apantisi).lower() != "nan":
                    st.success(f"✅ **Απάντηση:** {apantisi}")
                else:
                    st.warning("🕒 *Αναμένεται απάντηση...*")
                st.write("---")
    else:
        st.write("Δεν υπάρχουν ακόμα συζητήσεις.")

except Exception as e:
    st.error(f"Σύνδεση σε αναμονή... (Πατήστε Refresh στο site)")

# 5. ΚΡΥΦΗ ΠΕΡΙΟΧΗ ΔΙΑΧΕΙΡΙΣΗΣ (Sidebar)
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")

if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες Νεκτάριε!")
    # Το ΑΠΟΛΥΤΟ link για το αρχείο σου
    edit_url = f"https://google.com{sheet_id}/edit#gid=0"
    st.sidebar.markdown(f"[👉 ΑΝΟΙΓΜΑ GOOGLE SHEET]({edit_url})")
    st.sidebar.caption("Σημείωση: Πρέπει να είστε συνδεδεμένος στο Google λογαριασμό σας.")
