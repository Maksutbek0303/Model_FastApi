import streamlit as st
import requests

def avocado_chek():
    st.title('Avocado API')

    api_url = 'http://127.0.0.1:8000/Avocado/'

    firmness = st.number_input('твердость', min_value=0.0)
    hue = st.number_input('оттенок', min_value=0, step=1)
    saturation = st.number_input('насыщенность', min_value=0, step=1)
    brightness = st.number_input('яркость', min_value=0, step=0)
    sound_db = st.number_input('звук_бд', min_value=0, step=1)
    weight_g = st.number_input('вес_г', min_value=0, step=1)
    size_cm3 = st.number_input('размер_см3', min_value=0, step=1)
    color_category = st.selectbox('Цвет', ['dark green', 'green', 'purple', 'black'])

    avocado_data = {
        "firmness": firmness,
        "hue": hue,
        "saturation": saturation,
        "brightness": brightness,
        "sound_db": sound_db,
        "weight_g": weight_g,
        "size_cm3": size_cm3,
        "color_category": color_category
    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=avocado_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException as e:
            st.error(f'Не удалось подключиться к API: {e}')