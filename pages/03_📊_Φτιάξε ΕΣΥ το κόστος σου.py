import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import pytz
from supabase import create_client, Client

# -------------------------------------------------
# SUPABASE CONNECTION + ANALYTICS
# -------------------------------------------------
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_event(page, event, user=None, extra=None):
    try:
        supabase.table("analytics").insert({
            "page": page,
            "event": event,
            "user_email": user,
            "extra": extra
        }).execute()
    except:
        pass

def convert_utc_to_greece(ts):
    try:
        gr = pytz.timezone("Europe/Athens")
        return pd.to_datetime(ts).tz_convert(gr)
    except:
        return ts

# -------------------------------------------------
# GLOBAL ADMIN MODE
# -------------------------------------------------
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

st.sidebar.title("🔒 Admin Login")
admin_password = st.sidebar.text_input("Password", type="password")

if admin_password == "geyer123":
    st.session_state.is_admin = True

is_admin = st.session_state.is_admin

if is_admin:
    st.markdown("""
        <div style="
            position: fixed; top: 15px; right: 20px;
            background-color: #0b3c26; color: white;
            padding: 8px 15px; border-radius: 8px;
            font-size: 14px; font-weight: bold;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
            z-index: 9999;">
            🟢 Admin Mode ενεργό
        </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(page_title="Διαδραστικός Τιμοκατάλογος", layout="wide")
log_event("pricing", "visit")

# -------------------------------------------------
# GLOBAL CSS
# -------------------------------------------------

st.markdown("""
<style>

    /* APP */

    .stApp {
        background-color: #f7f8fa;
    }

    /* SIDEBAR */

    [data-testid="stSidebar"]{
        background:#ffffff;
        border-right:1px solid #e5e7eb;
    }

    [data-testid="stSidebar"] *{
        color:#1f2937 !important;
    }

    /* RESULT BOX */

    .display-box{
        background:#ffffff;
        padding:25px;
        border-left:6px solid #008c95;
        border-radius:20px;
        box-shadow:0 8px 24px rgba(0,0,0,.06);
    }

    /* OFFER TEXT */

    pre{
        font-family:'Consolas', monospace !important;
        font-size:13px !important;
        line-height:1.5 !important;
        color:#1f2937 !important;
    }

    /* HEADER */

    .main-header{
        text-align:center;
        color:#1f2937;
        margin-top:-15px;
    }

    /* INFO CARD */

    

    .info-text{

    background:linear-gradient(
        135deg,
        #008c95 0%,
        #006f77 100%
    );

    color:white;

    font-size:17px;

    line-height:1.8;

    padding:40px;

    border-radius:24px;

    margin-bottom:20px;

    box-shadow:0 8px 24px rgba(0,0,0,.08);

}

.info-text h4{
    color:white !important;
}

.info-text p{
    color:white !important;
}
    /* BUTTONS */

    .stButton > button{
        width:100%;
        height:55px;

        background:#008c95 !important;
        color:white !important;

        border:none !important;
        border-radius:12px !important;

        font-weight:700 !important;
    }

    .stButton > button:hover{
        background:#006f77 !important;
    }

</style>
""", unsafe_allow_html=True)
st.markdown("### GEYER SMART")

st.title("Φτιάξε εσύ την προσφορά σου")

st.caption(
    "Διαδραστικός υπολογισμός κόστους Smart Home με τεχνολογία GEYER"
)

st.info(
    """
🏠 LIVE PRICING SYSTEM

Δημιουργήστε τη δική σας ζήτηση Smart Home,
υπολογίστε ενδεικτικό κόστος υλικών και
αποστείλετέ την απευθείας στην GEYER.
"""
)

st.write("")

# -------------------------------------------------
# TABS
# -------------------------------------------------
tab_calc, tab_help = st.tabs(
    ["📊 LIVE PRICING", "📝 ΟΔΗΓΙΕΣ"]
)

st.markdown(
    "<div style='height:20px'></div>",
    unsafe_allow_html=True
)
# -------------------------------------------------
# ΤΙΜΟΚΑΤΑΛΟΓΟΣ GEYER
# -------------------------------------------------
PRICES = {
    "on_off": 63.92, "double_on_off": 63.92, "dim_220v": 63.92, "dim_1_10v": 66.81,
    "led_strip": 63.92, "dali": 162.63, "shutter": 63.92,
    "energy_1ph": 108.11, "energy_3ph": 155.06, "heater": 103.59,
    "heat_thermostat": 99.95, "fancoil_ctrl": 99.95, "electric_heat": 63.92,
    "split_ac": 120.61, "vrv_interface": 359.10,
    "hub_small": 158.04, "hub_large": 619.1
}

BRANDS = ["Daikin", "LG", "Toshiba", "Fujitsu", "Mitsubishi", "Panasonic", "Midea", "Άλλη"]
JOBS = ["", "Ηλεκτρολόγος", "Αρχιτέκτονας", "Μηχανικός", "Κατασκευαστής", "Ιδιώτης"]



# =================================================
# 1. LIVE PRICING TAB
# =================================================
with tab_calc:
    left, right = st.columns([1.1, 1.45])

    # ---------------- LEFT COLUMN ----------------
    with left:
        st.markdown("### 👤 Στοιχεία Πελάτη")

        v_name = st.text_input("Ονοματεπώνυμο", key="n")

        v_job = st.selectbox(
            "Ιδιότητα",
            JOBS,
            key="j"
        )

        v_addr = st.text_input(
            "Διεύθυνση έργου",
            key="a"
        )
        st.markdown("### 💡 Φωτισμός")

        c1, c2 = st.columns(2)

        int_l = c1.number_input(
        "Εσωτερικές",
        min_value=0
        )

        ext_l = c2.number_input(
        "Εξωτερικές",
         min_value=0
        )

        st.markdown("### 🌓 Είδος Γραμμών Φωτισμού")

        dim220 = st.number_input("Dimming 220V", min_value=0)

        dim110 = st.number_input("Dimming 1-10V", min_value=0)

        led = st.number_input(
        "Ταινίες LED με dimming",
        min_value=0
        )

        dali = st.number_input(
        "DALI",
        min_value=0
        )

        double = st.number_input(
        "Κομιτατέρ (Διπλή γραμμή φωτισμού)",
        min_value=0
        )

        st.markdown("### 🔥 Θέρμανση")

        h_list = [
          "Κανένα", "Καλοριφέρ", "Ενδοδαπέδια", "Fancoil οροφής",
          "Fancoil δαπέδου", "Θερμαντικά σώματα", "VRV/VRF", "Split Κλιματιστικά"
        ]

        h_type = st.selectbox("Επιλογή Θέρμανσης", h_list, key="ht")

        label_h = "Ποσότητα"

        if h_type in ["Καλοριφέρ", "Ενδοδαπέδια"]:
           label_h = "Αριθμός Θερμοστατών"
        elif "Fancoil" in h_type or h_type == "VRV/VRF":
           label_h = "Αριθμός Εσωτερικών Μονάδων"
        elif h_type == "Split Κλιματιστικά":
           label_h = "Αριθμός Κλιματιστικών"
        elif h_type == "Θερμαντικά σώματα":
           label_h = "Αριθμός Σωμάτων"

        h_qty_input = st.number_input(label_h, min_value=0, key="hq_val")
        h_qty = 0 if h_type == "Κανένα" else h_qty_input

        hb = st.selectbox("Brand (Θ)", BRANDS, key="hb") if h_type == "VRV/VRF" else ""


        
        st.markdown("### ❄️ Ψύξη")

        c_list = [
          "Κανένα", "Ενδοδαπέδια Δροσισμός", "Fancoil οροφής",
          "Fancoil δαπέδου", "VRV/VRF", "Split Κλιματιστικά"
        ]

        c_type = st.selectbox("Επιλογή Ψύξης", c_list, key="ct")

        label_c = "Ποσότητα"

        if c_type == "Ενδοδαπέδια Δροσισμός":
            label_c = "Αριθμός Θερμοστατών"
        elif "Fancoil" in c_type or c_type == "VRV/VRF":
            label_c = "Αριθμός Εσωτερικών Μονάδων"
        elif c_type == "Split Κλιματιστικά":
            label_c = "Αριθμός Κλιματιστικών"

        c_qty_input = st.number_input(label_c, min_value=0, key="cq_val")

        c_qty = 0 if c_type == "Κανένα" else c_qty_input

        cb = st.selectbox("Brand (Ψ)", BRANDS, key="cb") if c_type == "VRV/VRF" else ""
        
        st.markdown("### 🪟 Ρολά / Τέντες / Κουρτίνες")

        shutt = st.number_input("Τεμάχια", min_value=0)

        st.markdown("### 🔌 Πίνακας")

        energy = st.radio(
           "Μετρητής",
        ["Όχι", "Μονοφασικός", "Τριφασικός"],
        horizontal=True
        )

        heater = st.checkbox("Έλεγχος Θερμοσίφωνα")
        
      # ---------------- RIGHT COLUMN ----------------
    with right:
        st.markdown(
        """
        <div class='info-text'>
            <h4 style='margin-top:0;font-size:24px;color:white;'>
                🏠 LIVE PRICING SYSTEM
            </h4>

            Υπολογίστε άμεσα το κόστος ενός έργου Smart Home GEYER
            με βάση τις πραγματικές ανάγκες της εγκατάστασής σας.

            Συμπληρώστε τα στοιχεία του έργου και δείτε
            αναλυτικά την απαιτούμενη διάταξη υλικών,
            το συνολικό κόστος και το κόστος προγραμματισμού.

            📧 Μην ξεχάσετε να συμπεριλάβετε τα στοιχεία
            επικοινωνίας σας στις παρατηρήσεις.

        </div>
        """,
        unsafe_allow_html=True
    )




        # ---------------- VALIDATION ----------------
        on_off = (int_l + ext_l) - (dim220 + dim110 + led + dali + (double * 2))

        error = None
        if not v_name or not v_job or not v_addr:
            error = "⚠️ ΣΥΜΠΛΗΡΩΣΤΕ ΣΤΟΙΧΕΙΑ ΠΕΛΑΤΗ"
        elif on_off < 0:
            error = "❌ ΣΦΑΛΜΑ ΣΤΟ ΦΩΤΙΣΜΟ"
        elif (h_type == "VRV/VRF" and hb == "Άλλη") or (c_type == "VRV/VRF" and cb == "Άλλη"):
            error = "❌ ΜΗ ΣΥΜΒΑΤΟ: Η επιλογή 'Άλλη' στο VRV δεν υποστηρίζεται."
        elif h_type == "VRV/VRF" and c_type == "VRV/VRF" and hb != cb:
            error = "❌ ΛΑΘΟΣ: ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΑΡΚΕΣ VRV"

        is_exact = (
            (h_type == c_type and h_type != "Κανένα")
            or (h_type == "Ενδοδαπέδια" and c_type == "Ενδοδαπέδια Δροσισμός")
        )
        if not error and is_exact and h_qty != c_qty:
            error = f"❌ ΛΑΘΟΣ: Η ΠΟΣΟΤΗΤΑ ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΙΔΙΑ ΣΕ {h_type}"

        disp_text = ""
        notes = ""

        # ---------------- ERROR DISPLAY + ANALYTICS ----------------
        if error:
            log_event("pricing", "error", extra=error)

            st.markdown(
                f'<div class="display-box"><pre style="color:red; text-align:center;">{error}</pre></div>',
                unsafe_allow_html=True
            )
            disp_text = error

        else:
            # ---------------- HVAC CALCULATIONS ----------------
            h_c_hvac = 0
            h_det = []

            if is_exact:
                if "Fancoil" in h_type or "Δροσισμός" in h_type:
                    pk = "fancoil_ctrl"
                elif "VRV" in h_type:
                    pk = "vrv_interface"
                elif "Split" in h_type:
                    pk = "split_ac"
                else:
                    pk = "heat_thermostat"

                h_c_hvac = h_qty * PRICES[pk]
                h_det.append(
                    {
                        "n": f"{h_type} ({hb if 'VRV' in h_type else ''}) [Κοινό]",
                        "q": h_qty,
                        "p": h_c_hvac,
                    }
                )
            else:
                h_m = {
                    "Καλοριφέρ": "heat_thermostat",
                    "Ενδοδαπέδια": "heat_thermostat",
                    "Fancoil οροφής": "fancoil_ctrl",
                    "Fancoil δαπέδου": "fancoil_ctrl",
                    "Θερμαντικά σώματα": "electric_heat",
                    "VRV/VRF": "vrv_interface",
                    "Split Κλιματιστικά": "split_ac",
                    "Ενδοδαπέδια Δροσισμός": "heat_thermostat",
                }
                if h_qty > 0:
                    p = h_qty * PRICES[h_m.get(h_type, "heat_thermostat")]
                    h_c_hvac += p
                    h_det.append({"n": f"Θ: {h_type} {hb}", "q": h_qty, "p": p})
                if c_qty > 0:
                    p = c_qty * PRICES[h_m.get(c_type, "fancoil_ctrl")]
                    h_c_hvac += p
                    h_det.append({"n": f"Ψ: {c_type} {cb}", "q": c_qty, "p": p})

            # ---------------- PANEL / HUB LOGIC ----------------
            e_val = 110 if "Μονοφασικός" in energy else 160 if "Τριφασικός" in energy else 0

            base_c = (
                max(0, on_off)
                + double
                + dim220
                + dim110
                + led
                + dali
                + shutt
                + max(h_qty, c_qty)
                + (1 if e_val > 0 else 0)
                + (1 if heater else 0)
            )

            h_q = 1 if base_c <= 97 else 2
            if base_c <= 37:
                h_t = PRICES["hub_small"]
            elif base_c <= 97:
                h_t = PRICES["hub_large"]
            elif base_c <= 130:
                h_t = PRICES["hub_large"] + PRICES["hub_small"]
            else:
                h_t = PRICES["hub_large"] * 2

            total_dev = base_c + h_q

            if total_dev > 230:
                log_event("pricing", "error", extra="ΥΠΕΡΒΑΣΗ 230 ΣΥΣΚΕΥΩΝ")

                st.markdown(
                    '<div class="display-box"><pre style="color:red; text-align:center;">❌ ΣΦΑΛΜΑ: ΥΠΕΡΒΑΣΗ ΟΡΙΟΥ 230 ΣΥΣΚΕΥΩΝ</pre></div>',
                    unsafe_allow_html=True
                )
                disp_text = "ΣΦΑΛΜΑ ΟΡΙΟΥ"

            else:
                # ---------------- MATERIAL COST ----------------
                total_mat = (
                    max(0, on_off) * 63.92
                    + double * 63.92
                    + dim220 * 63.92
                    + dim110 * 52.0
                    + led * 63.92
                    + dali * 160.0
                    + shutt * 63.92
                    + h_c_hvac
                    + h_t
                    + e_val
                    + (95 if heater else 0)
                )
                prog_cost = total_mat * 0.25
                vat = total_mat * 0.24
                gen_total = total_mat + vat

                # ---------------- OFFER TEXT ----------------
                res = f"{'='*70}\n GEYER SMART HOME - ΑΝΑΛΥΤΙΚΗ ΠΡΟΣΦΟΡΑ\n{'='*70}\n"
                res += f"ΠΕΛΑΤΗΣ: {v_name.upper()} | {v_job}\nΔΙΕΥΘΥΝΣΗ: {v_addr}\n{'-'*70}\n"
                res += f"{'ΠΕΡΙΓΡΑΦΗ ΥΛΙΚΟΥ':<40} | {'TEM':<4} | {'ΤΙΜΗ':>10}\n{'-'*70}\n"

                # HUBS
                if base_c <= 37:
                    res += f"{'Κεντρική μονάδα (40 συσκευές)':<40} | {1:<4} | {PRICES['hub_small']:10.2f}€\n"
                elif base_c <= 97:
                    res += f"{'Κεντρική μονάδα (100 συσκευές)':<40} | {1:<4} | {PRICES['hub_large']:10.2f}€\n"
                elif base_c <= 130:
                    res += f"{'Κεντρική μονάδα (100 συσκευές)':<40} | {1:<4} | {PRICES['hub_large']:10.2f}€\n"
                    res += f"{'Κεντρική μονάδα (40 συσκευές)':<40} | {1:<4} | {PRICES['hub_small']:10.2f}€\n"
                else:
                    res += f"{'Κεντρική μονάδα (100 συσκευές)':<40} | {2:<4} | {(PRICES['hub_large']*2):10.2f}€\n"

                # LIGHTING
                if on_off > 0:
                    res += f"{'Γραμμές Φωτισμού On/Off':<40} | {on_off:<4} | {on_off*63.92:10.2f}€\n"
                if double > 0:
                    res += f"{'Διπλές Γραμμές (Κομιτατέρ)':<40} | {double:<4} | {double*63.92:10.2f}€\n"
                if dim220 > 0:
                    res += f"{'Dimming 220V':<40} | {dim220:<4} | {dim220*63.92:10.2f}€\n"
                if dim110 > 0:
                    res += f"{'Dimming 1-10V':<40} | {dim110:<4} | {dim110*52.00:10.2f}€\n"
                if led > 0:
                    res += f"{'Ταινίες LED Dimming':<40} | {led:<4} | {led*63.92:10.2f}€\n"
                if dali > 0:
                    res += f"{'Γραμμές DALI':<40} | {dali:<4} | {dali*160.00:10.2f}€\n"

                # HVAC DETAILS
                for d in h_det:
                    res += f"{d['n'][:40]:<40} | {d['q']:<4} | {d['p']:10.2f}€\n"

                # SHUTTERS
                if shutt > 0:
                    res += f"{'Ρολά / Τέντες / Κουρτίνες':<40} | {shutt:<4} | {shutt*63.92:10.2f}€\n"

                # ENERGY METER
                if e_val > 0:
                    res += f"{f'Μετρητής Ενέργειας ({energy})':<40} | 1    | {e_val:10.2f}€\n"

                # WATER HEATER
                if heater:
                    res += f"{'Έλεγχος Θερμοσίφωνα':<40} | 1    | {95.00:10.2f}€\n"

                # TOTALS
                res += f"{'-'*70}\n"
                res += f"{'ΣΥΝΟΛΟ ΣΥΣΚΕΩΝ:':<40} | {total_dev:<4} |\n"
                res += f"{'ΚΑΘΑΡΗ ΑΞΙΑ ΥΛΙΚΩΝ:':<48} {total_mat:10.2f}€\n"
                res += f"{'ΦΠΑ 24%:':<48} {vat:10.2f}€\n"
                res += f"{'='*70}\n"
                res += f"{'ΓΕΝΙΚΟ ΣΥΝΟΛΟ:':<48} {gen_total:10.2f}€\n"
                res += f"{'='*70}\n"
                res += f"{'ΚΟΣΤΟΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ (χωρίς ΦΠΑ):':<48} {prog_cost:10.2f}€"

                disp_text = res

                # ---------------- ANALYTICS: SUCCESSFUL CALC ----------------
                log_event("pricing", "calc", extra=f"{v_name} | {v_job}")

                # ---------------- DISPLAY RESULT ----------------
                st.markdown('<div class="display-box">', unsafe_allow_html=True)
                st.subheader("🖥️ LIVE PRICING SYSTEM")
                st.code(disp_text, language="text")
                st.markdown("</div>", unsafe_allow_html=True)

                st.write("---")
                notes = st.text_area("📝 Παρατηρήσεις Ζήτησης:")
        # ---------------- EMAIL BUTTON ----------------
        def send_email(disp_text: str, notes: str, v_name: str):
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

                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = receiver_email
                msg["Subject"] = subject
                msg.attach(MIMEText(body, "plain", "utf-8"))

                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()

                st.success("✅ Το email στάλθηκε επιτυχώς!")
                log_event("pricing", "email_send", extra=v_name)

            except Exception as e:
                st.error(f"❌ Σφάλμα αποστολής: {e}")
                log_event("pricing", "error", extra=f"email_fail: {e}")

        if st.button("🚀 ΑΠΟΣΤΟΛΗ EMAIL"):
            if not disp_text or "ΣΦΑΛΜΑ" in disp_text or "⚠️" in disp_text:
                st.error("❌ Δεν μπορεί να σταλεί email. Υπάρχει σφάλμα ή δεν έχει γίνει υπολογισμός.")
                log_event("pricing", "error", extra="email_blocked_no_calc")
            else:
                send_email(disp_text, notes, v_name)

    # =================================================
    # ADMIN ANALYTICS (ONLY IN LIVE PRICING TAB)
    # =================================================
    if is_admin:
        st.write("---")
        st.subheader("📊 Analytics LIVE PRICING (Admin Only)")

        try:
            result = supabase.table("analytics").select("*").eq("page", "pricing").order("id", desc=True).execute()

            if result.data:
                df = pd.DataFrame(result.data)
                df["timestamp"] = df["timestamp"].apply(convert_utc_to_greece)
                st.dataframe(df)
            else:
                st.info("Δεν υπάρχουν ακόμα δεδομένα.")
        except Exception as e:
            st.error(f"Σφάλμα φόρτωσης analytics: {e}")

# =================================================
# 2. ΟΔΗΓΙΕΣ TAB
# =================================================
with tab_help:
    st.title("📝 Οδηγίες Χρήσης του LIVE PRICING")

    st.markdown("""
    ## 🔍 Τι κάνει το LIVE PRICING;
    Το σύστημα LIVE PRICING υπολογίζει **αυτόματα** το κόστος ενός έργου Smart Home της GEYER, 
    με βάση τις πραγματικές ανάγκες του χώρου.

    Περιλαμβάνει:
    - Φωτισμό  
    - Dimming  
    - LED Strips  
    - DALI  
    - Θέρμανση  
    - Ψύξη  
    - Ρολά / Τέντες  
    - Μετρητές ενέργειας  
    - Θερμοσίφωνα  
    - Κεντρικές μονάδες (Hubs)  
    - ΦΠΑ  
    - Προαιρετικό κόστος προγραμματισμού  

    ---

    ## 🧩 Πώς συμπληρώνω τα πεδία;

    ### 1️⃣ Στοιχεία Πελάτη
    Συμπληρώνεις:
    - Ονοματεπώνυμο  
    - Ιδιότητα  
    - Διεύθυνση έργου  

    **Αν λείπει κάτι → εμφανίζεται προειδοποίηση.**

    ---

    ### 2️⃣ Φωτισμός
    Βάζεις:
    - Εσωτερικές γραμμές  
    - Εξωτερικές  
    - Πόσες είναι dimming  
    - Πόσες είναι κομιτατέρ  

    Το σύστημα υπολογίζει αυτόματα πόσες είναι **On/Off**.

    ---

    ### 3️⃣ Θέρμανση & Ψύξη
    Επιλέγεις τύπο:
    - Καλοριφέρ  
    - Ενδοδαπέδια  
    - Fancoil  
    - VRV/VRF  
    - Split  

    Το σύστημα:
    - Υπολογίζει σωστό τύπο συσκευής  
    - Ελέγχει ποσότητες  
    - Ελέγχει μάρκες VRV  

    ---

    ### 4️⃣ Ρολά / Τέντες
    Απλά βάζεις πόσα τεμάχια έχεις.

    ---

    ### 5️⃣ Μετρητής & Θερμοσίφωνας
    - Μονοφασικός → +110€  
    - Τριφασικός → +160€  
    - Θερμοσίφωνας → +103€  

    ---

    ## 🧮 Πώς υπολογίζεται το σύνολο;

    Το σύστημα υπολογίζει:
    - Όλες τις γραμμές φωτισμού  
    - Όλες τις μονάδες HVAC  
    - Τις κεντρικές μονάδες  
    - Μετρητή  
    - Θερμοσίφωνα  
    - ΦΠΑ  
    - Προγραμματισμό  

    ---

    ## 📧 Πώς στέλνω email;

    1. Κάνεις τον υπολογισμό  
    2. Γράφεις παρατηρήσεις  
    3. Πατάς **ΑΠΟΣΤΟΛΗ EMAIL**  

    ---

    ## ❗ Συχνά Λάθη

    - Αρνητικές γραμμές φωτισμού  
    - Διαφορετικές μάρκες VRV  
    - Διαφορετικές ποσότητες  
    - Πάνω από 230 συσκευές  
    - Κενά στοιχεία πελάτη  

    ---

    ## 🎯 Τελική Συμβουλή
    Αν έχεις αμφιβολία για κάτι, βάλε μια σημείωση στις παρατηρήσεις.  
    Θα το δω προσωπικά και θα σε καθοδηγήσω.
    """)
# ΤΕΛΟΣ ΑΡΧΕΙΟΥ LIVE PRICING
# -------------------------------------------------
# Δεν απαιτείται άλλη εντολή — το αρχείο ολοκληρώνεται εδώ.
# -------------------------------------------------
