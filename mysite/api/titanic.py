from fastapi import APIRouter
import joblib
from mysite.database.schema import TitanicSchema


titanic_router = APIRouter(prefix='/Titanic')

model = joblib.load('mysite/ml_models/tita_model.pkl')
scaler = joblib.load('mysite/ml_models/tita_scaler.pkl')

@titanic_router.post('/')
async def predict(titanic: TitanicSchema):
    titanic_dict = titanic.dict()


    new_embarked = titanic_dict.pop('Embarked')

    embarked1_0 = [
        1 if new_embarked == i else 0 for i in Embarked_list
    ]

    features = list(titanic_dict.values()) + embarked1_0
    data = scaler.transform([features])
    pred_class = model.predict(data)[0]
    final = "survived" if pred_class == 1 else "Died"

    return {"answer": final}