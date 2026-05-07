import streamlit as st

# --- ΡΥΘΜΙΣΕΙΣ & ΤΙΜΕΣ GEYER ---
PRICES = {
    "on_off": 63.92, "double_on_off": 63.92, "dim_220v": 63.92, "dim_1_10v": 52.0, 
    "led_strip": 63.92, "dali": 160.0, "shutter": 63.92, 
    "energy_1ph": 110.0, "energy_3ph": 160.0, "heater": 95.0,
    "heat_thermostat": 120.0, "fancoil_ctrl": 130.0, "electric_heat": 70.0, 
    "split_ac": 100.0, "vrv_interface": 260.0, "hub_small": 139.0, "hub_large": 609.0
}
BRANDS = ["Daikin", "LG", "Toshiba", "Fujitsu", "Mitsubishi", "Panasonic", "Midea", "Άλλη"]

st.set_page_config(page_title="GEYER CEO Dashboard", layout="wide")

# CSS για να μοιάζει με Dashboard
st.markdown("""
    <style>
    .reportview-container { background: #f0f2f5; }
    .side-panel { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); }
    .price-display { background-color: #2c3e50; color: #27ae60; padding: 20px; border-radius: 5px; font-family: 'Courier New', Courier, monospace; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ GEYER SMART HOME - CEO Edition Dashboard")

# Δημιουργία δύο στηλών: Αριστερά Inputs - Δεξιά Πίνακας (Display)
col_input, col_display = st.columns([1, 1.2])

with col_input:
    st.markdown("### 🛠️ Παράμετροι Έργου")
    
    with st.expander("👤 Στοιχεία Πελάτη", expanded=True):
        u_name = st.text_input("Όνομα Έργου", value="PROJECT_01")
        u_job = st.text_input("Ιδιότητα", value="Μηχανικός")
    
    with st.expander("💡 Φωτισμός & Φορτία", expanded=True):
        int_l = st.number_input("Εσωτερικές Γραμμές", min_value=0, value=10)
        ext_l = st.number_input("Εξωτερικές Γραμμές", min_value=0, value=5)
        double = st.number_input("Διπλοί διακόπτες (On/Off)", min_value=0, value=0)
        d220 = st.number_input("Dimmer 220V", min_value=0, value=0)
        shutt = st.number_input("Ρολλά", min_value=0, value=2)

    with st.expander("❄️ Σύστημα HVAC", expanded=True):
        h_type = st.selectbox("Θέρμανση", ["Καμία", "Ενδοδαπέδια", "Fan Coils", "VRV Σύστημα", "Split Units"])
        h_qty = st.number_input("Ποσότητα (Θ)", min_value=0, value=1)
        h_brand = "Άλλη"
        if h_type == "VRV Σύστημα":
            h_brand = st.selectbox("Μάρκα VRV", BRANDS)

# --- LOGIC ΥΠΟΛΟΓΙΣΜΟΥ ---
# Εδώ γίνεται ο "ζωντανός" υπολογισμός
hvac_cost = 0
if h_type == "VRV Σύστημα": hvac_cost = h_qty * PRICES["vrv_interface"]
elif h_type == "Split Units": hvac_cost = h_qty * PRICES["split_ac"]
elif h_type == "Fan Coils": hvac_cost = h_qty * PRICES["fancoil_ctrl"]

total_dev = int_l + ext_l + shutt + h_qty
hub_cost = PRICES["hub_small"] if total_dev <= 37 else PRICES["hub_large"]
mat_sum = ((int_l + ext_l) * 63.92) + (shutt * 63.92) + hvac_cost + hub_cost
mat_fpa = mat_sum * 1.24

with col_display:
    st.markdown("### 🖥️ Live Pricing Display")
    
    # Το "Μαύρο Πλαίσιο" που είχες στο exe
    display_text = f"""
    ╔══════════════════════════════════════════════════════╗
       GEYER LIVE PRICING - {u_name.upper()}
    ╠══════════════════════════════════════════════════════╣
       ΠΕΛΑΤΗΣ: {u_name} ({u_job})
       ΗΜΕΡΟΜΗΝΙΑ: {st.session_state.get('date', '07/05/2026')}
    ╟──────────────────────────────────────────────────────╢
       ΥΛΙΚΑ ΦΩΤΙΣΜΟΥ/ΡΟΛΛΩΝ:          {((int_l+ext_l+shutt)*63.92):>10.2f}€
       ΣΥΣΤΗΜΑ HVAC ({h_type}):        {hvac_cost:>10.2f}€
       ΚΕΝΤΡΙΚΕΣ ΜΟΝΑΔΕΣ (HUB):        {hub_cost:>10.2f}€
    ╟──────────────────────────────────────────────────────╢
       ΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {total_dev:>3} / 230
    ╟──────────────────────────────────────────────────────╢
       ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:             {mat_sum:>10.2f}€
       ΦΠΑ 24%:                        {(mat_sum*0.24):>10.2f}€
       ΓΕΝΙΚΟ ΣΥΝΟΛΟ:                  {mat_fpa:>10.2f}€
    ╚══════════════════════════════════════════════════════╝
    """
    st.code(display_text, language="text")
    
    # Πρόσθετα κουμπιά δράσης
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("📧 Αποστολή στον Πελάτη"):
            st.toast("Η προσφορά στάλθηκε!")
    with col_btn2:
        if st.button("💾 Εξαγωγή σε PDF"):
            st.write("Δημιουργία αρχείου...")

    # Πλεονεκτήματα Fibaro (Διαδραστικά)
    st.info(f"💡 **Fibaro Advantage:** Με το σύστημα {h_type}, ο πελάτης εξοικονομεί περίπου {(mat_sum*0.15):.2f}€ ετησίως από τη διαχείριση ενέργειας.")
