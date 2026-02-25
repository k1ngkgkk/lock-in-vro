#Made by @k1ngkgkk
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
    "go super saiyan",
    "go turbo",
    "go wild",
    "hustle",
    "put in work",
    "put in that work",
    "put in work for",
    "put in that work for",
    "put in work on",
    "put in that work on",
    "put in work with",
    "put in that work with",
    "put in work to",
    "put in that work to",
    "grind for",
    "grind on",
    "grind with",
    "grind to",
    "grind hard for",
    "grind hard on",
    "grind hard with",
    "grind hard to",
    "lock tf in"
    "lock the heck in",
    "lock the frick in",
    "lock the f*ck in",
    "go HARDCORE for",
    "go HARDCORE on",
    "go HARDCORE with",
    "go HARDCORE to",
    "go NUTS for",
    "go NUTS on",
    "go NUTS with",
    "go NUTS to"
]

template = [
    "You gotta {phrase} this {subject} vro.",
    "Vro, you gotta {phrase} this {subject}.",
    "You gotta {phrase} for this {subject} vro.",
    "Vro, you gotta {phrase} for this {subject}.",
    "I trust you can {phrase} this {subject} vro.",
    "I trust you can {phrase} for this {subject} vro.",
    "You better {phrase} this {subject} vro.",
    "You must {phrase} this {subject} vro.",
    "You should {phrase} this {subject} vro.",
    "You better {phrase} this {subject} vro."

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
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()

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