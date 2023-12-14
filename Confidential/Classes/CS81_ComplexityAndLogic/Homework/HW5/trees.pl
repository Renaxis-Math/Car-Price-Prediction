%% trees.pl
%%
%% Author(s):
%%
%% CS 81 HW 5, Problem 3

% If this file's syntax coloring is odd,
% make sure your editor is set to Prolog highlighting
% (or Plain Text), not Perl.

% some "nice" prolog settings...
:- set_prolog_flag( prompt_alternatives_on, groundness ).
:- set_prolog_flag(toplevel_print_options, [quoted(true),
     portray(true), attributes(portray), max_depth(999), priority(699)]).
:- set_prolog_flag(answer_write_options, [quoted(true),
     portray(true), attributes(portray), max_depth(999), priority(699)]).

% Finish the following four definitions,
% and add any other helper predicates you require

%%%%%%%%%%
% PART A %
%%%%%%%%%%

% We did the base case for you; an input
%   evaluates to itself if that input is a number.
% You just need to do all the other cases.

% Case 1: If the tree is a number, return it.
eval(X, X) :- number(X).

% Case 2: If the tree is an addition node, recursively evaluate the left and right subtrees and sum them.
eval([+, Subtree1, Subtree2], Result) :-
    eval(Subtree1, Left),
    eval(Subtree2, Right),
    Result is Left + Right.

% Case 3: If the tree is a subtraction node, recursively evaluate the left and right subtrees and subtract them.
eval([-, Subtree1, Subtree2], Result) :-
    eval(Subtree1, Left),
    eval(Subtree2, Right),
    Result is Left - Right.

% Case 4: If the tree is a multiplication node, recursively evaluate the left and right subtrees and multiply them.
eval([*, Subtree1, Subtree2], Result) :-
    eval(Subtree1, Left),
    eval(Subtree2, Right),
    Result is Left * Right.

% Case 5: If the tree is a division node, recursively evaluate the left and right subtrees and divide them.
eval([/, Subtree1, Subtree2], Result) :-
    eval(Subtree1, Left),
    eval(Subtree2, Right),
    % Ensure no division by zero
    Right \= 0,
    Result is Left // Right.

%%%%%%%%%%
% PART B %
%%%%%%%%%%
atree(_, [X], X).

atree(Ops, L, [Op, LeftSubtree, RightSubtree]) :-
    Ops \== [],
    member(Op, Ops),
    append(L1, L2, L),
    L1 \== [], L2 \== [],
    atree(Ops, L1, LeftSubtree),
    atree(Ops, L2, RightSubtree).

atree(Ops, L, Tree) :-
    Ops \== [],
    append(L1, L2, L),
    L1 \== [], L2 \== [],
    member(Op, Ops),
    atree(Ops, L1, LeftSubtree),
    atree(Ops, L2, RightSubtree),
    Tree = [Op, LeftSubtree, RightSubtree].

generate_trees(Ops, L, Trees) :-
    setof(Tree, atree(Ops, L, Tree), Trees).

%%%%%%%%%%
% PART C %
%%%%%%%%%%

solve(Ops, L, X, Tree) :-
    permutation(L, Perm),
    generate_trees(Ops, Perm, Trees),
    member(Tree, Trees),
    eval(Tree, X).

% Hint: recall that
%   permutation(L,M) is true if list L is a permutation of list M.
% (This is the only definition in the entire assignment
%  where permutations are useful!)
