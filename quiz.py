import random
from ai import generate_ai
import pygame
from loader import read_settings

#REAL TIPS (3 FOR QUIZ)
toothbrush_example1, toothbrush_example2, toothbrush_example3 = generate_ai("You are a video game character giving tips on how to brush your teeth effectively.", "Give the user 3 short tips in point form on how to brush their teeth effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
laundry_example1, laundry_example2, laundry_example3 = generate_ai("You are a video game character giving tips on how to do laundry effectively.", "Give the user 3 short tips in point form on how to do their laundry more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
handwashing_example1, handwashing_example2, handwashing_example3 = generate_ai("You are a video game character giving tips on how to wash hands effectively.", "Give the user 3 short tips in point form on how to wash hands effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")

toothbrush_tips = [toothbrush_example1, toothbrush_example2, toothbrush_example3]
laundry_tips = [laundry_example1, laundry_example2, laundry_example3]
handwashing_tips = [handwashing_example1, handwashing_example2, handwashing_example3]

#FALSE TIPS (3 FOR QUIZ)
false_toothbrush_tip1, false_toothbrush_tip2, false_toothbrush_tip3 = generate_ai("You are a video game character giving obviously false tips on how to brush their teeth effectively.", "Give the user 3 short obviously false tips in point form on how to brush their teeth more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
false_laundry_tip1, false_laundry_tip2, false_laundry_tip3 = generate_ai("You are a video game character giving obviously false tips on how to do laundry effectively.", "Give the user 3 short obviously false tips in point form on how to do their laundry more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
false_handwashing_tip1, false_handwashing_tip2, false_handwashing_tip3 = generate_ai("You are a video game character giving obviously false tips on how to wash hands effectively.", "Give the user 3 short obviously false tips in point form on how to wash hands more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")

false_toothbrush_tips = [false_toothbrush_tip1, false_toothbrush_tip2, false_toothbrush_tip3]
false_laundry_tips = [false_laundry_tip1, false_laundry_tip2, false_laundry_tip3]
false_handwashing_tips = [false_handwashing_tip1, false_handwashing_tip2, false_handwashing_tip3]


random_toothbrush_tip = random.choice(toothbrush_tips)
random_laundry_tip = random.choice(laundry_tips)
random_deoderant_tip = random.choice(handwashing_tips)

random_false_toothbrush_tip = random.choice(false_toothbrush_tips)
random_laundry_tip = random.choice(false_laundry_tips)
random_deoderant_tip = random.choice(false_handwashing_tips)



