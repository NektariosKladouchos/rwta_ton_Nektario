import streamlit as st
import pandas as pd

# 1. Ρύθμιση Σελίδας
st.set_page_config(page_title="Geyer Forum", page_icon="💬", layout="wide")

# 2. Το Link σου (Το απλό link κοινοποίησης)
# ΣΙΓΟΥΡΕΨΟΥ ότι το Sheet είναι "Οποιοσδήποτε διαθέτει τον σύνδεσμο"
url = "https://google.com"

st.title("💬 Forum Τεχνικής Υποστήριξης")
st.markdown("---")

st.subheader("Πρόσφατες Συζητήσεις")

# 3. Απευθείας διάβασμα με μετατροπή σε CSV link
try:
    csv_url = url.replace('/edit?usp=sharing', '/export?format=csv')
    df = pd.read_csv(csv_url)
    
    # Καθαρισμός στηλών
    df.columns = df.columns.str.strip()
    
    if not df.empty:
        # Φιλτράρισμα άδειων γραμμών
        df = df.dropna(subset=[df.columns[2]]) # Κοιτάει την 3η στήλη (Ερώτηση)
        
        for index, row in df.iterrows():
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
    st.error("⚠️ Η σύνδεση με το Google Sheets είναι σε αναμονή. Δοκιμάστε να κάνετε Refresh.")

# 4. ΠΕΡΙΟΧΗ ΔΙΑΧΕΙΡΙΣΗΣ
st.sidebar.markdown("---")
password = st.sidebar.text_input("Κωδικός Διαχειριστή", type="password")
if password == "geyer123":
    st.sidebar.success("Καλώς ήρθες!")
    st.sidebar.markdown(f"[👉 ΑΝΟΙΓΜΑ EXCEL]({url})")
