import random

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that",
              "Can you explain why ")

replacements = {"I": "you","me":"you", "my":"your",
                "we":"you", "us":"you", "mine": "yours"}

def reply(sentence):
    """Builds and returns a reply to the sentence."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
        """Replaces first person prunouns with second person
        prunouns."""
        word = sentence.split()
        replyWords = []
        replyWords.append(replacements.get(word, word))
        return " ".join('replyWords')

        def main():
            """Handles the interaction bewteen patient and doctor."""
        print("Good morning, I hope you are well today.")
        print("What can i do for you?")
        while true:
            sentence = input("\n>> ")
            if sentence.upper() =="QUIT":
                print("Have a nice day!")
                break
        print(reply(sentence))
    # The entry point for program execution
        var = if__name__ == "_main:"
        _
        main()