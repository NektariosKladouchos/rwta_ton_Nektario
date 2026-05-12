import streamlit as st
import pandas as pd

st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# ΑΥΤΟ ΕΙΝΑΙ ΤΟ ΣΩΣΤΟ LINK ΓΙΑ ΤΑ ΔΕΔΟΜΕΝΑ
sheet_id = "1d0Nr5QNiwq3OUbUN9sgieNy519CXv5Ui9Sqla_niYIU"
data_url = f"https://google.com{sheet_id}/gviz/tq?tqx=out:csv"

st.title("💬 Forum Τεχνικής Υποστήριξης")
st.write("---")

try:
    # Διαβάζουμε τα δεδομένα
    df = pd.read_csv(data_url)
    # Καθαρίζουμε τα ονόματα των στηλών από κενά
    df.columns = df.columns.str.strip()
    
    if not df.empty:
        for index, row in df.iterrows():
            if pd.notna(row.iloc[2]): # Αν υπάρχει ερώτηση στην 3η στήλη
                with st.container():
                    st.markdown(f"**👤 {row.iloc[1]}** | 📅 {row.iloc[0]}")
                    st.info(f"❓ {row.iloc[2]}")
                    apantisi = row.iloc[3]
                    if pd.notna(apantisi) and str(apantisi).strip() != "":
                        st.success(f"✅ **Απάντηση:** {apantisi}")
                    else:
                        st.warning("🕒 *Αναμένεται απάντηση...*")
                    st.write("---")
except Exception as e:
    st.error("Σύνδεση σε αναμονή... Παρακαλώ κάντε Refresh.")

# ΠΕΡΙΟΧΗ ΔΙΑΧΕΙΡΙΣΗΣ
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")
if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες!")
    # ΑΥΤΟ ΤΟ LINK ΘΑ ΣΕ ΠΑΕΙ ΚΑΤΕΥΘΕΙΑΝ ΣΤΟ EXCEL ΣΟΥ
    edit_link = f"https://google.com{sheet_id}/edit"
    st.sidebar.link_button("📝 ΑΝΟΙΓΜΑ EXCEL", edit_link)
