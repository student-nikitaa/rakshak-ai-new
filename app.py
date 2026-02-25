import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Rakshak AI", layout="wide")

st.title("🛡 Rakshak AI Dashboard")
st.write("System is running successfully ✅")

st.markdown("---")

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Active Alerts", "5")
col2.metric("Threat Level", "Medium")
col3.metric("System Status", "Running")

st.markdown("---")

# Chart
st.subheader("Threat Analysis Overview")

data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=["Zone A", "Zone B"]
)

st.line_chart(data)

st.success("App deployed successfully on Streamlit Cloud 🎉")

