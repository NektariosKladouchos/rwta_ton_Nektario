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

# --- CUSTOM CSS ΓΙΑ STICKY DISPLAY & UI ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    [data-testid="stVerticalBlock"] > div:has(div.display-box) {
        position: sticky;
        top: 2rem;
        z-index: 1000;
    }
    .display-box {
        background-color: #ffffff;
        padding: 20px;
        border: 2px solid #27ae60;
        font-family: 'Consolas', 'Courier New', monospace;
        color: black;
        white-space: pre;
        font-size: 13px;
        line-height: 1.1;
    }
    .main-header { text-align: center; color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-header'><h1>GEYER PORTAL</h1><h3>ΡΩΤΑ ΤΟΝ ΝΕΚΤΑΡΙΟ</h3></div>", unsafe_allow_html=True)

tab_home, tab_calc, tab_docs, tab_contact = st.tabs(["🏠 ΑΡΧΙΚΗ & ΙΔΕΕΣ", "📊 LIVE PRICING", "📂 ΒΙΒΛΙΟΘΗΚΗ", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    left, right = st.columns([1, 1.1])
    with left:
        st.subheader("1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ")
        v_name = st.text_input("Ονοματεπώνυμο")
        v_job = st.selectbox("Ιδιότητα", JOBS)
        v_addr = st.text_input("Διεύθυνση έργου")

        st.subheader("2. ΦΩΤΙΣΜΟΣ")
        c1, c2 = st.columns(2)
        int_l = c1.number_input("Εσωτερικές", min_value=0, value=0)
        ext_l = c2.number_input("Εξωτερικές", min_value=0, value=0)
        st.markdown("**2α. ΑΝΑΛΥΣΗ DIMMING**")
        dim220 = st.number_input("Dimming 220V", min_value=0, value=0)
        dim110 = st.number_input("Dimming 1-10V", min_value=0, value=0)
        led = st.number_input("Ταινίες LED Dim", min_value=0, value=0)
        dali = st.number_input("DALI", min_value=0, value=0)
        double = st.number_input("Κομιτατέρ (Διπλές)", min_value=0, value=0)

        st.subheader("3. ΘΕΡΜΑΝΣΗ")
        h_list = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split"]
        h_labels = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. σωμάτων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
        h_type = st.selectbox("Επιλογή Θέρμανσης", h_list)
        h_qty = st.number_input(h_labels[h_list.index(h_type)], min_value=0, key="h")
        h_brand = ""
        if h_type == "VRV/VRF": h_brand = st.selectbox("Μάρκα VRV (Θ)", BRANDS)

        st.subheader("4. ΨΥΞΗ")
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split"]
        c_labels = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
        c_type = st.selectbox("Επιλογή Ψύξης", c_list)
        c_qty = st.number_input(c_labels[c_list.index(c_type)], min_value=0, key="c")
        c_brand = ""
        if c_type == "VRV/VRF": c_brand = st.selectbox("Μάρκα VRV (Ψ)", BRANDS)

        st.subheader("5. ΡΟΛΑ")
        shutt = st.number_input("Ρολά / Τέντες / Κουρτίνες", min_value=0, value=0)

        st.subheader("6. ΠΙΝΑΚΑΣ")
        energy = st.radio("Μετρητής Ενέργειας", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        st.markdown('<div class="display-box">', unsafe_allow_html=True)
        st.subheader("🖥️ ΠΡΟΣΦΟΡΑ")
        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        
        if not v_name or not v_job or not v_addr:
            res = f"{'='*60}\n GEYER SMART HOME - ΠΡΟΣΦΟΡΑ\n{'='*60}\n⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ\n{'-'*60}\nΚΑΘΑΡΗ ΑΞΙΑ: 0.00€\n{'='*60}"
            st.text(res)
        elif on_off < 0:
            st.error("❌ ΣΦΑΛΜΑ: DIMMING > ΣΥΝΟΛΟ")
        else:
            hvac_cost = 0; hvac_details = []
            # Check for common thermostat logic
            is_common = (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός") or \
                        (h_type == "Fancoil οροφής" and c_type == "Fancoil οροφής") or \
                        (h_type == "VRV/VRF" and c_type == "VRV/VRF")
            
            if is_common:
                p_key = "fancoil_ctrl" if "Fancoil" in h_type or "Δροσισμός" in c_type else "vrv_interface" if "VRV" in h_type else "heat_thermostat"
                hvac_cost = h_qty * PRICES[p_key]
                hvac_details.append({"n": f"{h_type} (Κοινό)", "q": h_qty, "p": hvac_cost})
            else:
                if h_qty > 0:
                    h_keys = ["", "heat_thermostat", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "electric_heat", "vrv_interface", "split_ac"]
                    p = h_qty * PRICES[h_keys[h_list.index(h_type)]]
                    hvac_cost += p
                    hvac_details.append({"n": f"Θ: {h_type} {h_brand}", "q": h_qty, "p": p})
                if c_qty > 0:
                    c_keys = ["", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "vrv_interface", "split_ac"]
                    p = c_qty * PRICES[c_keys[c_list.index(c_type)]]
                    hvac_cost += p
                    hvac_details.append({"n": f"Ψ: {c_type} {c_brand}", "q": c_qty, "p": p})

            e_cost = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0
            dev_count = max(0, on_off) + double + dim220 + dim110 + led + dali + shutt + h_qty + (1 if e_cost > 0 else 0)
            hubs_cost = PRICES["hub_small"] if dev_count <= 37 else PRICES["hub_large"]
            mat_sum = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52) + (led*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + hubs_cost + e_cost + (95 if heater else 0)

            res = f"{'='*60}\n GEYER SMART HOME - ΠΡΟΣΦΟΡΑ\n{'='*60}\n"
            res += f"ΠΕΛΑΤΗΣ: {v_name.upper()}\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*60}\n"
            res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<28} | {'TEM':<4} | {'TIMH':<9}\n{'-'*60}\n"
            res += f"{'Hub Κεντρική Μονάδα':<28} | 1    | {hubs_cost:8.2f}€\n"
            if on_off > 0: res += f"{'Φωτισμός On/Off':<28} | {on_off:<4} | {on_off*63.92:8.2f}€\n"
            for d in hvac_details: res += f"{d['n'][:28]:<28} | {d['q']:<4} | {d['p']:8.2f}€\n"
            if shutt > 0: res += f"{'Ρολά / Τέντες':<28} | {shutt:<4} | {shutt*63.92:8.2f}€\n"
            if e_cost > 0: res += f"{'Μετρητής Ενέργειας':<28} | 1    | {e_cost:8.2f}€\n"
            if heater:    res += f"{'Έλεγχος Θερμοσίφωνα':<28} | 1    | {95.00:8.2f}€\n"
            res += f"{'-'*60}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {dev_count}\n"
            res += f"ΚΑΘΑΡΗ ΑΞΙΑ: {mat_sum:23.2f}€\n"
            res += f"ΜΕ ΦΠΑ 24%: {mat_sum*1.24:26.2f}€\n"
            res += f"ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ (20%): {mat_sum*0.20:17.2f}€\n{'='*60}"
            st.text(res)
            st.button("📩 Αποστολή")
        st.markdown('</div>', unsafe_allow_html=True)

with tab_home: st.markdown("### 🏠 Digital Showroom")
with tab_docs: st.markdown("### 📂 Βιβλιοθήκη")
with tab_contact: st.markdown("### 📨 Επικοινωνία")
