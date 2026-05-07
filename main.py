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

st.set_page_config(page_title="GEYER Tech Portal", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f5; }
    .display-text {
        background-color: #ffffff;
        padding: 25px;
        border: 2px solid #27ae60;
        font-family: 'Consolas', 'Courier New', monospace;
        color: black;
        white-space: pre;
        font-size: 13px;
        line-height: 1.2;
    }
    .main-title { color: #1E3A8A; font-size: 30px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR MENU ---
choice = st.sidebar.radio("Επιλογές Portal", ["🏠 Αρχική & Ιδέες", "📊 Live Pricing (CEO Edition)", "📂 Τεχνική Βιβλιοθήκη", "📨 Ερώτηση προς Τεχνικό"])

# --- 1. ΑΡΧΙΚΗ & ΙΔΕΕΣ ---
if choice == "🏠 Αρχική & Ιδέες":
    st.markdown("<div class='main-title'>📸 Ιδέες & Φωτογραφίες Έργων</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://unsplash.com", caption="Smart Lighting Control")
    with col2:
        st.image("https://unsplash.com", caption="Climate Control (Fibaro HVAC)")
    st.success("💡 Το σύστημα Fibaro είναι Retrofit: Τοποθετείται σε υπάρχοντα κουτιά χωρίς μερεμέτια.")

# --- 2. LIVE PRICING (ΟΛΟ ΤΟ LOGIC ΣΟΥ) ---
elif choice == "📊 Live Pricing (CEO Edition)":
    st.markdown("<div class='main-title'>📊 Live Pricing System</div>", unsafe_allow_html=True)
    left, right = st.columns([1, 1.2])

    with left:
        st.subheader("1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ")
        v_name = st.text_input("Ονοματεπώνυμο / Επωνυμία")
        v_job = st.selectbox("Ιδιότητα", JOBS)
        v_addr = st.text_input("Διεύθυνση έργου")

        st.subheader("2. ΦΩΤΙΣΜΟΣ")
        c1, c2 = st.columns(2)
        int_l = c1.number_input("Εσωτερικές Γραμμές", min_value=0)
        ext_l = c2.number_input("Εξωτερικές Γραμμές", min_value=0)
        st.markdown("**2α. ΕΙΔΗ ΓΡΑΜΜΩΝ DIMMING**")
        dim220 = st.number_input("Dimming 220V", min_value=0)
        dim110 = st.number_input("Dimming 1-10V", min_value=0)
        led = st.number_input("Ταινίες LED Dim", min_value=0)
        dali = st.number_input("DALI", min_value=0)
        double = st.number_input("Κομιτατέρ (Διπλές)", min_value=0)

        st.subheader("3. ΘΕΡΜΑΝΣΗ")
        h_list = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split"]
        h_labels = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. σωμάτων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
        h_type = st.selectbox("Επιλογή Θέρμανσης", h_list)
        h_qty = st.number_input(h_labels[h_list.index(h_type)], min_value=0, key="h_qty")
        if h_type == "VRV/VRF": h_brand = st.selectbox("Μάρκα VRV (Θ)", BRANDS)

        st.subheader("4. ΨΥΞΗ")
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split"]
        c_labels = ["Ποσότητα:", "Αρ. θερμοστατών:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. εσωτ. μονάδων:", "Αρ. κλιματιστικών:"]
        c_type = st.selectbox("Επιλογή Ψύξης", c_list)
        c_qty = st.number_input(c_labels[c_list.index(c_type)], min_value=0, key="c_qty")
        if c_type == "VRV/VRF": c_brand = st.selectbox("Μάρκα VRV (Ψ)", BRANDS)

        st.subheader("5 & 6 ΛΟΙΠΑ")
        shutt = st.number_input("Ρολά/Τέντες", min_value=0)
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        st.subheader("🖥️ LIVE PRICING DISPLAY")
        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        
        if not v_name or not v_job or not v_addr:
            st.warning("⚠️ ΠΑΡΑΚΑΛΩ ΣΥΜΠΛΗΡΩΣΤΕ ΟΝΟΜΑ, ΙΔΙΟΤΗΤΑ & ΔΙΕΥΘΥΝΣΗ")
        elif on_off < 0:
            st.error("❌ ΣΦΑΛΜΑ ΣΤΟ ΦΩΤΙΣΜΟ: DIMMING > ΣΥΝΟΛΟ ΓΡΑΜΜΩΝ")
        elif (h_type == "VRV/VRF" and h_brand == "Άλλη") or (c_type == "VRV/VRF" and c_brand == "Άλλη"):
            st.error("❌ ΜΗ ΣΥΜΒΑΤΟ ΣΥΣΤΗΜΑ VRV")
        else:
            # --- LOGIC ΥΠΟΛΟΓΙΣΜΟΥ ---
            hvac_cost = 0; hvac_details = []
            if h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός":
                hvac_cost = h_qty * PRICES["fancoil_ctrl"]
                hvac_details.append({"n": "Ενδοδαπέδια με Δροσισμό", "q": h_qty, "p": hvac_cost})
            else:
                if h_qty > 0:
                    h_keys = ["", "heat_thermostat", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "electric_heat", "vrv_interface", "split_ac"]
                    hvac_cost += h_qty * PRICES[h_keys[h_list.index(h_type)]]
                    hvac_details.append({"n": h_type, "q": h_qty, "p": h_qty * PRICES[h_keys[h_list.index(h_type)]]})
                if c_qty > 0:
                    c_keys = ["", "heat_thermostat", "fancoil_ctrl", "fancoil_ctrl", "vrv_interface", "split_ac"]
                    hvac_cost += c_qty * PRICES[c_keys[c_list.index(c_type)]]
                    hvac_details.append({"n": c_type, "q": c_qty, "p": c_qty * PRICES[c_keys[c_list.index(c_type)]]})

            e_cost = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0
            dev_count = max(0, on_off) + double + dim220 + dim110 + led + dali + shutt + h_qty + (1 if e_cost > 0 else 0)
            hubs_cost = PRICES["hub_small"] if dev_count <= 37 else PRICES["hub_large"]
            mat_sum = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52) + (led*63.92) + (dali*160) + (shutt*63.92) + hvac_cost + hubs_cost + e_cost + (95 if heater else 0)

            # --- DISPLAY ---
            res = f"{'='*65}\n GEYER SMART HOME - ΠΡΟΣΦΟΡΑ\n{'='*65}\n"
            res += f"ΠΕΛΑΤΗΣ: {v_name.upper()} ({v_job})\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*65}\n"
            res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<30} | {'TEM':<5} | {'TIMH':<10}\n{'-'*65}\n"
            res += f"{'Κεντρική Μονάδα Hub':<30} | 1     | {hubs_cost:9.2f}€\n"
            if on_off > 0: res += f"{'Φωτισμός On/Off':<30} | {on_off:<5} | {on_off*63.92:9.2f}€\n"
            for d in hvac_details: res += f"{d['n'][:30]:<30} | {d['q']:<5} | {d['p']:9.2f}€\n"
            if shutt > 0: res += f"{'Ρολά / Τέντες':<30} | {shutt:<5} | {shutt*63.92:9.2f}€\n"
            res += f"{'-'*65}\nΣΥΝΟΛΟ ΣΥΣΚΕΥΩΝ: {dev_count}\n"
            res += f"ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ: {mat_sum:23.2f}€\n"
            res += f"ΑΞΙΑ ΜΕ ΦΠΑ 24%: {mat_sum*1.24:26.2f}€\n"
            res += f"ΚΟΣΤΟΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ (20%): {mat_sum*0.20:17.2f}€\n{'='*65}"
            
            st.markdown(f"<div class='display-text'>{res}</div>", unsafe_allow_html=True)
            if st.button("📩 Αποστολή στον Νεκτάριο"):
                st.balloons()
                st.success("Η προσφορά καταγράφηκε!")

# --- 3. ΒΙΒΛΙΟΘΗΚΗ ---
elif choice == "📂 Τεχνική Βιβλιοθήκη":
    st.header("📄 Τεχνικά Φυλλάδια & Σχέδια")
    st.write("Εδώ μπορείτε να βρείτε όλο το υποστηρικτικό υλικό.")
    st.info("Συμβουλή: Ανέβασε τα PDF σου στο GitHub για να τα συνδέσουμε εδώ!")

# --- 4. ΕΠΙΚΟΙΝΩΝΙΑ ---
elif choice == "📨 Ερώτηση προς Τεχνικό":
    st.header("📨 Τεχνική Υποστήριξη")
    st.write("Περιγράψτε το ζήτημά σας και θα σας απαντήσω άμεσα.")
    question = st.text_area("Η ερώτησή σας:")
    if st.button("Αποστολή Ερώτησης"):
        st.success("Ευχαριστώ! Θα λάβετε απάντηση σύντομα.")
