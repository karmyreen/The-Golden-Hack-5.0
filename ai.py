import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a video game character giving tips on how to improve personal hygiene."},
    {"role": "user", "content": "Give the user 3 short tips in point form on how to improve personal hygiene. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer."},
  ]
)

response = str(completion.choices[0].message)
# Extract the content from the string
content = response.split(":")[2].strip()[1:-2]

# Split the content into a list of strings based on the \n character
tips = content.split("\\n")

# Extract the points and tips from each string using a list comprehension
points_and_tips = [tip.strip() for tip in tips if tip]

# Print the points and tips
for point_and_tip in points_and_tips:
    point, tip = point_and_tip.split(".", 1)
    print(f"{point.strip()}. {tip.strip()}")