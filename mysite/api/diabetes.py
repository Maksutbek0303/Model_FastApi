from fastapi import APIRouter
import joblib
from mysite.database.schema import DiabetesSchema

diabetes_router = APIRouter(prefix='/Diabetes')

scaler = joblib.load('mysite/ml_models/dia_scaler1 (1).pkl')
model = joblib.load('mysite/ml_models/dia_model1 (1).pkl')


@diabetes_router.post('/')
async def predict(diabetes: DiabetesSchema):
    data = diabetes.dict()

    features = [[
        data['Pregnancies'],data['Glucose'],data['BloodPressure'],data['SkinThickness'],
        data['Insulin'],data['BMI'],data['DiabetesPedigreeFunction'],data['Age']
    ]]

    scaled = scaler.transform(features)

    proba = model.predict_proba(scaled)[0][1]

    return {
        'diabetes': bool(proba >= 0.5),
        'probability': round(float(proba), 2)
    }