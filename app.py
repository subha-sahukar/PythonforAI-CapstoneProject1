from fastapi import FastAPI
from pydantic import BaseModel
from retro_analyzer import analyze_feedback

app = FastAPI()

class FeedbackInput(BaseModel):
    feedback: list[str]

@app.post("/analyze")
def analyze_sprint_feedback(data: FeedbackInput):
    themes = analyze_feedback(data.feedback)
    return {"themes": themes}