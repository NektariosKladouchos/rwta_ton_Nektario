
import os
from pathlib import Path
import streamlit as st

# --- Serve images from subpages/pictures as static files ---
pictures_path = Path("subpages/pictures")
st.static_path = pictures_path


def show():
    st.header("🏨 Αυτοματισμός Ενοικιαζόμενων Διαμερισμάτων")
    st.write("Δείτε πώς μετατρέψαμε μια πραγματική ανάγκη συνεργάτη μας σε ένα έξυπνο, αυτόματο και ενεργειακά αποδοτικό κατάλυμα.")

    # 1. Η Ζήτηση του Πελάτη
    st.subheader("📋 Η Ζήτηση του πελάτη και η ιδέα του συνεργάτη")
    st.info("""
    **Το Πρόβλημα:** Ιδιοκτήτης με ενοικιαζόμενα διαμερίσματα αναζητούσε μια λύση που να του εξασφαλίζει **μέγιστη εξοικονόμηση ενέργειας**, **απόλυτη άνεση** για τον πελάτη και **ασφάλεια** της περιουσίας, χωρίς να χρειάζεται η συνεχής φυσική του παρουσία ή η εκπαίδευση των ενοικιαστών.
    """)

    st.divider()

    # 2. Η Λύση Αυτοματισμού που Δώσαμε
    st.subheader("💡 Η Λύση μας: Έξυπνη Διαχείριση (Step-by-Step)")
    st.write("Αναπτύξαμε ένα κεντρικό σύστημα αυτοματισμού που ελέγχει και προστατεύει κάθε διαμέρισμα ξεχωριστά, προσφέροντας τις παρακάτω λειτουργίες:")

    with st.expander("💧 α) Αυτόματη Χρήση Ζεστού Νερού (Άνεση & Οικονομία)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Ο πελάτης έχει πάντα ζεστό νερό χωρίς να κάνει απολύτως τίποτα.
        * **Η τεχνολογία:** Το σύστημα αναγνωρίζει μέσω του καρτοδιακόπτη αν ο πελάτης βρίσκεται στο δωμάτιο. Ταυτόχρονα, μετράει τη θερμοκρασία του νερού στο boiler.
        * **Το αποτέλεσμα:** Ανοίγει και κλείνει μόνο του την ηλεκτρική αντίσταση όταν χρειάζεται, εξασφαλίζοντας ζεστό νερό οποιαδήποτε ώρα, χωρίς άσκοπη σπατάλη ρεύματος όταν το δωμάτιο είναι άδειο.
        """)

    with st.expander("🛡️ β) Έξυπνη Αποχώρηση & Έλεγχος Συναγερμού (Ασφάλεια)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Με την έξοδο του πελάτη, το κατάλυμα «κλειδώνει» και αυτοπροστατεύεται.
        * **Η τεχνολογία:** Όταν ο πελάτης αφαιρεί την κάρτα και φεύγει, το σύστημα το αντιλαμβάνεται. Κλείνει αυτόματα τα φώτα και τις πρίζες. **Σημαντικό:** Κλείνει τα κλιματιστικά στέλνοντας εντολή τερματισμού (OFF) και *όχι κόβοντας το ρεύμα*, προστατεύοντας τις ευαίσθητες ηλεκτρονικές πλακέτες τους από καταστροφή.
        * **Το αποτέλεσμα:** Αμέσως μετά, ενεργοποιεί την επίβλεψη σε παράθυρα και πόρτες σε κατάσταση συναγερμού. Αν γίνει οποιαδήποτε παραβίαση ή δολιοφθορά όσο ο πελάτης λείπει, το σύστημα ειδοποιεί αμέσως τον ιδιοκτήτη στο κινητό.
        """)

    with st.expander("📱 γ) Προκλιματισμός Δωματίου εξ Αποστάσεως (Εμπειρία Επισκέπτη)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Ο πελάτης μπαίνει σε ένα ήδη δροσερό ή ζεστό δωμάτιο.
        * **Η τεχνολογία:** Μόλις ο ιδιοκτήτης λάβει την ειδοποίηση κράτησης ή άφιξης, έχει τη δυνατότητα με μία μόνο κίνηση μέσα από το κινητό του να ανάψει το κλιματιστικό στην επιθυμητή θερμοκρασία.
        """)

    with st.expander("🧹 δ) Ειδοποίηση Καθαριότητας (Logistics)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Απόλυτος έλεγχος του χρόνου check-in και check-out.
        * **Η τεχνολογία:** Το σύστημα στέλνει αυτόματη ενημέρωση στο κινητό του ιδιοκτήτη τη στιγμή που ο πελάτης μπαίνει ή βγαίνει οριστικά από το κατάλυμα.
        """)

    with st.expander("📊 ε) Δυναμικά Όρια Θερμοκρασίας (Εξοικονόμηση)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Αποτροπή ακραίων ρυθμίσεων.
        * **Η τεχνολογία:** Οι θερμοστάτες των κλιματιστικών κλειδώνουν σε ανώτερα και κατώτερα επιτρεπτά όρια.
        """)

    with st.expander("🪄 ζ) Το «Μαγικό Χέρι» στα Παράθυρα (Έξυπνη Διαχείριση A/C)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Το κλιματιστικό λειτουργεί μόνο όταν πρέπει.
        * **Η τεχνολογία:** Αν ο πελάτης ανοίξει μπαλκονόπορτα ή παράθυρο και το αφήσει ανοιχτό για χρόνο που έχει ορίσει ο ιδιοκτήτης, το σύστημα κλείνει το κλιματιστικό στέλνοντας σήμα OFF.
        """)

    with st.expander("🚨 η) Κρίσιμες Ειδοποιήσεις (Μηδενικό Ρίσκο)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Ο ιδιοκτήτης προλαμβάνει τα παράπονα πριν καν δημιουργηθούν.
        * **Η τεχνολογία:** Το σύστημα επιβλέπει την υγειόητα του κτιρίου 24/7 και ειδοποιεί άμεσα σε περίπτωση προβλήματος.
        """)

    st.divider()

    # 3. Μελλοντική Επεκτασιμότητα
    st.subheader("🚀 Μελλοντική Επεκτασιμότητα (Future-Proof)")
    st.write("""
    Ένα από τα μεγαλύτερα πλεονεκτήματα του συστήματός μας είναι η **απόλυτη ευελιξία** του.
    """)

    st.markdown("""
    * **Έξυπνος Εξωτερικός Φωτισμός**
    * **Έλεγχος Σκίασης & Πισίνας**
    * **Διαχείριση Ήχου & Κατανάλωσης**
    * **Ασφάλεια & Πρόληψη**
    """)

    st.divider()
    
    # 4. Διασύνδεση & Εφαρμογές (Διαδραστικό Καρουσέλ Screenshots
    # --- Lightbox για μεγέθυνση εικόνων ---
    st.markdown("""
    <style>
    .lightbox-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.85);
        display: none;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }

    .lightbox-image {
        max-width: 90%;
        max-height: 90%;
        border-radius: 12px;
        box-shadow: 0 0 25px rgba(255,255,255,0.3);
    }

    .lightbox-close {
        position: absolute;
        top: 25px;
        right: 35px;
        font-size: 40px;
        color: white;
        cursor: pointer;
        font-weight: bold;
    }

    img {
        cursor: zoom-in;
        max-height: 450px !important;
        width: auto !important;
        object-fit: contain !important;
        border-radius: 10px;
    }
    </style>

    <script>
    function openLightbox(src) {
        document.getElementById("lightbox-img").src = src;
        document.getElementById("lightbox").style.display = "flex";
    }

    function closeLightbox() {
        document.getElementById("lightbox").style.display = "none";
    }
    </script>

    <div id="lightbox" class="lightbox-overlay" onclick="closeLightbox()">
        <span class="lightbox-close">&times;</span>
        <img id="lightbox-img" class="lightbox-image">
    </div>
    """, unsafe_allow_html=True)

    # 4. Διασύνδεση & Εφαρμογές (Διαδραστικό Καρουσέλ Screenshots)
    st.subheader("📱 Περιβάλλον Διαχείρισης (Live App & PC Screenshots)")
    st.write("Κάντε κλικ στις εικόνες για μεγέθυνση και περιηγηθείτε στις οθόνες της εφαρμογής και του διαχειριστικού προγράμματος.")

    col_carousel1, col_carousel2 = st.columns(2)

    # ------------------ ΣΤΗΛΗ 1: ΚΙΝΗΤΟ ------------------
    with col_carousel1:
        st.markdown("### 📱 Οθόνες Εφαρμογής Κινητού")

        app_images = [
            {"title": "Κεντρική Οθόνη (Favourites)", "url": "subpages/pictures/FAVOURITES_1.jpg", "desc": "Κεντρική οθόνη που ο κάθε χρήστης φτιάχνει την οθόνη του."},
            {"title": "Κεντρική Οθόνη", "url": "subpages/pictures/FAVOURITES_2.jpg", "desc": "Συγκεντρωτική εμφάνιση συσκευών ανά κατηγορία."},
            {"title": "Συσκευές ανά κατηγορία", "url": "subpages/pictures/FAVOURITES_3.jpg", "desc": "Ο χρήστης επιλέγει ποιες συσκευές θα εμφανίζονται."},
            {"title": "Ανάλυση συσκευών", "url": "subpages/pictures/FAVOURITES_4.jpg", "desc": "Αναλυτική εμφάνιση συσκευών ανά κατηγορία."},
            {"title": "Μετεωρολογικός Σταθμός", "url": "subpages/pictures/FAVOURITES_5.jpg", "desc": "Καιρικές συνθήκες, θερμοκρασία, υγρασία."},
            {"title": "Οθόνη Δωματίων", "url": "subpages/pictures/HOME_1.jpg", "desc": "Εμφάνιση δωματίων με θερμοκρασία & υγρασία."},
            {"title": "Ανάλυση Δωματίου", "url": "subpages/pictures/HOME_2.jpg", "desc": "Διαχείριση συσκευών ανά δωμάτιο."},
            {"title": "Ηλεκτρικός Πίνακας", "url": "subpages/pictures/HOME_3.jpg", "desc": "Παρακολούθηση παρουσίας & boiler."},
            {"title": "Σενάρια", "url": "subpages/pictures/SCENES_1.jpg", "desc": "Σενάρια παρουσίας & ζεστών νερών."},
            {"title": "Ρυθμίσεις Σκηνών", "url": "subpages/pictures/SCENES_5.jpg", "desc": "Ενεργοποίηση/απενεργοποίηση σεναρίων."},
            {"title": "Περισσότερα", "url": "subpages/pictures/MORE_1.jpg", "desc": "Live παρακολούθηση κλιματιστικών."}
        ]

        selected_app_page = st.selectbox(
            "Επιλέξτε οθόνη κινητού για προβολή:",
            [img["title"] for img in app_images],
            key="app_carousel_select"
        )

        for img in app_images:
            if img["title"] == selected_app_page:
                img_url = local_image(img["url"])
                st.markdown(
                    f'<img src="{img_url}" onclick="openLightbox(\'{img_url}\')" style="width:100%;">',
                    unsafe_allow_html=True
                )
                st.info(f"**ℹ️ Επεξήγηση:** {img['desc']}")

    # ------------------ ΣΤΗΛΗ 2: PC ------------------
    with col_carousel2:
        st.markdown("### 💻 Διαχειριστικό Πρόγραμμα PC")

        pc_images = [
            {"title": "Dashboard", "url": "subpages/pictures/01_Dashboard.png", "desc": "Πλήρες ταμπλό ελέγχου."},
            {"title": "Ιστορικό Θερμοστάτη", "url": "subpages/pictures/03_history_Thermostat_IR.png", "desc": "Παρακολούθηση χειρισμών θερμοστάτη."},
            {"title": "Ιστορικό Σκηνών", "url": "subpages/pictures/04_history_scene open window.png", "desc": "Ανίχνευση ανοικτού παραθύρου."},
            {"title": "Πίνακας Σκηνών", "url": "subpages/pictures/05_SCENES.png", "desc": "Σενάρια ανά δωμάτιο."},
            {"title": "Ρυθμίσεις Συσκευών", "url": "subpages/pictures/09_SETTINGS_DEVICES.png", "desc": "Παραμετροποίηση συσκευών."},
            {"title": "Ρυθμίσεις Δωματίων", "url": "subpages/pictures/10_SETTINGS_ROOMS.png", "desc": "Δημιουργία & ρύθμιση χώρων."},
            {"title": "Σενάρια Παρουσίας", "url": "subpages/pictures/12_SETTINGS_SCENES_2.png", "desc": "BLOCK SCENE για παρουσία."},
            {"title": "Σενάρια Θερμοσίφωνα", "url": "subpages/pictures/13_SETTINGS_SCENES_3.png", "desc": "Αυτόματη ενεργοποίηση θερμοσίφωνα."},
            {"title": "Τοποθεσία Συστήματος", "url": "subpages/pictures/21_SETTINGS_GENERAL_LOCATION.png", "desc": "Ορισμός τοποθεσίας."},
            {"title": "Μεταβλητές", "url": "subpages/pictures/23_SETTINGS_GENERAL_VARIABLES.png", "desc": "Ρυθμίσεις θερμοκρασιών."},
            {"title": "Backup", "url": "subpages/pictures/28_SETTINGS_BACKUP.png", "desc": "Αντίγραφα ασφαλείας."},
            {"title": "Alarm", "url": "subpages/pictures/33_SETTINGS_ALARM.png", "desc": "Ρύθμιση ζωνών συναγερμού."}
        ]

        selected_pc_page = st.selectbox(
            "Επιλέξτε οθόνη PC για προβολή:",
            [img["title"] for img in pc_images],
            key="pc_carousel_select"
        )

        for img in pc_images:
            if img["title"] == selected_pc_page:
                img_url = local_image(img["url"])
                st.markdown(
                    f'<img src="{img_url}" onclick="openLightbox(\'{img_url}\')" style="width:100%;">',
                    unsafe_allow_html=True
                )
                st.info(f"**ℹ️ Επεξήγηση:** {img['desc']}")
    
    
    
   

    # 5. Κόστος Project
    st.subheader("💰 Κόστος Project & Υλικών")
    st.write("Η επένδυση στον αυτοματισμό αποσβένεται γρήγορα μέσω της εξοικονόμησης ενέργειας και της μείωσης των ζημιών.")

    st.markdown("""
    | Κατηγορία Υλικών / Υπηρεσιών | Περιγραφή | Κόστος ανά Διαμέρισμα |
    | :--- | :--- | :---: |
    | **Κεντρικός Ελεγκτής & Sensors** | Κεντρική μονάδα αυτοματισμού, αισθητήρες θερμοκρασίας boiler, καλωδιακές παγίδες παραθύρων/πορτών (4 ζώνες). | **350 €** |
    | **Θερμοστάτες κλιματιστικών & Έλεγχος Φορτίων** | Έξυπνοι διακόπτες ρεύματος, έλεγχος αντίστασης νερού, έλεγχος 3 κλιματιστικών (IR/πλακέτα). | **420 €** |
    | **Παραμετροποίηση & Εφαρμογές** | Προγραμματισμός σεναρίων (μαγικό χέρι, συναγερμός, boiler), σύνδεση με Mobile App & PC. | **150 €** |
    | **Σύνολο Υλικών & Λογισμικού** | **Κόστος ανά μονάδα (διαμέρισμα)** | **920 €** |
    """)

    st.markdown("""
    *Σημείωση: Στις τιμές δεν περιλαμβάνεται ο Φ.Π.Α. και το κόστος της τοπικής ηλεκτρολογικής εγκατάστασης (καλωδιώσεις).  
    Για το συνολικό project των 3 διαμερισμάτων, παρέχεται ειδική έκπτωση κατόπιν επικοινωνίας.*
    """)

    st.success("📞 Επικοινωνήστε μαζί μας για να σχεδιάσουμε τη δική σας custom λύση αυτοματισμού!")
def show():
    st.header("🏨 Αυτοματισμός Ενοικιαζόμενων Διαμερισμάτων")
    st.write("Δείτε πώς μετατρέψαμε μια πραγματική ανάγκη συνεργάτη μας σε ένα έξυπνο, αυτόματο και ενεργειακά αποδοτικό κατάλυμα.")

    # 1. Η Ζήτηση του Πελάτη
    st.subheader("📋 Η Ζήτηση του πελάτη και η ιδέα του συνεργάτη")
    st.info("""
    **Το Πρόβλημα:** Ιδιοκτήτης με ενοικιαζόμενα διαμερίσματα αναζητούσε μια λύση που να του εξασφαλίζει **μέγιστη εξοικονόμηση ενέργειας**, **απόλυτη άνεση** για τον πελάτη και **ασφάλεια** της περιουσίας, χωρίς να χρειάζεται η συνεχής φυσική του παρουσία ή η εκπαίδευση των ενοικιαστών.
    """)

    st.divider()

    # 2. Η Λύση Αυτοματισμού που Δώσαμε
    st.subheader("💡 Η Λύση μας: Έξυπνη Διαχείριση (Step-by-Step)")
    st.write("Αναπτύξαμε ένα κεντρικό σύστημα αυτοματισμού που ελέγχει και προστατεύει κάθε διαμέρισμα ξεχωριστά, προσφέροντας τις παρακάτω λειτουργίες:")

    with st.expander("💧 α) Αυτόματη Χρήση Ζεστού Νερού (Άνεση & Οικονομία)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Ο πελάτης έχει πάντα ζεστό νερό χωρίς να κάνει απολύτως τίποτα.
        * **Η τεχνολογία:** Το σύστημα αναγνωρίζει μέσω του καρτοδιακόπτη αν ο πελάτης βρίσκεται στο δωμάτιο. Ταυτόχρονα, μετράει τη θερμοκρασία του νερού στο boiler.
        * **Το αποτέλεσμα:** Ανοίγει και κλείνει μόνο του την ηλεκτρική αντίσταση όταν χρειάζεται, εξασφαλίζοντας ζεστό νερό οποιαδήποτε ώρα, χωρίς άσκοπη σπατάλη ρεύματος όταν το δωμάτιο είναι άδειο.
        """)

    with st.expander("🛡️ β) Έξυπνη Αποχώρηση & Έλεγχος Συναγερμού (Ασφάλεια)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Με την έξοδο του πελάτη, το κατάλυμα «κλειδώνει» και αυτοπροστατεύεται.
        * **Η τεχνολογία:** Όταν ο πελάτης αφαιρεί την κάρτα και φεύγει, το σύστημα το αντιλαμβάνεται. Κλείνει αυτόματα τα φώτα και τις πρίζες. **Σημαντικό:** Κλείνει τα κλιματιστικά στέλνοντας εντολή τερματισμού (OFF) και *όχι κόβοντας το ρεύμα*, προστατεύοντας τις ευαίσθητες ηλεκτρονικές πλακέτες τους από καταστροφή.
        * **Το αποτέλεσμα:** Αμέσως μετά, ενεργοποιεί την επίβλεψη σε παράθυρα και πόρτες σε κατάσταση συναγερμού. Αν γίνει οποιαδήποτε παραβίαση ή δολιοφθορά όσο ο πελάτης λείπει, το σύστημα ειδοποιεί αμέσως τον ιδιοκτήτη στο κινητό.
        """)

    with st.expander("📱 γ) Προκλιματισμός Δωματίου εξ Αποστάσεως (Εμπειρία Επισκέπτη)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Ο πελάτης μπαίνει σε ένα ήδη δροσερό ή ζεστό δωμάτιο.
        * **Η τεχνολογία:** Μόλις ο ιδιοκτήτης λάβει την ειδοποίηση κράτησης ή άφιξης, έχει τη δυνατότητα με μία μόνο κίνηση μέσα από το κινητό του να ανάψει το κλιματιστικό στην επιθυμητή θερμοκρασία.
        """)

    with st.expander("🧹 δ) Ειδοποίηση Καθαριότητας (Logistics)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Απόλυτος έλεγχος του χρόνου check-in και check-out.
        * **Η τεχνολογία:** Το σύστημα στέλνει αυτόματη ενημέρωση στο κινητό του ιδιοκτήτη τη στιγμή που ο πελάτης μπαίνει ή βγαίνει οριστικά από το κατάλυμα.
        """)

    with st.expander("📊 ε) Δυναμικά Όρια Θερμοκρασίας (Εξοικονόμηση)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Αποτροπή ακραίων ρυθμίσεων.
        * **Η τεχνολογία:** Οι θερμοστάτες των κλιματιστικών κλειδώνουν σε ανώτερα και κατώτερα επιτρεπτά όρια.
        """)

    with st.expander("🪄 ζ) Το «Μαγικό Χέρι» στα Παράθυρα (Έξυπνη Διαχείριση A/C)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Το κλιματιστικό λειτουργεί μόνο όταν πρέπει.
        * **Η τεχνολογία:** Αν ο πελάτης ανοίξει μπαλκονόπορτα ή παράθυρο και το αφήσει ανοιχτό για χρόνο που έχει ορίσει ο ιδιοκτήτης, το σύστημα κλείνει το κλιματιστικό στέλνοντας σήμα OFF.
        """)

    with st.expander("🚨 η) Κρίσιμες Ειδοποιήσεις (Μηδενικό Ρίσκο)"):
        st.markdown("""
        * **Πώς λειτουργεί:** Ο ιδιοκτήτης προλαμβάνει τα παράπονα πριν καν δημιουργηθούν.
        * **Η τεχνολογία:** Το σύστημα επιβλέπει την υγειόητα του κτιρίου 24/7 και ειδοποιεί άμεσα σε περίπτωση προβλήματος.
        """)

    st.divider()

    # 3. Μελλοντική Επεκτασιμότητα
    st.subheader("🚀 Μελλοντική Επεκτασιμότητα (Future-Proof)")
    st.write("""
    Ένα από τα μεγαλύτερα πλεονεκτήματα του συστήματός μας είναι η **απόλυτη ευελιξία** του.
    """)

    st.markdown("""
    * **Έξυπνος Εξωτερικός Φωτισμός**
    * **Έλεγχος Σκίασης & Πισίνας**
    * **Διαχείριση Ήχου & Κατανάλωσης**
    * **Ασφάλεια & Πρόληψη**
    """)

    st.divider()
    # 4. Διασύνδεση & Εφαρμογές (Διαδραστικό Καρουσέλ Screenshots
    # --- Lightbox για μεγέθυνση εικόνων ---
    st.markdown("""
    <style>
    .lightbox-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.85);
        display: none;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }

    .lightbox-image {
        max-width: 90%;
        max-height: 90%;
        border-radius: 12px;
        box-shadow: 0 0 25px rgba(255,255,255,0.3);
    }

    .lightbox-close {
        position: absolute;
        top: 25px;
        right: 35px;
        font-size: 40px;
        color: white;
        cursor: pointer;
        font-weight: bold;
    }

    img {
        cursor: zoom-in;
        max-height: 450px !important;
        width: auto !important;
        object-fit: contain !important;
        border-radius: 10px;
    }
    </style>

    <script>
    function openLightbox(src) {
        document.getElementById("lightbox-img").src = src;
        document.getElementById("lightbox").style.display = "flex";
    }

    function closeLightbox() {
        document.getElementById("lightbox").style.display = "none";
    }
    </script>

    <div id="lightbox" class="lightbox-overlay" onclick="closeLightbox()">
        <span class="lightbox-close">&times;</span>
        <img id="lightbox-img" class="lightbox-image">
    </div>
    """, unsafe_allow_html=True)

    # 4. Διασύνδεση & Εφαρμογές (Διαδραστικό Καρουσέλ Screenshots)
    st.subheader("📱 Περιβάλλον Διαχείρισης (Live App & PC Screenshots)")
    st.write("Κάντε κλικ στις εικόνες για μεγέθυνση και περιηγηθείτε στις οθόνες της εφαρμογής και του διαχειριστικού προγράμματος.")

    col_carousel1, col_carousel2 = st.columns(2)

    # ------------------ ΣΤΗΛΗ 1: ΚΑΡΟΥΣΕΛ ΚΙΝΗΤΟΥ ------------------
    with col_carousel1:
        st.markdown("### 📱 Οθόνες Εφαρμογής Κινητού")

        app_images = [
            {"title": "Κεντρική Οθόνη (Favourites)", "url": "subpages/pictures/FAVOURITES_1.jpg", "desc": "Κεντρική οθόνη που ο κάθε χρήστης φτιάχνει την οθόνη του."},
            {"title": "Κεντρική Οθόνη", "url": "subpages/pictures/FAVOURITES_2.jpg", "desc": "Συγκεντρωτική εμφάνιση συσκευών ανά κατηγορία."},
            {"title": "Συσκευές ανά κατηγορία", "url": "subpages/pictures/FAVOURITES_3.jpg", "desc": "Ο χρήστης επιλέγει ποιες συσκευές θα εμφανίζονται."},
            {"title": "Ανάλυση συσκευών", "url": "subpages/pictures/FAVOURITES_4.jpg", "desc": "Αναλυτική εμφάνιση συσκευών ανά κατηγορία."},
            {"title": "Μετεωρολογικός Σταθμός", "url": "subpages/pictures/FAVOURITES_5.jpg", "desc": "Καιρικές συνθήκες, θερμοκρασία, υγρασία."},
            {"title": "Οθόνη Δωματίων", "url": "subpages/pictures/HOME_1.jpg", "desc": "Εμφάνιση δωματίων με θερμοκρασία & υγρασία."},
            {"title": "Ανάλυση Δωματίου", "url": "subpages/pictures/HOME_2.jpg", "desc": "Διαχείριση συσκευών ανά δωμάτιο."},
            {"title": "Ηλεκτρικός Πίνακας", "url": "subpages/pictures/HOME_3.jpg", "desc": "Παρακολούθηση παρουσίας & boiler."},
            {"title": "Σενάρια", "url": "subpages/pictures/SCENES_1.jpg", "desc": "Σενάρια παρουσίας & ζεστών νερών."},
            {"title": "Ρυθμίσεις Σκηνών", "url": "subpages/pictures/SCENES_5.jpg", "desc": "Ενεργοποίηση/απενεργοποίηση σεναρίων."},
            {"title": "Περισσότερα", "url": "subpages/pictures/MORE_1.jpg", "desc": "Live παρακολούθηση κλιματιστικών."}
        ]

        selected_app_page = st.selectbox(
            "Επιλέξτε οθόνη κινητού για προβολή:",
            [img["title"] for img in app_images],
            key="app_carousel_select"
        )

        for img in app_images:
            if img["title"] == selected_app_page:
                st.markdown(
                    f'<img src="{img["url"]}" onclick="openLightbox(\'{img["url"]}\')" style="width:100%;">',
                    unsafe_allow_html=True
                )
                st.info(f"**ℹ️ Επεξήγηση:** {img['desc']}")

    # ------------------ ΣΤΗΛΗ 2: ΚΑΡΟΥΣΕΛ ΥΠΟΛΟΓΙΣΤΗ ------------------
    with col_carousel2:
        st.markdown("### 💻 Διαχειριστικό Πρόγραμμα PC")

        pc_images = [
            {"title": "Dashboard", "url": "subpages/pictures/01_Dashboard.png", "desc": "Πλήρες ταμπλό ελέγχου."},
            {"title": "Ιστορικό Θερμοστάτη", "url": "subpages/pictures/03_history_Thermostat_IR.png", "desc": "Παρακολούθηση χειρισμών θερμοστάτη."},
            {"title": "Ιστορικό Σκηνών", "url": "subpages/pictures/04_history_scene open window.png", "desc": "Ανίχνευση ανοικτού παραθύρου."},
            {"title": "Πίνακας Σκηνών", "url": "subpages/pictures/05_SCENES.png", "desc": "Σενάρια ανά δωμάτιο."},
            {"title": "Ρυθμίσεις Συσκευών", "url": "subpages/pictures/09_SETTINGS_DEVICES.png", "desc": "Παραμετροποίηση συσκευών."},
            {"title": "Ρυθμίσεις Δωματίων", "url": "subpages/pictures/10_SETTINGS_ROOMS.png", "desc": "Δημιουργία & ρύθμιση χώρων."},
            {"title": "Σενάρια Παρουσίας", "url": "subpages/pictures/12_SETTINGS_SCENES_2.png", "desc": "BLOCK SCENE για παρουσία."},
            {"title": "Σενάρια Θερμοσίφωνα", "url": "subpages/pictures/13_SETTINGS_SCENES_3.png", "desc": "Αυτόματη ενεργοποίηση θερμοσίφωνα."},
            {"title": "Τοποθεσία Συστήματος", "url": "subpages/pictures/21_SETTINGS_GENERAL_LOCATION.png", "desc": "Ορισμός τοποθεσίας."},
            {"title": "Μεταβλητές", "url": "subpages/pictures/23_SETTINGS_GENERAL_VARIABLES.png", "desc": "Ρυθμίσεις θερμοκρασιών."},
            {"title": "Backup", "url": "subpages/pictures/28_SETTINGS_BACKUP.png", "desc": "Αντίγραφα ασφαλείας."},
            {"title": "Alarm", "url": "subpages/pictures/33_SETTINGS_ALARM.png", "desc": "Ρύθμιση ζωνών συναγερμού."}
        ]

        selected_pc_page = st.selectbox(
            "Επιλέξτε οθόνη PC για προβολή:",
            [img["title"] for img in pc_images],
            key="pc_carousel_select"
        )

        for img in pc_images:
            if img["title"] == selected_pc_page:
                st.markdown(
                    f'<img src="{img["url"]}" onclick="openLightbox(\'{img["url"]}\')" style="width:100%;">',
                    unsafe_allow_html=True
                )
                st.info(f"**ℹ️ Επεξήγηση:** {img['desc']}")

    # 5. Κόστος Project
    st.subheader("💰 Κόστος Project & Υλικών")
    st.write("Η επένδυση στον αυτοματισμό αποσβένεται γρήγορα μέσω της εξοικονόμησης ενέργειας και της μείωσης των ζημιών.")

    st.markdown("""
    | Κατηγορία Υλικών / Υπηρεσιών | Περιγραφή | Κόστος ανά Διαμέρισμα |
    | :--- | :--- | :---: |
    | **Κεντρικός Ελεγκτής & Sensors** | Κεντρική μονάδα αυτοματισμού, αισθητήρες θερμοκρασίας boiler, καλωδιακές παγίδες παραθύρων/πορτών (4 ζώνες). | **350 €** |
    | **Θερμοστάτες κλιματιστικών & Έλεγχος Φορτίων** | Έξυπνοι διακόπτες ρεύματος, έλεγχος αντίστασης νερού, έλεγχος 3 κλιματιστικών (IR/πλακέτα). | **420 €** |
    | **Παραμετροποίηση & Εφαρμογές** | Προγραμματισμός σεναρίων (μαγικό χέρι, συναγερμός, boiler), σύνδεση με Mobile App & PC. | **150 €** |
    | **Σύνολο Υλικών & Λογισμικού** | **Κόστος ανά μονάδα (διαμέρισμα)** | **920 €** |
    """)

    st.markdown("""
    *Σημείωση: Στις τιμές δεν περιλαμβάνεται ο Φ.Π.Α. και το κόστος της τοπικής ηλεκτρολογικής εγκατάστασης (καλωδιώσεις).  
    Για το συνολικό project των 3 διαμερισμάτων, παρέχεται ειδική έκπτωση κατόπιν επικοινωνίας.*
    """)

    st.success("📞 Επικοινωνήστε μαζί μας για να σχεδιάσουμε τη δική σας custom λύση αυτοματισμού!")
