# AI-Logic

####Psuedo Prolog
```
person(Frank)
person(John)
person(Cindy)
person(Julie)

playsGuitar(John)
playsGuitar(Julie)
playsguitar(Frank)

hasCar(Frank)
hasCar(Julie)

age(John, 18)
age(Julie, 26)
age(Cindy, 101)
age(Frank, 61)

married(Frank, Julie)
married(Julie, Frank)

//, = AND
//; = OR

AARPmember(x) :-
    person(x),
    age(x, y),
    y > 60.
    
takesLessons(x) :-
    person(x), 
    playsGuitar(x).
    
paysFees(x) :-
    person(x),
    AARPmember(x);   
    takesLessons(x).
    
isPoor(x) :-
    person(x),
    paysFees(x),
    age(x) < 25.
    
hasInsuranceDiscount(x) :-
    person(x),
    AARPmember(x),
    hasCar(x).
    
isKid(x) :-
    person(x),
    playsGuitar(x),
    age(x) <20,
    not(hasCar(x).
    
playsDuets(x) :-
    person(x),
    person(y),
    playsGuitar(x),
    playsGuitar(y),
    married(x, y).
    
hasItMade(x) :-
  person(x),
  person(y),
  playsDuets(x),
  not(isPoor(x)),
  hasInsuranceDiscount(y), 
  married(x, y).
  
```












### So this sucked.  Sorry :/
Every person orders a meal, drink and has a cost.

1. Zachary didn't order the spaghetti.
2. Of Zachary and the diner who paid $9.99, one had the water and the other had the iced tea.
3. Zachary, the diner who ordered the turkey plate, the one who got the lemonade, the diner who paid $9.99, the diner who paid $6.99 and the diner who ordered the hamburger were all different diners.
4. The diner who paid $8.99 didn't have the water.
5. Tracy paid 1 dollar more than Irene.
6. The one who got the lemonade paid more than the diner who ordered the sloppy joe.
7. The one who got the cream soda paid 3 dollars more than the one who got the root beer.
8. The one who got the lemonade paid 2 dollars less than Bradley.
9. The one who got the cream soda paid 3 dollars less than Lee.
10. The diner who paid $6.99 didn't order the tuna melt.
11. The diner who paid $6.99 didn't order the spaghetti.
12. The one who got the lemonade paid 1 dollar less than the one who got the orange soda.
13. Of the one who got the cream soda and the diner who paid $6.99, one was Perry and the other ordered the turkey plate.
14. The diner who paid $5.99 was either the one who got the iced tea or the diner who ordered the club sandwich.
