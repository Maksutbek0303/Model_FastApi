from fastapi import FastAPI
import uvicorn
from mysite.api import (house, student, titanic,
                        bank, diabetes, avocado,
                        mushrooms, telecom)
model_app = FastAPI(title='Models Project')
model_app.include_router(house.house_router)
model_app.include_router(student.student_router)
model_app.include_router(titanic.titanic_router)
model_app.include_router(bank.bank_router)
model_app.include_router(diabetes.diabetes_router)
model_app.include_router(avocado.avocado_router)
model_app.include_router(mushrooms.mushroom_router)
model_app.include_router(telecom.telecom_router)



if __name__ == '__main__':
    uvicorn.run(model_app, host='127.0.0.1', port=8000)