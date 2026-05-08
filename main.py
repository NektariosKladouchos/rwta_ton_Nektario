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
    .stMarkdown h3 { font-size: 15px !important; margin-bottom: -10px !important; color: #1E3A8A; }
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

with tab_calc:
    left, right = st.columns([1.1, 1.45])
    
    with left:
        st.markdown("### 👤 1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ")
        v_name = st.text_input("Ονοματεπώνυμο", key="n")
        v_job = st.selectbox("Ιδιότητα", JOBS, key="j")
        v_addr = st.text_input("Διεύθυνση έργου", key="a")
        st.markdown("### 💡 2. ΦΩΤΙΣΜΟΣ")
        c1, c2 = st.columns(2); int_l = c1.number_input("Εσωτερικές", min_value=0); ext_l = c2.number_input("Εξωτερικές", min_value=0)
        dim220 = st.number_input("Dimming 220V", min_value=0); dim110 = st.number_input("Dimming 1-10V", min_value=0)
        led = st.number_input("LED Dimming", min_value=0); dali = st.number_input("DALI", min_value=0)
        double = st.number_input("Κομιτατέρ (Διπλές)", min_value=0)
        st.markdown("### 🔥 3. ΘΕΡΜΑΝΣΗ")
        h_type = st.selectbox("Επιλογή Θ", ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split Κλιματιστικά"], key="ht")
        h_qty = st.number_input("Ποσότητα (Θ)", min_value=0, key='hq')
        hb = st.selectbox("Brand (Θ)", BRANDS, key="hb") if h_type == "VRV/VRF" else ""
        st.markdown("### ❄️ 4. ΨΥΞΗ")
        c_type = st.selectbox("Επιλογή Ψ", ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split Κλιματιστικά"], key="ct")
        c_qty = st.number_input("Ποσότητα (Ψ)", min_value=0, key='cq')
        cb = st.selectbox("Brand (Ψ)", BRANDS, key="cb") if c_type == "VRV/VRF" else ""
        st.markdown("### 🪟 5. ΡΟΛΑ & 🔌 6. ΠΙΝΑΚΑΣ")
        shutt = st.number_input("Τεμάχια Ρολών", min_value=0)
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        error = None
        if not v_name or not v_job or not v_addr: error = "⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
        elif on_off < 0: error = "❌ ΣΦΑΛΜΑ ΣΤΟ ΦΩΤΙΣΜΟ"
        
        # Δικλίδες HVAC
        is_exact = (h_type == c_type and h_type != "Κανένα") or (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός")
        if not error and is_exact and h_qty != c_qty: error = "❌ ΛΑΘΟΣ ΠΟΣΟΤΗΤΑ ΣΕ Θ/Ψ"

        final_offer = ""; t_dev = 0; t_val = 0

        if not error:
            # Πλήρης Logic υπολογισμών
            h_cost = (h_qty + c_qty) * 100 # Προσωρινό για τη δοκιμή
            t_val = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52.0) + (led*63.92) + (dali*160.0) + (shutt*63.92) + h_cost
            t_dev = on_off + double + dim220 + dim110 + led + dali + shutt + h_qty + c_qty
            
            res = f"ΠΕΛΑΤΗΣ: {v_name.upper()}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {t_dev}\nΑΞΙΑ ΥΛΙΚΩΝ: {t_val:.2f}€\nΓΕΝΙΚΟ ΣΥΝΟΛΟ: {(t_val*1.20)*1.24:.2f}€"
            final_offer = res

        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.markdown('<div class="display-box">', unsafe_allow_html=True)
        st.subheader("🖥️ LIVE PRICING SYSTEM")
        st.code(final_offer if final_offer else error, language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("---")
        # --- Η ΑΠΟΛΥΤΗ ΛΥΣΗ ΓΙΑ ΤΟ EMAIL (FORMSubmit με καθαρά πεδία) ---
        # Χρησιμοποιούμε κρυφά πεδία που ΔΕΝ περιέχουν τον πίνακα για να μην βγάζει "Whoops"
        form_html = f"""
            <form action="https://formsubmit.co" method="POST">
                <input type="hidden" name="_subject" value="Νέα Ζήτηση: {v_name}">
                <input type="hidden" name="Πελάτης" value="{v_name}">
                <input type="hidden" name="Διεύθυνση" value="{v_addr}">
                <input type="hidden" name="Σύνολο_Συσκευών" value="{t_dev}">
                <input type="hidden" name="Τελικό_Ποσό" value="{(t_val*1.20)*1.24 if not error else 0:.2f} €">
                
                <p style="font-family:sans-serif; font-weight:bold; margin-bottom:5px;">📝 Παρατηρήσεις Ζήτησης:</p>
                <textarea name="Παρατηρήσεις" style="width:100%; height:80px; border:1px solid #ccc; border-radius:5px; padding:10px; margin-bottom:10px;" placeholder="Γράψτε εδώ..."></textarea>
                
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="_next" value="https://streamlit.app">
                
                <button type="submit" style="width:100%; background-color:#27ae60; color:white; border:none; padding:15px; border-radius:5px; font-weight:bold; cursor:pointer; font-size:16px;">
                    📩 ΟΛΟΚΛΗΡΩΣΗ & ΑΠΟΣΤΟΛΗ ΖΗΤΗΣΗΣ
                </button>
            </form>
        """
        st.markdown(form_html, unsafe_allow_html=True)

with tab_home: st.markdown("### 🏠 Digital Showroom")
