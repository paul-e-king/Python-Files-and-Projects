import random as r

# A "wokese" Bullshit generator. Some of the output is anti-woke, which is
# a bug. The trick here was to output tortured English phrases, but to
# always be on-point with wokese. 

advs = ["aggressively", "vigorously", "oppressively", "humanely",
         "dutifully", "anti-oppresively", "non-disruptively",
        "intersectionally", "systemically", "multiculturally", "seen-feeling"]
nouns = ["allyships", "colorisms", "critical race theories", "cultural activism",
         "cultural appropriations", "identity politics", "oppressions",
         "microaggressions", "oppressions", "safe spaces", "tokenism",
         "white fragility", "gestational parents", "journeys", "lived experiences",
         "menstruators", "pronouns", "womxn", "Latinx", "your truth",
         "pregnant people", "laboring person", "womyn", "enbyphobia", "voices",
         "spaces", "privelege"]
adjs = ["racial", "gender-based", "race-based", "class-based", "gender binary",
        "genderqueer", "organized", "anti-speciesist", "anti-abelist",
        "non-cisheteropatriarchical", "multicultural"]
verbs = ["decolonozing", "appropriating", "demarginalizing", "anti-oppressing",
         "creating", "tokenizing", "equalizing", "problematizing", "disrupting",
         "decolorizing", "anti-gaslighting", "cancelling", "identifying",
         "marginalizing", "organizing", "virtue signalling", "cancelling",
         "identifying", "marginalizing", "organizing", "virtue signalling",
         "doing the work of", "erasing", "gaze", "un-marginalizing",
         "ways of knowing", "punching down", "queering", "platforming",
         "deplatforming"]
    
for i in range(20):
    # verb adverb adjective noun
    print(r.choice(advs), r.choice(verbs), end = " ")
    print(r.choice(adjs), r.choice(nouns))
