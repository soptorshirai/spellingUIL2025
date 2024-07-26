import random
import webbrowser
import time

lines = []
word_list = []
amount = 400
red = "\033[0;31m"
green = "\033[0;32m"
reset = "\033[0m"


def openURL(word):
  url = f"https://www.ahdictionary.com/application/resources/wavs/{word[:8]}.wav"
  try:
    webbrowser.open(url)
    print(url)
  except Exception as e:
    print("Failed to open the URL:", e)
  if (len(word) > 8):
    if (word[10] == "-"):
      correction = "end"
    else:
      correction = "beginning"
    print(red + "\nNext Word's Correction (add this to the " + correction +
          "): " + word[9:] + reset)


def checkAns(num):
  openURL(lines[num])
  user = input()
  user_parts = user.split(', ')
  correct_spellings = word_list[num].split(', ')
  if (len(correct_spellings) > 1):
    correct = any(part.strip() in correct_spellings for part in user_parts)
    if correct:
      print(green + "Correct!" + reset)
      print("Answers that would work: " + word_list[num] + "\n")
    else:
      print(red + "Incorrect :(\n" + reset + "Correct answer is " +
            ', '.join(correct_spellings) + "\n\n")
      time.sleep(3)
  else:
    if (user == word_list[num]):
      print(green + "Correct!\n" + reset)
    else:
      print(red + "Incorrect :(" + reset)
      print("Correct answer is " + word_list[num] + "\n\n")
      time.sleep(3)


with open("words.txt", "r") as file:
  for line in file:
    lines.append(line.strip())
# print(lines)

with open("spellings.txt", "r") as file:
  for liney in file:
    parts = liney.strip().split(' ', 1)
    if len(parts) > 1:
      word = parts[1].strip(' •')
      if word:
        word_list.append(word)

start = int(
    input("Which numbered word do you want to start with?(Enter a number) "))
end = int(
    input("Which numbered word do you want to end with?(Enter a number) "))
print("")

if (start < 0):
  start = 0
if (start > amount):
  start = amount
if (end > amount):
  end = amount - 1
if (end < 0):
  end = 1
if (end <= start):
  end = start + 1

mode = int(input("Random or ordered? Answer as 1 or 2, respectively: "))

print("\n")
if (mode == 1):
  while (True):
    random_index = random.randint(start - 1, end - 1)
    # openURL(lines[random_index])
    try:
      checkAns(random_index)
    except Exception as e:
      continue

if (mode == 2):
  for i in range(start - 1, end):
    try:
      checkAns(i)
    except Exception as e:
      continue
