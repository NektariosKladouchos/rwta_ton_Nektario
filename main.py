import streamlit as st

# --- ΤΙΜΟΚΑΤΑΛΟΓΟΣ GEYER ---
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

# --- CSS ΓΙΑ ΑΠΟΛΥΤΗ ΣΤΑΘΕΡΟΤΗΤΑ ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stNumberInput, .stSelectbox, .stTextInput, .stRadio { margin-bottom: -20px !important; }
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
        h_qty = st.number_input("Ποσότητα (Θ)", min_value=0, key='h_qty_in')
        hb = ""
        if h_type == "VRV/VRF": hb = st.selectbox("Brand (Θ)", BRANDS, key="hb")

        st.markdown("### ❄️ 4. ΨΥΞΗ")
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split Κλιματιστικά"]
        c_type = st.selectbox("Επιλογή Ψ", c_list, key="ct")
        c_qty = st.number_input("Ποσότητα (Ψ)", min_value=0, key='c_qty_in')
        cb = ""
        if c_type == "VRV/VRF": cb = st.selectbox("Brand (Ψ)", BRANDS, key="cb")

        st.markdown("### 🪟 5. ΡΟΛΑ")
        shutt = st.number_input("Τεμάχια Ρολών", min_value=0)

        st.markdown("### 🔌 6. ΠΙΝΑΚΑΣ")
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        with st.expander("🏆 10 ΛΟΓΟΙ ΓΙΑ ΝΑ ΕΠΙΛΕΞΕΤΕ ΤΟ ΣΥΣΤΗΜΑ ΜΑΣ"):
            st.write("1. Retrofit | 2. Z-Wave | 3. Εξοικονόμηση 30% | 4. App | 5. Σενάρια | 6. Επεκτασιμότητα | 7. Συμβατότητα | 8. Ελληνική Υποστήριξη | 9. Design | 10. Αξία Ακινήτου")

        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        
        # Υπολογισμοί
        on_off_calc = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        
        # --- ΕΛΕΓΧΟΙ ΚΑΙ ΔΗΜΙΟΥΡΓΙΑ ΠΡΟΣΦΟΡΑΣ ---
        offer_to_show = ""
        error_to_show = None

        if not v_name or not v_job or not v_addr:
            error_to_show = "⚠️ ΠΑΡΑΚΑΛΩ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
        elif on_off_calc < 0:
            error_to_show = "❌ ΣΦΑΛΜΑ: ΕΙΔΗ ΦΩΤΙΣΜΟΥ > ΣΥΝΟΛΟ ΓΡΑΜΜΩΝ"
        elif h_type == "VRV/VRF" and c_type == "VRV/VRF" and hb != cb:
            error_to_show = "❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV ΣΕ Θ/Ψ"
        elif (h_type == "VRV/VRF" and hb == "Άλλη") or (c_type == "VRV/VRF" and cb == "Άλλη"):
            error_to_show = "❌ ΜΗ ΣΥΜΒΑΤΟ ΣΥΣΤΗΜΑ VRV"
        else:
            # HVAC Logic
            hvac_cost = 0; hvac_details = []
            is_common = (h_type == c_type and h_type != "Κανένα") or (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός")
            
            if is_common:
                p_key = "fancoil_ctrl" if "Fancoil" in h_type or "Δροσισμός" in c_type else "vrv_interface" if "VRV" in h_type else "split_ac" if "Split" in h_type else "heat_thermostat"
                hvac_cost = h_qty * PRICES[p_key]
                hvac_details.append({"n": f"{h_type} {hb if h_type=='VRV/VRF' else ''} (Κοινό)", "q": h_qty, "p": hvac_cost})
            else:
                h_price_keys = [None, "heat_thermostat", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "electric_heat", "vrv_interface", "split_ac"]
                if h_qty > 0 and h_type != "Κανένα":
                    p = h_qty * PRICES[h_price_keys[h_list.index(h_type)]]; hvac_cost += p
                    hvac_details.append({"n": f"Θ: {h_type} {hb}", "q": h_qty, "p": p})
                c_price_keys = [None, "fancoil_ctrl", "fancoil_ctrl", "fancoil_ctrl", "vrv_interface", "split_ac"]
                if c_qty > 0 and c_type != "Κανένα":
                    p = c_qty * PRICES[c_price_keys[c_list.index(c_type)]]; hvac_cost += p
                    hvac_details.append({"n": f"Ψ: {c_type} {cb}", "q": c_qty, "p": p})

            e_cost = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0
            h_cost = 95 if heater else 0
            base_count = max(0, on_off_calc) + double + dim220 + dim110 + led + dali + shutt + max(h_qty, c_qty) + (1 if e_cost > 0 else 0) + (1 if h_cost > 0 else 0)
            
            h_rows = []; h_q = 0; h_total = 0
            if base_count <= 37: h_total = PRICES["hub_small"]; h_q = 1; h_rows.append(f"{'Κεντρική μονάδα (40 συσκευές)':<40} | 1       | {h_total:9.2f}€")
            elif base_count <= 97: h_total = PRICES["hub_large"]; h_q = 1; h_rows.append(f"{'Κεντρική μονάδα (100 συσκευές)':<40} | 1       | {h_total:9.2f}€")
            elif base_count <= 130: h_total = PRICES["hub_large"]+PRICES["hub_small"]; h_q = 2; h_rows.append(f"{'Κεντρική μονάδα (100)':<40} | 1       | {PRICES['hub_large']:9.2f}€"); h_rows.append(f"{'Κεντρική μονάδα (40)':<40} | 1       | {PRICES['hub_small']:9.2f}€")
            else: h_total = PRICES["hub_large"] * 2; h_q = 2; h_rows.append(f"{'Κεντρική μονάδα (100)':<40} | 2       | {h_total:9.2f}€")
            
            total_dev = base_count + h_q
            if total_dev > 230: error_to_show = f"❌ ΟΡΙΟ 230 ΣΥΣΚΕΥΩΝ"
            else:
                mat_sum = (max(0,on_off_calc)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52) + (led*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + h_total + e_cost + h_cost
                res = f"{'='*72}\n GEYER SMART HOME - ΑΝΑΛΥΤΙΚΗ ΠΡΟΣΦΟΡΑ\n{'='*72}\n"
                res += f"ΠΕΛΑΤΗΣ: {v_name.upper()} | {v_job}\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*72}\n"
                res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<40} | {'TEM':<7} | {'ΤΙΜΗ':<10}\n{'-'*72}\n"
                for row in h_rows: res += row + "\n"
                if on_off_calc > 0: res += f"{'Γραμμές Φωτισμού On/Off':<40} | {on_off_calc:<7} | {on_off_calc*63.92:9.2f}€\n"
                if double > 0: res += f"{'Διπλές Γραμμές (Κομιτατέρ)':<40} | {double:<7} | {double*63.92:9.2f}€\n"
                if dim220 > 0: res += f"{'Dimming 220V':<40} | {dim220:<7} | {dim220*63.92:9.2f}€\n"
                if dim110 > 0: res += f"{'Dimming 1-10V':<40} | {dim110:<7} | {dim110*52.00:9.2f}€\n"
                if led > 0:    res += f"{'Ταινίες LED Dimming':<40} | {led:<7} | {led*63.92:9.2f}€\n"
                if dali > 0:   res += f"{'Γραμμές DALI':<40} | {dali:<7} | {dali*160.00:9.2f}€\n"
                for d in hvac_details: res += f"{d['n'][:40]:<40} | {d['q']:<7} | {d['p']:9.2f}€\n"
                if shutt > 0:  res += f"{'Ρολά / Τέντες':<40} | {shutt:<7} | {shutt*63.92:9.2f}€\n"
                if e_cost > 0: res += f"{'Μετρητής Ενέργειας':<40} | 1       | {e_cost:9.2f}€\n"
                if h_cost > 0: res += f"{'Έλεγχος Θερμοσίφωνα':<40} | 1       | {h_cost:9.2f}€\n"
                res += f"{'-'*72}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev}\n"
                res += f"{'ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:':<51} {mat_sum:10.2f}€\n"
                res += f"{'ΚΟΣΤΟΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ (20%):':<51} {mat_sum*0.20:10.2f}€\n"
                res += f"{'ΦΠΑ 24%:':<51} {(mat_sum*1.20)*0.24:10.2f}€\n"
                res += f"{'='*72}\n{'ΓΕΝΙΚΟ ΣΥΝΟΛΟ:':<51} {(mat_sum*1.20)*1.24:10.2f}€\n{'='*72}"
                offer_to_show = res

        # --- ΕΜΦΑΝΙΣΗ ΜΟΝΟ ΜΙΑ ΦΟΡΑ ---
        st.markdown('<div class="display-box">', unsafe_allow_html=True)
        st.subheader("🖥️ LIVE PRICING SYSTEM")
        if error_to_show:
            st.code(f"{'='*72}\n        {error_to_show}\n{'='*72}")
        else:
            st.code(offer_to_show, language="text")
        st.markdown('</div>', unsafe_allow_html=True)

        st.write("---")
        user_notes = st.text_area("📝 Παρατηρήσεις Ζήτησης:", placeholder="Γράψτε εδώ τυχόν ειδικές σημειώσεις...")
        
        # HTML Φόρμα για αποστολή
        email_body = f"Νέα Ζήτηση GEYER\nΠελάτης: {v_name}\n\n{offer_to_show}\n\nΠΑΡΑΤΗΡΗΣΕΙΣ:\n{user_notes}"
        form_html = f"""
            <form action="https://formsubmit.co" method="POST">
                <input type="hidden" name="_subject" value="Νέα Ζήτηση GEYER - {v_name}">
                <input type="hidden" name="Περιεχόμενο" value="{email_body}">
                <input type="hidden" name="_captcha" value="false">
                <button type="submit" style="background-color: #27ae60; color: white; padding: 12px 25px; border: none; border-radius: 5px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold;">
                    📩 Αποστολή Ζήτησης
                </button>
            </form>
        """
        st.markdown(form_html, unsafe_allow_html=True)

with tab_home: st.markdown("### 🏠 Digital Showroom")
with tab_docs: st.markdown("### 📂 Βιβλιοθήκη")
with tab_contact: st.markdown("### 📨 Επικοινωνία")
