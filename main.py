import streamlit as st

# --- ΤΙΜΟΚΑΤΑΛΟΓΟΣ & CONFIG ---
PRICES = {
    "on_off": 63.92, "double_on_off": 63.92, "dim_220v": 63.92, "dim_1_10v": 52.0, 
    "led_strip": 63.92, "dim_rgb": 63.92, "dali": 160.0, "shutter": 63.92, 
    "energy_1ph": 110.0, "energy_3ph": 160.0, "heater": 95.0,
    "heat_thermostat": 120.0, "fancoil_ctrl": 130.0, "electric_heat": 70.0, 
    "split_ac": 100.0, "vrv_interface": 260.0, "hub_small": 139.0, "hub_large": 609.0
}
BRANDS = ["Daikin", "LG", "Toshiba", "Fujitsu", "Mitsubishi", "Panasonic", "Midea", "Άλλη"]
JOBS = ["", "Ηλεκτρολόγος", "Αρχιτέκτονας", "Μηχανικός", "Κατασκευαστής", "Ιδιώτης"]

st.set_page_config(page_title="GEYER Portal", layout="wide")

# --- CSS ΓΙΑ ΣΤΑΘΕΡΟ UI ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stNumberInput, .stSelectbox, .stTextInput, .stRadio { margin-bottom: -20px !important; }
    .stMarkdown h3 { font-size: 16px !important; margin-bottom: -10px !important; color: #1E3A8A; }
    .spacer { height: 280px; } 
    [data-testid="stVerticalBlock"] > div:has(div.display-box) { position: sticky; top: 0.5rem; z-index: 1000; }
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
        c1, c2 = st.columns(2)
        int_l = c1.number_input("Εσωτερικές", min_value=0)
        ext_l = c2.number_input("Εξωτερικές", min_value=0)
        
        st.markdown("### 🌓 2α. ΕΙΔΟΣ ΓΡΑΜΜΩΝ ΦΩΤΙΣΜΟΥ")
        dim220 = st.number_input("Dimming 220V", min_value=0)
        dim110 = st.number_input("Dimming 1-10V", min_value=0)
        led = st.number_input("LED Dimming", min_value=0)
        dali = st.number_input("DALI", min_value=0)
        double = st.number_input("Κομιτατέρ (Διπλές)", min_value=0)
        
        st.markdown("### 🔥 3. ΘΕΡΜΑΝΣΗ")
        h_list = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split Κλιματιστικά"]
        h_type = st.selectbox("Επιλογή Θ", h_list, key="ht")
        h_qty = st.number_input("Ποσότητα (Θ)", min_value=0, key='hq_val')
        hb = st.selectbox("Brand (Θ)", BRANDS, key="hb") if h_type == "VRV/VRF" else ""
        
        st.markdown("### ❄️ 4. ΨΥΞΗ")
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split Κλιματιστικά"]
        c_type = st.selectbox("Επιλογή Ψ", c_list, key="ct")
        c_qty = st.number_input("Ποσότητα (Ψ)", min_value=0, key='cq_val')
        cb = st.selectbox("Brand (Ψ)", BRANDS, key="cb") if c_type == "VRV/VRF" else ""
        
        st.markdown("### 🪟 5. ΡΟΛΑ & 🔌 6. ΠΙΝΑΚΑΣ")
        shutt = st.number_input("Τεμάχια Ρολών", min_value=0)
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        
        # --- ΔΙΚΛΙΔΕΣ ---
        error = None
        if not v_name or not v_job or not v_addr: error = "⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
        elif on_off < 0: error = "❌ ΣΦΑΛΜΑ ΣΤΟ ΦΩΤΙΣΜΟ"
        elif h_type == "VRV/VRF" and c_type == "VRV/VRF" and hb != cb: error = "❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV"
        
        is_exact = (h_type == c_type and h_type != "Κανένα") or (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός")
        if not error and is_exact and h_qty != c_qty: error = f"❌ ΛΑΘΟΣ: ΙΔΙΑ ΠΟΣΟΤΗΤΑ ΣΕ {h_type}"

        final_display = ""
        total_sum = 0
        total_dev = 0

        if not error:
            # Πλήρης Υπολογισμός
            h_c = 0; h_det = []
            if is_exact:
                pk = "vrv_interface" if "VRV" in h_type else "fancoil_ctrl" if "Fancoil" in h_type or "Δροσισμός" in h_type else "split_ac" if "Split" in h_type else "heat_thermostat"
                h_c = h_qty * PRICES[pk]
                h_det.append({"n": f"{h_type} ({hb if 'VRV' in h_type else ''}) [Κοινό]", "q": h_qty, "p": h_c})
            else:
                h_m = {"Καλοριφέρ":"heat_thermostat","Ενδοδαπέδια":"heat_thermostat","Fancoil οροφής":"fancoil_ctrl","Fancoil δαπέδου":"fancoil_ctrl","Θερμαντικά σώματα":"electric_heat","VRV/VRF":"vrv_interface","Split Κλιματιστικά":"split_ac"}
                if h_qty > 0: p = h_qty * PRICES[h_m[h_type]]; h_c += p; h_det.append({"n": f"Θ:{h_type} {hb}", "q": h_qty, "p": p})
                if c_qty > 0: p = c_qty * PRICES[h_m.get(c_type, "fancoil_ctrl")]; h_c += p; h_det.append({"n": f"Ψ:{c_type} {cb}", "q": c_qty, "p": p})

            base = max(0, on_off) + double + dim220 + dim110 + led + dali + shutt + max(h_qty, c_qty) + (1 if energy != "Όχι" else 0) + (1 if heater else 0)
            
            # Hub Logic
            h_r = []; h_q = 0; h_t = 0
            if base <= 37: h_t = PRICES["hub_small"]; h_q = 1; h_r.append(f"{'Κεντρική μονάδα (40)':<40} | 1       | {h_t:9.2f}€")
            elif base <= 97: h_t = PRICES["hub_large"]; h_q = 1; h_r.append(f"{'Κεντρική μονάδα (100)':<40} | 1       | {h_t:9.2f}€")
            elif base <= 130: h_t = PRICES["hub_large"]+PRICES["hub_small"]; h_q = 2; h_r.append(f"{'Κεντρική μονάδα (100)':<40} | 1       | {PRICES['hub_large']:9.2f}€"); h_r.append(f"{'Κεντρική μονάδα (40)':<40} | 1       | {PRICES['hub_small']:9.2f}€")
            else: h_t = PRICES["hub_large"]*2; h_q = 2; h_r.append(f"{'Κεντρική μονάδα (100)':<40} | 2       | {h_t:9.2f}€")
            
            total_dev = base + h_q
            total_sum = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52.0) + (led*63.92) + (dali*160.0) + (shutt*63.92) + h_c + h_t + (110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0) + (95 if heater else 0)
            
            res = f"ΠΕΛΑΤΗΣ: {v_name.upper()}\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n"
            res += f"{'-'*60}\n"
            for r in h_r: res += r + "\n"
            if on_off > 0: res += f"{'Γραμμές On/Off':<40} | {on_off:<7} | {on_off*63.92:9.2f}€\n"
            for d in h_det: res += f"{d['n'][:40]:<40} | {d['q']:<7} | {d['p']:9.2f}€\n"
            res += f"{'-'*60}\n"
            res += f"ΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev}\n"
            res += f"ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ: {total_sum:10.2f}€\n"
            res += f"ΓΕΝΙΚΟ ΣΥΝΟΛΟ: {(total_sum*1.20)*1.24:10.2f}€"
            final_display = res

        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.markdown('<div class="display-box">', unsafe_allow_html=True)
        st.subheader("🖥️ LIVE PRICING SYSTEM")
        st.code(final_display if not error else error, language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("---")
        # --- ΚΑΘΑΡΗ ΦΟΡΜΑ ΧΩΡΙΣ ΣΥΜΒΟΛΑ ΠΟΥ ΣΠΑΝΕ ΤΟ HTML ---
        clean_email_offer = final_display.replace('\n', ' | ')
        
        form_html = f"""
            <div style="background:#fff; padding:10px; border-radius:5px;">
                <form action="https://formsubmit.co" method="POST">
                    <p style="font-weight:bold; margin-bottom:5px;">📝 Παρατηρήσεις Ζήτησης:</p>
                    <textarea name="Παρατηρήσεις" style="width:100%; height:80px; border:1px solid #ccc; margin-bottom:10px; padding:5px;"></textarea>
                    <input type="hidden" name="Πελάτης" value="{v_name}">
                    <input type="hidden" name="Προσφορά" value="{clean_email_offer}">
                    <input type="hidden" name="_captcha" value="false">
                    <button type="submit" style="width:100%; background:#27ae60; color:white; border:none; padding:15px; font-weight:bold; border-radius:5px; cursor:pointer;">
                        📩 ΑΠΟΣΤΟΛΗ ΖΗΤΗΣΗΣ
                    </button>
                </form>
            </div>
        """
        st.markdown(form_html, unsafe_allow_html=True)

with tab_home: st.markdown("### 🏠 Digital Showroom")
