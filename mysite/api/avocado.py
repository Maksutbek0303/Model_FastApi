from fastapi import APIRouter
import joblib
from mysite.database.schema import AvocadoSchema

avocado_router = APIRouter(prefix='/Avocado')

scaler = joblib.load('mysite/ml_models/avoc_scaler.pkl')
log_model = joblib.load('mysite/ml_models/avoc_model.pkl')

color_list = ['dark green', 'green', 'purple']

@avocado_router.post('/')
async def avocado_predicted(avocado: AvocadoSchema):
    avocado_dict = avocado.dict()

    new_color_category = avocado_dict.pop('color_category')

    color1or_0 = [
        1 if new_color_category == i else 0 for i in color_list
    ]

    features = list(avocado_dict.values()) + color1or_0
    scaled_data = scaler.transform([features])
    pred = log_model.predict(scaled_data)[0]

    reverse_map = {0: 'hard', 1: 'pre-conditioned', 2: 'breaking', 3: 'firm-ripe', 4: 'ripe'}

    return {'predict': reverse_map[int(pred)]}