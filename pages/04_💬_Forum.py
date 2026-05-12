import streamlit as st
import pandas as pd

st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# Το link των δεδομένων σου
sheet_id = "1d0Nr5QNiwq3OUbUN9sgieNy519CXv5Ui9Sqla_niYIU"
data_url = f"https://google.com{sheet_id}/export?format=csv"

st.title("💬 Forum Τεχνικής Υποστήριξης")
st.write("---")

try:
    # Διάβασμα δεδομένων
    df = pd.read_csv(data_url)
    # Καθαρισμός κενών από τους τίτλους
    df.columns = df.columns.str.strip()
    
    if not df.empty:
        for index, row in df.iterrows():
            # Έλεγχος αν η γραμμή έχει ερώτηση (3η στήλη)
            if pd.notna(row.iloc[2]):
                with st.container():
                    st.markdown(f"**👤 {row.iloc[1]}** | 📅 {row.iloc[0]}")
                    st.info(f"❓ {row.iloc[2]}")
                    
                    # Έλεγχος για απάντηση (4η στήλη)
                    apantisi = row.iloc[3]
                    if pd.notna(apantisi) and str(apantisi).strip() != "":
                        st.success(f"✅ **Απάντηση:** {apantisi}")
                    else:
                        st.warning("🕒 *Αναμένεται απάντηση...*")
                    st.write("---")
    else:
        st.write("Δεν υπάρχουν ακόμα συζητήσεις.")
except Exception as e:
    st.error("Η σύνδεση με το Google Sheets είναι σε αναμονή. Παρακαλώ κάντε Refresh στη σελίδα.")

# Διαχείριση (Sidebar)
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")
if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες Νεκτάριε!")
    st.sidebar.link_button("📝 ΑΝΟΙΓΜΑ EXCEL", f"https://google.com{sheet_id}/edit")
