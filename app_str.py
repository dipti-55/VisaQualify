import streamlit as st
from us_visa.pipline.prediction_pipeline import USvisaData, USvisaClassifier
from us_visa.pipline.training_pipeline import TrainPipeline

st.set_page_config(page_title="🛂 US Visa Eligibility Classifier", layout="centered")

st.title("🛂 US Visa Eligibility Classifier")

# Sidebar
# with st.sidebar:
#     st.header("Developer Options")
#     if st.button("🚀 Train Model"):
#         try:
#             pipeline = TrainPipeline()
#             pipeline.run_pipeline()
#             st.success("✅ Model trained successfully!")
#         except Exception as e:
#             st.error(f"Training failed: {e}")

st.markdown("### ✍️ Enter Visa Application Details Below")

with st.form("visa_form"):
    continent = st.selectbox("🌍 Continent", ["Asia", "Africa", "North America", "Europe", "South America", "Oceania"])
    education_of_employee = st.selectbox("🎓 Education of Employee", ["High School", "Bachelor's", "Master's", "Doctorate"])
    has_job_experience = st.selectbox("💼 Has Job Experience?", ["Y", "N"])
    requires_job_training = st.selectbox("📘 Requires Job Training?", ["Y", "N"])
    
    no_of_employees = st.number_input("🏢 Number of Employees", min_value=14500, max_value=40000, value=20000)
    company_age = st.number_input("🏗️ Age of the Company (in months)", min_value=15, max_value=180, value=60)
    
    region_of_employment = st.selectbox("🗺️ Region of Employment", ["West", "Northeast", "South", "Midwest", "Island"])
    prevailing_wage = st.number_input("💵 Prevailing Wage", min_value=600.0, max_value=70000.0, value=60000.0)
    
    unit_of_wage = st.selectbox("📆 Contract Tenure", ["Hour", "Year", "Week", "Month"])
    full_time_position = st.selectbox("🕒 Full Time Position?", ["Y", "N"])
    
    submit = st.form_submit_button("🔍 Predict Visa Status")

if submit:
    try:
        # Create USvisaData object
        data = USvisaData(
            continent=continent,
            education_of_employee=education_of_employee,
            has_job_experience=has_job_experience,
            requires_job_training=requires_job_training,
            no_of_employees=no_of_employees,
            company_age=company_age,
            region_of_employment=region_of_employment,
            prevailing_wage=prevailing_wage,
            unit_of_wage=unit_of_wage,
            full_time_position=full_time_position,
        )

        input_df = data.get_usvisa_input_data_frame()

        # Predict
        model = USvisaClassifier()
        prediction = model.predict(dataframe=input_df)[0]

        if prediction == 1:
            st.success("✅ Visa Status: Approved")
        else:
            st.error("❌ Visa Status: Not Approved")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
