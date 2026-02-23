import random

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
    "seama":
]

template = ["You gotta {phrase} this {subject} vro."]

def lockinvro(subject):
    phrase = random.choice(word)
    tmp = random.choice(template)
    print(tmp.format(phrase=phrase, subject=subject))

if __name__ == "__main__":
    test = str(input("What u studying for vro? : "))
    lockinvro(test)