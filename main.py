import streamlit as st
import pandas as pd

# --- ΡΥΘΜΙΣΕΙΣ ΣΕΛΙΔΑΣ ---
st.set_page_config(page_title="GEYER Expert Hub | Νεκτάριος", page_icon="⚡", layout="wide")

# --- CUSTOM CSS ΓΙΑ ΕΠΑΓΓΕΛΜΑΤΙΚΟ LOOK ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-title { color: #1E3A8A; font-size: 40px; font-weight: bold; text-align: center; }
    .feature-card { background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #1E3A8A; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>⚡ GEYER & Fibaro Technical Portal</div>", unsafe_allow_html=True)
st.write("---")

# --- MENU ΠΛΟΗΓΗΣΗΣ ---
choice = st.sidebar.radio("Μενού Επιλογών", ["🏠 Αρχική & Ιδέες", "📊 Live Pricing System", "📂 Τεχνική Βιβλιοθήκη", "📨 Ερώτηση προς Τεχνικό"])

# --- ΕΝΟΤΗΤΑ 1: ΑΡΧΙΚΗ & ΙΔΕΕΣ (Φωτογραφίες Έργων) ---
if choice == "🏠 Αρχική & Ιδέες":
    st.header("📸 Ιδέες & Φωτογραφίες Έργων")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://unsplash.com", caption="Smart Lighting Project")
    with col2:
        st.image("https://unsplash.com", caption="HVAC Control με Fibaro")
    
    st.info("💡 **Tip:** Το Fibaro μπορεί να ελέγξει από τον φωτισμό μέχρι την ασφάλεια του κτιρίου χωρίς νέα καλώδια.")

# --- ΕΝΟΤΗΤΑ 2: LIVE PRICING (Με αποστολή email) ---
elif choice == "📊 Live Pricing System":
    st.header("🧮 Live Pricing & Παραγγελία")
    st.write("Συμπληρώστε τα στοιχεία του έργου και θα λάβετε την εκτίμηση στο email σας.")
    
    with st.form("order_form"):
        name = st.text_input("Ονοματεπώνυμο / Εταιρεία")
        email = st.text_input("Το Email σας")
        project_type = st.selectbox("Τύπος Έργου", ["Κατοικία", "Ξενοδοχείο", "Γραφεία", "Βιομηχανικό"])
        devices = st.slider("Πλήθος Συσκευών", 1, 230, 10)
        smart_upgrade = st.toggle("Επιθυμώ αναβάθμιση σε Fibaro Smart Home")
        msg = st.text_area("Σημειώσεις για το έργο")
        
        submit = st.form_submit_button("📩 Αποστολή Εκτίμησης & Ειδοποίηση Τεχνικού")
        
        if submit:
            # Εδώ χρησιμοποιούμε το FormSubmit (δωρεάν υπηρεσία) για να σου έρχεται email
            # Πρέπει να γραφτείς στο formsubmit.co με το email σου
            st.success(f"Ευχαριστούμε {name}! Η φόρμα στάλθηκε. Θα λάβετε την προσφορά σύντομα.")
            st.toast("Ειδοποίηση στάλθηκε στον Νεκτάριο!")

# --- ΕΝΟΤΗΤΑ 3: ΤΕΧΝΙΚΗ ΒΙΒΛΙΟΘΗΚΗ ---
elif choice == "📂 Τεχνική Βιβλιοθήκη":
    st.header("📄 Σχέδια & Τεχνικά Φυλλάδια")
    st.write("Επιλέξτε το αρχείο που θέλετε να κατεβάσετε:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='feature-card'><b>Σχέδια HVAC</b><br>VRV Connection Diagrams</div>", unsafe_allow_html=True)
        # st.download_button(...) - Εδώ θα μπούν τα κουμπιά όταν ανεβάσεις τα PDF
    with col2:
        st.markdown("<div class='feature-card'><b>Οδηγοί Fibaro</b><br>Z-Wave Mesh Setup</div>", unsafe_allow_html=True)

# --- ΕΝΟΤΗΤΑ 4: ΑΜΦΙΔΡΟΜΗ ΕΠΙΚΟΙΝΩΝΙΑ ---
elif choice == "📨 Ερώτηση προς Τεχνικό":
    st.header("🤔 Έχετε μια ερώτηση;")
    st.write("Περιγράψτε την τεχνική πρόκληση που αντιμετωπίζετε και θα σας στείλω τη λύση σε σχέδιο!")
    
    user_q = st.text_area("Η ερώτησή σας (π.χ. Πώς θα συνδέσω το VRV της Brand A με το Fibaro;)")
    upload = st.file_uploader("Ανεβάστε μια φωτογραφία ή σχέδιο του χώρου", type=['jpg', 'png', 'pdf'])
    
    if st.button("Αποστολή Ερώτησης"):
        st.balloons()
        st.info("Η ερώτησή σας καταγράφηκε. Θα επικοινωνήσω μαζί σας εντός 24 ωρών.")

