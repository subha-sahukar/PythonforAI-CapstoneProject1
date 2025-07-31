# 🧠 Sprint Retrospective AI Analyzer

This project is an AI-powered assistant that clusters and summarizes retrospective feedback from Agile teams. It enables TPMs and Engineering Leaders to extract themes, blockers, and wins — automatically.

## 📌 Features
- Clusters raw sprint feedback into meaningful themes
- Available as FastAPI REST API and Streamlit demo app
- Easy to deploy on Render, Hugging Face, or Streamlit Cloud

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

Then POST feedback list to `/analyze` endpoint.

## 🌐 Streamlit

```bash
streamlit run streamlit_app.py
```

## 🐳 Docker

```bash
docker build -t sprint-retro-ai .
docker run -p 10000:10000 sprint-retro-ai
```

## 🧪 CI/CD

GitHub Actions automatically validates core analyzer logic on update.

## 🧭 TPM-AI Impact

| Impact Area        | Implementation |
|--------------------|----------------|
| Spot AI Use Cases  | NLP clustering of retrospective feedback |
| Data Hooks         | Google Forms / Confluence / Slack → FastAPI |
| Measurable Outcomes| Thematic summary in seconds vs hours |

---