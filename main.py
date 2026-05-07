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

# --- CSS ΓΙΑ ZERO-SCROLL DASHBOARD ---
st.markdown("""
    <style>
    /* Εξαφάνιση περιθωρίων σελίδας */
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    .stApp { background-color: #f8f9fa; }
    
    /* Compact Widgets */
    .stNumberInput, .stSelectbox, .stTextInput { margin-bottom: -15px !important; }
    div[data-testid="stMarkdownContainer"] p { font-size: 13px !important; font-weight: bold; margin-bottom: -5px; }
    
    /* Display Box - Σταθερό ύψος για να χωράει στην οθόνη */
    .display-box {
        background-color: #ffffff; padding: 10px; border: 2px solid #27ae60;
        border-radius: 8px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        height: auto;
    }
    pre {
        font-family: 'Consolas', monospace !important;
        font-size: 11px !important; line-height: 1.1 !important; color: #000 !important;
        background-color: #fff !important; border: none !important;
    }
    /* Σμίκρυνση Tabs */
    .stTabs [data-baseweb="tab"] { height: 35px; font-size: 14px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #1E3A8A; margin-top: -20px;'>GEYER PORTAL - ΡΩΤΑ ΤΟΝ ΝΕΚΤΑΡΙΟ</h3>", unsafe_allow_html=True)

tab_calc, tab_home, tab_docs, tab_contact = st.tabs(["📊 LIVE PRICING", "🏠 ΙΔΕΕΣ", "📂 ΒΙΒΛΙΟΘΗΚΗ", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    # 45% Ερωτήσεις - 55% Πίνακας
    left, right = st.columns([1, 1.2]) 
    
    with left:
        # 1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ (Σε μία σειρά)
        st.write("👤 **1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ**")
        c_p1, c_p2 = st.columns(2)
        v_name = c_p1.text_input("Ονοματεπώνυμο", key="name")
        v_job = c_p2.selectbox("Ιδιότητα", JOBS, key="job")
        v_addr = st.text_input("Διεύθυνση έργου", key="addr")

        # 2. ΦΩΤΙΣΜΟΣ (Πολύ compact)
        st.write("💡 **2. ΦΩΤΙΣΜΟΣ & DIMMING**")
        c1, c2, c3 = st.columns(3)
        int_l = c1.number_input("Εσωτερικές", min_value=0, value=0)
        ext_l = c2.number_input("Εξωτερικές", min_value=0, value=0)
        double = c3.number_input("Διπλές", min_value=0, value=0)
        
        c4, c5, c6, c7 = st.columns(4)
        dim220 = c4.number_input("Dim 220V", min_value=0)
        dim110 = c5.number_input("Dim 1-10V", min_value=0)
        led = c6.number_input("LED Dim", min_value=0)
        dali = c7.number_input("DALI", min_value=0)

        # 3 & 4 HVAC (Δίπλα δίπλα)
        st.write("🔥❄️ **3 & 4. ΘΕΡΜΑΝΣΗ & ΨΥΞΗ**")
        ch1, ch2 = st.columns(2)
        h_list = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split"]
        h_type = ch1.selectbox("Θέρμανση", h_list, key="h_type")
        h_qty = ch2.number_input("Ποσότητα (Θ)", min_value=0, key="h_qty")
        
        cc1, cc2 = st.columns(2)
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split"]
        c_type = cc1.selectbox("Ψύξη", c_list, key="c_type")
        c_qty = cc2.number_input("Ποσότητα (Ψ)", min_value=0, key="c_qty")
        
        if h_type == "VRV/VRF" or c_type == "VRV/VRF":
            st.write("**Μάρκα VRV:**")
            v_brand = st.selectbox("Επιλογή Brand", BRANDS, key="v_brand")
        else: v_brand = "Daikin"

        # 5 & 6 ΛΟΙΠΑ
        st.write("🪟🔌 **5 & 6. ΡΟΛΑ & ΠΙΝΑΚΑΣ**")
        cl1, cl2, cl3 = st.columns([1, 1.5, 1])
        shutt = cl1.number_input("Ρολά", min_value=0)
        energy = cl2.radio("Μετρητής", ["Όχι", "Μονοφ.", "Τριφ."], horizontal=True)
        heater = cl3.checkbox("Θερμοσίφ.")

    with right:
        st.markdown('<div class="display-box">', unsafe_allow_html=True)
        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        
        error_msg = None
        if not v_name or not v_job or not v_addr:
            error_msg = "⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
        elif on_off < 0:
            error_msg = "❌ ΣΦΑΛΜΑ: DIMMING > ΣΥΝΟΛΟ"
        elif h_type == "VRV/VRF" and c_type == "VRV/VRF" and v_brand == "Άλλη":
            error_msg = "❌ ΜΗ ΣΥΜΒΑΤΟ VRV"

        if error_msg:
            st.code(f"{'='*68}\n          {error_msg}\n{'='*68}")
        else:
            # Logic HVAC - Αποφυγή διπλοχρέωσης
            hvac_cost = 0; hvac_details = []
            is_common = (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός") or (h_type == c_type and h_type != "Κανένα")
            
            if is_common:
                p_key = "fancoil_ctrl" if "Fancoil" in h_type or "Δροσισμός" in c_type else "vrv_interface" if "VRV" in h_type else "split_ac" if "Split" in h_type else "heat_thermostat"
                hvac_cost = max(h_qty, c_qty) * PRICES[p_key]
                hvac_details.append({"n": f"{h_type} (Κοινό)", "q": max(h_qty, c_qty), "p": hvac_cost})
            else:
                if h_qty > 0:
                    h_keys = ["", "heat_thermostat", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "electric_heat", "vrv_interface", "split_ac"]
                    p = h_qty * PRICES[h_keys[h_list.index(h_type)]]; hvac_cost += p
                    hvac_details.append({"n": f"Θ:{h_type}", "q": h_qty, "p": p})
                if c_qty > 0:
                    c_keys = ["", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "vrv_interface", "split_ac"]
                    p = c_qty * PRICES[c_keys[c_list.index(c_type)]]; hvac_cost += p
                    hvac_details.append({"n": f"Ψ:{c_type}", "q": c_qty, "p": p})

            e_cost = 110 if "Μονοφ." in energy else 160 if "Τριφ." in energy else 0
            h_cost = 95 if heater else 0
            base_count = max(0, on_off) + double + dim220 + dim110 + led + dali + shutt + max(h_qty, c_qty) + (1 if e_cost > 0 else 0) + (1 if h_cost > 0 else 0)
            
            # Hub Logic
            h_cost_tot = 0; h_rows = []; h_q = 0
            if base_count <= 37:
                h_cost_tot = PRICES["hub_small"]; h_q = 1; h_rows.append(f"{'Κεντρική μονάδα (40)':<35} | 1       | {h_cost_tot:9.2f}€")
            elif base_count <= 97:
                h_cost_tot = PRICES["hub_large"]; h_q = 1; h_rows.append(f"{'Κεντρική μονάδα (100)':<35} | 1       | {h_cost_tot:9.2f}€")
            elif base_count <= 130:
                h_cost_tot = PRICES["hub_large"] + PRICES["hub_small"]; h_q = 2
                h_rows.append(f"{'Κεντρική μονάδα (100)':<35} | 1       | {PRICES['hub_large']:9.2f}€")
                h_rows.append(f"{'Κεντρική μονάδα (40)':<35} | 1       | {PRICES['hub_small']:9.2f}€")
            else:
                h_cost_tot = PRICES["hub_large"] * 2; h_q = 2; h_rows.append(f"{'Κεντρική μονάδα (100)':<35} | 2       | {h_cost_tot:9.2f}€")
            
            total_dev = base_count + h_q
            mat_sum = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52) + (led*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + h_cost_tot + e_cost + h_cost

            res = f"{'='*65}\n GEYER SMART HOME - LIVE PRICING\n{'='*65}\n"
            res += f"ΠΕΛΑΤΗΣ: {v_name.upper()} | {v_job}\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*65}\n"
            res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<35} | {'TEM':<7} | {'TIMH':<10}\n{'-'*65}\n"
            for hr in h_rows: res += f"{hr}\n"
            if on_off > 0: res += f"{'Φωτισμός On/Off':<35} | {on_off:<7} | {on_off*63.92:9.2f}€\n"
            if double > 0: res += f"{'Κομιτατέρ (Διπλές)':<35} | {double:<7} | {double*63.92:9.2f}€\n"
            for d in hvac_details: res += f"{d['n'][:35]:<35} | {d['q']:<7} | {d['p']:9.2f}€\n"
            if shutt > 0: res += f"{'Ρολά / Τέντες':<35} | {shutt:<7} | {shutt*63.92:9.2f}€\n"
            if heater:    res += f"{'Έλεγχος Θερμοσίφωνα':<35} | 1       | {95.00:9.2f}€\n"
            res += f"{'-'*65}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev} / 230\n"
            res += f"{'ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:':<46} {mat_sum:10.2f}€\n"
            res += f"{'ΦΠΑ 24%:':<46} {mat_sum*0.24:10.2f}€\n"
            res += f"{'ΓΕΝΙΚΟ ΣΥΝΟΛΟ:':<46} {mat_sum*1.24:10.2f}€\n"
            res += f"{'='*65}"
            st.code(res, language="text")
            st.button("📩 Αποστολή")
        st.markdown('</div>', unsafe_allow_html=True)
