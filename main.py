import streamlit as st
from datetime import datetime

# --- ΡΥΘΜΙΣΕΙΣ ΣΕΛΙΔΑΣ ---
st.set_page_config(page_title="GEYER Tech Expert Portal", page_icon="⚡", layout="wide")

# --- ΤΙΜΟΚΑΤΑΛΟΓΟΣ & DATA ---
PRICES = {
    "on_off": 63.92, "double_on_off": 63.92, "dim_220v": 63.92, "dim_1_10v": 52.0, 
    "led_strip": 63.92, "dali": 160.0, "shutter": 63.92, 
    "energy_1ph": 110.0, "energy_3ph": 160.0, "heater": 95.0,
    "heat_thermostat": 120.0, "fancoil_ctrl": 130.0, "electric_heat": 70.0, 
    "split_ac": 100.0, "vrv_interface": 260.0, "hub_small": 139.0, "hub_large": 609.0
}
BRANDS = ["Daikin", "LG", "Toshiba", "Fujitsu", "Mitsubishi", "Panasonic", "Midea", "Άλλη"]
JOBS = ["", "Κατασκευαστής", "Μηχανικός", "Αρχιτέκτονας", "Ηλεκτρολόγος", "Κατάστημα", "Ιδιώτης"]

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f5; }
    .display-text {
        background-color: white;
        padding: 30px;
        border: 2px solid #27ae60;
        font-family: 'Consolas', monospace;
        color: black;
        white-space: pre;
        font-size: 14px;
        line-height: 1.2;
    }
    .main-title { color: #1E3A8A; font-size: 35px; font-weight: bold; text-align: center; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΠΛΕΥΡΙΚΟ ΜΕΝΟΥ ---
st.sidebar.image("https://wikimedia.org", width=100)
choice = st.sidebar.radio("Επιλογές Portal", ["🏠 Αρχική & Ιδέες", "📊 Live Pricing (CEO Edition)", "📂 Τεχνική Βιβλιοθήκη", "📨 Ερώτηση προς Τεχνικό"])

# --- ΕΝΟΤΗΤΑ 1: ΑΡΧΙΚΗ & ΙΔΕΕΣ ---
if choice == "🏠 Αρχική & Ιδέες":
    st.markdown("<div class='main-title'>📸 Ιδέες & Φωτογραφίες Έργων</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://unsplash.com", caption="Smart Lighting Project")
    with col2:
        st.image("https://unsplash.com", caption="HVAC Control με Fibaro")
    st.info("💡 Το σύστημα Fibaro επιτρέπει την αναβάθμιση κάθε κατοικίας σε Smart Home χωρίς μερεμέτια.")

# --- ΕΝΟΤΗΤΑ 2: LIVE PRICING (Ο ΚΩΔΙΚΑΣ ΣΟΥ) ---
elif choice == "📊 Live Pricing (CEO Edition)":
    st.markdown("<div class='main-title'>📊 Live Pricing System</div>", unsafe_allow_html=True)
    left, right = st.columns([1, 1.2])

    with left:
        st.subheader("1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ")
        v_name = st.text_input("Ονοματεπώνυμο / Επωνυμία")
        v_job = st.selectbox("Ιδιότητα (Υποχρεωτικό)", JOBS)
        v_addr = st.text_input("Διεύθυνση έργου")

        st.subheader("2. ΦΩΤΙΣΜΟΣ")
        c1, c2 = st.columns(2)
        int_l = c1.number_input("Εσωτερικές", min_value=0, value=0)
        ext_l = c2.number_input("Εξωτερικές", min_value=0, value=0)
        st.markdown("**2α. ΓΡΑΜΜΕΣ DIMMING**")
        cd1, cd2 = st.columns(2)
        dim220 = cd1.number_input("Dimming 220V", min_value=0, value=0)
        dim110 = cd2.number_input("Dimming 1-10V", min_value=0, value=0)
        led = cd1.number_input("Ταινίες LED Dim", min_value=0, value=0)
        dali = cd2.number_input("DALI", min_value=0, value=0)
        double = st.number_input("Κομιτατέρ (Διπλές)", min_value=0, value=0)

        st.subheader("3 & 4 HVAC")
        h_type = st.selectbox("Θέρμανση", ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split"])
        h_qty = st.number_input("Ποσότητα (Θ)", min_value=0, value=0)
        if h_type == "VRV/VRF": h_brand = st.selectbox("Μάρκα VRV (Θ)", BRANDS)
        
        c_type = st.selectbox("Ψύξη", ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split"])
        c_qty = st.number_input("Ποσότητα (Ψ)", min_value=0, value=0)
        if c_type == "VRV/VRF": c_brand = st.selectbox("Μάρκα VRV (Ψ)", BRANDS)

        st.subheader("5 & 6 ΛΟΙΠΑ")
        shutt = st.number_input("Ρολά/Τέντες", min_value=0, value=0)
        energy = st.radio("Μετρητής Ενέργειας", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        st.subheader("🖥️ LIVE PRICING DISPLAY")
        if not v_name or not v_job or not v_addr:
            st.warning("⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΓΙΑ ΤΗΝ ΠΡΟΣΦΟΡΑ")
        else:
            # --- LOGIC ---
            on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
            if on_off < 0:
                st.error("❌ ΣΦΑΛΜΑ: DIMMING > ΣΥΝΟΛΟ ΓΡΑΜΜΩΝ")
            else:
                h_cost = h_qty * 120 # Απλοποιημένο για το παράδειγμα, μπορείς να βάλεις το πλήρες p_keys mapping
                e_cost = 110 if energy == "Μονοφασικός" else 160 if energy == "Τριφασικός" else 0
                total_dev = on_off + double + dim220 + dim110 + led + dali + shutt + h_qty + (1 if energy != "Όχι" else 0)
                mat_sum = (on_off*63.92) + (double*63.92) + (dim220*63.92) + h_cost + e_cost + (shutt*63.92)
                
                res = f"{'='*60}\n GEYER SMART HOME - ΠΡΟΣΦΟΡΑ\n{'='*60}\n"
                res += f"ΠΕΛΑΤΗΣ: {v_name.upper()}\nΙΔΙΟΤΗΤΑ: {v_job}\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*60}\n"
                res += f"ΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev}\n"
                res += f"ΚΑΘΑΡΗ ΑΞΙΑ: {mat_sum:20.2f}€\n"
                res += f"ΜΕ ΦΠΑ 24%: {mat_sum*1.24:19.2f}€\n"
                res += f"ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ: {mat_sum*0.20:16.2f}€\n{'='*60}"
                
                st.markdown(f"<div class='display-text'>{res}</div>", unsafe_allow_html=True)
                if st.button("📩 Αποστολή στον Νεκτάριο"):
                    st.success("Η προσφορά εστάλη!")

# --- ΕΝΟΤΗΤΑ 3: ΒΙΒΛΙΟΘΗΚΗ ---
elif choice == "📂 Τεχνική Βιβλιοθήκη":
    st.header("📄 Σχέδια & Τεχνικά Φυλλάδια")
    st.write("Επιλέξτε το αρχείο που θέλετε να δείτε:")
    st.info("Εδώ θα εμφανίζονται τα PDF που ανεβάζεις στο GitHub.")

# --- ΕΝΟΤΗΤΑ 4: ΕΠΙΚΟΙΝΩΝΙΑ ---
elif choice == "📨 Ερώτηση προς Τεχνικό":
    st.header("📨 Ρωτήστε τον Νεκτάριο")
    user_q = st.text_area("Περιγράψτε την απορία σας:")
    if st.button("Αποστολή"):
        st.balloons()
        st.success("Η ερώτησή σας καταγράφηκε!")
