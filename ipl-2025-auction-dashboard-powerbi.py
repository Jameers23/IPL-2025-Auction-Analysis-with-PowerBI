import streamlit as st
import streamlit.components.v1 as components

# Title of the Streamlit app
st.title("IPL 2025 Power BI Report")

# Embed the Power BI iframe using Streamlit components with full width and height
components.html("""
<style>
    iframe {
        width: 100%;
        height: 90vh; /* Adjust height as needed, 90% of the viewport height */
        border: none;
    }
</style>
<iframe title="IPL 2025" src="https://app.powerbi.com/view?r=eyJrIjoiYzhiOGUwZDQtNzk5Yy00NTE4LTg5MGEtOGMwMzY4MWNjOTFhIiwidCI6IjRhZDIzNDAxLTliODgtNGQ0ZC04ZmY3LWE5Y2M0OTZkODhiMyJ9" allowFullScreen="true"></iframe>
""", height=0, scrolling=True)
