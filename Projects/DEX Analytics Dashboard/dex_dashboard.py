import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

# Streamlit Page Config
st.set_page_config(
    page_title="DEX Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 DEX Analytics Dashboard")
st.markdown("View trending DEX pools by trading volume, liquidity, transactions, and more.")

# --- Constants / Setup --- #
BASE_API = "https://api.geckoterminal.com/api/v2"
DEFAULT_NETWORK = "eth"

# --- Sidebar Controls --- #
st.sidebar.title("⚙️ Controls")

network_options = {
    "Ethereum": "eth",
    "Polygon": "polygon_pos",
    "BSC": "bsc",
    "Arbitrum": "arbitrum",
    "Avalanche": "avax",
    "Solana": "solana",         
    "Fantom": "fantom",  
    "Optimism": "optimism"
}

selected_network = st.sidebar.selectbox("Select Blockchain Network:", options=list(network_options.keys()))
network_id = network_options[selected_network]

# --- Pool Data Fetch --- #
@st.cache_data(ttl=1800)
def fetch_trending_pools(network):
    try:
        url = f"{BASE_API}/networks/{network}/trending_pools"
        res = requests.get(url, timeout=10)
        res.raise_for_status()

        pools = []
        for item in res.json().get("data", []):
            attr = item["attributes"]
            txns = attr.get("transactions", {}).get("h24", {})
            buys = txns.get("buys", 0)
            sells = txns.get("sells", 0)
            pool = {
                "Pool Name": attr.get("name", "Unnamed"),
                "Volume (24h)": float(attr.get("volume_usd", {}).get("h24", 0)),
                "Liquidity (USD)": float(attr.get("reserve_in_usd", 0)),
                "Price Change (24h)": float(attr.get("price_change_percentage", {}).get("h24", 0)),
                "24h Buys": int(buys),
                "24h Sells": int(sells),
                "Total Transactions": int(buys) + int(sells)
            }
            pools.append(pool)
        return pools
    except Exception as e:
        st.error(f"❌ Error fetching  {e}")
        return []

# --- Data Processing --- #
with st.spinner(f"Loading trending pools from {selected_network}..."):
    data = fetch_trending_pools(network_id)

if not data: 
    st.warning("No data returned. Try changing the network.")
    st.stop()

df = pd.DataFrame(data)

# --- High-Level Metrics --- #
st.subheader("🚀 Key Protocol Metrics")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Volume (Top Pools)", f"${df['Volume (24h)'].sum():,.0f}")
col2.metric("Total Liquidity", f"${df['Liquidity (USD)'].sum():,.0f}")
col3.metric("Average % Change", f"{df['Price Change (24h)'].mean():.2f} %")
col4.metric("Total Transactions", f"{df['Total Transactions'].sum():,}")

# --- Charts --- #
st.subheader("📈 Top Pools - Analytics")

# Top 10 by volume
top_volume = df.sort_values(by="Volume (24h)", ascending=False).head(10)
fig1 = px.bar(
    top_volume,
    x="Volume (24h)",
    y="Pool Name",
    orientation="h",
    title="Top 10 DEX Pools by 24h Volume",
    labels={"Volume (24h)": "USD Volume"},
    text_auto=".2s"
)
fig1.update_layout(height=500)
st.plotly_chart(fig1, use_container_width=True)

# Liquidity vs Volume
fig2 = px.scatter(
    df,
    x="Liquidity (USD)",
    y="Volume (24h)",
    size="Total Transactions",
    color="Price Change (24h)",
    hover_name="Pool Name",
    title="Liquidity vs Volume (Bubble = Trades)",
    color_continuous_scale="RdYlGn"
)
fig2.update_layout(height=500)
st.plotly_chart(fig2, use_container_width=True)

# Distribution of Price Changes
fig3 = px.histogram(
    df,
    x="Price Change (24h)",
    nbins=20,
    title="Distribution of 24h Price Changes (%)"
)
st.plotly_chart(fig3, use_container_width=True)

# --- Data Table --- #
st.subheader("🧾 Pool Details")
st.dataframe(df.sort_values(by="Volume (24h)", ascending=False), use_container_width=True)

# Footer
st.markdown("---")
st.markdown(f"📅 Data as of: **{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**")

