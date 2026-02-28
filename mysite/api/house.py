from fastapi import APIRouter
from mysite.database.schema import HousePredictSchema
import joblib

house_router = APIRouter(prefix='/House', tags=['House API'])

scaler = joblib.load('mysite/ml_models/scaler (2).pkl')
model = joblib.load('mysite/ml_models/model (1).pkl')

Neighborhood_list = ['Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor', 'Edwards',
                     'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NPkVill', 'NWAmes',
                     'NoRidge', 'NridgHt', 'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst',
                     'StoneBr', 'Timber', 'Veenker']

@house_router.post('/')
async def predict_price(house: HousePredictSchema):
    house_dict = house.dict()

    new_nei = house_dict.pop('Neighborhood')
    neighborhood1_0 = [
        1 if new_nei == i else 0 for i in Neighborhood_list
    ]


    features = list(house_dict.values()) + neighborhood1_0
    scaled_data = scaler.transform([features])
    pred = model.predict(scaled_data)[0]
    return {'Price': round(pred)}
