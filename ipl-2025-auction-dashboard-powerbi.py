import streamlit as st
import streamlit.components.v1 as components

# Title of the Streamlit app
st.title("IPL 2025 Power BI Report")

# Embed the Power BI iframe using Streamlit components
components.html("""
<iframe title="IPL 2025" width="600" height="373.5" 
src="https://app.powerbi.com/view?r=eyJrIjoiYzhiOGUwZDQtNzk5Yy00NTE4LTg5MGEtOGMwMzY4MWNjOTFhIiwidCI6IjRhZDIzNDAxLTliODgtNGQ0ZC04ZmY3LWE5Y2M0OTZkODhiMyJ9" 
frameborder="0" allowFullScreen="true"></iframe>
""", height=400)
