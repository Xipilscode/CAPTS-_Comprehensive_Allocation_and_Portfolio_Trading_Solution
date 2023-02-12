# Import dependencies
import streamlit as st

# Create containers
with st.container():    
    description = st.container()
    cap_allocation = st.container()
    machine_learning = st.container()
    grid_bot = st.container()

# Write in the container 
with description:
    st.title("CAPTS: Comprehensive Allocation and Portfolio Trading Solution")
    description = """
    <div style="text-align:justify;">
    This project aims to provide a comprehensive and integrated solution for financial analysis and algorithmic trading of three asset classes. By combining three sub-projects throughout the duration of the class, utilizing technologies such as Pandas, JSON, Numpy, PyViz, SQL, and machine learning algorithms, we will develop an adaptable system for analyzing investment data and executing algorithmic GRID bot trades.
    """
    st.markdown(description, unsafe_allow_html=True)