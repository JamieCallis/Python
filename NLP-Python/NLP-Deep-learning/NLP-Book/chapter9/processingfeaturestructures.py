# Processing feature structures

import nltk
from nltk import load_parser
# in nltk we define feature structures as follows.
fs1 = nltk.FeatStruct(PER=3, NUM='pl', GND='fem')


# we can view the structures as a kind of dictionary.
# such we can acess values by indexing in the ususal way.
print fs1['GND']

# adding to the feature structure
fs1['CASE'] = 'acc'

# We can also build more complex feature structures as follows.
fs2 = nltk.FeatStruct(POS='N', ARG=fs1)
print fs2
print fs2['ARG']
print fs2['ARG']['PER']

# feature structures are general purpose structures
# such we don't have to only use the for linguistic features.
print(nltk.FeatStruct(NAME='Lee', TELNO='01 27 86 42 96', AGE=33))

'''
    We can think of feature structures as graphs
    more specifically.

    Directed acyclic graphs (DAGs)

    Of which we would often think of such graphs
    in terms of paths through the graph. A feature path
    is a sequence of arcs that can be followed from the root node.

    Paths will be represneted as truples.

    Another point to note is we can share sub-graph points
    between different arcs. Siad to be equivalent.
    
    Such reducing the amount of repeat code.
'''

fs3 = nltk.FeatStruct("""[NAME='Lee', ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'],
                        SPOUSE=[NAME='Kim', ADDRESS->(1)]]""")
print fs3

# Subsumption and Unification

'''
    When combining feature sets they are
    partical information objects. 

    We can order features by how much
    information they contain. 

    E.g.
    
    a.		
[NUMBER = 74]

b.		
[NUMBER = 74          ]
[STREET = 'rue Pascal']

c.		
[NUMBER = 74          ]
[STREET = 'rue Pascal']
[CITY = 'Paris'       ]

This ordering is called subsumption.

b subsumes a, and c subsumes b. Such that
if all the information in a feature set is
contained within another featureset. 

It is consumed by the featureset. Such
to not repeat information.
'''

# Unification 

fs1 = nltk.FeatStruct(NUMBER=74, STREET='rue Pascal')
fs2 = nltk.FeatStruct(CITY='Paris')
print fs1.unify(fs2)

'''
    Unification is the process of joining
    two feature sets together. 

    It create a Union between the two 
    feature sets such as.

    FS0 u FS1 = FS1 u FS0

    If we unify two feature structures which
    stand in the subsumption relationship,
    then the result of unification is the most
    informative of the two.

    Aka. The one with the largest amount
    of data.

    Unification process will fail if the
    two feature structures share the same
    path but the values are atomically distinct.
'''

# Looking at hw unification interacts with
# structure sharing.

fs0 = nltk.FeatStruct("""[NAME=Lee,
                           ADDRESS=[NUMBER=74,
                                    STREET='rue Pascal'],
                           SPOUSE= [NAME=Kim,
                                    ADDRESS=[NUMBER=74,
                                             STREET='rue Pascal']]]""")

print fs0

# lets say we want to add a city feature for kim's address
fs1 = nltk.FeatStruct("[SPOUSE = [ADDRESS = [CITY = Paris]]]")
print fs1.unify(fs0)

# can be noted that fs1 had to take the entire
# fs0 feature structure.

# if we create a new feature adding in 
# address sharing
fs2 = nltk.FeatStruct("""[NAME=Lee, ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'],
                           SPOUSE=[NAME=Kim, ADDRESS->(1)]]""")
print fs1.unify(fs2)

# we see that the address category adds city
# as an attribute.

# Since we can express features sets with variables
fs1 = nltk.FeatStruct("[ADDRESS1=[NUMBER=74, STREET='rue Pascal']]")
fs2 = nltk.FeatStruct("[ADDRESS1=?x, ADDRESS2=?x]")
print fs2
print fs2.unify(fs1) # shall build the relationship between address 2 and 1
# giving them the attributes of number and street.


# X-Bar Syntax - Heads Revisited

'''
    Is a method of abstracting out the
    notion of 'phrasal level'. 

    Normally represents three levels

    such that if N represents the lexical
    level, then N' represents the next
    level up, sorresponding to the more
    transitional category NOM.

    While N'' represnts the phrasal level
    corresponding to the category NP.

    S           -> N[BAR=2] V[BAR=2]
    N[BAR=2]    -> Det N[BAR=1]
    N[BAR=1]    -> N[BAR=1] P[BAR=2]
    N[BAR=1]    -> N[BAR=0] P[BAR=2]
    N[BAR=1]    -> N[BAR=0]XS
'''








