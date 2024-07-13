from pyswip import Prolog
from statement import classify


ARTICLES = ["and", "is", "the", "of", "a", "are", "an", "is", "who"]
KEYWORDS = [
    "siblings", "brother", "sister", "brothers", "sisters",
    "parent", "parents", "mother", "father",
    "grandparent", "grandmother", "grandfather",
    "child", "children", "son", "daughter", "sons", "daughters",
    "relative", "relatives", "aunt", "uncle", "cousin", "cousins"
]

segment = lambda x,y: [a for a in x if a not in y]
punct = lambda x: x[:-1]

class Statement:
    def __init__(self, relation, people=None, source=None, gender = None, question=False):
        self.relation = relation    # Involved relationship keyword/s
        self.source = source        # Source person to base relationship off
        self.people = people        # People involved in this relationship
        self.question = question	# if the statement is a question query

def question(sentence):
    try:
        k = set(sentence).intersection(KEYWORDS).pop()
    except KeyError: # catches unknown keywords
        print("Sorry, I couldn't read that. Are you sure your request is formed correctly?")
        return

    if k == "parents" or k == "children":
        s = Statement(k, sentence[:-2], source=sentence[-1], question=True)
    elif k == "siblings" or k == "relatives":
        s = Statement(k, sentence[0], source=sentence[1], question=True)
    else:
        s = Statement(k, sentence[0], source=sentence[2], question=True)
    classify(s)

def add(sentence):
    try:
        k = set(sentence).intersection(KEYWORDS).pop()
    except KeyError: # catches unknown keywords
        print("Sorry, I couldn't read that. Are you sure your request is formed correctly?")
        return

    if k == "parents" or k == "children":
        s = Statement(k, sentence[:-2], source=sentence[-1])
    elif k == "siblings" or k == "relatives":
        s = Statement(k, sentence[0], source=sentence[1])
    else:
        s = Statement(k, sentence[0], source=sentence[2])
    classify(s)

def who_question(sentence):
    try:
        k = set(sentence).intersection(KEYWORDS).pop()
    except KeyError: # catches unknown keywords
        print("Sorry, I couldn't read that. Are you sure your request is formed correctly?")
        return

    s = Statement(k, sentence[1],question=True)
    classify(s)
    
def parse(prompt):
    
    is_q = True if prompt.endswith('?') else False
    prompt = prompt.rstrip("?")
    prompt = prompt.rstrip(".")
    
    prompt = prompt.split(" ")
    
    sentence = segment(prompt, ARTICLES)
    
    try:
        if not is_q:
            add(sentence)
        
        if is_q:
            if prompt[0] == "who":
                who_question(sentence)
            else:
                question(sentence)
    except IndexError:
        print("\t Sorry, I couldn't read that. Are you sure the syntax is correct?")
        print("------------------------\n")


def main():
    
    print("Enter Message [Type 'Exit' to exit]:")

    while True:
        user = input("> ").lower()
        user = user.strip()
        user = user.replace(',','')

        if "exit" in user:
            print("\t Goodbye User...")
            break
        elif user.endswith('?') or user.endswith('.'):
            parse(user)
            
        else:
            print("\t Sorry, I couldn't read that. Did you check your punctuation marks?")
            print("------------------------\n")

if __name__ == "__main__":
    main()



