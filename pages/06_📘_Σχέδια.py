import streamlit as st
import os

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="📘 Τεχνικά Σχέδια",
    page_icon="📘",
    layout="wide"
)

# ---------------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------------
st.title("📘 Τεχνικά Σχέδια")
st.write("""
Καλώς ήρθατε στην ενότητα Τεχνικών Σχεδίων.  
Εδώ θα βρείτε οργανωμένα παραδείγματα, αναλύσεις και οδηγίες για:
- Συνδέσεις DALI  
- Συνδέσεις LED & Drivers  
- HVAC αυτοματισμούς  
- Παραδείγματα προγραμματισμού  
- Εκπαιδευτικό υλικό  
""")

st.write("---")

# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "🔌 Σχέδια Σύνδεσης",
    "⚙️ Τρόποι Προγραμματισμού",
    "🎓 Μαθήματα"
])

# ---------------------------------------------------------
# FUNCTION: LOAD TXT
# ---------------------------------------------------------
def load_txt_data(txt_path):
    data = {"title": "", "description": "", "electrician": "", "customer": ""}

    if not os.path.exists(txt_path):
        return data

    section = None
    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.lower() == "[title]":
                section = "title"
                continue
            elif line.lower() == "[description]":
                section = "description"
                continue
            elif line.lower() == "[electrician]":
                section = "electrician"
                continue
            elif line.lower() == "[customer]":
                section = "customer"
                continue

            if section:
                data[section] += line + "\n"

    return data

