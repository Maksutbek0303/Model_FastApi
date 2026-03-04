from fastapi import APIRouter
from mysite.database.schema import HREmployeeSchema
import joblib

HREmployee_router = APIRouter(prefix='/HREmployee', tags=['HREmployee API'])


model = joblib.load('mysite/ml_models/HRE_model.pkl')
scaler = joblib.load('mysite/ml_models/HRE_scaler.pkl')

Department_list = ['Research & Development', 'Sales']
EducationField_list = ['Life Sciences', 'Marketing', 'Medical', 'Other', 'Technical Degree']
JobRole_list = ['Human Resources', 'Laboratory Technician', 'Manager', 'Manufacturing Director',
                'Research Director', 'Research Scientist', 'Sales Executive', 'Sales Representative']
MaritalStatus_list = ['Married', 'Single']
BusinessTravel_list = ['Travel_Frequently', 'Travel_Rarely']
Gender_list = ['Male']
OverTime_list = ['Yes']


@HREmployee_router.post('/', response_model=dict)
async def predict_hremployee(hremployee: HREmployeeSchema):
    hremployee_dict = hremployee.dict()

    Department = hremployee_dict.pop('Department')
    Department1_0 = [1 if Department == i else 0 for i in Department_list]

    EducationField = hremployee_dict.pop('EducationField')
    EducationField1_0 = [1 if EducationField == i else 0 for i in EducationField_list]

    JobRole = hremployee_dict.pop('JobRole')
    JobRole1_0 = [1 if JobRole == i else 0 for i in JobRole_list]

    MaritalStatus = hremployee_dict.pop('MaritalStatus')
    MaritalStatus1_0 = [1 if MaritalStatus == i else 0 for i in MaritalStatus_list]

    BusinessTravel = hremployee_dict.pop('BusinessTravel')
    BusinessTravel1_0 = [1 if BusinessTravel == i else 0 for i in BusinessTravel_list]

    Gender = hremployee_dict.pop('Gender')
    Gender1_0 = [1 if Gender == i else 0 for i in Gender_list]

    OverTime = hremployee_dict.pop('OverTime')
    OverTime1_0 = [1 if OverTime == i else 0 for i in OverTime_list]

    hremployee_data = list(hremployee_dict.values()) + Department1_0 + EducationField1_0 + JobRole1_0 + MaritalStatus1_0 + BusinessTravel1_0 + Gender1_0 + OverTime1_0

    scaled_data = scaler.transform([hremployee_data])
    pred = model.predict(scaled_data)[0]
    final = 'Yes' if pred == 'Yes' else 'No'
    return {"Answer": final}
