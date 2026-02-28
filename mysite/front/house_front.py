import streamlit as st
import requests

def house_chek():
    api_url = 'http://127.0.0.1:8000/House/'

    GrLivArea = st.number_input('жилая площадь дома', min_value=0, step=1)
    YearBuilt = st.number_input('Год постройки', min_value=1960, max_value=2026, step=1)
    GarageCars = st.number_input('Гараж', min_value=0, step=1)
    TotalBsmtSF = st.number_input('площадь подвала', min_value=0, step=1)
    FullBath = st.number_input('Полная ванна', min_value=0, step=1)
    OverallQual = st.number_input('Общее качество', min_value=0, step=1)
    Neighborhood = st.selectbox('Район', ['Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor', 'Edwards',
                                          'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NPkVill', 'NWAmes',
                                          'NoRidge', 'NridgHt', 'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst',
                                          'StoneBr', 'Timber', 'Veenker'])

    house_data = {
        "GrLivArea": GrLivArea,
        "YearBuilt": YearBuilt,
        "GarageCars": GarageCars,
        "TotalBsmtSF": TotalBsmtSF,
        "FullBath": FullBath,
        "OverallQual": OverallQual,
        "Neighborhood": Neighborhood
    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=house_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException as e:
            st.error(f'Не удалось подключиться к API: {e}')