import streamlit as st

# Page config
st.set_page_config(page_title="Healthcare AI Assistant", layout="wide", page_icon="💉")

# --- Sidebar ---
st.sidebar.title("Welcome!")
st.sidebar.write("Select any option from the main page below.")

# --- Main Area ---
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Healthcare AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("---")
st.write("Select the service you want to use:")

# Columns for cards
col1, col2, col3 = st.columns(3, gap="large")

# Card 1: Pneumonia
with col1:
    st.image("https://images.unsplash.com/photo-1588776814546-0f0d0f7032d6?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_column_width=True)
    if st.button("Pneumonia (Chest X-Ray)"):
        st.session_state['page'] = 'pneumonia'

# Card 2: Brain Tumor
with col2:
    st.image("https://images.unsplash.com/photo-1581091215365-7b1ed195c8c4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_column_width=True)
    if st.button("Brain Tumor (MRI)"):
        st.session_state['page'] = 'brain_tumor'

# Card 3: BMI Calculator
with col3:
    st.image("https://images.unsplash.com/photo-1599058917211-2f8c47a8f5fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_column_width=True)
    if st.button("BMI Calculator"):
        st.session_state['page'] = 'bmi'

# --- Display Selected Page ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

page = st.session_state['page']

if page == 'pneumonia':
    st.header("Pneumonia Prediction Page")
    st.write("Upload Chest X-Ray image to predict Pneumonia.")
    uploaded_file = st.file_uploader("Upload X-Ray Image", type=["png","jpg","jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.success("Prediction will appear here after model integration.")

elif page == 'brain_tumor':
    st.header("Brain Tumor Prediction Page")
    st.write("Upload MRI image to predict Brain Tumor type.")
    uploaded_file = st.file_uploader("Upload MRI Image", type=["png","jpg","jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.success("Prediction will appear here after model integration.")

elif page == 'bmi':
    st.header("BMI Calculator")
    st.write("Enter your height and weight to calculate BMI.")
    height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
    weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=70)
    if st.button("Calculate BMI"):
        bmi = weight / ((height/100)**2)
        st.success(f"Your BMI is {bmi:.2f}")
