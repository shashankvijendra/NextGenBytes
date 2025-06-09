import requests
# from deepai import DeepAI

api_key = "84be4446-b39d-4552-8ed5-2eb03d15f1ae"
response = requests.post(
    "https://api.deepai.org/api/text2img",
    data={"text": "A handsome man with wavy black hair, wearing a black suit with a white shirt and striped tie, holding a red rose"},
    headers={"api-key": api_key}
)

print(response.json())
