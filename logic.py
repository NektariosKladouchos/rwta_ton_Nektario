import streamlit as st

# --- ΣΤΑΘΕΡΕΣ ΤΙΜΕΣ ΑΠΟ EXE ---
PRICES = {
    "on_off": 63.92, "double_on_off": 63.92, "dim_220v": 63.92, "dim_1_10v": 52.0, 
    "led_strip": 63.92, "dali": 160.0, "shutter": 63.92, 
    "energy_1ph": 110.0, "energy_3ph": 160.0, "heater": 95.0,
    "heat_thermostat": 120.0, "fancoil_ctrl": 130.0, "electric_heat": 70.0, 
    "split_ac": 100.0, "vrv_interface": 260.0, "hub_small": 139.0, "hub_large": 609.0
}
BRANDS = ["Daikin", "LG", "Toshiba", "Fujitsu", "Mitsubishi", "Panasonic", "Midea", "Άλλη"]
JOBS = ["", "Κατασκευαστής", "Μηχανικός", "Αρχιτέκτονας", "Ηλεκτρολόγος", "Κατάστημα", "Ιδιώτης"]

st.set_page_config(page_title="GEYER Live Pricing Dashboard", layout="wide")

# CSS για να φύγει το μαύρο φόντο και να μοιάζει με το EXE
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f5; }
    .display-box {
        background-color: #ecf0f1;
        padding: 20px;
        border: 1px solid #d1d1d1;
        font-family: 'Consolas', 'Courier New', monospace;
        white-space: pre;
        color: #2c3e50;
        font-size: 14px;
        line-height: 1.2;
    }
    .header-style { background-color: #27ae60; padding: 10px; color: white; text-align: center; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='header-style'><h1>GEYER SMART HOME</h1><p>LIVE PRICING SYSTEM</p></div>", unsafe_allow_html=True)

l_col, r_col = st.columns([1, 1.1])

with l_col:
    # 1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ
    st.subheader("1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ")
    v_name = st.text_input("Ονοματεπώνυμο / Επωνυμία")
    v_job = st.selectbox("Ιδιότητα (Υποχρεωτικό)", JOBS)
    v_addr = st.text_input("Διεύθυνση έργου")

    # 2. ΦΩΤΙΣΜΟΣ
    st.subheader("2. ΣΥΝΟΛΙΚΕΣ ΓΡΑΜΜΕΣ ΦΩΤΙΣΜΟΥ")
    c1, c2 = st.columns(2)
    int_l = c1.number_input("Εσωτερικές", min_value=0, step=1)
    ext_l = c2.number_input("Εξωτερικές", min_value=0, step=1)
    
    st.write("**2α. ΕΙΔΗ ΓΡΑΜΜΩΝ ΠΟΥ ΘΕΛΟΥΜΕ DIMMING**")
    cd1, cd2 = st.columns(2)
    dim220 = cd1.number_input("Dimming 220V", min_value=0)
    dim110 = cd2.number_input("Dimming 1-10V", min_value=0)
    led = cd1.number_input("Ταινίες LED Dim", min_value=0)
    dali = cd2.number_input("DALI", min_value=0)
    double = st.number_input("Κομιτατέρ (Διπλές)", min_value=0)

    # 3 & 4 HVAC
    st.subheader("3. ΘΕΡΜΑΝΣΗ")
    h_type = st.selectbox("Επιλογή Θέρμανσης", ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil νερού οροφής", "Fancoil νερού δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Κλιματιστικά split"])
    h_qty = st.number_input("Ποσότητα (Θ)", min_value=0)
    h_brand = "Daikin"
    if h_type == "VRV/VRF": h_brand = st.selectbox("Μάρκα VRV (Θ)", BRANDS)

    st.subheader("4. ΨΥΞΗ")
    c_type = st.selectbox("Επιλογή Ψύξης", ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil νερού οροφής", "Fancoil νερού δαπέδου", "VRV/VRF", "Κλιματιστικά split"])
    c_qty = st.number_input("Ποσότητα (Ψ)", min_value=0)
    c_brand = "Daikin"
    if c_type == "VRV/VRF": c_brand = st.selectbox("Μάρκα VRV (Ψ)", BRANDS)

    # 5 & 6
    st.subheader("5. ΡΟΛΑ / ΤΕΝΤΕΣ")
    shutt = st.number_input("Τεμάχια", min_value=0)
    st.subheader("6. ΠΙΝΑΚΑΣ")
    energy = st.radio("Έλεγχος Ενέργειας", ["Όχι", "Μονοφασικός μετρητής", "Τριφασικός μετρητής"], horizontal=True)
    heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

# --- BACKEND LOGIC (ΑΠΟ ΤΟ EXE) ---
def calculate():
    on_off_lines = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
    
    # HVAC Logic
    hvac_cost = 0
    hvac_details = []
    
    # Ειδική περίπτωση Δροσισμού
    if h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός":
        cost = h_qty * PRICES["fancoil_ctrl"]
        hvac_cost = cost
        hvac_details.append({"name": "Ενδοδαπέδια με Δροσισμό", "qty": h_qty, "price": cost})
    else:
        if h_qty > 0:
            h_keys = ["", "heat_thermostat", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "electric_heat", "vrv_interface", "split_ac"]
            # Map index
            h_idx = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil νερού οροφής", "Fancoil νερού δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Κλιματιστικά split"].index(h_type)
            if h_idx > 0:
                cost = h_qty * PRICES[h_keys[h_idx]]
                hvac_cost += cost
                hvac_details.append({"name": f"Θ: {h_type}", "qty": h_qty, "price": cost})
        
        if c_qty > 0:
            c_keys = ["", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "vrv_interface", "split_ac"]
            c_idx = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil νερού οροφής", "Fancoil νερού δαπέδου", "VRV/VRF", "Κλιματιστικά split"].index(c_type)
            if c_idx > 0:
                cost = c_qty * PRICES[c_keys[c_idx]]
                hvac_cost += cost
                hvac_details.append({"name": f"Ψ: {c_type}", "qty": c_qty, "price": cost})

    e_cost = 110 if energy == "Μονοφασικός μετρητής" else 160 if energy == "Τριφασικός μετρητής" else 0
    h_cost = 95 if heater else 0
    
    base_dev_count = max(0, on_off_lines) + double + dim220 + dim110 + led + dali + shutt + h_qty + (1 if e_cost > 0 else 0) + (1 if h_cost > 0 else 0)
    
    # Hub Logic
    hubs_cost = 0; hub_rows = []
    if base_dev_count <= 37:
        hubs_cost = PRICES["hub_small"]
        hub_rows.append(f"{'Κεντρική μονάδα (40 συσκευές)':<35} | 1       | {PRICES['hub_small']:9.2f}€")
    elif base_dev_count <= 97:
        hubs_cost = PRICES["hub_large"]
        hub_rows.append(f"{'Κεντρική μονάδα (100 συσκευές)':<35} | 1       | {PRICES['hub_large']:9.2f}€")
    else:
        hubs_cost = PRICES["hub_large"] + PRICES["hub_small"]
        hub_rows.append(f"{'Κεντρική μονάδα (100+40)':<35} | 1       | {hubs_cost:9.2f}€")

    mat_sum = (max(0, on_off_lines)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52) + (led*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + hubs_cost + e_cost + h_cost
    prog_fee = mat_sum * 0.20
    
    return on_off_lines, base_dev_count, mat_sum, prog_fee, hub_rows, hvac_details, e_cost, h_cost

with r_col:
    st.subheader("🖥️ LIVE PRICING DISPLAY")
    if not v_name or not v_job or not v_addr:
        st.warning("⚠️ LIVE PRICING: ΣΥΜΠΛΗΡΩΣΤΕ ΟΝΟΜΑ, ΙΔΙΟΤΗΤΑ & ΔΙΕΥΘΥΝΣΗ")
    else:
        on_off, total_dev, mat_sum, prog_fee, hub_rows, hvac_details, e_cost, h_cost = calculate()
        
        res = f"{'='*70}\n GEYER SMART HOME - ΑΝΑΛΥΤΙΚΗ ΠΡΟΣΦΟΡΑ\n{'='*70}\n"
        res += f"ΠΕΛΑΤΗΣ: {v_name.upper()} ({v_job})\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*70}\n"
        res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<35} | {'ΤΕΜΑΧΙΑ':<7} | {'ΤΙΜΗ':<10}\n{'-'*70}\n"
        for hr in hub_rows: res += f"{hr}\n"
        if on_off > 0: res += f"{'Γραμμές Φωτισμού On/Off':<35} | {on_off:<7} | {on_off*63.92:9.2f}€\n"
        if double > 0: res += f"{'Κομιτατέρ (Διπλές)':<35} | {double:<7} | {double*63.92:9.2f}€\n"
        for d in hvac_details: res += f"{d['name'][:35]:<35} | {d['qty']:<7} | {d['price']:9.2f}€\n"
        if e_cost > 0: res += f"{'Μετρητής Ενέργειας':<35} | 1       | {e_cost:9.2f}€\n"
        if h_cost > 0: res += f"{'Έλεγχος Θερμοσίφωνα':<35} | 1       | {h_cost:9.2f}€\n"
        res += f"{'-'*70}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev}\n"
        res += f"ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ: {mat_sum:27.2f}€\n"
        res += f"ΑΞΙΑ ΥΛΙΚΩΝ ΜΕ ΦΠΑ 24%: {mat_sum*1.24:23.2f}€\n{'-'*70}\n"
        res += f"ΚΟΣΤΟΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ: {prog_fee:23.2f}€\n(Προαιρετική υπηρεσία)\n{'='*70}"
        
        st.markdown(f"<div class='display-box'>{res}</div>", unsafe_allow_html=True)
        
        if st.button("💾 ΑΠΟΣΤΟΛΗ & ΑΠΟΘΗΚΕΥΣΗ"):
            st.balloons()
            st.success("Η προσφορά καταγράφηκε!")
