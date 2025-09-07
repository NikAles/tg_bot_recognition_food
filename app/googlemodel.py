from google import genai
from google.genai import types
import json

class Model():
  def __init__(self, proxy, api_key):
    self.http_options = types.HttpOptions(
        client_args={'proxy': f"http://{proxy}"},
        async_client_args={'proxy': f"http://{proxy}"},
    )
    self.api_key=api_key
    
  def predict(self, path_image=None, to_bytes=True, image_bytes=None):
    if to_bytes == True:
        with open(path_image, 'rb') as f:
            self.image_bytes = f.read()
    else:
       self.image_bytes = image_bytes
    
    self.client = genai.Client(api_key=self.api_key, http_options=self.http_options)

    self.prompt = ( 
    'Determine if the photo shows food. If it shows food, provide the name of the dish and the approximate average nutritional value per 100 grams.'
    'Return the answer strictly format using the following template without additional words or text, dont use markdown:'
    '{"food": "YES or NO","name": "Name of the dish in Russian","kilocalories": number,"proteins": number,"carbohydrates": number,"fats": number}'
    )
    self.ansfer = self.client.models.generate_content(
      model='gemini-2.5-flash-lite', 
      contents=[
      types.Part.from_text(text=self.prompt),
      types.Part.from_bytes(data=self.image_bytes, mime_type='image/jpeg')
    ])

    try:
      ansfer_json = json.loads(self.ansfer.text)
    except json.JSONDecodeError as e:
      print("Ошибка при декодировании JSON:", e)
      ansfer_json = None

    return ansfer_json

