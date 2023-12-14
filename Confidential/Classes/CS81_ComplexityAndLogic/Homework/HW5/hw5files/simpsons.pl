%%
%% file: simpsons.pl
%%
%% Author(s):
%%
%% CS 81 HW 5, Question 1

% If this file's syntax coloring is odd,
% make sure your editor is set to Prolog highlighting
% (or Plain Text), not Perl.

% some "nice" prolog settings...
:- set_prolog_flag( prompt_alternatives_on, groundness ).
:- set_prolog_flag(toplevel_print_options, [quoted(true),
     portray(true), attributes(portray), max_depth(999), priority(699)]).
:- set_prolog_flag(answer_write_options, [quoted(true),
     portray(true), attributes(portray), max_depth(999), priority(699)]).

% Below you'll find some example predicates that
% define family relationships, along with lots
% of prolog-formatted facts about the Simpson family.
% [Disclaimer: many of these Simpson facts are fiction.]

/*
 * Here are three example rules about families
 * Feel free to use these -- or to create new
 * helper predicates of your own...
 */

%% child(X,Y)
%%
%% X is a child of Y if Y is a parent of X
%
child(X, Y) :- parent(Y, X).


%% mother(X,Y)
%%
%% X is a (the) mother of Y
%% if X is female and X is a parent of Y
%
mother(X, Y) :- female(X), parent(X, Y).


%% anc(X,Y)
%%
%% X is an ancestor of Y if X is a parent of Y.
%% Alternatively, X is an ancestor of Y if
%%   X is (recursively) an ancestor of a parent of X.
%
anc(X, Y) :- parent(X, Y).
anc(X, Y) :- parent(Z, Y), anc(X, Z).





%% Remember, in Prolog, you're focused more on what each
%% relationship _means_ than _how_ to compute it!

%% grandparent(X, Y)
%%
%% this predicate should be true if X is a grandparent of Y
%
grandparent(_,_) :- fail.   % This is just a placeholder - replace it!



%% cousins(X, Y)
%%
%% this predicate should be true if X and Y are
%% first cousins, but not siblings (or the same person!)
%
cousins(_, _) :- fail.   % This is just a placeholder - replace it!



%% hasDaughterAndSon(P)
%%
%% this predicate should be true if P has both a female
%% and a male child
%
hasDaughterAndSon(_) :- fail.   % This is just a placeholder - replace it!




%% hasOlderSibling(X)
%%
%% this predicate should be true if X has a sibling
%% that is _strictly_ older than X
%
hasOlderSibling(_) :- fail.  % This is just a plceholder - replace it!




/*
 * here are the primitive facts on which others are built...
 *
 * You will not need all of these, but you
 * can infer a lot about the Simpsons with them!
 *
 * DO NOT CHANGE OR EXTEND THE FACTS BELOW!
 */


/*
 * the parent predicate
 */

parent(olf, skug).
parent(helga, skug).

parent(skug, esmerelda).
parent(skugerina, esmerelda).

parent(esmerelda, klotho).
parent(gemini, klotho).

parent(esmerelda, atropos).
parent(gemini, atropos).

parent(esmerelda, lachesis).
parent(gemini, lachesis).

parent(olf, homericus).
parent(helga, homericus).

parent(ug, matilda).
parent(uggette, matilda).

parent(homericus, homer).
parent(matilda, homer).

parent(homericus, gomer).
parent(matilda, gomer).

parent(homer, bart).
parent(marge, bart).

parent(homer, lisa).
parent(marge, lisa).

parent(homer, maggie).
parent(marge, maggie).

parent(john, marge).
parent(jackie, marge).

parent(john, selma).
parent(jackie, selma).

parent(john, patty).
parent(jackie, patty).

parent(john, glum).
parent(jackie, glum).

parent(glum, millhouse).
parent(cher, millhouse).

parent(glum, terpsichore).
parent(cher, terpsichore).

/*
 * the female predicate
 */

female(helga).
female(esmerelda).
female(skugerina).
female(uggette).
female(matilda).
female(marge).
female(jackie).
female(selma).
female(patty).
female(cher).
female(lisa).
female(maggie).
female(klotho).
female(atropos).
female(lachesis).
female(terpsichore).

/*
 * the male predicate
 */

male(olf).
male(skug).
male(homericus).
male(ug).
male(homer).
male(gomer).
male(gemini).
male(john).
male(glum).
male(bart).
male(millhouse).

/*
 * the age predicate
 */

age(helga, 97).
age(olf, 99).
age(uggette, 93).
age(ug, 92).
age(matilda, 65).
age(homericus, 76).
age(skugerina, 101).
age(skug, 78).
age(esmerelda, 55).
age(gemini, 54).
age(klotho, 20).
age(atropos, 19).
age(lachesis, 18).
age(marge, 35).
age(homer, 38).
age(lisa, 8).
age(maggie, 1).
age(bart, 10).
age(gomer, 41).
age(john, 62).
age(jackie, 59).
age(patty, 38).
age(selma, 38).
age(glum, 27).
age(cher, 44).
age(millhouse, 8).
age(terpsichore, 8).

/*
 * the person predicate
 */

person(helga).
person(olf).
person(uggette).
person(ug).
person(matilda).
person(homericus).
person(skugerina).
person(skug).
person(esmerelda).
person(gemini).
person(klotho).
person(atropos).
person(lachesis).
person(marge).
person(homer).
person(lisa).
person(maggie).
person(bart).
person(gomer).
person(john).
person(jackie).
person(patty).
person(selma).
person(glum).
person(cher).
person(millhouse).
person(terpsichore).
