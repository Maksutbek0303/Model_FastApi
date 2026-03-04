import streamlit as st
import requests

def hremployee_chek():
    api_url = 'http://127.0.0.1:8000/HREmployee/'

    st.title('HREmployee Project')
    Age = st.number_input('Age', min_value=18, max_value=100, value=30, step=1)
    DailyRate = st.number_input('Daily Rate', min_value=0, step=10)
    DistanceFromHome = st.number_input('Distance From Home', min_value=0, step=1)
    Education = st.number_input('Education (1-5)', min_value=1, max_value=5, step=1)
    EnvironmentSatisfaction = st.number_input('Environment Satisfaction (1-4)', min_value=1, max_value=4, step=1)
    HourlyRate = st.number_input('Hourly Rate', min_value=0, step=5)
    JobInvolvement = st.number_input('Job Involvement (1-4)', min_value=1, max_value=4, step=1)
    JobLevel = st.number_input('Job Level (1-5)', min_value=1, max_value=5, step=1)
    JobSatisfaction = st.number_input('Job Satisfaction (1-4)', min_value=1, max_value=4, step=1)
    MonthlyIncome = st.number_input('Monthly Income', min_value=0, step=100)
    MonthlyRate = st.number_input('Monthly Rate', min_value=0, step=100)
    NumCompaniesWorked = st.number_input('Num Companies Worked', min_value=0, step=1)
    PercentSalaryHike = st.number_input('Percent Salary Hike', min_value=0, step=1)
    PerformanceRating = st.number_input('Performance Rating (1-4)', min_value=1, max_value=4, step=1)
    RelationshipSatisfaction = st.number_input('Relationship Satisfaction (1-4)', min_value=1, max_value=4, step=1)
    StockOptionLevel = st.number_input('Stock Option Level (0-3)', min_value=0, max_value=3, step=1)
    TotalWorkingYears = st.number_input('Total Working Years', min_value=0, step=1)
    TrainingTimesLastYear = st.number_input('Training Times Last Year', min_value=0, step=1)
    WorkLifeBalance = st.number_input('Work Life Balance (1-4)', min_value=1, max_value=4, step=1)
    YearsAtCompany = st.number_input('Years At Company', min_value=0, step=1)
    YearsInCurrentRole = st.number_input('Years In Current Role', min_value=0, step=1)
    YearsSinceLastPromotion = st.number_input('Years Since Last Promotion', min_value=0, step=1)
    YearsWithCurrManager = st.number_input('Years With Current Manager', min_value=0, step=1)
    BusinessTravel = st.selectbox('Business Travel', ['Travel_Frequently', 'Travel_Rarely'])
    Gender = st.selectbox('Gender', ['Male'])
    OverTime = st.selectbox('Over Time', ['Yes'])
    Department = st.selectbox('Department', ['Research & Development', 'Sales'])
    EducationField = st.selectbox('Education Field',
                                  ['Life Sciences', 'Marketing', 'Medical', 'Other', 'Technical Degree'])
    JobRole = st.selectbox('Job Role', ['Human Resources', 'Laboratory Technician', 'Manager', 'Manufacturing Director',
                                        'Research Director', 'Research Scientist', 'Sales Executive',
                                        'Sales Representative'])
    MaritalStatus = st.selectbox('Marital Status', ['Married', 'Single'])

    hr_data = {
        "Age": Age,
        "BusinessTravel": BusinessTravel,
        "DailyRate": DailyRate,
        "DistanceFromHome": DistanceFromHome,
        "Education": Education,
        "EnvironmentSatisfaction": EnvironmentSatisfaction,
        "Gender": Gender,
        "HourlyRate": HourlyRate,
        "JobInvolvement": JobInvolvement,
        "JobLevel": JobLevel,
        "JobSatisfaction": JobSatisfaction,
        "MonthlyIncome": MonthlyIncome,
        "MonthlyRate": MonthlyRate,
        "NumCompaniesWorked": NumCompaniesWorked,
        "OverTime": OverTime,
        "PercentSalaryHike": PercentSalaryHike,
        "PerformanceRating": PerformanceRating,
        "RelationshipSatisfaction": RelationshipSatisfaction,
        "StockOptionLevel": StockOptionLevel,
        "TotalWorkingYears": TotalWorkingYears,
        "TrainingTimesLastYear": TrainingTimesLastYear,
        "WorkLifeBalance": WorkLifeBalance,
        "YearsAtCompany": YearsAtCompany,
        "YearsInCurrentRole": YearsInCurrentRole,
        "YearsSinceLastPromotion": YearsSinceLastPromotion,
        "YearsWithCurrManager": YearsWithCurrManager,
        "Department": Department,
        "EducationField": EducationField,
        "JobRole": JobRole,
        "MaritalStatus": MaritalStatus
    }

    if st.button('Проверка'):
        try:
            response = requests.post(api_url, json=hr_data, timeout=10)
            if response.status_code == 200:
                result = response.json()
                st.json(result)
            else:
                st.error(f'Ошибка: {response.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подключиться к API')
