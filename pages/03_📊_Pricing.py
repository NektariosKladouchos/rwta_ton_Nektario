import streamlit as st
import urllib.parse

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
# Οριστικό CSS για σκούρο πράσινο μενού και λευκά γράμματα ΜΟΝΟ στην αριστερή μπάρα
st.markdown(
    """
    <style>
        /* Φόντο αριστερής μπάρας */
        [data-testid="stSidebar"] {
            background-color: #0b3c26 !important;
        }
        /* Γράμματα και σύνδεσμοι αριστερής μπάρας */
        [data-testid="stSidebarNav"] span {
            color: white !important;
        }
        /* Εικονίδια αριστερής μπάρας */
        [data-testid="stSidebarNav"] svg {
            fill: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --- CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stNumberInput, .stSelectbox, .stTextInput, .stRadio { margin-bottom: -20px !important; }
    .stMarkdown h3 { font-size: 15px !important; margin-bottom: -10px !important; color: #1E3A8A; }
    .display-box {
        background-color: #ffffff; padding: 15px; border: 2px solid #27ae60;
        border-radius: 8px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    pre { font-family: 'Consolas', monospace !important; font-size: 11px !important; line-height: 1.2 !important; color: #000 !important; }
    .main-header { text-align: center; color: #1E3A8A; margin-top: -30px; }
    .info-text { background-color: #e8f4fd; padding: 15px; border-radius: 8px; border-left: 5px solid #1E3A8A; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-header'><h1>GEYER PORTAL</h1><p><b>ΡΩΤΑ ΤΟΝ ΝΕΚΤΑΡΙΟ</b></p></div>", unsafe_allow_html=True)

tab_calc, tab_home, tab_docs, tab_contact = st.tabs(["📊 LIVE PRICING", "🏠 ΙΔΕΕΣ", "📂 ΒΙΒΛΙΟΘΗΚΗ", "📨 ΕΠΙΚΟΙΝΩΝΙΑ"])

with tab_calc:
    left, right = st.columns([1.1, 1.45])
    
    with left:
        st.markdown("### 👤 1. ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ")
        v_name = st.text_input("Ονοματεπώνυμο", key="n")
        v_job = st.selectbox("Ιδιότητα", JOBS, key="j")
        v_addr = st.text_input("Διεύθυνση έργου", key="a")
        
        st.markdown("### 💡 2. ΦΩΤΙΣΜΟΣ")
        c1, c2 = st.columns(2); int_l = c1.number_input("Εσωτερικές", min_value=0); ext_l = c2.number_input("Εξωτερικές", min_value=0)
        
        st.markdown("### 🌓 2α. ΕΙΔΟΣ ΓΡΑΜΜΩΝ ΦΩΤΙΣΜΟΥ")
        dim220 = st.number_input("Dimming 220V", min_value=0)
        dim110 = st.number_input("Dimming 1-10V", min_value=0)
        led = st.number_input("Ταινίες LED με dimming", min_value=0)
        dali = st.number_input("DALI", min_value=0)
        double = st.number_input("Κομιτατέρ (Διπλή γραμμή φωτισμού)", min_value=0)

        st.markdown("### 🔥 3. ΘΕΡΜΑΝΣΗ")
        h_list = ["Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής", "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split Κλιματιστικά"]
        h_type = st.selectbox("Επιλογή Θ", h_list, key="ht")
        
        label_h = "Ποσότητα"
        if h_type in ["Καλοριφέρ", "Ενδοδαπέδια"]: label_h = "Αριθμός Θερμοστατών"
        elif "Fancoil" in h_type or h_type == "VRV/VRF": label_h = "Αριθμός Εσωτερικών Μονάδων"
        elif h_type == "Split Κλιματιστικά": label_h = "Αριθμός Κλιματιστικών"
        elif h_type == "Θερμαντικά σώματα": label_h = "Αριθμός Σωμάτων"
        
        h_qty_input = st.number_input(label_h, min_value=0, key='hq_val')
        h_qty = 0 if h_type == "Κανένα" else h_qty_input
        hb = st.selectbox("Brand (Θ)", BRANDS, key="hb") if h_type == "VRV/VRF" else ""
        
        st.markdown("### ❄️ 4. ΨΥΞΗ")
        c_list = ["Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής", "Fancoil δαπέδου", "VRV/VRF", "Split Κλιματιστικά"]
        c_type = st.selectbox("Επιλογή Ψ", c_list, key="ct")
        
        label_c = "Ποσότητα"
        if c_type == "Ενδοδαπέδια Δροσισμός": label_c = "Αριθμός Θερμοστατών"
        elif "Fancoil" in c_type or c_type == "VRV/VRF": label_c = "Αριθμός Εσωτερικών Μονάδων"
        elif c_type == "Split Κλιματιστικά": label_c = "Αριθμός Κλιματιστικών"
        
        c_qty_input = st.number_input(label_c, min_value=0, key='cq_val')
        c_qty = 0 if c_type == "Κανένα" else c_qty_input
        cb = st.selectbox("Brand (Ψ)", BRANDS, key="cb") if c_type == "VRV/VRF" else ""
        
        st.markdown("### 🪟 5. ΡΟΛΑ / ΤΕΝΤΕΣ / ΚΟΥΡΤΙΝΕΣ")
        shutt = st.number_input("Τεμάχια", min_value=0)
        
        st.markdown("### 🔌 6. ΠΙΝΑΚΑΣ")
        energy = st.radio("Μετρητής", ["Όχι", "Μονοφασικός", "Τριφασικός"], horizontal=True)
        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")

    with right:
        st.markdown("""
        <div class='info-text'>
            <h4 style='margin-top:0;'>🏠 Υπολογισμός Smart Home από την GEYER</h4>
            Φτιάξτε τα υλικά της ζήτησης με βάση το κόστος και τις ανάγκες σας και στείλτε μου email. 
            Εμείς θα αναλάβουμε όλα τα επόμενα βήματα. Βάλτε τα στοιχεία επικοινωνίας σας στις παρατηρήσεις.
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🏆 20 ΛΟΓΟΙ ΓΙΑ ΝΑ ΕΠΙΛΕΞΕΤΕ ΤΟ ΣΥΣΤΗΜΑ ΜΑΣ"):
            st.markdown("""
            1. **Λειτουργία χωρίς Internet:** Το σύστημα παραμένει πλήρως λειτουργικό τοπικά.
            2. **Οποιοσδήποτε Φωτισμός:** Πλήρης διαχείριση DALI, 1-10V, Phase Cut και RGB.
            3. **Retrofit Τεχνολογία:** Τοποθέτηση σε υφιστάμενες εγκαταστάσεις χωρίς μερεμέτια.
            4. **Ανοιχτό Πρωτόκολλο:** Επικοινωνία μέσω Z-Wave για μέγιστη συμβατότητα.
            5. **Δωρεάν Ενσωματώσεις:** Alexa, Google Assistant, Philips HUE, Sonos κ.α.
            6. **Σύνδεση με Home Assistant:** Για τους λάτρεις του απόλυτου ελέγχου.
            7. **Εύκολα Σενάρια:** Δημιουργία σκηνών (π.χ. Αναχώρηση) με ελάχιστα κλικ.
            8. **Lua Scripting:** Δυνατότητα για εξειδικευμένο προγραμματισμό από επαγγελματίες.
            9. **Cloud & Local Backup:** Μην ξανασετάρετε ποτέ τις συσκευές σας.
            10. **Mesh Επικοινωνία:** Κάθε συσκευή λειτουργεί ως επαναλήπτης για τέλειο σήμα.
            11. **Τεράστια Γκάμα Υλικών:** Καλύπτουμε κάθε ανάγκη αυτοματισμού.
            12. **Απομακρυσμένη Υποστήριξη:** Μέσω της εφαρμογής Installer App.
            13. **Ενεργειακή Παρακολούθηση:** Δείτε την κατανάλωση σε πραγματικό χρόνο.
            14. **Θερμικές Ζώνες:** Ανεξάρτητος έλεγχος θερμοκρασίας ανά δωμάτιο.
            15. **Αυτόματο Πότισμα:** Έξυπνη διαχείριση του κήπου σας.
            16. **Push Notifications:** Διαδραστική επικοινωνία για κάθε συμβάν στο σπίτι.
            17. **Εξοικονόμηση 30%:** Σημαντική μείωση στο κόστος ρεύματος και θέρμανσης.
            18. **Ελληνική Υποστήριξη:** Άμεση βοήθεια από την τεχνική ομάδα της GEYER.
            19. **Design:** Συσκευές που "κρύβονται" ή αναδεικνύουν τον χώρο σας.
            20. **Αξία Ακινήτου:** Άμεση αναβάθριση της εμπορικής αξίας του έργου.
            """)

        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))
        
        error = None
        if not v_name or not v_job or not v_addr: error = "⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
        elif on_off < 0: error = "❌ ΣΦΑΛΜΑ ΣΤΟ ΦΩΤΙΣΜΟ"
        elif (h_type == "VRV/VRF" and hb == "Άλλη") or (c_type == "VRV/VRF" and cb == "Άλλη"):
            error = "❌ ΜΗ ΣΥΜΒΑΤΟ: Η επιλογή 'Άλλη' στο VRV δεν υποστηρίζεται απευθείας."
        elif h_type == "VRV/VRF" and c_type == "VRV/VRF" and hb != cb: error = "❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV"

        is_exact = (h_type == c_type and h_type != "Κανένα") or (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός")
        if not error and is_exact and h_qty != c_qty: error = f"❌ ΛΑΘΟΣ: Η ΠΟΣΟΤΗΤΑ ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΙΔΙΑ ΣΕ {h_type}"

        if error:
            st.markdown(f'<div class="display-box"><pre style="color:red; text-align:center;">{error}</pre></div>', unsafe_allow_html=True)
            disp_text = error
        else:
            h_c_hvac = 0; h_det = []
            if is_exact:
                pk = "fancoil_ctrl" if "Fancoil" in h_type or "Δροσισμός" in h_type else "vrv_interface" if "VRV" in h_type else "split_ac" if "Split" in h_type else "heat_thermostat"
                h_c_hvac = h_qty * PRICES[pk]
                h_det.append({"n": f"{h_type} ({hb if 'VRV' in h_type else ''}) [Κοινό]", "q": h_qty, "p": h_c_hvac})
            else:
                h_m = {"Καλοριφέρ":"heat_thermostat","Ενδοδαπέδια":"heat_thermostat","Fancoil οροφής":"fancoil_ctrl","Fancoil δαπέδου":"fancoil_ctrl","Θερμαντικά σώματα":"electric_heat","VRV/VRF":"vrv_interface","Split Κλιματιστικά":"split_ac"}
                if h_qty > 0: p = h_qty * PRICES[h_m.get(h_type, "heat_thermostat")]; h_c_hvac += p; h_det.append({"n": f"Θ: {h_type} {hb}", "q": h_qty, "p": p})
                if c_qty > 0: p = c_qty * PRICES[h_m.get(c_type, "fancoil_ctrl")]; h_c_hvac += p; h_det.append({"n": f"Ψ: {c_type} {cb}", "q": c_qty, "p": p})

            e_val = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0
            base_c = max(0, on_off) + double + dim220 + dim110 + led + dali + shutt + max(h_qty, c_qty) + (1 if e_val > 0 else 0) + (1 if heater else 0)
            h_q = 1 if base_c <= 97 else 2
            h_t = PRICES["hub_small"] if base_c <= 37 else PRICES["hub_large"] if base_c <= 97 else (PRICES["hub_large"] + PRICES["hub_small"]) if base_c <= 130 else PRICES["hub_large"]*2
            
            total_dev = base_c + h_q
            if total_dev > 230:
                st.markdown(f'<div class="display-box"><pre style="color:red; text-align:center;">❌ ΣΦΑΛΜΑ: ΥΠΕΡΒΑΣΗ ΟΡΙΟΥ 230 ΣΥΣΚΕΥΩΝ</pre></div>', unsafe_allow_html=True)
                disp_text = "ΣΦΑΛΜΑ ΟΡΙΟΥ"
            else:
                total_mat = (max(0,on_off)*63.92) + (double*63.92) + (dim220*63.92) + (dim110*52.0) + (led*63.92) + (dali*160.0) + (shutt*63.92) + h_c_hvac + h_t + e_val + (95 if heater else 0)
                prog_cost, vat = total_mat * 0.20, total_mat * 0.24
                gen_total = total_mat + vat
                
                res = f"{'='*70}\n GEYER SMART HOME - ΑΝΑΛΥΤΙΚΗ ΠΡΟΣΦΟΡΑ\n{'='*70}\n"
                res += f"ΠΕΛΑΤΗΣ: {v_name.upper()} | {v_job}\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*70}\n"
                res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<40} | {'TEM':<4} | {'ΤΙΜΗ':>10}\n{'-'*70}\n"
                if base_c <= 37: res += f"{'Κεντρική μονάδα (40 συσκευές)':<40} | 1    | {PRICES['hub_small']:10.2f}€\n"
                elif base_c <= 97: res += f"{'Κεντρική μονάδα (100 συσκευές)':<40} | 1    | {PRICES['hub_large']:10.2f}€\n"
                elif base_c <= 130: res += f"{'Κεντρική μονάδα (100)':<40} | 1    | {PRICES['hub_large']:10.2f}€\n{'Κεντρική μονάδα (40)':<40} | 1    | {PRICES['hub_small']:10.2f}€\n"
                else: res += f"{'Κεντρική μονάδα (100)':<40} | 2    | {PRICES['hub_large']*2:10.2f}€\n"
                if on_off > 0: res += f"{'Γραμμές Φωτισμού On/Off':<40} | {on_off:<4} | {on_off*63.92:10.2f}€\n"
                if double > 0: res += f"{'Διπλές Γραμμές (Κομιτατέρ)':<40} | {double:<4} | {double*63.92:10.2f}€\n"
                if dim220 > 0: res += f"{'Dimming 220V':<40} | {dim220:<4} | {dim220*63.92:10.2f}€\n"
                if dim110 > 0: res += f"{'Dimming 1-10V':<40} | {dim110:<4} | {dim110*52.00:10.2f}€\n"
                if led > 0:    res += f"{'Ταινίες LED Dimming':<40} | {led:<4} | {led*63.92:10.2f}€\n"
                if dali > 0:   res += f"{'Γραμμές DALI':<40} | {dali:<4} | {dali*160.00:10.2f}€\n"
                for d in h_det: res += f"{d['n'][:40]:<40} | {d['q']:<4} | {d['p']:10.2f}€\n"
                if shutt > 0:  res += f"{'Ρολά / Τέντες / Κουρτίνες':<40} | {shutt:<4} | {shutt*63.92:10.2f}€\n"
                if e_val > 0:  res += f"{f'Μετρητής Ενέργειας ({energy})':<40} | 1    | {e_val:10.2f}€\n"
                if heater:     res += f"{'Έλεγχος Θερμοσίφωνα':<40} | 1    | {95.00:10.2f}€\n"
                res += f"{'-'*70}\n"
                res += f"{'ΣΥΝΟΛΟ ΣΥΣΚΕΩΝ:':<40} | {total_dev:<4} | \n"
                res += f"{'ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:':<48} {total_mat:10.2f}€\n"
                res += f"{'ΦΠΑ 24%:':<48} {vat:10.2f}€\n"
                res += f"{'='*70}\n"
                res += f"{'ΓΕΝΙΚΟ ΣΥΝΟΛΟ:':<48} {gen_total:10.2f}€\n"
                res += f"{'='*70}\n"
                res += f"{'ΚΟΣΤΟΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ προαιρετικό  (χωρίς ΦΠΑ):':<48} {prog_cost:10.2f}€"
                disp_text = res

                st.markdown('<div class="display-box">', unsafe_allow_html=True)
                st.subheader("🖥️ LIVE PRICING SYSTEM")
                st.code(disp_text, language="text")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.write("---")
                notes = st.text_area("📝 Παρατηρήσεις Ζήτησης:")
if st.button("🚀 ΑΠΟΣΤΟΛΗ EMAIL"):

    try:

        sender_email = st.secrets["email"]["sender"]
        sender_password = st.secrets["email"]["password"]
        receiver_email = st.secrets["email"]["receiver"]
        smtp_server = st.secrets["email"]["smtp_server"]
        smtp_port = st.secrets["email"]["smtp_port"]

        subject = f"Ζήτηση Portal - {v_name}"

        body = f"""
ΠΡΟΣΦΟΡΑ:

{disp_text}

ΠΑΡΑΤΗΡΗΣΕΙΣ:

{notes}
"""

        # Create email
        msg = MIMEMultipart()

        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(
            MIMEText(body, "plain", "utf-8")
        )

        # SMTP
        server = smtplib.SMTP(
            smtp_server,
            smtp_port
        )

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        st.success(
            "✅ Το email στάλθηκε επιτυχώς!"
        )

    except Exception as e:

        st.error(
            f"❌ Σφάλμα αποστολής: {e}"
        )
            
                
             
