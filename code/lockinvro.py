import random
import requests
from flask import Flask, request, send_file, render_template_string
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

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

template = [
    "You gotta {phrase} this {subject} vro.",
    "Vro, you gotta {phrase} this {subject}.",
    "You gotta {phrase} for this {subject} vro.",
    "Vro, you gotta {phrase} for this {subject}.",
    "I trust you can {phrase} this {subject} vro."
]

def lockinvro(subject):
    phrase = random.choice(word)
    tmp = random.choice(template)
    return tmp.format(phrase=phrase, subject=subject)

HTML = """
<!doctype html>
<title>Lock In Vro</title>
<h2>What u studying for vro?</h2>
<form method="post">
  <input type="text" name="subject">
  <button type="submit">Generate</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        subject = request.form["subject"]
        text = lockinvro(subject)

        imgUrl = "https://picsum.photos/1080"
        response = requests.get(imgUrl)
        img = Image.open(BytesIO(response.content)).convert("RGB")

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 40)

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (img.width - text_width) / 2
        y = (img.height - text_height) / 2

        draw.text((x, y), text, font=font, fill="white")

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        return send_file(buffer, mimetype="image/png")

    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)