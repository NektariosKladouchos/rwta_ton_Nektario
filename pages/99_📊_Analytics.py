import streamlit as st
import pandas as pd
import pytz
from supabase import create_client, Client
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------------------------
# SUPABASE CONNECTION
# -------------------------------------------------
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def convert_utc_to_greece(ts):
    try:
        gr = pytz.timezone("Europe/Athens")
        return pd.to_datetime(ts).tz_convert(gr)
    except:
        return ts

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(page_title="📊 Analytics Dashboard", layout="wide")

# -------------------------------------------------
# ADMIN LOGIN
# -------------------------------------------------
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

st.sidebar.title("🔒 Admin Login")
admin_password = st.sidebar.text_input("Password", type="password")

if admin_password == "geyer123":
    st.session_state.is_admin = True

if not st.session_state.is_admin:
    st.error("⛔ Πρόσβαση μόνο για Admin.")
    st.stop()

# -------------------------------------------------
# PREMIUM CSS
# -------------------------------------------------
st.markdown("""
<style>
    .stApp { background-color: #f5f7fa; }
    .metric-card {
        background: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-left: 6px solid #27ae60;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# LOAD ANALYTICS DATA
# -------------------------------------------------
result = supabase.table("analytics").select("*").order("id", desc=True).execute()

if not result.data:
    st.info("Δεν υπάρχουν δεδομένα analytics ακόμα.")
    st.stop()

df = pd.DataFrame(result.data)
df["timestamp"] = df["timestamp"].apply(convert_utc_to_greece)
df["date"] = df["timestamp"].dt.date
df["hour"] = df["timestamp"].dt.strftime("%Y-%m-%d %H:00")
# -------------------------------------------------
# FILTERS
# -------------------------------------------------
st.sidebar.header("📌 Φίλτρα")

pages = ["Όλες"] + sorted(df["page"].unique())
events = ["Όλα"] + sorted(df["event"].unique())

f_page = st.sidebar.selectbox("Σελίδα", pages)
f_event = st.sidebar.selectbox("Event", events)
f_date = st.sidebar.date_input("Ημερομηνία", None)

filtered = df.copy()

if f_page != "Όλες":
    filtered = filtered[filtered["page"] == f_page]

if f_event != "Όλα":
    filtered = filtered[filtered["event"] == f_event]

if f_date:
    filtered = filtered[filtered["date"] == f_date]

# -------------------------------------------------
# REAL‑TIME METRICS
# -------------------------------------------------
st.markdown("## ⚡ Real‑Time Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Σύνολο Events", len(filtered))
col2.metric("Μοναδικές Σελίδες", filtered["page"].nunique())
col3.metric("Μοναδικά Events", filtered["event"].nunique())
col4.metric("Τελευταίο Event", filtered.iloc[0]["event"])

# -------------------------------------------------
# TOP STATS
# -------------------------------------------------
st.markdown("## 🏆 Top Statistics")

c1, c2 = st.columns(2)

with c1:
    st.markdown("### 🔝 Top Pages")
    st.bar_chart(filtered["page"].value_counts())

with c2:
    st.markdown("### 🎯 Top Events")
    st.bar_chart(filtered["event"].value_counts())
# -------------------------------------------------
# TIMELINE
# -------------------------------------------------
st.markdown("## ⏱️ Timeline Events")
timeline = filtered.groupby("hour").size()
st.line_chart(timeline)

# -------------------------------------------------
# PIE CHART
# -------------------------------------------------
st.markdown("## 🥧 Ποσοστά Events")
pie = filtered["event"].value_counts()
fig_pie = px.pie(values=pie.values, names=pie.index)
st.plotly_chart(fig_pie, use_container_width=True)

# -------------------------------------------------
# HEATMAP (Ημέρα × Ώρα)
# -------------------------------------------------
st.markdown("## 🔥 Heatmap Events")

filtered["day"] = filtered["timestamp"].dt.strftime("%Y-%m-%d")
filtered["hour_only"] = filtered["timestamp"].dt.hour

heat = filtered.groupby(["day", "hour_only"]).size().reset_index(name="count")
heat_pivot = heat.pivot(index="day", columns="hour_only", values="count").fillna(0)

fig_heat = px.imshow(
    heat_pivot,
    labels=dict(x="Ώρα", y="Ημέρα", color="Events"),
    aspect="auto",
    color_continuous_scale="Greens"
)
st.plotly_chart(fig_heat, use_container_width=True)

# -------------------------------------------------
# USER FLOW (Απλό Sankey)
# -------------------------------------------------
st.markdown("## 🔀 User Flow (Page → Event)")

flow = filtered.groupby(["page", "event"]).size().reset_index(name="count")

fig_flow = px.sunburst(flow, path=["page", "event"], values="count")
st.plotly_chart(fig_flow, use_container_width=True)

# -------------------------------------------------
# FUNNEL (Visit → Calc → Email)
# -------------------------------------------------
st.markdown("## 🧪 Funnel Conversion")

funnel = pd.DataFrame({
    "step": ["Visit", "Calc", "Email"],
    "value": [
        len(df[df["event"] == "visit"]),
        len(df[df["event"] == "calc"]),
        len(df[df["event"] == "email_send"])
    ]
})

fig_funnel = px.funnel(funnel, x="value", y="step")
st.plotly_chart(fig_funnel, use_container_width=True)

# -------------------------------------------------
# 🧹 ΚΑΘΑΡΙΣΜΟΣ ANALYTICS ΑΝΑ ΗΜΕΡΟΜΗΝΙΑ (ADMIN ONLY)
# -------------------------------------------------
st.write("---")
st.subheader("🧹 Καθαρισμός Analytics ανά Ημερομηνία")

clean_date = st.date_input("Επίλεξε ημερομηνία για διαγραφή")

if st.button("⚠️ Διαγραφή analytics για αυτή την ημερομηνία"):
    if clean_date:
        try:
            start_ts = f"{clean_date} 00:00:00"
            end_ts   = f"{clean_date} 23:59:59"

            supabase.table("analytics").delete() \
                .gte("timestamp", start_ts) \
                .lte("timestamp", end_ts) \
                .execute()

            st.success(f"✅ Τα analytics της {clean_date} διαγράφηκαν επιτυχώς!")
            st.rerun()

        except Exception as e:
            st.error(f"❌ Σφάλμα διαγραφής: {e}")
    else:
        st.warning("⚠️ Δεν έχεις επιλέξει ημερομηνία.")
