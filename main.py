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

st.set_page_config(page_title="GEYER Live Pricing", layout="wide")

# --- MENU ---
menu = st.sidebar.radio("Πλοήγηση", ["🏠 Αρχική", "📊 Live Pricing System", "📂 Τεχνική Βιβλιοθήκη"])

if menu == "📊 Live Pricing System":
    st.title("📊 GEYER Live Pricing Dashboard")
    st.info("Συμπληρώστε τα στοιχεία για αυτόματο υπολογισμό κόστους.")

    # Στοιχεία Πελάτη
    with st.expander("👤 Στοιχεία Έργου", expanded=True):
        col_p1, col_p2 = st.columns(2)
        u_name = col_p1.text_input("Ονοματεπώνυμο")
        u_job = col_p2.text_input("Ιδιότητα (π.χ. Αρχιτέκτονας)")

    # Φωτισμός & Ρολλά
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💡 Φωτισμός & Φορτία")
        int_l = st.number_input("Εσωτερικές Γραμμές", min_value=0, value=0)
        ext_l = st.number_input("Εξωτερικές Γραμμές", min_value=0, value=0)
        double = st.number_input("Διπλοί διακόπτες (On/Off)", min_value=0, value=0)
        d220 = st.number_input("Dimmer 220V", min_value=0, value=0)
        dali = st.number_input("Γραμμές DALI", min_value=0, value=0)
    
    with col2:
        st.subheader("🪟 Ρολλά & Ενέργεια")
        shutt = st.number_input("Αριθμός Ρολλών", min_value=0, value=0)
        energy = st.selectbox("Έλεγχος Ενέργειας", ["Όχι", "Μονοφασικό", "Τριφασικό"])
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    # HVAC LOGIC (Το δύσκολο κομμάτι σου)
    st.subheader("❄️ Θέρμανση & Ψύξη (HVAC)")
    c_h1, c_h2 = st.columns(2)
    h_type = c_h1.selectbox("Τύπος Θέρμανσης", ["Καμία", "Ενδοδαπέδια (Αυτονομία)", "Ενδοδαπέδια με Δροσισμό", "Fan Coils (2-pipe)", "Fan Coils (4-pipe)", "Ηλεκτρικά Σώματα", "VRV Σύστημα", "Split Units"])
    h_qty = c_h2.number_input("Ποσότητα (Θέρμανση)", min_value=0, value=0)
    
    h_brand = "Άλλη"
    if h_type == "VRV Σύστημα":
        h_brand = st.selectbox("Μάρκα VRV (Θ)", BRANDS)

    c_c1, c_c2 = st.columns(2)
    c_type = c_c1.selectbox("Τύπος Ψύξης", ["Καμία", "Δροσισμός (Ενδοδαπέδια)", "Fan Coils (2-pipe)", "Fan Coils (4-pipe)", "VRV Σύστημα", "Split Units"])
    c_qty = c_c2.number_input("Ποσότητα (Ψύξη)", min_value=0, value=0)
    
    c_brand = "Άλλη"
    if c_type == "VRV Σύστημα":
        c_brand = st.selectbox("Μάρκα VRV (Ψ)", BRANDS)

    # ΥΠΟΛΟΓΙΣΜΟΣ (Logic)
    if st.button("🚀 Υπολογισμός & Έκδοση Προσφοράς"):
        error = False
        if h_type == "VRV Σύστημα" and h_brand == "Άλλη":
            st.error("❌ ΜΗ ΣΥΜΒΑΤΟ ΣΥΣΤΗΜΑ VRV")
            error = True
        if h_type == "VRV Σύστημα" and c_type == "VRV Σύστημα" and h_brand != c_brand:
            st.error("❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV")
            error = True
            
        if not error:
            # Υπολογισμός Κόστους HVAC
            hvac_cost = 0
            if h_type == "VRV Σύστημα": hvac_cost += h_qty * PRICES["vrv_interface"]
            elif h_type == "Split Units": hvac_cost += h_qty * PRICES["split_ac"]
            # ... προσθέτουμε τα υπόλοιπα logic εδώ ...

            # Υπολογισμός Hubs (Logic 40/100 συσκευών)
            total_dev = int_l + ext_l + shutt + h_qty + c_qty
            hub_cost = PRICES["hub_small"] if total_dev <= 37 else PRICES["hub_large"]
            
            final_sum = (total_dev * 63.92) + hvac_cost + hub_cost
            
            st.balloons()
            st.success(f"### Συνολικό Κόστος Υλικών: {final_sum:,.2f} €")
            st.write(f"Πελάτης: {u_name} | Συσκευές: {total_dev}")
            st.info("💡 Η προσφορά περιλαμβάνει το Logic Fibaro για εξοικονομηση ενέργειας.")

else:
    st.title("🏠 Καλώς ήρθατε")
    st.write("Επιλέξτε το 'Live Pricing System' για να ξεκινήσετε.")
