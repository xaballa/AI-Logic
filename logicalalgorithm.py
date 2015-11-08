when we tell the program to run a query: first get the string
then create an object --> LogicalSegment("isPoor(x)",NULL)
feed this into the algorithm below

We'll have person(x) in other rules, so how to feed the variable in?
-->We know to that we have a matching segment when we find something like "person(" which indicates there is indeed a 

match. However, we must make sure that this iterated statement actually contains the name that we tossed in. So 

compare the characters directly after "person(" and that it matches the name tossed into the algorithm.

def algorithm(queryobject,name1,name2) //for the married situation?
-->anytime we must prove that they are both a person, the algorithm will have the program iterate to a rule in the 

list that corresponds to the people. We cannot remove them at the same time, but only when the algorithm iterates to 

the corresponding truth in the initial table. For example, in one turn we can get rid of Frank using person(x), so 

that segment disappears when creating the new query. And then when we iterate again, we'll eventually come across 

person(Julie), and can get rid of that segment when creating a newer query.

def algorithm(queryobject,name)

    currentsource = queryobject
    rules = iteratedrules[]
    
    for elem in (iteratedrules):
        index = iteratedrules.index(elem)
        if(elem.RHS != NULL):
            if( string in LHS of query matches one on the RHS of iterated statement ):
                currentsource = LogicalSegment(elem.LHS,currentsource.RHS)
                iteratedrules.pop(index)
        else: //if the RHS is NULL and thus a truth function. BUT we must make sure this actually makes sense
            if( string in LHS of query matches one on the LHS of iterated statement ):
                if( string after the ( is equal to the name tossed in ):
                    stringobject = parse LHS string to remove the matched segment
                               //its removal is equivalent to appearing as a truth (T ^ blah() -> F)

        if(elem.LHS = "") //check if we've reached that T -> F
            return true

        if( reaching the end of the iteratedrules[] list )
            return false
            
