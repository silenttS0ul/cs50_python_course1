
emotion = "v.v"

def main():
    global emotion
    say("is anyone here")
    emotion = ":D"
    say("Oh Hi!!")


def say(text):
    print(text + " " + emotion)


main()


