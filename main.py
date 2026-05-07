import streamlit as st
from datetime import datetime

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

# --- CUSTOM CSS ΓΙΑ COMPACT UI & GRAPHICS ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .spacer { height: 230px; } 
    [data-testid="stVerticalBlock"] > div:has(div.display-box) {
        position: sticky; top: 0.5rem; z-index: 1000;
    }
    /* Μίκρυμα γραμματοσειρών αριστερά */
    .compact-label { font-size: 14px !important; font-weight: bold; color: #1E3A8A; margin-bottom: -15px; }
    .stNumberInput label, .stSelectbox label, .stRadio label { font-size: 12px !important; }
    
    .display-box {
        background-color: #ffffff; padding: 15px; border: 2px solid #27ae60;
        border-radius: 5px; box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
    }
    pre {
        font-family: 'Consolas', 'Lucida Console', monospace !important;
        font-size: 12px !important; line-height: 1.1 !important; color: #000000 !important;
    }
    .main-header { text-align: center; color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-header'><h1>GEYER PORTAL</h1><p style='font-size:18px;'>ΡΩΤΑ ΤΟΝ ΝΕΚΤΑΡΙΟ</p></div>", unsafe_allow_html=True)

tab_home, tab_calc, tab_docs, tab_contact = st.tabs(["🏠 ΑΡΧΙΚΗ & ΙΔΕΕΣ", "📊 LIVE PRICING", "📂 ΒΙΒΛΙΟΘΗΚΗ", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    left, right = st.columns([1, 1.3])
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
        # Μηδενισμός ποσότητας αν είναι 'Κανένα'
        h_val = 0 if h_type == "Κανένα" else st.session_state.get('h_qty', 0)
        h_qty = st.number_input(h_labels[h_list.index(h_type)], min_value=0, value=h_val, key="h_qty")

        h_brand = "Daikin"
        if h_type == "VRV/VRF": h_brand = st.selectbox("Μάρκα VRV (Θ)", BRANDS)

        st.markdown("<p class='compact-label'>❄️ 4. ΨΥΞΗ</p>", unsafe_allow_html=True)
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split"]
        c_labels = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
        c_type = st.selectbox("Επιλογή Ψύξης", c_list, key="c_type")
        # Μηδενισμός ποσότητας αν είναι 'Κανένα'
        c_val = 0 if c_type == "Κανένα" else st.session_state.get('c_qty', 0)
        c_qty = st.number_input(c_labels[c_list.index(c_type)], min_value=0, value=c_val, key="c_qty")
        
        c_brand = "Daikin"
        if c_type == "VRV/VRF": c_brand = st.selectbox("Μάρκα VRV (Ψ)", BRANDS)

        st.markdown("<p class='compact-label'>🪟 5. ΡΟΛΑ</p>", unsafe_allow_html=True)
        shutt = st.number_input("Ρολά / Τέντες", min_value=0, value=0)

        st.markdown("<p class='compact-label'>🔌 6. ΠΙΝΑΚΑΣ</p>", unsafe_allow_html=True)
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True) 
        st.markdown('<div class="display-box">', unsafe_allow_html=True)
        st.subheader("🖥️ LIVE PRICING SYSTEM")
        
        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        
        error_msg = None
        if not v_name or not v_job or not v_addr:
            # Εμφάνιση του display ακόμα και χωρίς στοιχεία, αλλά με προειδοποίηση
            error_msg = "⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
        elif on_off < 0:
            error_msg = "❌ ΣΦΑΛΜΑ: DIMMING > ΣΥΝΟΛΟ"
        
        # HVAC Logic (με μηδενισμό αν Κανένα)
        hvac_cost = 0; hvac_details = []
        
        # Έλεγχος συμβατότητας
        if not error_msg:
            if h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός" and h_qty != c_qty:
                error_msg = "❌ ΛΑΘΟΣ: ΙΔΙΑ ΠΟΣΟΤΗΤΑ ΣΕ ΕΝΔΟΔΑΠΕΔΙΑ Θ/Ψ"
            elif h_type == c_type and h_type != "Κανένα" and h_qty != c_qty:
                error_msg = f"❌ ΛΑΘΟΣ: ΙΔΙΑ ΠΟΣΟΤΗΤΑ ΣΕ {h_type}"
            elif h_type == "VRV/VRF" and c_type == "VRV/VRF" and h_brand != c_brand:
                error_msg = "❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV"

        if error_msg:
            st.code(f"{'='*68}\n        {error_msg}\n{'='*68}")
        else:
            # Calculations
            if h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός":
                hvac_cost = h_qty * PRICES["fancoil_ctrl"]
                hvac_details.append({"n": "Ενδοδαπέδια με Δροσισμό", "q": h_qty, "p": hvac_cost})
            else:
                if h_qty > 0 and h_type != "Κανένα":
                    h_keys = ["", "heat_thermostat", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "electric_heat", "vrv_interface", "split_ac"]
                    p = h_qty * PRICES[h_keys[h_list.index(h_type)]]
                    hvac_cost += p
                    hvac_details.append({"n": f"Θ: {h_type} {h_brand if 'VRV' in h_type else ''}", "q": h_qty, "p": p})
                if c_qty > 0 and c_type != "Κανένα":
                    c_keys = ["", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "vrv_interface", "split_ac"]
                    p = c_qty * PRICES[c_keys[c_list.index(c_type)]]
                    hvac_cost += p
                    hvac_details.append({"n": f"Ψ: {c_type} {c_brand if 'VRV' in c_type else ''}", "q": c_qty, "p": p})

            e_cost = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0
            h_cost = 95 if heater else 0
            base_count = max(0, on_off) + double + dim220 + dim110 + led + dali + shutt + h_qty + (1 if e_cost > 0 else 0) + (1 if h_cost > 0 else 0)
            
            # Hub Selection
            hubs_cost = 0; hub_rows = []; hub_qty_total = 0
            if base_count <= 37:
                hubs_cost = PRICES["hub_small"]; hub_qty_total = 1
                hub_rows.append(f"{'Κεντρική μονάδα (40 συσκευές)':<35} | 1       | {PRICES['hub_small']:9.2f}€")
            elif base_count <= 97:
                hubs_cost = PRICES["hub_large"]; hub_qty_total = 1
                hub_rows.append(f"{'Κεντρική μονάδα (100 συσκευές)':<35} | 1       | {PRICES['hub_large']:9.2f}€")
            elif 97 < base_count <= 130:
                hubs_cost = PRICES["hub_large"] + PRICES["hub_small"]; hub_qty_total = 2
                hub_rows.append(f"{'Κεντρική μονάδα (100)':<35} | 1       | {PRICES['hub_large']:9.2f}€")
                hub_rows.append(f"{'Κεντρική μονάδα (40)':<35} | 1       | {PRICES['hub_small']:9.2f}€")
            else:
                hubs_cost = PRICES["hub_large"] * 2; hub_qty_total = 2
                hub_rows.append(f"{'Κεντρική μονάδα (100)':<35} | 2       | {PRICES['hub_large']*2:9.2f}€")
            
            total_dev = base_count + hub_qty_total

            if total_dev > 230:
                st.error(f"❌ ΣΦΑΛΜΑ: {total_dev} ΣΥΣΚΕΥΕΣ (ΟΡΙΟ 230)")
            else:
                mat_sum = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52) + (led*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + hubs_cost + e_cost + h_cost
                
                res = f"{'='*68}\n GEYER SMART HOME - ΑΝΑΛΥΤΙΚΗ ΠΡΟΣΦΟΡΑ\n{'='*68}\n"
                res += f"ΠΕΛΑΤΗΣ: {v_name.upper()}\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*68}\n"
                res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<35} | {'ΤΕΜΑΧΙΑ':<7} | {'ΤΙΜΗ':<10}\n{'-'*68}\n"
                for row in hub_rows: res += f"{row}\n"
                if on_off > 0: res += f"{'Γραμμές Φωτισμού On/Off':<35} | {on_off:<7} | {on_off*63.92:9.2f}€\n"
                if double > 0: res += f"{'Κομιτατέρ (Διπλές)':<35} | {double:<7} | {double*63.92:9.2f}€\n"
                for d in hvac_details: res += f"{d['n'][:35]:<35} | {d['q']:<7} | {d['p']:9.2f}€\n"
                if shutt > 0:  res += f"{'Ρολά / Τέντες':<35} | {shutt:<7} | {shutt*63.92:9.2f}€\n"
                if e_cost > 0: res += f"{'Μετρητής Ενέργειας':<35} | 1       | {e_cost:9.2f}€\n"
                if h_cost > 0: res += f"{'Έλεγχος Θερμοσίφωνα':<35} | 1       | {95.00:9.2f}€\n"
                res += f"{'-'*68}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev}\n"
                res += f"{'ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:':<46} {mat_sum:11.2f}€\n"
                res += f"{'ΦΠΑ 24%:':<46} {mat_sum*0.24:11.2f}€\n"
                res += f"{'ΓΕΝΙΚΟ ΣΥΝΟΛΟ:':<46} {mat_sum*1.24:11.2f}€\n"
                res += f"{'='*68}"
                st.code(res, language="text")
                st.button("📩 Αποστολή")
        st.markdown('</div>', unsafe_allow_html=True)

with tab_home: st.markdown("### 🏠 Digital Showroom")
with tab_docs: st.markdown("### 📂 Βιβλιοθήκη")
with tab_contact: st.markdown("### 📨 Επικοινωνία")
