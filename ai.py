import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai(role, content):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": role},
      {"role": "user", "content": content},
    ]
  )

  response = str(completion.choices[0].message)
  # Extract the content from the string
  content = response.split(":")[2].strip()[1:-2]

  # Split the content into a list of strings based on the \n character
  tips = content.split("\\n")

  # Extract the points and tips from each string using a list comprehension
  points_and_tips = [tip.strip().split(".", 1) for tip in tips if tip]

  # Store each point and tip in their own variable using tuple unpacking
  point1, tip1 = points_and_tips[0]
  point2, tip2 = points_and_tips[1]
  point3, tip3 = points_and_tips[2]

  # Print the points and tips
  final_pt1 = (point1 + "." + tip1)
  print(final_pt1)
  final_pt2 = (point2 + "." + tip2)
  print(final_pt2)
  final_pt3 = (point3 + "." + tip3)
  print(final_pt3)

  return final_pt1, final_pt2, final_pt3

ai_example = generate_ai("You are a video game character giving tips on how to brush your teeth effectively.", "Give the user 3 short tips in point form on how to brush their teeth more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
print(ai_example)