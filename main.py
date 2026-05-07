import streamlit as st

st.title("GEYER Technical Expert Hub")
st.write("Καλώς ήρθατε στο προσωπικό μου εργαλείο τεχνικής υποστήριξης.")

tab1, tab2 = st.tabs(["🧮 Live Pricing", "📄 Τεχνικά Σχέδια"])

with tab1:
    st.header("Υπολογισμός Κόστους & Fibaro Logic")
    # Εδώ θα βάλουμε το δικό σου logic από το .exe
    qty = st.number_input("Ποσότητα Συσκευών", min_value=1)
    st.write(f"Εκτιμώμενο Κόστος: {qty * 120}€")

with tab2:
    st.header("Βιβλιοθήκη Αρχείων")
    st.write("Εδώ μπορείτε να δείτε τα σχέδια που ανεβάζω.")
    # Παράδειγμα link για PDF
    st.info("Σύντομα θα προστεθούν τα επίσημα σχέδια VRV.")
