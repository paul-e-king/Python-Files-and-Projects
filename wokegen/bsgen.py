import random as r

verbs = []
nouns = []
adjs = []
advs = []

files = ["verbs.txt", "adjectives.txt", "nouns.txt", "adverbs.txt"]

for f in files:
    fh = open(f, "r")
    for w in fh:
        if (f == "verbs.txt"):
            verbs.append(w.strip())
        elif (f == "adjectives.txt"):
            adjs.append(w.strip())
        elif (f == "nouns.txt"):
            nouns.append(w.strip())
        else:
            advs.append(w.strip())
    fh.close()
    
for i in range(20):
    # verb adverb adjective noun
    print(r.choice(advs), r.choice(verbs), end = " ")
    print(r.choice(adjs), r.choice(nouns))