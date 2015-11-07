rules[] //array of the initial rules
usedrules[] //array of the rules that are already used during an 

class LogicalSegment(object):
    
    def __init__(left,right):
        self.left = left
        self.right = right

def create_laws()
    rules.append(LogicalSegment("person(Frank)",NULL)
    rules.append(LogicalSegment("person(John)",NULL)
    rules.append(LogicalSegment("person(Cindy)",NULL)
    rules.append(LogicalSegment("person(Julie)",NULL)
    rules.append(LogicalSegment("playsGuitar(John)",NULL)
    rules.append(LogicalSegment("playsGuitar(Julie)",NULL)
    rules.append(LogicalSegment("playsGuitar(Frank)",NULL)
    rules.append(LogicalSegment("married(Frank,Julie)",NULL)
    rules.append(LogicalSegment("married(Julie,Frank)",NULL)
    rules.append(LogicalSegment("person(x) ^ playsGuitar(x) ^ !hasCar(x)","isKid(x)")
    rules.append(LogicalSegment("person(x) ^ ageRetire(x,z)","AARPmember(x)")
    rules.append(LogicalSegment("person(x) ^ playsGuitar(x)","takesLessons(x)")
    rules.append(LogicalSegment("person(x) ^ AARPmember(x) v takesLessons(x)","paysFees(x)")
    rules.append(LogicalSegment("person(x) ^ ageYoung(x,z)","isPoor(x)")
    rules.append(LogicalSegment("person(x) ^ AARPmember(x) ^ hasCar(x)","hasInsuranceDiscount(x)")
    rules.append(LogicalSegment("person(x) ^ person(y) ^ playsGuitar(x) ^ playsGuitar(y) ^ married(x,y)","playsDuets(x,y)")
    rules.append(LogicalSegment("person(x) ^ person(y) ^ playsDuets(x,y) ^ !isPoor(x), hasInsuranceDiscount(x), married(x,y)","hasItMade(x,y)")


//Rules missing from this list are the ones that deal with inequality. Not sure how to go about this without using a method.

def ageRetire(y)
    is y larger than 60?
    if so return true, otherwise return false

def ageYoung(y)
    is y smaller than 26?
    is so return true, otherwise return false

def ageKid(y)
    is y smaller than 20?
    if so return true, otherwise return false

def algorithm(query)

    loop through the query
    on iteration, we take the logical sentence and examine it:
    investigate the object CURRENTLY iterated by its righthand side. Parsing through the string, see if it matches the query or NEWLY FORMED SENTENCE FROM BEFORE by its lefthand side. 
    If not, move on to the next object statement in the list
    The moment that we find a match, COMBINE the two sentences and form a new one, while temporarily removing the sentence from the list we used (NOT the query, or further combined sentences)
    If we cannot find a match, this will make the query return a false altogether

    Bear in mind we have special cases. When a sentence in the list has a NULL righthand side(i.e. if object.right == NULL), this means it is a
    statement like person(John), which would return a true. So when we reach a sentence that has a null rightside,
    we compare it to the lefthand side of the current, NEW statement formed and see if it matches. We then create
    a new sentence that removes said match from the old sentence
    -->This will also lead to a T -> F eventually, like the lawyer problem.

    Once T -> F is attained as the new sentence, we can return a true. Otherwise return false.


def main()
    
    Here, we will prompt the computer to decipher some queries for each person.
    Make sure to keep it slow for demonstration. Show how sentences are formed

    create_laws()

    algorithm("person(Frank)") --> returns whether it is true or not (obviously this would return true)
    algorithm("isKid(Frank)") --> returns whether this is true or not
    ...
    
    do it for all people present
