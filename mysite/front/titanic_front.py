import streamlit as st
import requests

def check_titanic():
    st.title('Titanic API')

    api_url = 'http://127.0.0.1:8000/Titanic/'

    Pclass = st.number_input('Класс пассажира', min_value=0, max_value=3, step=1)
    Sex = st.number_input('Пол 0=М 1=Ж', min_value=0, max_value=1, step=1)
    Age = st.number_input('Возраст', min_value=0, step=1)
    SibSp = st.number_input('Количество родственников', min_value=0, max_value=15, step=1)
    Parch = st.number_input('Сколько родителей или детей', min_value=0, step=1)
    Fare = st.number_input('Стоимость билета', min_value=0, step=1)
    Embarked = st.selectbox('Порт', ['Q', 'S', 'C'])

    titanic_data = {
        "Pclass": Pclass,
        "Sex": Sex,
        "Age": Age,
        "SibSp": SibSp,
        "Parch": Parch,
        "Fare": Fare,
        "Embarked": Embarked
    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=titanic_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException as e:
            st.error(f'Не удалось подключиться к API: {e}')