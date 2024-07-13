:- dynamic parent/2.
:- dynamic sibling/2.
:- dynamic grandparent/2.
:- dynamic relative/2.
:- dynamic male/1.
:- dynamic female/1.
:- dynamic person/1.

%person fact for tracking if a person has already been added
%person(p)

%quantifier for gender
%male(p)
%female(p)

%main relationships:
%parent(parent,child)
%sibling(sib1,sib2)
%grandparent(gp, child)
%relative(rel, child)

%checking functions

%check if a person has already been added to the knowledge base
exists(X) :- person(X).


%if X is male
is_male(X) :- male(X).

%if X is female
is_female(X) :- female(X).


%if X is a child of Y
is_parent(X,Y) :- parent(X,Y).

is_parent(X,Y) :- parent(X,Z), 
				(sibling(Y,Z) ; sibling(Z,Y)).


is_child(X,Y)  :- is_parent(Y,X).


%if X is a sibling of Y 
is_sibling(X,Y) :- sibling(X,Y); sibling(Y,X).

is_sibling(X,Y) :- is_child(X,Z),
					is_child(Y,Z).

is_sibling(X,Y) :- X \= Y, sibling(X,Z), is_sibling(Z,Y).

%if X is a grandparent of Y
is_grandparent(X,Y) :- grandparent(X,Y).

is_grandparent(X,Y) :- is_parent(Z,Y),
						is_parent(X,Z).


%if X is a descendant of Y (child, grandchild, great...)
is_descendant(X,Y) :- 	is_parent(Y,X); is_grandparent(Y,X).

is_descendant(X,Y) :- 	is_parent(Z,X),
						is_descendant(Z,Y).
						
is_descendant(X,Y) :- 	is_grandparent(Z,X),
						is_descendant(Z,Y).


%if X is only a relative to Y
is_relative(X,Y) :- 	has_relation(X,Y); is_descendant(Y,X); is_cousin(X,Y); is_sibling(X,Y).

is_relative(X,Y) :- 	(is_descendant(Y,Z), (is_sibling(X,Z) ; is_descendant(X,Z)));
						(is_descendant(X,Z), (is_sibling(Y,Z) ; is_descendant(Y,Z))).
		
is_relative(X,Y) :-		(is_descendant(Y,Z), is_sibling(Z,W), (is_descendant(W,X); is_descendant(X,W)));
						(is_descendant(X,Z), is_sibling(Z,W), (is_descendant(W,Y); is_descendant(X,W))).

%if X is a cousin of Y (same generation relative)
is_cousin(X,Y)	 :- 	is_parent(Z,Y), is_sibling(Z,W), is_parent(W,X).

is_cousin(X,Y)	 :-		is_parent(Z,X), is_sibling(Z,W), is_parent(W,Y).

%if X has any direct connection				
has_relation(X,Y) :-	parent(X,Y); parent(Y,X);
						grandparent(X,Y); grandparent(Y,X);
						relative(X,Y); relative(Y,X);
						sibling(X,Y); sibling(Y,X).

%if X has an existing gender
has_gender(X) :- 	male(X); female(X).

%gender role check
is_father(X,Y) :- 	is_male(X), is_parent(X,Y).

is_mother(X,Y) :- 	is_female(X), is_parent(X,Y).

is_son(X,Y) :- 		is_male(X), is_child(X,Y).

is_daughter(X,Y) :-	is_female(X), is_child(X,Y).

is_grandfather(X,Y) :-	is_male(X), is_grandparent(X,Y).

is_grandmother(X,Y) :- is_female(X), is_grandparent(X,Y).

is_brother(X,Y) :-	is_male(X), is_sibling(X,Y).

is_sister(X,Y) :-	is_female(X), is_sibling(X,Y).

is_uncle(X,Y) :- 	is_male(X), is_relative(X,Y), 
					(has_relation(X,Y); (is_sibling(Y,Z), has_relation(Z,X)); 
					(is_parent(Z,Y), is_sibling(Z,X)) ; (is_cousin(Y,W), is_parent(X,W))).

is_aunt(X,Y) :-		is_female(X), is_relative(X,Y),
					(has_relation(X,Y); (is_sibling(Y,Z), has_relation(Z,X));
					(is_parent(Z,Y), is_sibling(Z,X)) ; (is_cousin(Y,W), is_parent(X,W))).

