import streamlit as st


# ---------------------------------------------------------
# 🔄 CAROUSEL FUNCTION (PC + MOBILE)
# ---------------------------------------------------------
def image_carousel(title, images):
    st.markdown(f"## {title}")

    key_index = f"carousel_index_{title}"
    if key_index not in st.session_state:
        st.session_state[key_index] = 0

    index = st.session_state[key_index]

    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        if st.button("⬅️", key=title + "_prev"):
            st.session_state[key_index] = (index - 1) % len(images)

    with col2:
        st.image(images[index]["path"], use_column_width=True)
        st.markdown(f"**{images[index]['caption']}**")
        st.caption(images[index]["description"])

    with col3:
        if st.button("➡️", key=title + "_next"):
            st.session_state[key_index] = (index + 1) % len(images)


# ---------------------------------------------------------
# 🔥 MAIN PAGE
# ---------------------------------------------------------
def show():
    # Τίτλος σελίδας
    st.header("🔥 Heating / Cooling – Έξυπνη Θέρμανση & Ψύξη χωρίς Διπλούς Θερμοστάτες")

    st.write(
        "Ολοκληρωμένη λύση για κατοικίες με ενδοδαπέδια θέρμανση, fan coil οροφής και αντλία θερμότητας. "
        "Καταργούμε τους διπλούς θερμοστάτες και προσφέρουμε δύο λύσεις: Απλή & Premium, "
        "με έναν θερμοστάτη ανά ζώνη και πλήρη απομακρυσμένη διαχείριση από το κινητό."
    )

    st.divider()

    # 1. Το πρόβλημα
    st.subheader("❗ Το πρόβλημα με τους διπλούς θερμοστάτες")

    st.markdown(
        """
        Σε σύγχρονες κατοικίες με:

        - **Ενδοδαπέδια θέρμανση**
        - **Fan coil οροφής για ψύξη**
        - **Αντλία θερμότητας**

        ο χρήστης συχνά βρίσκεται μπροστά σε **δύο θερμοστάτες ανά δωμάτιο**:

        - έναν για την ενδοδαπέδια  
        - έναν για το fan coil  

        Αυτό δημιουργεί:

        - **σύγχυση**  
        - **κακή αισθητική**  
        - **λάθος χειρισμούς**  
        - **διπλές ρυθμίσεις θερμοκρασίας**  
        - **αδυναμία αυτοματισμού & σεναρίων**  
        - **αδυναμία επιλογής τρόπου λειτουργίας από το κινητό**  
        """
    )

    st.divider()

    # 2. Περιορισμός – ΜΟΝΟ με αντλία θερμότητας
    st.subheader("🚫 Συμβατότητα – Μόνο με Αντλία Θερμότητας, όχι VRV/VRF")

    st.markdown(
        """
        Η λύση μας λειτουργεί **αποκλειστικά** σε συστήματα με αντλία θερμότητας νερού.

        Δεν εφαρμόζεται σε VRV/VRF, γιατί:

        - χρησιμοποιούν **ψυκτικό μέσο**, όχι νερό  
        - δεν υπάρχουν **ηλεκτροβάνες νερού**  
        - δεν υπάρχει **ενδοδαπέδια με νερό**  
        - δεν υπάρχουν **fan coil νερού**  
        - δεν υπάρχει δυνατότητα **HEAT/COOL μέσω επαφών**  
        """
    )

    st.info("Η λύση ισχύει μόνο για εγκαταστάσεις με αντλία θερμότητας νερού, ενδοδαπέδια και fan coil.")

    st.divider()

    # 3. Οι 2 λύσεις συνοπτικά
    st.subheader("🟦 Οι 2 προτεινόμενες λύσεις")

    st.markdown(
        """
        Και οι δύο λύσεις προσφέρουν:

        - **Απομακρυσμένη διαχείριση από κινητό / υπολογιστή**
        - **Έλεγχο θερμοκρασίας ανά ζώνη**
        - **Έλεγχο ηλεκτροβανών ενδοδαπέδιας & fan coil**
        - **Έναν θερμοστάτη ανά δωμάτιο**

        Η διαφορά είναι:

        ### ✔ Απλή Λύση → Απομακρυσμένη διαχείριση θερμοκρασίας  
        ### ✔ Premium Λύση → Απομακρυσμένη διαχείριση + Επιλογή Mode (Τρόπος λειτουργίας)
        """
    )

    st.divider()

    # 4. Απλή λύση
    st.subheader("1️⃣ Απλή Λύση – Smart Θερμοστάτης ανά Ζώνη")

    st.markdown(
        """
        Στην απλή λύση:

        - **Ένας Smart Θερμοστάτης** ανά ζώνη αναλαμβάνει:
          - **Θέρμανση από ενδοδαπέδια**  
          - **Ψύξη από fan coil**  

        Ο χρήστης μπορεί:

        - να ρυθμίζει θερμοκρασία από το κινητό  
        - να βλέπει την κατάσταση της ζώνης  
        - να ενεργοποιεί/απενεργοποιεί θέρμανση & ψύξη  

        👉 Δεν υπάρχει επιλογή Mode (π.χ. Floor Cooling, FC Cooling, Mixed).
        """
    )

    st.markdown("### 🔧 Υδραυλική Υποδομή – Απλή Λύση")
    st.markdown(
        """
        - 1 **ηλεκτροβάνα ενδοδαπέδιας** ανά ζώνη  
        - 1 **ηλεκτροβάνα fan coil** ανά ζώνη  
        - 1 **fan coil οροφής** ανά ζώνη  
        - 1 **Smart Θερμοστάτης** ανά ζώνη  
        - 1 **Μικρή κεντρική μονάδα**  
        """
    )

    with st.expander("🔄 Flowchart – Απλή Λειτουργία Smart Θερμοστάτη"):
        st.code(
            """
Smart Thermostat
       │
 ┌─────┴─────┐
 │           │
HEAT Mode  COOL Mode
 │           │
 │      Κλείνει ενδοδαπέδια
 │      Ανοίγει βαλβίδα fan coil
 │      Fan ON (Low/Med/High)
 │           │
Ανοίγει βαλβίδα   Ψύξη χώρου
ενδοδαπέδιας
Fan Coil OFF
Θέρμανση χώρου
            """,
            language="text",
        )

    st.success("💰 Τελικό κόστος για 5 ζώνες: **657,79 €**")

    st.divider()

    # 5. Premium λύση
    st.subheader("2️⃣ Premium Λύση – Smart Controller + Επιλογή Mode από Κινητό")

    st.markdown(
        """
        Στην premium λύση:

        - **Smart Θερμοστάτης ανά ζώνη**
        - **Κεντρική μονάδα Smart Home**
        - **Ηλεκτροβάνες ενδοδαπέδιας & fan coil**
        - **Έλεγχος της αντλίας θερμότητας μέσω επαφών**

        Ο χρήστης μπορεί:

        - να ρυθμίζει θερμοκρασία από το κινητό  
        - να επιλέγει Mode λειτουργίας (Heat / Cool / Mixed)  
        - να ελέγχει ενδοδαπέδια, fan coil & αντλία θερμότητας  
        """
    )

    st.markdown("### 🔧 Υδραυλική Υποδομή – Premium Λύση")
    st.markdown(
        """
        - Κεντρικές ηλεκτροβάνες  
        - Modules για έλεγχο βανών & εντολών αντλίας  
        - Έλεγχος HEAT / COOL / ON / OFF  
        - Προαιρετικά: αισθητήρες υγρασίας  
        """
    )

    with st.expander("🔄 Flowchart – Premium Λειτουργία"):
        st.code(
            """
Smart Controller
       │
       │  Επιλογή από Κινητό:
       │  - Floor Cooling
       │  - Floor + FC Cooling
       │  - FC Cooling Only
       │  - Heating Modes
       │
 ┌─────┼───────────────────────────────┬───────────────────────────────┐
 │     │                               │                               │
Floor Cooling                  Floor + FC Cooling              FC Cooling Only
 │                               │                               │
Ανοίγει ενδοδαπέδια        Ανοίγει ενδοδαπέδια & FC       Κλείνει ενδοδαπέδια
Κλείνει FC                 Ρυθμίζει Fan Coil             Ανοίγει FC
Αντλία σε COOL             Αντλία σε COOL                Αντλία σε COOL
Ήπιος δροσισμός           Ισχυρός δροσισμός             Ψύξη από FC

Heating Modes
 │
Επιλογή:
- Floor Heating
- FC Heating
- Mixed
 │
Αντλία σε HEAT
Θέρμανση από ενδοδαπέδια / FC / συνδυασμό
            """,
            language="text",
        )

    st.success("💰 Τελικό κόστος για 5 ζώνες: **1.310,61 €**")

    st.divider()

    # 6. Σύγκριση λύσεων
    st.subheader("🧱 Τι αλλάζει υδραυλικά μεταξύ Απλής & Premium Λύσης;")

    st.markdown(
        """
        | Στοιχείο                             | Απλή Λύση | Premium Λύση |
        |--------------------------------------|-----------|--------------|
        | Απομακρυσμένη διαχείριση            | ✔         | ✔            |
        | Επιλογή Mode από κινητό             | ✖         | **✔**        |
        | Ηλεκτροβάνες ενδοδαπέδιας           | ✔         | ✔            |
        | Ηλεκτροβάνες fan coil               | ✔         | ✔            |
        | Κεντρικές ηλεκτροβάνες              | ✖         | ✔            |
        | Έλεγχος αντλίας μέσω επαφών         | Προαιρετικός | **Απαραίτητος** |
        | Δροσισμός ενδοδαπέδιας              | ✖         | **✔**        |
        | Μικτά modes (ενδοδαπέδια + FC)      | ✖         | **✔**        |
        | Προστασία υγρασίας                  | ✖         | **✔**        |
        """
    )

    st.divider()

    # 7. Συμπέρασμα
    st.subheader("🧠 Γιατί ο συνδυασμός Smart Θερμοστάτη + Controller είναι η ιδανική λύση;")

    st.markdown(
        """
        - Καταργεί τους **διπλούς θερμοστάτες**  
        - Προσφέρει **καθαρή αισθητική**  
        - Δίνει **premium λειτουργίες**  
        - Επιτρέπει **επιλογή mode από το κινητό**  
        - Λειτουργεί **μόνο με αντλία θερμότητας**  
        - Προσφέρει **μέγιστη εξοικονόμηση**  
        - Είναι **100% επεκτάσιμο**  
        """
    )

    st.success("✅ Δύο λύσεις – μία φιλοσοφία: Έξυπνη, καθαρή και premium διαχείριση θέρμανσης & ψύξης χωρίς διπλούς θερμοστάτες.")

    # ---------------------------------------------------------
    # 📸 CAROUSELS SECTION
    # ---------------------------------------------------------
    st.divider()
    st.header("📸 Εικόνες Συστήματος – PC & Mobile")

    # PC Screens
    pc_images = [
        {"path": "subpages/pictures/heating/01_thermostats.png", "caption": "Κεντρική Επισκόπηση Θερμοστατών", "description": "Προβολή όλων των ζωνών."},
        {"path": "subpages/pictures/heating/02_thermostats.png", "caption": "Αναλυτική Προβολή Θερμοστάτη", "description": "Ρύθμιση θερμοκρασίας & mode."},
        {"path": "subpages/pictures/heating/03_thermostats.png", "caption": "Διάγραμμα Θερμοκρασίας", "description": "Καταγραφή θερμοκρασίας χώρου."},
        {"path": "subpages/pictures/heating/04_thermostats.png", "caption": "Ρυθμίσεις Συσκευών", "description": "Παράμετροι Z-Wave."},
        {"path": "subpages/pictures/heating/05_thermostats.png", "caption": "Ρυθμίσεις Θερμοστάτη", "description": "Offset & advanced settings."},
        {"path": "subpages/pictures/heating/06_Calibration_thermostat.png", "caption": "Calibration Θερμοστάτη", "description": "Βαθμονόμηση αισθητήρων."},
        {"path": "subpages/pictures/heating/07_antlia_rithmisis.png", "caption": "Ρυθμίσεις Αντλίας", "description": "Έλεγχος θέρμανσης & ψύξης."},
        {"path": "subpages/pictures/heating/08_antlia_rithmisis.png", "caption": "Dashboard Αντλίας", "description": "Κεντρική διαχείριση λειτουργιών."},
    ]

    image_carousel("🟦 PC Screens", pc_images)

    st.divider()

    # Mobile Screens
    mobile_images = [
        {"path": "subpages/pictures/heating/09_tropos_litourgias_antlias.jpg", "caption": "Τρόποι Λειτουργίας Αντλίας", "description": "Επιλογή mode από το κινητό."},
        {"path": "subpages/pictures/heating/10_mobile_thermostats.jpg", "caption": "Θερμοστάτες στο Κινητό", "description": "Προβολή όλων των ζωνών."},
        {"path": "subpages/pictures/heating/11_mobile_devices.jpg", "caption": "Συσκευές Σπιτιού", "description": "Έλεγχος θέρμανσης & ψύξης."},
        {"path": "subpages/pictures/heating/12_mobile_home.jpg", "caption": "Αρχική Οθόνη", "description": "Θερμοκρασίες ανά δωμάτιο."},
        {"path": "subpages/pictures/heating/13_mobile_pump.jpg", "caption": "Οθόνη Αντλίας", "description": "Έλεγχος λειτουργιών αντλίας."},
        {"path": "subpages/pictures/heating/14_mobile_energy.jpg", "caption": "Energy Panel", "description": "Κατανάλωση ενέργειας."},
        {"path": "subpages/pictures/heating/15_mobile_summary.jpg", "caption": "Σύνοψη Σπιτιού", "description": "Θερμοκρασία & κατανάλωση."},
        {"path": "subpages/pictures/heating/16_mobile_kouzina.jpg", "caption": "Οθόνη Κουζίνας", "description": "Θερμοστάτης & φωτισμός."},
    ]

    image_carousel("🟩 Mobile Screens", mobile_images)
