import streamlit as st
import pandas as pd

# Title
st.title("Sales Summary App")
st.subheader("Simple interactive dashboard for sales data")

# Data
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Tablet", "Phone"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Sales": [50000, 1500, 3000, 20000, 40000]
}

df = pd.DataFrame(data)

# Sidebar filter
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter data
filtered_df = df[df["Category"] == category]

# Show table
st.dataframe(filtered_df)

# Line chart
st.line_chart(filtered_df["Sales"])