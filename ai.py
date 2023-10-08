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
  #print(final_pt1)
  final_pt2 = (point2 + "." + tip2)
  #print(final_pt2)
  final_pt3 = (point3 + "." + tip3)
  #print(final_pt3)

  return final_pt1, final_pt2, final_pt3

toothbrush_example1, toothbrush_example2, toothbrush_example3 = generate_ai("You are a video game character giving tips on how to brush your teeth effectively.", "Give the user 3 short tips in point form on how to brush their teeth effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
print(toothbrush_example1 + "\n" + toothbrush_example2 + "\n" + toothbrush_example3)

laundry_example1, laundry_example2, laundry_example3 = generate_ai("You are a video game character giving tips on how to do laundry effectively.", "Give the user 3 short tips in point form on how to do their laundry more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
print(laundry_example1 + "\n" + laundry_example2 + "\n" + laundry_example3)

deoderant_example1, deoderant_example2, deoderant_example3 = generate_ai("You are a video game character giving tips on how to wash hands effectively.", "Give the user 3 short tips in point form on how to wash hands effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
print(deoderant_example1 + "\n" + deoderant_example2 + "\n" + deoderant_example3)

# get a random toothbrush tip, laundry tip, and hand washing tip for a total of 3 tips