import streamlit as st
import requests

def diabetes_chek():

    api_url = 'http://127.0.0.1:8000/Diabetes/'

    st.title('Diabetes API')

    Pregnancies = st.number_input('Беременности', min_value=0, step=1)
    Glucose = st.number_input('Глюкоза', min_value=0.0, )
    BloodPressure = st.number_input('Кровяное давление', min_value=0.0, )
    SkinThickness = st.number_input('Толщина кожи', min_value=0.0)
    Insulin = st.number_input('Инсулин', min_value=0.0, )
    BMI = st.number_input('Индекс массы тела', min_value=0.0)
    DiabetesPedigreeFunction = st.number_input('Функция родословной диабета', min_value=0.0)
    Age = st.number_input('Возраст', min_value=0, step=1)

    diabetes_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=diabetes_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException as e:
            st.error(f'Не удалось подключиться к API: {e}')