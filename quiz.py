from minigames import toothbrush_example1, toothbrush_example2, toothbrush_example3, laundry_example1, laundry_example2, laundry_example3, deoderant_example1, deoderant_example2, deoderant_example3
import random
from ai import generate_ai

# get a random toothbrush tip, laundry tip, and deoderant tip for a total of 3 tips
toothbrush_tips = [toothbrush_example1, toothbrush_example2, toothbrush_example3]
laundry_tips = [laundry_example1, laundry_example2, laundry_example3]
deoderant_tips = [deoderant_example1, deoderant_example2, deoderant_example3]
random_toothbrush_tip = random.choice(toothbrush_tips)
random_laundry_tip = random.choice(laundry_tips)
random_deoderant_tip = random.choice(deoderant_tips)

false_tip_1 = generate_ai("You are a video game character false giving tips on how to do laundry effectively (ie. giving pretty obviously fake tips).", "Give the user 3 short false tips in point form on how to do their laundry more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")