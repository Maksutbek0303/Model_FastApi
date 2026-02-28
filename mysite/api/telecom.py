from fastapi import APIRouter
import joblib
from mysite.database.schema import TelecomPredictSchema

scaler = joblib.load('mysite/ml_models/tel_scaler.pkl')
model = joblib.load('mysite/ml_models/tel_model.pkl')

telecom_router = APIRouter(prefix='/Telecom')


gender = ['Male']
Partner = ['Yes']
Dependents = ['Yes']
PhoneService = ['Yes']
MultipleLines = ['No phone service', 'Yes']
InternetService = ['Fiber optic', 'No']
OnlineSecurity = ['No internet service', 'Yes']
OnlineBackup = ['No internet service', 'Yes']
DeviceProtection = ['No internet service', 'Yes']
TechSupport = ['No internet service', 'Yes']
StreamingTV = ['No internet service', 'Yes']
StreamingMovies = ['No internet service', 'Yes']
Contract = ['One year', 'Two year']
PaperlessBilling = ['Yes']
PaymentMethod = ['Credit card (automatic)', 'Electronic check', 'Mailed check']

@telecom_router.post('/', response_model=dict)
async def telecom_predict(telecom: TelecomPredictSchema):
    telecom_dict = telecom.dict()

    new_gender = telecom_dict.pop('gender')
    gender1or_0 = [
        1 if new_gender == i else 0 for i in gender
    ]

    new_partner = telecom_dict.pop('Partner')
    partner1or_0 = [
        1 if new_partner == i else 0 for i in Partner
    ]

    new_depends = telecom_dict.pop('Dependents')
    depends1or_0 = [
        1 if new_depends == i else 0 for i in Dependents
    ]

    new_phone = telecom_dict.pop('PhoneService')
    phone1or_0 = [
        1 if new_phone == i else 0 for i in PhoneService
    ]

    new_multiple = telecom_dict.pop('MultipleLines')
    multiple1or_0 = [
        1 if new_multiple == i else 0 for i in MultipleLines
    ]

    new_internet = telecom_dict.pop('InternetService')
    internet1or_0 = [
        1 if new_internet == i else 0 for i in InternetService
    ]

    new_security = telecom_dict.pop('OnlineSecurity')
    security1or_0 = [
        1 if new_security == i else 0 for i in OnlineSecurity
    ]

    new_backup = telecom_dict.pop('OnlineBackup')
    backup1or_0 = [
        1 if new_backup == i else 0 for i in OnlineBackup
    ]

    new_device = telecom_dict.pop('DeviceProtection')
    device1or_0 = [
        1 if new_device == i else 0 for i in DeviceProtection
    ]

    new_support = telecom_dict.pop('TechSupport')
    support1or_0 = [
        1 if new_support == i else 0 for i in TechSupport
    ]

    new_streaming = telecom_dict.pop('StreamingTV')
    streaming1or_0 = [
        1 if new_streaming == i else 0 for i in StreamingTV
    ]

    new_movies = telecom_dict.pop('StreamingMovies')
    movies1or_0 = [
        1 if new_movies == i else 0 for i in StreamingMovies
    ]

    new_contract = telecom_dict.pop('Contract')
    contract1or_0 = [
        1 if new_contract == i else 0 for i in Contract
    ]

    new_paperless = telecom_dict.pop('PaperlessBilling')
    paperless1or_0 = [
        1 if new_paperless == i else 0 for i in PaperlessBilling
    ]
    new_payment = telecom_dict.pop('PaymentMethod')
    payment1or_0 = [
        1 if new_payment == i else 0 for i in PaymentMethod
    ]

    telecom_data = (
        [telecom_dict['tenure'], telecom_dict['MonthlyCharges'], telecom_dict['TotalCharges']]
        + gender1or_0 + [telecom_dict['SeniorCitizen']]
        + partner1or_0 + depends1or_0 + phone1or_0 + multiple1or_0
        + internet1or_0 + security1or_0 + backup1or_0 + device1or_0 + support1or_0
        + streaming1or_0 + movies1or_0 + contract1or_0 + paperless1or_0 + payment1or_0
    )
    scaled_data = scaler.transform([telecom_data])
    proba = model.predict_proba(scaled_data)[0]
    probability = float(proba[1])
    if probability > 0.5:
        telecom_label = "True"
    else:
        telecom_label = "False"
    return {'churn': telecom_label,
            'probability': round(probability, 2)
            }