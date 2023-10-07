import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a video game character giving tips on how to improve personal hygiene."},
    {"role": "user", "content": "Give the user 3 short tips in point form on how to improve personal hygiene. Don't include backslash n for new lines in the answer."},
  ]
)

response = completion.choices[0].message
print(response)