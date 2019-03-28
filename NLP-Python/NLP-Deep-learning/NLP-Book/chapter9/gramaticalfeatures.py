import nltk

# feature structures
kim = {'CAT': 'NP', 'ORTH': 'Kim', 'REF': 'k'}
chase = {'CAT': 'V', 'ORTH': 'chased', 'REL': 'chase'}

chase['AGT'] = 'sbj'
chase['PAT'] = 'obj'

'''
    We want to "bind" the verb's agent role
    to the subject and the patient role to
    the object.

    We can do this by assuming that NPs
    immediately to the left and right of 
    the verb are the subject and object
    respectively.
'''

sent = "Kim chased Lee"
tokens = sent.split()
lee = {'CAT': 'NP', 'ORTH': 'Lee', 'REF': '1'}

def lex2fs(word):
    for fs in [kim, lee, chase]:
        if fs['ORTH'] == word:
            return fs

subj, verb, obj = lex2fs(tokens[0]), lex2fs(tokens[1]), lex2fs(tokens[2])
verb['AGT'] = subj['REF']
verb['PAT'] = obj['REF']

for k in ['ORTH', 'REL', 'AGT', 'PAT']:
    print("%-5s => %s" % (k, verb[k]))

'''
    We can apply the same approach
    to as many different verbs as we want 
    too.

    E.g. surprise
'''

surprise = {'CAT': 'V', 'ORTH': 'surprised', 'REL': 'surprise',
           'SRC': 'sbj', 'EXP': 'obj'}


'''
Agreement Paradigm for English Regular Verbs
                Singular        Plural
1st person      I run           We run
2nd person      you run         you run
3rd person      he/she/it runs  they run

We use "3" for 3rd person, "SG" for singular
and "PL" for plural.
'''

grammar = nltk.CFG.fromstring("""
    S       -> NP_SG VP_SG
    S       -> NP_PL VP_PL
    NP_SG   -> Det_SG N_SG
    NP_PL   -> Det_PL N_PL
    VP_SG   -> V_SG
    VP_PL   -> V_PL

    Det_SG  -> 'this'
    Det_PL  -> 'these'
    N_SG    -> 'dog'
    N_PL    -> 'dogs'
    V_SG    -> 'runs'
    V_PL    -> 'run'
""")

# But using this approach would mean blowing
# up the dataset by a factor of 6. In order
# to cover all of the posabilities. 

# Using Attributes and Constraints

grammar1 = nltk.CFG.fromstring("""
    N[NUM=pl]

    DET[NUM=sg] ->  'this'
    DET[NUM=pl] ->  'these'

    N[NUM=sg]   ->  'dog'
    N[NUM=pl]   ->  'dogs'
    V[NUM=sg]   ->  'runs
    V[NUM=pl]   ->  'run'
""")

# This is forced the English person context
# rules. 

# But we can take this a set up again using
# variables.
# forces the NP and VP to take the same rule.
# Since you have to have both as singular, or plural.
# In the event that the rule isn't met the result will be an fail.

grammar2 = nltk.CFG.fromstring("""
    S           ->  NP[NUM=?n]  VP[NUM=?n]
    NP[NUM=?n]  ->  Det[NUM=?n] N[NUM=?n]
    VP[NUM=?n]  ->  V[NUM=?n]
""")

'''
    Features such as values like sg and pl. Are called
    atomic.

    We can also get boolean values such as 'auxiliary verbs'
    such as can, may, will, do. 

    The following classifies as true / false
    V[TENSE=pres, +AUX] -> 'can'
    V[TENSE=pres, +AUX] -> 'may'

    V[TENSE=pres, -AUX] -> 'walks'
    V[TENSE=pres, -AUX] -> 'likes'
'''

# Nested feature structures

'''
    In addition to atomic-valued features, features may
    take values that are themsleves feature structures.

    We can create groups of categories such as:-

    [POS = N           ]
    [                  ]
    [AGR = [PER = 3   ]]
    [      [NUM = pl  ]]
    [      [GND = fem ]]
    
    - Order is not specific.

    Grouped together as AGR. We say that AGR has a complex value.

    Depicts the structure, in a format known as an attribute 
    value matrix (AVM).
'''



