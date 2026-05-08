import streamlit as st

# --- CONFIG GEYER ---
PRICES = {
    "on_off": 63.92, "double_on_off": 63.92, "dim_220v": 63.92, "dim_1_10v": 52.0, 
    "led_strip": 63.92, "dali": 160.0, "shutter": 63.92, 
    "energy_1ph": 110.0, "energy_3ph": 160.0, "heater": 95.0,
    "heat_thermostat": 120.0, "fancoil_ctrl": 130.0, "electric_heat": 70.0, 
    "split_ac": 100.0, "vrv_interface": 260.0, "hub_small": 139.0, "hub_large": 609.0
}
BRANDS = ["Daikin", "LG", "Toshiba", "Fujitsu", "Mitsubishi", "Panasonic", "Midea", "Άλλη"]
JOBS = ["", "Ηλεκτρολόγος", "Αρχιτέκτονας", "Μηχανικός", "Κατασκευαστής", "Ιδιώτης"]

st.set_page_config(page_title="GEYER Portal", layout="wide")

# --- CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stNumberInput, .stSelectbox, .stTextInput, .stRadio { margin-bottom: -20px !important; }
    .spacer { height: 280px; } 
    .display-box {
        background-color: #ffffff; padding: 15px; border: 2px solid #27ae60;
        border-radius: 8px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    pre { font-family: 'Consolas', monospace !important; font-size: 11px !important; line-height: 1.1 !important; color: #000 !important; }
    .main-header { text-align: center; color: #1E3A8A; margin-top: -30px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-header'><h1>GEYER PORTAL</h1><p><b>ΡΩΤΑ ΤΟΝ ΝΕΚΤΑΡΙΟ</b></p></div>", unsafe_allow_html=True)

tab_calc, tab_home, tab_docs, tab_contact = st.tabs(["📊 LIVE PRICING", "🏠 ΙΔΕΕΣ", "📂 ΒΙΒΛΙΟΘΗΚΗ", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

# --- TAB 1: PRICING (Logic Only) ---
with tab_calc:
    left, right = st.columns([1.1, 1.45])
    with left:
        st.markdown("### 👤 ΣΤΟΙΧΕΙΑ")
        v_name = st.text_input("Ονοματεπώνυμο", key="n_p")
        v_addr = st.text_input("Διεύθυνση έργου", key="a_p")
        st.markdown("### 💡 ΦΩΤΙΣΜΟΣ")
        c1, c2 = st.columns(2); int_l = c1.number_input("Εσωτερικές", min_value=0); ext_l = c2.number_input("Εξωτερικές", min_value=0)
        st.markdown("### 🔥 ΘΕΡΜΑΝΣΗ & ❄️ ΨΥΞΗ")
        h_type = st.selectbox("Είδος", ["Κανένα", "VRV/VRF", "Split", "Fancoils"], key="h_p")
        h_qty = st.number_input("Ποσότητα", min_value=0, key="q_p")
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)

    with right:
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.markdown('<div class="display-box">', unsafe_allow_html=True)
        st.subheader("🖥️ LIVE PRICING SYSTEM")
        # Απλός υπολογισμός για το display
        temp_sum = (int_l + ext_l) * 63.92 + (h_qty * 100)
        res = f"ΠΕΛΑΤΗΣ: {v_name.upper()}\n"
        res += f"ΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {int_l + ext_l + h_qty}\n"
        res += f"ΑΞΙΑ ΥΛΙΚΩΝ: {temp_sum:.2f}€\n"
        st.code(res, language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        st.info("Για αποστολή ζήτησης, χρησιμοποιήστε το Tab 'ΕΠΙΚΟΙΝΩΝΙΑ'")

# --- TAB 2 & 3 ---
with tab_home: st.markdown("### 🏠 Digital Showroom")
with tab_docs: st.markdown("### 📂 Βιβλιοθήκη")

# --- TAB 4: ΕΠΙΚΟΙΝΩΝΙΑ (ΕΔΩ Η ΔΟΚΙΜΗ) ---
with tab_contact:
    st.markdown("### 📨 Φόρμα Επικοινωνίας & Ζήτησης")
    st.write("Συμπληρώστε το κείμενό σας παρακάτω για να δοκιμάσουμε την αποστολή.")
    
    # Χρησιμοποιούμε μια πολύ απλή φόρμα
    contact_form = f"""
    <form action="https://formsubmit.co" method="POST" style="background: white; padding: 20px; border-radius: 10px; border: 1px solid #ccc;">
        <input type="hidden" name="_subject" value="Μήνυμα από Portal">
        
        <label style="font-weight:bold;">Το όνομά σας:</label><br>
        <input type="text" name="name" placeholder="π.χ. Νεκτάριος" required style="width:100%; padding:10px; margin-bottom:15px; border-radius:5px; border:1px solid #ccc;"><br>
        
        <label style="font-weight:bold;">Το email σας:</label><br>
        <input type="email" name="email" placeholder="email@example.com" required style="width:100%; padding:10px; margin-bottom:15px; border-radius:5px; border:1px solid #ccc;"><br>
        
        <label style="font-weight:bold;">Παρατηρήσεις / Ζήτηση:</label><br>
        <textarea name="message" placeholder="Γράψτε εδώ τις λεπτομέρειες..." style="width:100%; height:150px; padding:10px; margin-bottom:15px; border-radius:5px; border:1px solid #ccc;"></textarea>
        
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://streamlit.app">
        
        <button type="submit" style="background-color: #27ae60; color: white; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 100%;">
            🚀 ΔΟΚΙΜΗ ΑΠΟΣΤΟΛΗΣ
        </button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

