import streamlit as st

# --- CONFIG ---
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
        
        st.markdown("### 🌓 2α. ΕΙΔΟΣ ΓΡΑΜΜΩΝ ΦΩΤΙΣΜΟΥ")
        dim220 = st.number_input("Dimming 220V", min_value=0); dim110 = st.number_input("Dimming 1-10V", min_value=0)
        led = st.number_input("LED Dimming", min_value=0); dali = st.number_input("DALI", min_value=0)
        double = st.number_input("Κομιτατέρ (Διπλές)", min_value=0)
        
        st.markdown("### 🔥 3. ΘΕΡΜΑΝΣΗ")
        h_list = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split Κλιματιστικά"]
        h_type = st.selectbox("Επιλογή Θ", h_list, key="ht"); h_qty = st.number_input("Ποσότητα (Θ)", min_value=0, key='hq_val')
        hb = st.selectbox("Brand (Θ)", BRANDS, key="hb") if h_type == "VRV/VRF" else ""
        
        st.markdown("### ❄️ 4. ΨΥΞΗ")
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split Κλιματιστικά"]
        c_type = st.selectbox("Επιλογή Ψ", c_list, key="ct"); c_qty = st.number_input("Ποσότητα (Ψ)", min_value=0, key='cq_val')
        cb = st.selectbox("Brand (Ψ)", BRANDS, key="cb") if c_type == "VRV/VRF" else ""
        
        st.markdown("### 🪟 5. ΡΟΛΑ & 🔌 6. ΠΙΝΑΚΑΣ")
        shutt = st.number_input("Τεμάχια Ρολών", min_value=0)
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        
        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        
        # --- ΕΛΕΓΧΟΙ / ΔΙΚΛΙΔΕΣ ---
        error = None
        if not v_name or not v_job or not v_addr: error = "⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
        elif on_off < 0: error = "❌ ΣΦΑΛΜΑ: ΕΙΔΗ ΦΩΤΙΣΜΟΥ > ΣΥΝΟΛΟ"
        elif h_type == "VRV/VRF" and c_type == "VRV/VRF" and hb != cb: error = "❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV"
        elif hb == "Άλλη" or cb == "Άλλη": error = "❌ ΜΗ ΣΥΜΒΑΤΟ VRV ('Άλλη')"
        
        # Δικλίδα ίδιας ποσότητας για ίδια είδη
        is_exact_same = (h_type == c_type and h_type != "Κανένα") or (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός") or (h_type == "Split Κλιματιστικά" and c_type == "Split Κλιματιστικά")
        if not error and is_exact_same and h_qty != c_qty:
            error = f"❌ ΛΑΘΟΣ: Η ΠΟΣΟΤΗΤΑ ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΙΔΙΑ ΣΕ {h_type}"

        disp_text = ""
        total_sum = 0
        total_dev = 0

        if error:
            disp_text = f"{'='*72}\n        {error}\n{'='*72}"
        else:
            # HVAC Logic
            h_cost_hvac = 0; h_details = []
            if is_exact_same:
                p_key = "fancoil_ctrl" if "Fancoil" in h_type or "Δροσισμός" in h_type else "vrv_interface" if "VRV" in h_type else "split_ac" if "Split" in h_type else "heat_thermostat"
                h_cost_hvac = h_qty * PRICES[p_key]
                name = f"{h_type} ({hb if 'VRV' in h_type else ''}) [Κοινό]"
                h_details.append({"n": name.replace("()", ""), "q": h_qty, "p": h_cost_hvac})
            else:
                h_map = {"Καλοριφέρ":"heat_thermostat","Ενδοδαπέδια":"heat_thermostat","Fancoil οροφής":"fancoil_ctrl","Fancoil δαπέδου":"fancoil_ctrl","Θερμαντικά σώματα":"electric_heat","VRV/VRF":"vrv_interface","Split Κλιματιστικά":"split_ac"}
                if h_qty > 0 and h_type in h_map:
                    p = h_qty * PRICES[h_map[h_type]]; h_cost_hvac += p
                    h_details.append({"n": f"Θ: {h_type} {hb}", "q": h_qty, "p": p})
                c_map = {"Ενδοδαπέδια Δροσισμός":"fancoil_ctrl","Fancoil οροφής":"fancoil_ctrl","Fancoil δαπέδου":"fancoil_ctrl","VRV/VRF":"vrv_interface","Split Κλιματιστικά":"split_ac"}
                if c_qty > 0 and c_type in c_map:
                    p = c_qty * PRICES[c_map[c_type]]; h_cost_hvac += p
                    h_details.append({"n": f"Ψ: {c_type} {cb}", "q": c_qty, "p": p})

            e_cost = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0
            base_count = max(0, on_off) + double + dim220 + dim110 + led + dali + shutt + max(h_qty, c_qty) + (1 if e_cost > 0 else 0) + (1 if heater else 0)
            
            # --- HUB LOGIC (EXE ACCURATE) ---
            h_rows = []; h_q = 0; h_total = 0
            if base_count <= 37: h_total = PRICES["hub_small"]; h_q = 1; h_rows.append(f"{'Κεντρική μονάδα (40 συσκευές)':<40} | 1       | {h_total:9.2f}€")
            elif base_count <= 97: h_total = PRICES["hub_large"]; h_q = 1; h_rows.append(f"{'Κεντρική μονάδα (100 συσκευές)':<40} | 1       | {h_total:9.2f}€")
            elif base_count <= 130: h_total = PRICES["hub_large"]+PRICES["hub_small"]; h_q = 2; h_rows.append(f"{'Κεντρική μονάδα (100)':<40} | 1       | {PRICES['hub_large']:9.2f}€"); h_rows.append(f"{'Κεντρική μονάδα (40)':<40} | 1       | {PRICES['hub_small']:9.2f}€")
            else: h_total = PRICES["hub_large"]*2; h_q = 2; h_rows.append(f"{'Κεντρική μονάδα (100)':<40} | 2       | {h_total:9.2f}€")
            
            total_dev = base_count + h_q
            if total_dev > 230: disp_text = f"{'='*72}\n        ❌ ΟΡΙΟ 230 ΣΥΣΚΕΥΩΝ\n{'='*72}"
            else:
                total_sum = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52.0) + (led*63.92) + (dali*160.0) + (shutt*63.92) + h_cost_hvac + h_total + e_cost + (95 if heater else 0)
                res = f"{'='*72}\n GEYER SMART HOME - ΑΝΑΛΥΤΙΚΗ ΠΡΟΣΦΟΡΑ\n{'='*72}\n"
                res += f"ΠΕΛΑΤΗΣ: {v_name.upper()} | {v_job}\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*72}\n"
                res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<40} | {'TEM':<7} | {'ΤΙΜΗ':<10}\n{'-'*72}\n"
                for r in h_rows: res += r + "\n"
                if on_off > 0: res += f"{'Γραμμές Φωτισμού On/Off':<40} | {on_off:<7} | {on_off*63.92:9.2f}€\n"
                if double > 0: res += f"{'Διπλές Γραμμές (Κομιτατέρ)':<40} | {double:<7} | {double*63.92:9.2f}€\n"
                if dim220 > 0: res += f"{'Dimming 220V':<40} | {dim220:<7} | {dim220*63.92:9.2f}€\n"
                if dim110 > 0: res += f"{'Dimming 1-10V':<40} | {dim110:<7} | {dim110*52.00:9.2f}€\n"
                if led > 0:    res += f"{'Ταινίες LED Dimming':<40} | {led:<7} | {led*63.92:9.2f}€\n"
                if dali > 0:   res += f"{'Γραμμές DALI':<40} | {dali:<7} | {dali*160.00:9.2f}€\n"
                for d in h_details: res += f"{d['n'][:40]:<40} | {d['q']:<7} | {d['p']:9.2f}€\n"
                if shutt > 0:  res += f"{'Ρολά / Τέντες':<40} | {shutt:<7} | {shutt*63.92:9.2f}€\n"
                if heater:     res += f"{'Έλεγχος Θερμοσίφωνα':<40} | 1       | {95.00:9.2f}€\n"
                res += f"{'-'*72}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev}\n"
                res += f"{'ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:':<51} {total_sum:10.2f}€\n"
                res += f"{'ΓΕΝΙΚΟ ΣΥΝΟΛΟ (ΜΕ ΦΠΑ 24%):':<51} {(total_sum*1.20)*1.24:10.2f}€\n{'='*72}"
                disp_text = res

        st.markdown('<div class="display-box">', unsafe_allow_html=True)
        st.subheader("🖥️ LIVE PRICING SYSTEM")
        st.code(disp_text, language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("---")
        notes = st.text_area("📝 Παρατηρήσεις Ζήτησης:", key="usr_notes")
        
        form_html = f"""
            <form action="https://formsubmit.co" method="POST">
                <input type="hidden" name="_subject" value="Νέα Ζήτηση: {v_name}">
                <input type="hidden" name="Πελάτης" value="{v_name}">
                <input type="hidden" name="Συσκευές" value="{total_dev}">
                <input type="hidden" name="Ποσό_με_ΦΠΑ" value="{(total_sum*1.20)*1.24:.2f} €">
                <input type="hidden" name="Παρατηρήσεις" value="{notes}">
                <input type="hidden" name="_captcha" value="false">
                <button type="submit" style="background-color: #27ae60; color: white; padding: 12px; border: none; border-radius: 5px; width: 100%; font-weight: bold; cursor: pointer;">
                    📩 Αποστολή Ζήτησης
                </button>
            </form>
        """
        st.markdown(form_html, unsafe_allow_html=True)

with tab_home: st.markdown("### 🏠 Digital Showroom")
with tab_docs: st.markdown("### 📂 Βιβλιοθήκη")
with tab_contact: st.markdown("### 📨 Επικοινωνία")