%auxiliary rule for adding new facts
add_rule(X,Y) :- 	(X \= Y,
					not(has_relation(X,Y)),
					not(is_descendant(Y,X)),
					not(is_descendant(X,Y)),
					not(is_relative(X,Y))) ->
					((add_person(X) -> add_person(Y); add_person(Y)); true).

add_parent_rule(X,Y) :-	aggregate_all(count, parent(_,Y), N),
						N < 2,
						add_rule(X,Y).

%adds a parent if add_rule is successful
add_parent(X,Y) :-	add_parent_rule(X,Y),
					asserta(parent(X,Y)).

%adds a grandparent if add_rule is successful
add_grandparent(X,Y) :- aggregate_all(count, grandparent(_,Y), N),
						N < 4,
						add_rule(X,Y),
						asserta(grandparent(X,Y)).

%adds a sibling if add_rule and is_sibling is not already implied
add_sibling(X,Y) :-	not(is_sibling(X,Y)),
					add_rule(X,Y),
					asserta(sibling(X,Y)).

%adds a relative if  add_rule is successful
add_relative(X,Y) :- 	not(is_relative(X,Y)),
						add_rule(X,Y),
						asserta(relative(X,Y)).

%adds a gender to X if one isnt set yet
add_male(X) :- not(has_gender(X)),
				asserta(male(X)).

add_female(X) :- 	not(has_gender(X)),
					asserta(female(X)).

%adds a person to the knowledge base
add_person(X) :-	not(exists(X)),
					asserta(person(X)).

%gender-specific fact additions

add_grandfather(X,Y) :-	aggregate_all(count, is_grandfather(_,Y), N),
						N < 2,
						(not(has_gender(X)); male(X)),
						add_grandparent(X,Y) -> (add_male(X); male(X));
						((is_grandparent(X,Y), not(has_gender(X))) -> (add_male(X); male(X))).

add_grandmother(X,Y) :- aggregate_all(count, is_grandmother(_,Y), N),
						N < 2,
						(not(has_gender(X)); female(X)),
						add_grandparent(X,Y) -> (add_female(X); female(X));
						((is_grandparent(X,Y), not(has_gender(X))) -> (add_female(X); female(X))).

add_father(X,Y) :-	not(is_father(_,Y)),
					(not(has_gender(X)); male(X)),
					(add_parent(X,Y) -> (add_male(X); male(X));
					(is_parent(X,Y) -> (add_male(X); male(X)))).

add_mother(X,Y) :-	not(is_mother(_,Y)),
					(not(has_gender(X)); female(X)),
					(add_parent(X,Y) -> (add_female(X); female(X));
					(is_parent(X,Y) -> (add_female(X); female(X)))).

add_son(X,Y) :-		(not(has_gender(X)); male(X)),
					add_parent(Y,X) -> (add_male(X); male(X));
					((is_parent(Y,X), not(has_gender(X))) -> (add_male(X); male(X))).

add_daughter(X,Y) :- 	(not(has_gender(X)); female(X)),
						add_parent(Y,X) -> (add_female(X); female(X));
						((is_parent(Y,X), not(has_gender(X))) -> (add_female(X); female(X))).

add_sister(X,Y) :-	(not(has_gender(X)); female(X)),
					add_sibling(X,Y) -> (add_female(X); female(X));
					((is_sibling(X,Y), not(has_gender(X))) -> (add_female(X); female(X))).

add_brother(X,Y) :-	(not(has_gender(X)); male(X)),
					add_sibling(X,Y) -> (add_male(X); male(X));
					((is_sibling(X,Y), not(has_gender(X))) -> (add_male(X); male(X))).

add_uncle(X,Y) :-	(not(has_gender(X)); male(X)),
					add_relative(X,Y) -> (add_male(X); male(X));
					((is_relative(X,Y); is_relative(Y,X)), not(has_gender(X)), 
					not(is_descendant(Y,X); is_sibling(X,Y); is_cousin(X,Y)) -> (add_male(X); male(X))).

add_aunt(X,Y) :- 	(not(has_gender(X)); female(X)),
					add_relative(X,Y) -> (add_female(X); female(X));
					((is_relative(X,Y); is_relative(Y,X)), not(has_gender(X)), 
					not(is_descendant(Y,X); is_sibling(X,Y); is_cousin(X,Y)) -> (add_female(X); female(X))).
