# Energy Regression Dockerized App

This is a demo Flask application that loads a saved regression model (`energy_model.pkl`) and provides a web UI to predict household appliances energy consumption.

## Quick start (local)

1. Create and activate a Python virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
flask run
```

Open http://127.0.0.1:5000 in your browser.

## Run with Docker

1. Build the image:
```bash
docker build -t energy-app .
```

2. Run the container:
```bash
docker run -p 5000:5000 energy-app
```

Then open http://localhost:5000

## Notes

- Replace `energy_model.pkl` with your trained regression model that accepts 5 features in the order: `T1, RH_1, T_out, Windspeed, lights`.
- For production deployment, consider using Gunicorn and reverse proxy (e.g., Nginx), and add input validation & preprocessing similar to what you used during model training.
