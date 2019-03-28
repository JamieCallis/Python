import nltk
from nltk.corpus import gutenberg, treebank, ppattach
from collections import defaultdict

groucho_grammar = nltk.CFG.fromstring("""
    S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'an' | 'my'
    N -> 'elephant' | 'pajamas'
    V -> 'shot'
    P -> 'in'
""")

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    print(tree)

'''
    Consituent structure is based on the
    observation that words combine with 
    other words to form units.

    NP -> Noun phrase
    VP -> Verb phrase
    PP -> prepositional phrase

    Each node in a tree is called a
    'consituent'. 
'''

grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)

sent = "Mary saw Bob".split()

rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print tree

'''
    When using a CFGs for parsing in NLTK. You cannot combine
    grammatical categories with lexical items on the righthand
    side of the same production. 

    E.g. PP -> 'of' NP is disallowed

    Not premitted to place multi-word lexical itmes on the right
    hand side.

    E.g. NP -> 'New York' is disallowed 
         NP -> 'New_York'   is allowed
'''

# recursion in Syntactic structures

grammar2 = nltk.CFG.fromstring("""
  S  -> NP VP
  NP -> Det Nom | PropN
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'the' | 'a'
  N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
  Adj  -> 'angry' | 'frightened' |  'little' | 'tall'
  V ->  'chased'  | 'saw' | 'said' | 'thought' | 'was' | 'put'
  P -> 'on'
  """)

sent = "the angry bear chased the frightened little squirrel".split()

rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sent):
    print tree

''' 
    A grammar is siad to be recursive if a category occuring
    on the let hand side of a production also appears on the
    righthand side of a production.

    E.G. Nom -> Adj Nom (Direct recursion)

    Indirect recursion on S arises from the combination of
    two productions.

    E.G. S -> NP VP and VP -> V S (Indirect recusions)
'''

# RecursiveDescentParsers() has an optional
# paramteter trace. Reports the steps taken.

rd_parser = nltk.RecursiveDescentParser(grammar1, trace=2)
sent = 'Mary saw a dog'.split()
for tree in rd_parser.parse(sent):
    print tree

# Dpendencies and Dependency Grammar

'''
  Sentences are broken down into head's (the parent)
  with dependents (this children).

  The head of a sentence is usually taken to
  be the tensed verb, and every other word
  is either dependent on the sentence head
  or connects to it through as path of
  depdencies.
''' 

groucho_dep_grammar = nltk.DependencyGrammar.fromstring("""
  'shot' -> 'I' | 'elephant'| 'in'
  'elephant' -> 'an' | 'in'
  'in' -> 'pajamas'
  'pajamas' -> 'my'
""")

print(groucho_dep_grammar)

'''
  A dependency graphic is projective if,
  when all teh words written for the sentence
  are in linear order.

  Such at an eddge can be drawn above the words
  without crossing.
'''

pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = 'I shot an elephant in my pajamas'.split()
trees = pdp.parse(sent)
for tree in trees:
  print(tree)

# Valency and the Lexicon

'''
  The following are known as completements
  of the respective verbs

  VP -> V Adj was
  VP -> V Np saw
  VP -> V S thought
  VP -> V NP PP put

  such that the words on the rightmost can
  only occur if the Verb phrase matches the
  given pattern.

  If multiple words are subcategorized such
  as transitive verbs e.g. chased and saw.

  We can do the following

  VP -> TV NP
  TV -> 'chased' | 'saw'

  other  subcategories are:-

  Symbol  Meaning             Example
  IV      intransitive verb   barked
  DatV    dative verb         gave a dog to a man
  SV      sentential verb     said that a dog barked
'''


# Working with corpuses
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
print(t)

# we can use the data too build up grammar.
def filter(tree):
  child_nodes = [child.label() for child in tree
                if isinstance(child, nltk.Tree)]
  return (tree.label() == 'VP') and ('S' in child_nodes)

print [subtree for tree in treebank.parsed_sents()
          for subtree in tree.subtrees(filter)]

# mining another corpus for finding pairs of
# prepositional phrases, where the preposition and
# noun are fixed. But verb determines is it's attached to a
# VP or to the NP.

entries = nltk.corpus.ppattach.attachments('training')
table = defaultdict(lambda: defaultdict(set))
for entry in entries:
  key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
  table[key][entry.attachment].add(entry.verb)


for key in sorted(table):
  if len(table[key]) > 1:
    print(key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V']))

# weighted grammar

def give(t):
    return t.label() == 'VP' and len(t) > 2 and t[1].label() == 'NP'\
           and (t[2].label() == 'PP-DTV' or t[2].label() == 'NP')\
           and ('give' in t[0].leaves() or 'gave' in t[0].leaves())
def sent(t):
    return ' '.join(token for token in t.leaves() if token[0] not in '*-0')
def print_node(t, width):
        output = "%s %s: %s / %s: %s" %\
            (sent(t[0]), t[1].label(), sent(t[1]), t[2].label(), sent(t[2]))
        if len(output) > width:
            output = output[:width] + "..."
        print(output)
 	
for tree in nltk.corpus.treebank.parsed_sents():
     for t in tree.subtrees(give):
        print_node(t, 72)

# probabilistic context free grammar
grammar = nltk.PCFG.fromstring("""
    S    -> NP VP              [1.0]
    VP   -> TV NP              [0.4]
    VP   -> IV                 [0.3]
    VP   -> DatV NP NP         [0.3]
    TV   -> 'saw'              [1.0]
    IV   -> 'ate'              [1.0]
    DatV -> 'gave'             [1.0]
    NP   -> 'telescopes'       [0.8]
    NP   -> 'Jack'             [0.2]
""")

print(grammar)

viterbi_parser = nltk.ViterbiParser(grammar)
for tree in viterbi_parser.parse(['Jack', 'saw', 'telescopes']):
  print(tree)