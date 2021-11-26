python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn demo-server.main:app