# ---------------------------------------------------------
# TAB 1 — ΣΧΕΔΙΑ ΣΥΝΔΕΣΗΣ
# ---------------------------------------------------------
with tab1:
    st.subheader("🔌 Σχέδια Σύνδεσης")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SXEDIA_DIR = os.path.join(BASE_DIR, "sxedia")

    categories = {
        "Φωτισμός": "fotismos",
        "Μοτέρ Σκίασης": "moter",
        "HVAC": "hvac",
        "Ζεστά Νερά": "znx",
        "Συναγερμός": "synagermos",
        "Αισθητήρες": "aisthitires",
        "Σενάρια": "senaria",
        "Μετρητές": "metrites",
        "Άλλα": "alla"
    }

    cat_choice = st.selectbox("Επιλέξτε κατηγορία σχεδίων:", list(categories.keys()))
    folder = os.path.join(SXEDIA_DIR, categories[cat_choice])

    st.write("---")

    if not os.path.exists(folder):
        st.warning("⚠️ Ο φάκελος δεν υπάρχει ακόμα.")
        st.stop()

    files = [
        f for f in os.listdir(folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    if len(files) == 0:
        st.info("ℹ️ Δεν υπάρχουν σχέδια σε αυτή την κατηγορία.")
        st.stop()

    choice = st.selectbox("Επιλέξτε σχέδιο:", files)
    img_path = os.path.join(folder, choice)

    st.image(img_path, use_container_width=True)

    # ---------------------------------------------------------
    # LOAD TXT FOR THIS IMAGE
    # ---------------------------------------------------------
    txt_name = choice.rsplit(".", 1)[0] + ".txt"
    txt_path = os.path.join(folder, txt_name)
    info = load_txt_data(txt_path)

    clean_title = choice.rsplit(".", 1)[0].replace("_", " ").title()

    st.markdown("### 📘 Τίτλος Σχεδίου")
    st.write(info["title"] if info["title"] else clean_title)

    st.markdown("### 📝 Γρήγορη Επεξήγηση")
    st.write(info["description"] if info["description"] else "Δεν υπάρχει περιγραφή.")

    st.markdown("### ⚠️ Τι πρέπει να προσέξει ο ηλεκτρολόγος")
    st.write(info["electrician"] if info["electrician"] else "Δεν υπάρχουν παρατηρήσεις.")

    st.markdown("### ⭐ Τι κερδίζει ο πελάτης")
    st.write(info["customer"] if info["customer"] else "Δεν υπάρχουν οφέλη.")

# ---------------------------------------------------------
# TAB 2 — ΤΡΟΠΟΙ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ
# ---------------------------------------------------------
with tab2:
    st.subheader("⚙️ Τρόποι Προγραμματισμού")

    επιλογή2 = st.selectbox(
        "Επιλέξτε διαδικασία:",
        [
            "Δημιουργία Σκηνής",
            "Ρύθμιση Χρονοπρογράμματος",
            "Ομαδοποίηση Φωτισμού",
            "Ρύθμιση Θερμοκρασίας",
            "Αυτοματισμός με Συνθήκες"
        ]
    )

    st.write("---")

    if επιλογή2 == "Δημιουργία Σκηνής":
        st.markdown("### 🎛️ Δημιουργία Σκηνής")
        st.write("""
        1. Επιλογή γραμμών φωτισμού  
        2. Ορισμός επιπέδου φωτισμού  
        3. Αποθήκευση σκηνής  
        4. Έλεγχος από εφαρμογή ή οθόνη  
        """)

    elif επιλογή2 == "Ρύθμιση Χρονοπρογράμματος":
        st.markdown("### 🕒 Ρύθμιση Χρονοπρογράμματος")
        st.write("""
        1. Επιλογή ημέρας  
        2. Ορισμός ώρας  
        3. Επιλογή σκηνής ή γραμμής  
        4. Ενεργοποίηση  
        """)

    elif επιλογή2 == "Ομαδοποίηση Φωτισμού":
        st.markdown("### 💡 Ομαδοποίηση Φωτισμού")
        st.write("""
        - Ομαδοποίηση πολλών γραμμών σε μία εντολή  
        - Ιδανικό για κεντρικό έλεγχο  
        """)

    elif επιλογή2 == "Ρύθμιση Θερμοκρασίας":
        st.markdown("### 🌡️ Ρύθμιση Θερμοκρασίας")
        st.write("""
        - Ρύθμιση θερμοστάτη  
        - Έλεγχος Fan Coil / Boiler  
        """)

    elif επιλογή2 == "Αυτοματισμός με Συνθήκες":
        st.markdown("### ⚡ Αυτοματισμός με Συνθήκες")
        st.write("""
        - Ενεργοποίηση βάσει αισθητήρων  
        - Παράδειγμα: Άνοιγμα παραθύρου → Σβήσιμο θέρμανσης  
        """)

# ---------------------------------------------------------
# TAB 3 — ΜΑΘΗΜΑΤΑ
# ---------------------------------------------------------
with tab3:
    st.subheader("🎓 Μαθήματα")

    επιλογή3 = st.selectbox(
        "Επιλέξτε μάθημα:",
        [
            "Τι είναι το 0-10V",
            "Τι είναι το DALI",
            "Πώς λειτουργεί το LED Driver",
            "Εισαγωγή στο HVAC",
            "Βασικές Αρχές Αυτοματισμού"
        ]
    )

    st.write("---")

    if επιλογή3 == "Τι είναι το 0-10V":
        st.markdown("### 🎓 Τι είναι το 0-10V")
        st.write("""
        - Αναλογικό σήμα ελέγχου φωτισμού  
        - 0V = χαμηλή ένταση, 10V = μέγιστη  
        """)

    elif επιλογή3 == "Τι είναι το DALI":
        st.markdown("### 🎓 Τι είναι το DALI")
        st.write("""
        - Ψηφιακό πρωτόκολλο φωτισμού  
        - Διπολικό bus  
        """)

    elif επιλογή3 == "Πώς λειτουργεί το LED Driver":
        st.markdown("### 🎓 Πώς λειτουργεί το LED Driver")
        st.write("""
        - Μετατρέπει AC → DC  
        - Σταθερό ρεύμα ή τάση  
        """)

    elif επιλογή3 == "Εισαγωγή στο HVAC":
        st.markdown("### 🎓 Εισαγωγή στο HVAC")
        st.write("""
        - Θέρμανση, εξαερισμός, κλιματισμός  
        """)

    elif επιλογή3 == "Βασικές Αρχές Αυτοματισμού":
        st.markdown("### 🎓 Βασικές Αρχές Αυτοματισμού")
        st.write("""
        - Είσοδοι, έξοδοι, αισθητήρες  
        - Λογικές συνθήκες  
        """)
