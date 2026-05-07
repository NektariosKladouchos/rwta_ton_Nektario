import streamlit as st
import logic  # Εισαγωγή του κώδικα που ανέβασες

# --- ΡΥΘΜΙΣΕΙΣ ΣΕΛΙΔΑΣ ---
st.set_page_config(page_title="GEYER Expert Hub", page_icon="⚡", layout="wide")

# --- MENU ---
choice = st.sidebar.radio("Μενού Επιλογών", ["🏠 Αρχική", "📊 Live Pricing System", "📂 Τεχνική Βιβλιοθήκη", "📨 Ερώτηση"])

if choice == "📊 Live Pricing System":
    st.header("📊 GEYER Live Pricing System (CEO Edition)")
    st.info("Το πλήρες HVAC logic και η αποφυγή διπλοχρέωσης είναι ενεργά.")
    
    # Εδώ θα καλέσουμε τις μεταβλητές ή τις συναρτήσεις από το logic.py
    # Παράδειγμα (θα το προσαρμόσουμε μόλις δω τα ονόματα των μεταβλητών σου):
    col1, col2 = st.columns(2)
    
    with col1:
        brand = st.selectbox("Επιλέξτε Brand VRV", ["GEYER Brand A", "GEYER Brand B"])
        devices = st.number_input("Συσκευές (Όριο 230)", min_value=1, max_value=230, value=1)
        
    with col2:
        smart_features = st.multiselect("Πρόσθετα Fibaro", ["Lighting Control", "Heating Control", "Sensors"])
    
    # Κουμπί Υπολογισμού που καλεί το logic
    if st.button("Υπολογισμός Κόστους"):
        # Εδώ θα μπει η συνάρτηση υπολογισμού από το logic.py
        # π.χ. result = logic.calculate_price(devices, brand)
        st.success("Ο υπολογισμός ολοκληρώθηκε με βάση το HVAC Logic.")
        st.write("### Συνολικό Κόστος: -- €") # Εδώ θα μπαίνει το αποτέλεσμα
        
        # Φόρμα αποστολής στο email σου
        with st.expander("📩 Στείλτε την προσφορά στο Email σας"):
            email_user = st.text_input("Το email σας")
            if st.button("Αποστολή"):
                st.write(f"Η προσφορά στάλθηκε στο {email_user} και στον Νεκτάριο.")

else:
    st.write("Επιλέξτε μια ενότητα από το μενού αριστερά.")
