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
response = response.replace('\n', '')  # Remove the \n characters
tips = response.split('.')  # Split the response into a list of strings based on the . character
tip1, tip2, tip3 = [tip.strip() for tip in tips if tip]  # Remove leading/trailing whitespace and assign to variables

print(tip1)
print(tip2)
print(tip3)