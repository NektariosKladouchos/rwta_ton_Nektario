import streamlit as st
import urllib.parse

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

# --- CSS ΓΙΑ ΣΤΑΘΕΡΗ ΕΜΦΑΝΙΣΗ ---
st.markdown("""
    <style>
    .stNumberInput, .stSelectbox, .stTextInput, .stRadio { margin-bottom: -20px !important; }
    .stMarkdown h3 { font-size: 15px !important; margin-bottom: -10px !important; color: #1E3A8A; }
    .display-box {
        background-color: #ffffff; padding: 15px; border: 2px solid #27ae60;
        border-radius: 8px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        overflow-x: hidden !important;
    }
    pre { font-family: 'Consolas', monospace !important; font-size: 11px !important; color: #000 !important; white-space: pre-wrap !important; }
    .info-text { background-color: #e8f4fd; padding: 15px; border-radius: 8px; border-left: 5px solid #1E3A8A; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

left, right = st.columns([1.1, 1.45])

with left:
    st.markdown("### 👤 1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ")
    v_name = st.text_input("Ονοματεπώνυμο", key="n")
    v_job = st.selectbox("Ιδιότητα", JOBS, key="j")
    v_addr = st.text_input("Διεύθυνση έργου", key="a")
    
    st.markdown("### 💡 2. ΦΩΤΙΣΜΟΣ")
    c1, c2 = st.columns(2); int_l = c1.number_input("Εσωτερικές", min_value=0); ext_l = c2.number_input("Εξωτερικές", min_value=0)
    
    st.markdown("### 🌓 2α. ΕΙΔΟΣ ΓΡΑΜΜΩΝ")
    dim220 = st.number_input("Dimming 220V", min_value=0)
    dim110 = st.number_input("Dimming 1-10V", min_value=0)
    led = st.number_input("Ταινίες LED με dimming", min_value=0)
    dali = st.number_input("DALI", min_value=0)
    double = st.number_input("Κομιτατέρ (Διπλή γραμμή)", min_value=0)

    st.markdown("### 🔥 3. ΘΕΡΜΑΝΣΗ")
    h_list = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split Κλιματιστικά"]
    h_type = st.selectbox("Επιλογή Θ", h_list, key="ht"); h_qty = st.number_input("Ποσότητα (Θ)", min_value=0, key='hq_val')
    hb = st.selectbox("Brand (Θ)", BRANDS, key="hb") if h_type == "VRV/VRF" else ""
    
    st.markdown("### ❄️ 4. ΨΥΞΗ")
    c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split Κλιματιστικά"]
    c_type = st.selectbox("Επιλογή Ψ", c_list, key="ct"); c_qty = st.number_input("Ποσότητα (Ψ)", min_value=0, key='cq_val')
    cb = st.selectbox("Brand (Ψ)", BRANDS, key="cb") if c_type == "VRV/VRF" else ""
    
    st.markdown("### 🪟 5. ΡΟΛΑ & ΤΕΝΤΕΣ")
    shutt = st.number_input("Τεμάχια Ρολών", min_value=0)
    
    st.markdown("### 🔌 6. ΠΙΝΑΚΑΣ")
    energy = st.radio("Μετρητής Ενέργειας", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
    heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

with right:
    st.markdown("""<div class='info-text'>🏠 <b>Υπολογισμός Smart Home GEYER</b></div>""", unsafe_allow_html=True)
    
    with st.expander("🏆 20 ΛΟΓΟΙ ΓΙΑ ΝΑ ΕΠΙΛΕΞΕΤΕ ΤΟ ΣΥΣΤΗΜΑ ΜΑΣ"):
        st.write("1. Local Λειτουργία | 2. DALI/1-10V | 3. Retrofit | 4. Z-Wave | 5. Alexa/Google | 6. Home Assistant | 7. Σενάρια | 8. Lua | 9. Backup | 10. Mesh | 11. Μεγάλη Γκάμα | 12. Installer App | 13. Energy | 14. Ζώνες | 15. Πότισμα | 16. Notifications | 17. -30% Ενέργεια | 18. Υποστήριξη | 19. Design | 20. Αξία")

    on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
    
    error = None
    if not v_name or not v_job or not v_addr: error = "⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
    elif on_off < 0: error = "❌ ΣΦΑΛΜΑ ΣΤΟ ΦΩΤΙΣΜΟ"
    elif (h_type == "VRV/VRF" and hb == "Άλλη") or (c_type == "VRV/VRF" and cb == "Άλλη"):
        error = "❌ ΜΗ ΣΥΜΒΑΤΟ: Επιλογή 'Άλλη' στο VRV."
    elif h_type == "VRV/VRF" and c_type == "VRV/VRF" and hb != cb: error = "❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV"

    is_exact = (h_type == c_type and h_type != "Κανένα") or (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός")
    if not error and is_exact and h_qty != c_qty: error = f"❌ ΛΑΘΟΣ ΠΟΣΟΤΗΤΑΣ {h_type}"

    if error:
        st.error(error)
        disp_text = f"ΣΦΑΛΜΑ: {error}"
    else:
        h_c_hvac = 0; h_det = []
        if is_exact:
            pk = "fancoil_ctrl" if "Fancoil" in h_type or "Δροσισμός" in h_type else "vrv_interface" if "VRV" in h_type else "split_ac" if "Split" in h_type else "heat_thermostat"
            h_c_hvac = h_qty * PRICES[pk]; h_det.append({"n": f"{h_type} [Κοινό]", "q": h_qty, "p": h_c_hvac})
        else:
            h_m = {"Καλοριφέρ":"heat_thermostat","Ενδοδαπέδια":"heat_thermostat","Fancoil οροφής":"fancoil_ctrl","Fancoil δαπέδου":"fancoil_ctrl","Θερμαντικά σώματα":"electric_heat","VRV/VRF":"vrv_interface","Split Κλιματιστικά":"split_ac"}
            if h_qty > 0: p = h_qty * PRICES[h_m.get(h_type, "heat_thermostat")]; h_c_hvac += p; h_det.append({"n": f"Θ:{h_type}", "q": h_qty, "p": p})
            if c_qty > 0: p = c_qty * PRICES[h_m.get(c_type, "fancoil_ctrl")]; h_c_hvac += p; h_det.append({"n": f"Ψ:{c_type}", "q": c_qty, "p": p})

        e_val = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0
        base_c = max(0, on_off) + double + dim220 + dim110 + led + dali + shutt + max(h_qty, c_qty) + (1 if e_val > 0 else 0) + (1 if heater else 0)
        h_t = PRICES["hub_small"] if base_c <= 37 else PRICES["hub_large"] if base_c <= 97 else (PRICES["hub_large"] + PRICES["hub_small"]) if base_c <= 130 else PRICES["hub_large"]*2
        
        total_dev = base_c + (1 if base_c <= 97 else 2)
        total_mat = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52.0) + (led*63.92) + (dali*160.0) + (shutt*63.92) + h_c_hvac + h_t + e_val + (95 if heater else 0)
        prog_cost, vat = total_mat * 0.20, total_mat * 0.24
        gen_total = total_mat + vat
            
        line = "-" * 56
        res = f"{'='*56}\n GEYER SMART HOME - ΠΡΟΣΦΟΡΑ\n{'='*56}\n"
        res += f"ΠΕΛΑΤΗΣ: {v_name.upper()[:25]}\nΔΙΕΥΘΥΝΣΗ: {v_addr[:25]}\n{line}\n"
        res += f"{'ΠΕΡΙΓΡΑΦΗ':<35} | {'TEM':<3} | {'ΤΙΜΗ':>10}\n{line}\n"
        
        if base_c <= 37: res += f"{'Κεντρική μονάδα (40)':<35} | 1   | {PRICES['hub_small']:10.2f}€\n"
        elif base_c <= 97: res += f"{'Κεντρική μονάδα (100)':<35} | 1   | {PRICES['hub_large']:10.2f}€\n"
        elif base_c <= 130: res += f"{'Hub Large + Small':<35} | 1+1 | {PRICES['hub_large']+PRICES['hub_small']:10.2f}€\n"
        else: res += f"{'Hub Large x2':<35} | 2   | {PRICES['hub_large']*2:10.2f}€\n"
        
        if on_off > 0: res += f"{'Φωτισμός On/Off':<35} | {on_off:<3} | {on_off*63.92:10.2f}€\n"
        if double > 0: res += f"{'Διπλές Γραμμές':<35} | {double:<3} | {double*63.92:10.2f}€\n"
        if dim220 > 0: res += f"{'Dimming 220V':<35} | {dim220:<3} | {dim220*63.92:10.2f}€\n"
        if dim110 > 0: res += f"{'Dimming 1-10V':<35} | {dim110:<3} | {dim110*52.00:10.2f}€\n"
        if led > 0:    res += f"{'LED Dimming':<35} | {led:<3} | {led*63.92:10.2f}€\n"
        if dali > 0:   res += f"{'DALI Lighting':<35} | {dali:<3} | {dali*160.00:10.2f}€\n"
        for d in h_det: res += f"{d['n'][:35]:<35} | {d['q']:<3} | {d['p']:10.2f}€\n"
        if shutt > 0:  res += f"{'Ρολά / Τέντες':<35} | {shutt:<3} | {shutt*63.92:10.2f}€\n"
        if e_val > 0:  res += f"{f'Μετρητής ({energy})':<35} | 1   | {e_val:10.2f}€\n"
        if heater:     res += f"{'Έλεγχος Θερμοσίφωνα':<35} | 1   | {95.00:10.2f}€\n"
        res += f"{line}\n"
        res += f"{'ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:':<43} {total_mat:10.2f}€\n"
        res += f"{'ΦΠΑ 24%:':<43} {vat:10.2f}€\n"
        res += f"{'='*56}\n"
        res += f"{'ΓΕΝΙΚΟ ΣΥΝΟΛΟ:':<43} {gen_total:10.2f}€\n"
        res += f"{'='*56}\n"
        res += f"Προγραμματισμός (χωρίς ΦΠΑ): {prog_cost:10.2f}€"
        disp_text = res

    st.markdown('<div class="display-box">', unsafe_allow_html=True)
    st.subheader("🖥️ LIVE PRICING SYSTEM")
    st.code(disp_text, language="text")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("---")
    notes = st.text_area("📝 Παρατηρήσεις Ζήτησης:")
    
    if st.button("🚀 1. ΠΡΟΕΤΟΙΜΑΣΙΑ ΑΠΟΣΤΟΛΗΣ"):
        subject = f"Ζήτηση Portal - {v_name}"
        body = f"Προσφορά:\n\n{disp_text}\n\nΠΑΡΑΤΗΡΗΣΕΙΣ:\n{notes}"
        mailto_link = f"mailto:kladouxos@geyer.gr?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
        st.success("Έτοιμο!")
        st.markdown(f'<a href="{mailto_link}" style="background-color: #27ae60; color: white; padding: 15px; text-decoration: none; border-radius: 5px; font-weight: bold; display: block; text-align: center;">📩 2. ΠΑΤΗΣΤΕ ΕΔΩ ΓΙΑ ΑΠΟΣΤΟΛΗ</a>', unsafe_allow_html=True)
