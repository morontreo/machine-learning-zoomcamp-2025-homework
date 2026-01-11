import pickle
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel, Field

class StudentMetrics(BaseModel):
    marital_status: int
    application_mode: int
    application_order: int
    course: int
    daytime_evening_attendance: int
    previous_qualification: int
    nationality: int
    mother_qualification: int
    father_qualification: int
    mother_occupation: int
    father_occupation: int
    displaced: int
    educational_special_needs: int
    debtor: int
    tuition_fees_up_to_date: int
    gender: int
    scholarship_holder: int
    age_at_enrollment: int
    international: int
    curricular_units_1st_sem_credited: int
    curricular_units_1st_sem_enrolled: int
    curricular_units_1st_sem_evaluations: int
    curricular_units_1st_sem_approved: int
    curricular_units_1st_sem_grade: float
    curricular_units_1st_sem_without_evaluations: int
    curricular_units_2nd_sem_credited: int
    curricular_units_2nd_sem_enrolled: int
    curricular_units_2nd_sem_evaluations: int
    curricular_units_2nd_sem_approved: int
    curricular_units_2nd_sem_grade: float
    curricular_units_2nd_sem_without_evaluations: int
    unemployment_rate: float
    inflation_rate: float
    gdp: float

class PredictResponse(BaseModel):
    student_graduate_probability: float
    student_graduate: bool

app = FastAPI(title="student-graduate-prediction")

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(studentMetrics):
    result = pipeline.predict_proba(studentMetrics)[0, 1]
    return float(result)

@app.post("/predict")
def predict(studentMetrics: StudentMetrics) -> PredictResponse:
    prob = predict_single(studentMetrics.model_dump())

    return PredictResponse(
        student_graduate_probability=prob,
        student_graduate=prob >= 0.60
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)