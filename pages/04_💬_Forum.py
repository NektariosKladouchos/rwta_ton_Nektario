import streamlit as st
import pandas as pd

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# Το Link σου σε ειδική μορφή που η Google ΔΕΝ μπορεί να μπλοκάρει
# Το link σου σε μορφή που διαβάζεται από παντού
# Το νέο δημοσιευμένο link σου
sheet_url = "https://google.com"


st.title("💬 Forum Τεχνικής Υποστήριξης")
st.write("---")

# Φόρμα Ερώτησης
with st.expander("➕ Κάντε μια ερώτηση στον Νεκτάριο"):
    st.info("Για υποβολή ερώτησης, χρησιμοποιήστε το κουμπί 'Διαχείριση' στο πλάι για να μπείτε στο Sheet, ή περιμένετε την ενεργοποίηση της φόρμας.")

st.subheader("Πρόσφατες Συζητήσεις")

# Διάβασμα δεδομένων με "Force Refresh"
try:
    # Το κολπάκι με το skiprows=0 διασφαλίζει ότι διαβάζει από την αρχή
    df = pd.read_csv(sheet_url, on_bad_lines='skip')
    
    if not df.empty:
        # Καθαρίζουμε τυχόν κενές γραμμές
        df = df.dropna(subset=['Ερώτηση'])
        
        for index, row in df.iterrows():
            with st.container():
                st.markdown(f"**👤 {row['Όνομα']}** | 📅 {row['Ημερομηνία']}")
                st.info(f"❓ {row['Ερώτηση']}")
                if pd.notna(row['Απάντηση']):
                    st.success(f"✅ **Απάντηση:** {row['Απάντηση']}")
                else:
                    st.warning("🕒 *Αναμένεται απάντηση...*")
                st.write("---")
    else:
        st.write("Δεν βρέθηκαν ερωτήσεις.")
except Exception as e:
    st.error(f"Σύνδεση σε αναμονή... (Τεχνικό: {e})")

# Διαχείριση (Sidebar)
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")
if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες!")
    st.sidebar.link_button("📝 Απάντησε / Σβήσε Ερωτήσεις", "https://google.com1d0Nr5QNiwq3OUbUN9sgieNy519CXv5Ui9Sqla_niYIU/edit")
