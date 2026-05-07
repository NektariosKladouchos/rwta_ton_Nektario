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
JOBS = ["", "Κατασκευαστής", "Μηχανικός", "Αρχιτέκτονας", "Ηλεκτρολόγος", "Κατάστημα", "Ιδιώτης"]

st.set_page_config(page_title="GEYER Portal", layout="wide")

# --- CSS ΓΙΑ FULL WIDE & STICKY DISPLAY ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    /* Sticky Right Column - Κλειδώνει το Display δεξιά */
    [data-testid="stVerticalBlock"] > div:has(div.display-box) {
        position: sticky; top: 0.5rem; z-index: 1000;
    }
    .display-box {
        background-color: #ffffff; padding: 15px; border: 2px solid #27ae60;
        border-radius: 8px; box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        width: 100%;
    }
    pre {
        font-family: 'Consolas', 'Lucida Console', monospace !important;
        font-size: 11px !important; line-height: 1.1 !important; color: #000 !important;
    }
    .compact-label { font-size: 14px !important; font-weight: bold; color: #1E3A8A; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>GEYER PORTAL</h1>", unsafe_allow_html=True)

tab_home, tab_calc, tab_docs, tab_contact = st.tabs(["🏠 ΑΡΧΙΚΗ & ΙΔΕΕΣ", "📊 LIVE PRICING", "📂 ΒΙΒΛΙΟΘΗΚΗ", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    # Χωρισμός 40% ερωτήσεις - 60% Display για μέγιστη ορατότητα
    left, right = st.columns([1, 1.5]) 
    
    with left:
        st.markdown("<p class='compact-label'>👤 1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ</p>", unsafe_allow_html=True)
        v_name = st.text_input("Ονοματεπώνυμο", key="name")
        v_job = st.selectbox("Ιδιότητα", JOBS, key="job")
        v_addr = st.text_input("Διεύθυνση έργου", key="addr")

        st.markdown("<p class='compact-label'>💡 2. ΦΩΤΙΣΜΟΣ</p>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        int_l = c1.number_input("Εσωτερικές", min_value=0, value=0)
        ext_l = c2.number_input("Εξωτερικές", min_value=0, value=0)
        
        st.markdown("<p class='compact-label'>🌓 2α. ΕΙΔΟΣ ΓΡΑΜΜΩΝ ΦΩΤΙΣΜΟΥ</p>", unsafe_allow_html=True)
        dim220 = st.number_input("Dimming 220V", min_value=0, value=0)
        dim110 = st.number_input("Dimming 1-10V", min_value=0, value=0)
        led = st.number_input("Ταινίες LED Dim", min_value=0, value=0)
        dali = st.number_input("DALI", min_value=0, value=0)
        double = st.number_input("Κομιτατέρ (Διπλές)", min_value=0, value=0)

        st.markdown("<p class='compact-label'>🔥 3. ΘΕΡΜΑΝΣΗ</p>", unsafe_allow_html=True)
        h_list = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split"]
        h_labels = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. σωμάτων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
        h_type = st.selectbox("Επιλογή Θέρμανσης", h_list, key="h_type")
        h_val = 0 if h_type == "Κανένα" else st.session_state.get('h_qty', 0)
        h_qty = st.number_input(h_labels[h_list.index(h_type)], min_value=0, value=h_val, key="h_qty")
        h_brand = "Daikin"
        if h_type == "VRV/VRF": h_brand = st.selectbox("Μάρκα VRV (Θ)", BRANDS)

        st.markdown("<p class='compact-label'>❄️ 4. ΨΥΞΗ</p>", unsafe_allow_html=True)
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split"]
        c_labels = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
        c_type = st.selectbox("Επιλογή Ψύξης", c_list, key="c_type")
        c_val = 0 if c_type == "Κανένα" else st.session_state.get('c_qty', 0)
        c_qty = st.number_input(c_labels[c_list.index(c_type)], min_value=0, value=c_val, key="c_qty")
        c_brand = "Daikin"
        if c_type == "VRV/VRF": c_brand = st.selectbox("Μάρκα VRV (Ψ)", BRANDS)

        st.markdown("<p class='compact-label'>🪟 5. ΡΟΛΑ & 🔌 ΠΙΝΑΚΑΣ</p>", unsafe_allow_html=True)
        shutt = st.number_input("Ρολά / Τέντες", min_value=0, value=0)
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        st.markdown('<div class="display-box">', unsafe_allow_html=True)
        st.subheader("🖥️ LIVE PRICING SYSTEM")
        
        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        
        # Επικύρωση (Validation)
        error_msg = None
        if not v_name or not v_job or not v_addr:
            error_msg = "⚠️ ΠΑΡΑΚΑΛΩ ΣΥΜΠΛΗΡΩΣΤΕ ΤΑ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
        elif on_off < 0:
            error_msg = "❌ ΣΦΑΛΜΑ ΣΤΟ ΦΩΤΙΣΜΟ: DIMMING > ΣΥΝΟΛΟ"
        elif h_type == "VRV/VRF" and c_type == "VRV/VRF" and h_brand != c_brand:
            error_msg = "❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV ΣΕ Θ/Ψ"

        if error_msg:
            st.code(f"{'='*70}\n          {error_msg}\n{'='*70}")
        else:
            # HVAC Logic: Αποφυγή διπλοχρέωσης θερμοστατών
            hvac_cost = 0; hvac_details = []
            is_common = (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός") or \
                        (h_type == c_type and h_type != "Κανένα")
            
            if is_common:
                p_key = "fancoil_ctrl" if "Fancoil" in h_type or "Δροσισμός" in c_type else "vrv_interface" if "VRV" in h_type else "split_ac" if "Split" in h_type else "heat_thermostat"
                hvac_cost = max(h_qty, c_qty) * PRICES[p_key]
                hvac_details.append({"n": f"{h_type} (Κοινό Σύστημα)", "q": max(h_qty, c_qty), "p": hvac_cost})
            else:
                if h_qty > 0:
                    h_keys = ["", "heat_thermostat", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "electric_heat", "vrv_interface", "split_ac"]
                    p = h_qty * PRICES[h_keys[h_list.index(h_type)]]; hvac_cost += p
                    hvac_details.append({"n": f"Θ: {h_type} {h_brand if 'VRV' in h_type else ''}", "q": h_qty, "p": p})
                if c_qty > 0:
                    c_keys = ["", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "vrv_interface", "split_ac"]
                    p = c_qty * PRICES[c_keys[c_list.index(c_type)]]; hvac_cost += p
                    hvac_details.append({"n": f"Ψ: {c_type} {c_brand if 'VRV' in c_type else ''}", "q": c_qty, "p": p})

            e_cost = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0
            h_cost = 95 if heater else 0
            base_count = max(0, on_off) + double + dim220 + dim110 + led + dali + shutt + max(h_qty, c_qty) + (1 if e_cost > 0 else 0) + (1 if h_cost > 0 else 0)
            
            # Hub Logic
            hubs_cost = 0; hub_rows = []; h_qty_tot = 0
            if base_count <= 37:
                hubs_cost = PRICES["hub_small"]; h_qty_tot = 1
                hub_rows.append(f"{'Κεντρική μονάδα (40 συσκευές)':<40} | 1       | {PRICES['hub_small']:10.2f}€")
            elif base_count <= 97:
                hubs_cost = PRICES["hub_large"]; h_qty_tot = 1
                hub_rows.append(f"{'Κεντρική μονάδα (100 συσκευές)':<40} | 1       | {PRICES['hub_large']:10.2f}€")
            elif 97 < base_count <= 130:
                hubs_cost = PRICES["hub_large"] + PRICES["hub_small"]; h_qty_tot = 2
                hub_rows.append(f"{'Κεντρική μονάδα (100)':<40} | 1       | {PRICES['hub_large']:10.2f}€")
                hub_rows.append(f"{'Κεντρική μονάδα (40)':<40} | 1       | {PRICES['hub_small']:10.2f}€")
            else:
                hubs_cost = PRICES["hub_large"] * 2; h_qty_tot = 2
                hub_rows.append(f"{'Κεντρική μονάδα (100)':<40} | 2       | {PRICES['hub_large']*2:10.2f}€")
            
            total_dev = base_count + h_qty_tot

            if total_dev > 230:
                st.error(f"❌ ΣΦΑΛΜΑ: {total_dev} ΣΥΣΚΕΥΕΣ. ΤΟ ΟΡΙΟ ΕΙΝΑΙ 230.")
            else:
                mat_sum = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52) + (led*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + hubs_cost + e_cost + h_cost
                
                res = f"{'='*75}\n GEYER SMART HOME - ΑΝΑΛΥΤΙΚΗ ΠΡΟΣΦΟΡΑ\n{'='*75}\n"
                res += f"ΠΕΛΑΤΗΣ: {v_name.upper()} ({v_job})\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*75}\n"
                res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<40} | {'ΤΕΜΑΧΙΑ':<7} | {'ΤΙΜΗ':<11}\n{'-'*75}\n"
                for hr in hub_rows: res += f"{hr}\n"
                if on_off > 0: res += f"{'Φωτισμός On/Off':<40} | {on_off:<7} | {on_off*63.92:11.2f}€\n"
                if double > 0: res += f"{'Κομιτατέρ (Διπλές)':<40} | {double:<7} | {double*63.92:11.2f}€\n"
                if dim220 > 0: res += f"{'Dimming 220V':<40} | {dim220:<7} | {dim220*63.92:11.2f}€\n"
                for d in hvac_details: res += f"{d['n'][:40]:<40} | {d['q']:<7} | {d['p']:11.2f}€\n"
                if shutt > 0:  res += f"{'Ρολά / Τέντες':<40} | {shutt:<7} | {shutt*63.92:11.2f}€\n"
                if e_cost > 0: res += f"{'Μετρητής Ενέργειας':<40} | 1       | {e_cost:11.2f}€\n"
                if h_cost > 0: res += f"{'Έλεγχος Θερμοσίφωνα':<40} | 1       | {95.00:11.2f}€\n"
                res += f"{'-'*75}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev}\n"
                res += f"{'ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:':<51} {mat_sum:11.2f}€\n"
                res += f"{'ΦΠΑ 24%:':<51} {mat_sum*0.24:11.2f}€\n"
                res += f"{'ΓΕΝΙΚΟ ΣΥΝΟΛΟ:':<51} {mat_sum*1.24:11.2f}€\n"
                res += f"{'='*75}"
                st.code(res, language="text")
                st.button("📩 Αποστολή στον Νεκτάριο")
        st.markdown('</div>', unsafe_allow_html=True)
