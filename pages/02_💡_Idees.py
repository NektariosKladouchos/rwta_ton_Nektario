import streamlit as st
import os

st.set_page_config(page_title="Ιδέες & Λύσεις - Geyer", page_icon="💡", layout="wide")

st.markdown("<h1 style='text-align: center; color: #28a745;'>Οικιακός & Επαγγελματικός Φωτισμός</h1>", unsafe_allow_html=True)
st.write("---")

# Λίστα με τις εικόνες που περιμένουμε να δούμε
images = {
    "home": "home_light.jpg",
    "pro": "pro_light.jpg"
}

col1, col2 = st.columns(2)

with col1:
    if os.path.exists(images["home"]):
        st.image(images["home"], caption="Smart Οικιακός Φωτισμός", use_container_width=True)
    elif os.path.exists(os.path.join("..", images["home"])): # Δοκιμή αν είναι στον πάνω φάκελο
        st.image(os.path.join("..", images["home"]), caption="Smart Οικιακός Φωτισμός", use_container_width=True)
    else:
        st.warning(f"⚠️ Η εικόνα {images['home']} δεν βρέθηκε στο GitHub.")
    st.write("Δημιουργήστε ατμόσφαιρα στο σπίτι σας.")

with col2:
    if os.path.exists(images["pro"]):
        st.image(images["pro"], caption="Επαγγελματικές Λύσεις", use_container_width=True)
    elif os.path.exists(os.path.join("..", images["pro"])): # Δοκιμή αν είναι στον πάνω φάκελο
        st.image(os.path.join("..", images["pro"]), caption="Επαγγελματικές Λύσεις", use_container_width=True)
    else:
        st.warning(f"⚠️ Η εικόνα {images['pro']} δεν βρέθηκε στο GitHub.")
    st.write("Αποδοτικός φωτισμός για επαγγελματικούς χώρους.")

st.write("---")
# Κώδικας για το PDF... (όπως πριν)
