import streamlit as st
import pandas as pd
from pathlib import Path

# Define the path to the presentation file
presentation_path = Path(__file__).parent / 'assets' / "Barwon Of A Kind.pptx"

# Add logo at the top of the page
st.image('assets/Logo.png', width=200)

# Title with subscript
st.markdown("<h2>H<sub>2</sub>Overview Dashboard</h2>", unsafe_allow_html=True)

# Sidebar message with a download button for the presentation
st.sidebar.success("Navigate through the pages using the sidebar.")

# Ensure the file exists before offering it for download
if presentation_path.exists():
    with open(presentation_path, "rb") as file:
        st.sidebar.download_button(
            label="📥 Download the Barwon of a Kind Presentation",
            data=file,
            file_name="Barwon_Of_A_Kind.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
else:
    st.sidebar.error("Presentation file not found.")

# Main content: Introduction and dashboard description
st.markdown(
    """
    Welcome to **Barwon of a Kind**'s IWN Hackathon Dashboard, designed to provide comprehensive insights into the water quality data collected from the Little Coliban River catchment area.
    This dashboard is built for **Coliban Water management** and focuses on comparing real-time sensor data with lab-based water quality measurements, rainfall, and streamflow data.
    
    ### Dashboard Overview:
    - **Data Collection Map**: See the exact locations of the data collection points within the catchment area.
    - **Water Quality Comparison**: Compare data from the Eco Dev sensors and lab tests for parameters such as turbidity, nitrate, and phosphorus.
    - **Rainfall & Streamflow**: Analyze how rainfall and streamflow impact water quality.
    - **Alerts**: Get notified when thresholds (e.g., 20mm of rainfall or high streamflow) are exceeded, triggering the need for further testing.
    - **Conclusions & Recommendations**: Summarize key findings and provide recommendations for ongoing sensor deployment and data management.
    
    **👈 Select a page from the sidebar** to start exploring the data, or **download our presentation** to get a full overview of the project.
    
    ### Need assistance?
    - Meet **John**, our AI assistant! John has access to all the water quality, rainfall, and streamflow data available on this dashboard.
    - You can ask John questions in a natural language format, and he'll provide insights, data summaries, and help you navigate through the dashboard.
    - To interact with John, click on the chat icon in the bottom right corner of any page.
    
    ### Want to dive deeper?
    - Explore the interactive data visualizations and insights on each site-specific page.
    """
)

# Add a file upload section
st.markdown("### 📁 Upload and Update Data")
st.markdown("Upload new data files to update the dashboard. You can upload **CSV** or **Excel** files containing EcoDetection, Rainfall, Streamflow, or Lab data.")

# Allow multiple file uploads
uploaded_files = st.file_uploader("Choose CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Check file extension and load data accordingly
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
            st.success(f"Uploaded CSV file: {uploaded_file.name}")
        elif uploaded_file.name.endswith(".xlsx"):
            data = pd.read_excel(uploaded_file, sheet_name=None)  # Load all sheets if it's Excel
            st.success(f"Uploaded Excel file: {uploaded_file.name}")
        
        # Display the uploaded data
        st.write(f"**Data preview from {uploaded_file.name}:**")
        st.write(data)
        
        # Here, you could add functionality to process, save, or update the dashboard with the new data
        # For now, we're just showing the data as a preview
