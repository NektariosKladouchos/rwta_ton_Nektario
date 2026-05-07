import streamlit as st
from datetime import datetime

# --- ΣΤΑΘΕΡΕΣ & ΤΙΜΕΣ ΑΠΟ ΤΟ EXE ---
PRICES = {
    "on_off": 63.92, "double_on_off": 63.92, "dim_220v": 63.92, "dim_1_10v": 52.0, 
    "led_strip": 63.92, "dali": 160.0, "shutter": 63.92, 
    "energy_1ph": 110.0, "energy_3ph": 160.0, "heater": 95.0,
    "heat_thermostat": 120.0, "fancoil_ctrl": 130.0, "electric_heat": 70.0, 
    "split_ac": 100.0, "vrv_interface": 260.0, "hub_small": 139.0, "hub_large": 609.0
}
BRANDS = ["Daikin", "LG", "Toshiba", "Fujitsu", "Mitsubishi", "Panasonic", "Midea", "Άλλη"]
JOBS = ["Ηλεκτρολόγος", "Αρχιτέκτονας", "Μηχανικός", "Κατασκευαστής", "Ιδιώτης"]

st.set_page_config(page_title="GEYER CEO Dashboard", layout="wide")

st.markdown("""
    <style>
    code { color: #27ae60 !important; background: #2c3e50 !important; font-size: 15px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ GEYER SMART HOME - Live Pricing Dashboard")

col_left, col_right = st.columns([1, 1.2])

with col_left:
    st.markdown("### 📝 Στοιχεία Προσφοράς")
    var_name = st.text_input("Ονοματεπώνυμο (Υποχρεωτικό)")
    var_addr = st.text_input("Διεύθυνση Έργου (Υποχρεωτικό)")
    var_job = st.selectbox("Ιδιότητα", JOBS)

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        int_l = st.number_input("Εσωτερικές Γραμμές", min_value=0, value=0)
        ext_l = st.number_input("Εξωτερικές Γραμμές", min_value=0, value=0)
        double = st.number_input("Διπλοί Διακόπτες", min_value=0, value=0)
    with c2:
        d220 = st.number_input("Dimmer 220V", min_value=0, value=0)
        shutt = st.number_input("Ρολλά", min_value=0, value=0)
        dali = st.number_input("Γραμμές DALI", min_value=0, value=0)

    st.markdown("---")
    h_type = st.selectbox("Θέρμανση", ["Καμία", "Ενδοδαπέδια", "Ενδοδαπέδια με Δροσισμό", "Fan Coils", "VRV Σύστημα", "Split Units"])
    h_qty = st.number_input("Ποσότητα Μονάδων", min_value=0, value=0)
    
    h_brand = "Άλλη"
    if h_type == "VRV Σύστημα":
        h_brand = st.selectbox("Μάρκα VRV", BRANDS)

# --- ΤΕΧΝΙΚΟ LOGIC ΥΠΟΛΟΓΙΣΜΟΥ ---
on_off_lines = (int_l + ext_l) - (d220 + double*2 + dali)
hvac_cost = 0

# Logic Δροσισμού & HVAC
if h_type == "Ενδοδαπέδια με Δροσισμό":
    hvac_cost = h_qty * PRICES["fancoil_ctrl"]
elif h_type == "VRV Σύστημα": 
    hvac_cost = h_qty * PRICES["vrv_interface"]
elif h_type == "Split Units": 
    hvac_cost = h_qty * PRICES["split_ac"]
elif h_type == "Fan Coils": 
    hvac_cost = h_qty * PRICES["fancoil_ctrl"]
elif h_type == "Ενδοδαπέδια":
    hvac_cost = h_qty * PRICES["heat_thermostat"]

base_dev_count = max(0, on_off_lines) + double + d220 + dali + shutt + h_qty

# Hub Selection Logic
hubs_cost = 0
hub_label = ""
if base_dev_count <= 37:
    hubs_cost = PRICES["hub_small"]; hub_label = "Κεντρική μονάδα (40 συσκ.)"
elif base_dev_count <= 97:
    hubs_cost = PRICES["hub_large"]; hub_label = "Κεντρική μονάδα (100 συσκ.)"
else:
    hubs_cost = PRICES["hub_large"] + PRICES["hub_small"]; hub_label = "Hub 100 + Hub 40"

mat_sum = (max(0, on_off_lines)*63.92) + (double*63.92) + (d220*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + hubs_cost
prog_fee = mat_sum * 0.20
total_without_fpa = mat_sum + prog_fee
total_final = total_without_fpa * 1.24

with col_right:
    st.markdown("### 🖥️ LIVE PRICING DISPLAY")
    
    # Έλεγχος υποχρεωτικών πεδίων
    if not var_name or not var_addr:
        st.warning("⚠️ ΠΑΡΑΚΑΛΩ ΣΥΜΠΛΗΡΩΣΤΕ ΟΝΟΜΑ ΚΑΙ ΔΙΕΥΘΥΝΣΗ ΓΙΑ ΝΑ ΕΚΔΟΘΕΙ Η ΠΡΟΣΦΟΡΑ")
    elif h_brand == "Άλλη" and h_type == "VRV Σύστημα":
        st.error("❌ ΜΗ ΣΥΜΒΑΤΟ ΣΥΣΤΗΜΑ VRV (ΕΠΙΛΕΞΤΕ ΥΠΟΣΤΗΡΙΖΟΜΕΝΗ ΜΑΡΚΑ)")
    elif base_dev_count > 230:
        st.error(f"❌ ΣΦΑΛΜΑ: {base_dev_count} ΣΥΣΚΕΥΕΣ. ΤΟ ΟΡΙΟ ΕΙΝΑΙ 230.")
    else:
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        display = f"""
╔══════════════════════════════════════════════════════════╗
   GEYER LIVE PRICING - {var_name.upper()}
╠══════════════════════════════════════════════════════════╣
   ΠΕΛΑΤΗΣ: {var_name[:20]} | ΙΔΙΟΤΗΤΑ: {var_job}
   ΔΙΕΥΘΥΝΣΗ: {var_addr[:20]} | ΗΜ/ΝΙΑ: {now}
╟──────────────────────────────────────────────────────────╢
   ΥΛΙΚΑ ΦΩΤΙΣΜΟΥ (On/Off):        {max(0, on_off_lines):>3}  | {(max(0, on_off_lines)*63.92):>9.2f}€
   ΔΙΠΛΟΙ ΔΙΑΚΟΠΤΕΣ (On/Off):      {double:>3}  | {(double*63.92):>9.2f}€
   ΣΥΣΤΗΜΑ HVAC ({h_type[:10]}):     {h_qty:>3}  | {hvac_cost:>9.2f}€
   {hub_label[:28]:<28}      | {hubs_cost:>9.2f}€
╟──────────────────────────────────────────────────────────╢
   ΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {base_dev_count:>3} / 230
╟──────────────────────────────────────────────────────────╢
   ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:               {mat_sum:>12.2f}€
   ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ (20%):            {prog_fee:>12.2f}€
   ΦΠΑ 24%:                          {(total_final - total_without_fpa):>12.2f}€
   ΓΕΝΙΚΟ ΣΥΝΟΛΟ:                    {total_final:>12.2f}€
╚══════════════════════════════════════════════════════════╝
        """
        st.code(display, language="text")
        st.success("✅ Η τιμολόγηση είναι έτοιμη για αποστολή.")
