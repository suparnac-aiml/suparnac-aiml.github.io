import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
from datetime import datetime

# Streamlit page config
st.set_page_config(
    page_title="Historical Pool Analysis",
    layout="wide"
)

st.title("📈 Historical Pool Analysis")

# Sidebar controls
st.sidebar.header("Controls")
network = st.sidebar.selectbox(
    "Select Network",
    ["eth", "polygon_pos", "bsc", "arbitrum", "avax"]
)
pool_address = st.sidebar.text_input(
    "Enter Pool Address",
    placeholder="e.g. 0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640"
)
timeframe = st.sidebar.selectbox("Timeframe", ["hour", "day", "week"])
limit = st.sidebar.slider("Data Points to Fetch", min_value=10, max_value=100, value=30)

# Function to fetch OHLCV data
def fetch_pool_ohlcv(network: str, pool: str, timeframe: str, limit: int):
    base_url = "https://api.geckoterminal.com/api/v2"
    url = f"{base_url}/networks/{network}/pools/{pool}/ohlcv/{timeframe}"
    params = {"limit": limit}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        raw = resp.json().get("data", {}).get("attributes", {}).get("ohlcv_list", [])
        # ohlcv_list is a list of lists: [timestamp, open, high, low, close, volume]
        df = pd.DataFrame(raw, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
        return df
    except Exception as e:
        st.error(f"Error fetching OHLCV  {e}")
        return pd.DataFrame()

# Main logic
if pool_address:
    st.subheader(f"Pool: {pool_address} on {network.upper()}")
    df_ohlcv = fetch_pool_ohlcv(network, pool_address, timeframe, limit)
    
    if df_ohlcv.empty:
        st.warning("No data returned. Check pool address and network.")
        st.stop()
    
    # Candlestick chart
    st.markdown("### Candlestick Price Chart")
    fig_candle = go.Figure(
        data=go.Candlestick(
            x=df_ohlcv["timestamp"],
            open=df_ohlcv["open"],
            high=df_ohlcv["high"],
            low=df_ohlcv["low"],
            close=df_ohlcv["close"],
            increasing_line_color="green",
            decreasing_line_color="red"
        )
    )
    fig_candle.update_layout(
        xaxis_title="Time",
        yaxis_title="Price (USD)",
        height=600,
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig_candle, use_container_width=True)
    
    # Volume bar chart
    st.markdown("### Trading Volume Over Time")
    fig_vol = go.Figure()
    fig_vol.add_trace(
        go.Bar(
            x=df_ohlcv["timestamp"],
            y=df_ohlcv["volume"],
            marker_color="blue"
        )
    )
    fig_vol.update_layout(
        xaxis_title="Time",
        yaxis_title="Volume",
        height=300,
        margin=dict(l=40, r=40, t=20, b=20)
    )
    st.plotly_chart(fig_vol, use_container_width=True)
    
    # Show raw data table
    st.markdown("### Raw OHLCV Data")
    st.dataframe(df_ohlcv.style.format({
        "open": "{:.4f}",
        "high": "{:.4f}",
        "low": "{:.4f}",
        "close": "{:.4f}",
        "volume": "{:,.0f}"
    }), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown(f"Data fetched at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

else:
    st.info("Enter a valid pool address above to view historical analysis.")

