# Import dependencies
import streamlit as st

# Create containers
with st.beta_container90:    
    description = st.beta_container()
    cap_allocation = st.beta_container()
    machine_learning = st.beta_container()
    grid_bot = st.beta_container()

# Write in the container 
with description:
    st.title('CAPTS: Comprehensive Allocation and Portfolio Trading Solution')