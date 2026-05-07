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

st.set_page_config(page_title="GEYER Technical Portal", layout="wide")

# --- CUSTOM CSS ΓΙΑ DISPLAY & UI ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .display-text {
        background-color: #ffffff;
        padding: 25px;
        border: 1px solid #d1d1d1;
        font-family: 'Consolas', 'Courier New', monospace;
        color: black;
        white-space: pre;
        font-size: 13px;
        line-height: 1.2;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- ΚΕΝΤΡΙΚΟ ΜΕΝΟΥ ΠΑΝΩ ---
tab_home, tab_calc, tab_docs, tab_contact = st.tabs(["🏠 ΑΡΧΙΚΗ & ΙΔΕΕΣ", "📊 LIVE PRICING", "📂 ΒΙΒΛΙΟΘΗΚΗ", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

# --- 1. ΑΡΧΙΚΗ ---
with tab_home:
    st.markdown("<h2 style='text-align: center;'>📸 Digital Showroom & Ιδέες</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.image("https://unsplash.com", caption="Smart Lighting")
    with c2: st.image("https://unsplash.com", caption="HVAC Control")

# --- 2. LIVE PRICING (ΟΛΟΚΛΗΡΩΜΕΝΟ) ---
with tab_calc:
    st.markdown("<h2 style='text-align: center;'>📊 Live Pricing System (CEO Edition)</h2>", unsafe_allow_html=True)
    left, right = st.columns([1, 1.1])

    with left:
        st.subheader("1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ")
        v_name = st.text_input("Ονοματεπώνυμο")
        v_job = st.selectbox("Ιδιότητα", JOBS)
        v_addr = st.text_input("Διεύθυνση έργου")

        st.subheader("2. ΦΩΤΙΣΜΟΣ")
        c1, c2 = st.columns(2)
        int_l = c1.number_input("Εσωτερικές", min_value=0)
        ext_l = c2.number_input("Εξωτερικές", min_value=0)
        st.markdown("**2α. ΑΝΑΛΥΣΗ DIMMING**")
        d220 = st.number_input("Dimming 220V", min_value=0)
        d110 = st.number_input("Dimming 1-10V", min_value=0)
        led = st.number_input("Ταινίες LED Dim", min_value=0)
        dali = st.number_input("DALI", min_value=0)
        double = st.number_input("Κομιτατέρ (Διπλές)", min_value=0)

        st.subheader("3. ΘΕΡΜΑΝΣΗ")
        h_list = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split"]
        h_labels = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. σωμάτων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
        h_type = st.selectbox("Επιλογή Θέρμανσης", h_list)
        h_qty = st.number_input(h_labels[h_list.index(h_type)], min_value=0, key="h")
        if h_type == "VRV/VRF": h_brand = st.selectbox("Μάρκα VRV (Θ)", BRANDS)

        st.subheader("4. ΨΥΞΗ")
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split"]
        c_labels = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
        c_type = st.selectbox("Επιλογή Ψύξης", c_list)
        c_qty = st.number_input(c_labels[c_list.index(c_type)], min_value=0, key="c")
        if c_type == "VRV/VRF": c_brand = st.selectbox("Μάρκα VRV (Ψ)", BRANDS)

        st.subheader("5 & 6 ΛΟΙΠΑ")
        shutt = st.number_input("Ρολά/Τέντες", min_value=0)
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        st.subheader("🖥️ ΠΡΟΣΦΟΡΑ")
        on_off = (int_l + ext_l) - (d220 + d110 + led + dali + (double * 2))
        
        if not v_name or not v_job or not v_addr:
            st.warning("⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ")
        elif on_off < 0:
            st.error("❌ ΣΦΑΛΜΑ: DIMMING > ΣΥΝΟΛΟ ΓΡΑΜΜΩΝ")
        elif (h_type == "VRV/VRF" and h_brand == "Άλλη") or (c_type == "VRV/VRF" and c_brand == "Άλλη"):
            st.error("❌ ΜΗ ΣΥΜΒΑΤΟ ΣΥΣΤΗΜΑ VRV")
        else:
            # Logic HVAC
            hvac_cost = 0; hvac_details = []
            if h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός":
                hvac_cost = h_qty * PRICES["fancoil_ctrl"]
                hvac_details.append({"n": "Ενδοδαπέδια με Δροσισμό", "q": h_qty, "p": hvac_cost})
            else:
                if h_qty > 0:
                    h_keys = ["", "heat_thermostat", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "electric_heat", "vrv_interface", "split_ac"]
                    p = h_qty * PRICES[h_keys[h_list.index(h_type)]]
                    hvac_cost += p
                    hvac_details.append({"n": h_type, "q": h_qty, "p": p})
                if c_qty > 0:
                    c_keys = ["", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "vrv_interface", "split_ac"]
                    p = c_qty * PRICES[c_keys[c_list.index(c_type)]]
                    hvac_cost += p
                    hvac_details.append({"n": c_type, "q": c_qty, "p": p})

            e_cost = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0
            dev_count = max(0, on_off) + double + d220 + d110 + led + dali + shutt + h_qty + (1 if e_cost > 0 else 0)
            hubs_cost = PRICES["hub_small"] if dev_count <= 37 else PRICES["hub_large"]
            mat_sum = (max(0,on_off)*63.92) + (double*63.92) + (d220*63.92) + (d110*52) + (led*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + hubs_cost + e_cost + (95 if heater else 0)

            # --- DISPLAY ---
            res = f"{'='*65}\n GEYER SMART HOME - ΑΝΑΛΥΤΙΚΗ ΠΡΟΣΦΟΡΑ\n{'='*65}\n"
            res += f"ΠΕΛΑΤΗΣ: {v_name.upper()} ({v_job})\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*65}\n"
            res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<30} | {'TEM':<5} | {'TIMH':<10}\n{'-'*65}\n"
            res += f"{'Κεντρική Μονάδα Hub':<30} | 1     | {hubs_cost:9.2f}€\n"
            if on_off > 0: res += f"{'Φωτισμός On/Off':<30} | {on_off:<5} | {on_off*63.92:9.2f}€\n"
            if double > 0: res += f"{'Κομιτατέρ (Διπλές)':<30} | {double:<5} | {double*63.92:9.2f}€\n"
            if d220 > 0:   res += f"{'Dimming 220V':<30} | {d220:<5} | {d220*63.92:9.2f}€\n"
            if d110 > 0:   res += f"{'Dimming 1-10V':<30} | {d110:<5} | {d110*52.00:9.2f}€\n"
            if led > 0:    res += f"{'Ταινίες LED Dim':<30} | {led:<5} | {led*63.92:9.2f}€\n"
            if dali > 0:   res += f"{'Γραμμές DALI':<30} | {dali:<5} | {dali*160.00:9.2f}€\n"
            for d in hvac_details: res += f"{d['n'][:30]:<30} | {d['q']:<5} | {d['p']:9.2f}€\n"
            if shutt > 0:  res += f"{'Ρολά / Τέντες':<30} | {shutt:<5} | {shutt*63.92:9.2f}€\n"
            if e_cost > 0: res += f"{'Μετρητής Ενέργειας':<30} | 1     | {e_cost:9.2f}€\n"
            if heater:     res += f"{'Έλεγχος Θερμοσίφωνα':<30} | 1     | {95.00:9.2f}€\n"
            res += f"{'-'*65}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {dev_count}\nΚΑΘΑΡΗ ΑΞΙΑ: {mat_sum:27.2f}€\n"
            res += f"ΜΕ ΦΠΑ 24%: {mat_sum*1.24:28.2f}€\nΚΟΣΤΟΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ: {mat_sum*0.20:19.2f}€\n{'='*65}"
            
            st.markdown(f"<div class='display-text'>{res}</div>", unsafe_allow_html=True)
            st.button("📩 Αποστολή στον Νεκτάριο")

# --- 3. ΒΙΒΛΙΟΘΗΚΗ ---
with tab_docs:
    st.subheader("📂 Τεχνικά Φυλλάδια")
    st.write("Εδώ θα βρείτε τα PDF που ανεβάζετε στο GitHub.")

# --- 4. ΕΠΙΚΟΙΝΩΝΙΑ ---
with tab_contact:
    st.subheader("📨 Ρωτήστε τον Νεκτάριο")
    st.text_area("Περιγράψτε την ερώτησή σας:")
    st.button("Αποστολή Ερώτησης")
