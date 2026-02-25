import random
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

word = [
    "grind",
    "lock in for",
    "channelise those vibes",
    "channel them brainwaves",
    "go ballistic",
    "go ham",
    "go hard",
    "go off",
    "go savage"
]

imgUrl = "https://picsum.photos/1080"
response = requests.get(imgUrl)
img = Image.open(BytesIO(response.content)).convert("RGB")


template = ["You gotta {phrase} this {subject} vro.",
            "Vro, you gotta {phrase} this {subject}.",
            "You gotta {phrase} for this {subject} vro.",
            "Vro, you gotta {phrase} for this {subject}.",
            "I trust you can {phrase} this {subject} vro."]

def lockinvro(subject):
    phrase = random.choice(word)
    tmp = random.choice(template)
    return(tmp.format(phrase=phrase, subject=subject))

if __name__ == "__main__":
    test = str(input("What u studying for vro? : "))
    text = lockinvro(test)

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 40)
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (img.width - text_width) / 2
y = (img.height - text_height) / 2
draw.text((x, y), text, font=font, fill="white")
img.show()