import requests
import pandas as pd
from io import BytesIO

url = "http://localhost:8000/api/export_app"
params = {"app": "questionnaire"}
headers = {
    "Authorization": "Token YOUR_API_TOKEN"
}

r = requests.get(url, params=params, headers=headers)
print(f"URL requested: {r.url}")
r.raise_for_status()

df = pd.read_csv(BytesIO(r.content))

with open("questionnaire.csv", "wb") as f:
    f.write(r.content)
    
