import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

st.set_page_config(page_title="Customer Segmentation", layout="wide")

st.title("📊 Customer Segmentation Dashboard")

st.markdown("---")

# Display the cluster plot
if os.path.exists("outputs/cluster_plot.png"):
    st.subheader("Cluster Visualization")
    image = Image.open("outputs/cluster_plot.png")
    st.image(image, use_container_width=True)
else:
    st.warning("Cluster plot not found. Please run main.py first.")

# Display the customer segments data
if os.path.exists("outputs/customer_segments.csv"):
    st.subheader("Customer Segments Data")
    df = pd.read_csv("outputs/customer_segments.csv")
    st.dataframe(df, use_container_width=True)
    
    st.subheader("Segment Statistics")
    st.write(df.groupby('Cluster').agg({
        'Recency': ['mean', 'min', 'max'],
        'Frequency': ['mean', 'min', 'max'],
        'Monetary': ['mean', 'min', 'max']
    }).round(2))
else:
    st.warning("Customer segments data not found. Please run main.py first.")

st.markdown("---")
st.info("💡 Run `streamlit run app.py` from the project directory to start the server.")
