from pyswip import Prolog

prolog = Prolog()
prolog.consult("rule.pl")

# call 'classify' function to easily classify which query 


def add_parent(s):
    b = bool(list(prolog.query("add_parent({}, {})".format(s.people, s.source))))
    return b

def add_parents(s):
    has_new_fact = True
    for p in s.people:
        if not bool(list(prolog.query("add_parent_rule({}, {})".format(p, s.source)))):
            return False
        
    for p in s.people:
        has_new_fact = bool(list(prolog.query("add_parent({}, {})".format(p, s.source))))
        if not has_new_fact:
            return False
        
    return True

def add_father(s):
    b = bool(list(prolog.query("add_father({},{})".format(s.people,s.source))))
    return b

def add_mother(s):
    b = bool(list(prolog.query("add_mother({},{})".format(s.people,s.source))))
    return b

def add_grandfather(s):
    b = bool(list(prolog.query("add_grandfather({},{})".format(s.people, s.source))))
    return b

def add_grandmother(s):
    b = bool(list(prolog.query("add_grandmother({},{})".format(s.people, s.source))))
    return b

def add_child(s):
    b = bool(list(prolog.query("add_parent({},{})".format(s.source, s.people[0]))))
    return b

def add_children(s):
    has_new_fact = True
    for p in s.people:
        if not bool(list(prolog.query("add_parent_rule({}, {})".format(s.source,p)))):
            return False
        
    for p in s.people:
        if not bool(list(prolog.query("is_parent({}, {})".format(s.source,p)))):
            
            has_new_fact = bool(list(prolog.query("add_parent({}, {})".format(s.source,p))))
            if not has_new_fact:
                return False
        
        
    return True

def add_son(s):
    b = bool(list(prolog.query("add_son({},{})".format(s.people, s.source))))
    return b

def add_daughter(s):
    b = bool(list(prolog.query("add_daughter({},{})".format(s.people, s.source))))
    return b

def add_uncle(s):
    b = bool(list(prolog.query("add_uncle({},{})".format(s.people, s.source))))
    return b

def	add_aunt(s):
    b = bool(list(prolog.query("add_aunt({},{})".format(s.people, s.source))))
    return b

def add_sibling(s):
    b = bool(list(prolog.query("add_sibling({},{})".format(s.people, s.source))))
    return b

def	add_brother(s):
    b = bool(list(prolog.query("add_brother({},{})".format(s.people, s.source))))
    return b

def	add_sister(s):
    b = bool(list(prolog.query("add_sister({},{})".format(s.people, s.source))))
    return b

def is_male(s):
    b = bool(list(prolog.query("is_male({})".format(s.people))))
    return b

def is_female(s):
    b = bool(list(prolog.query("is_female({})".format(s.people))))
    return b

def is_parent(s):
    b = bool(list(prolog.query("is_parent({},{})".format(s.people,s.source))))
    return b

def are_parents(s):
    for p in s.people:
        b = bool(list(prolog.query("is_parent({}, {})".format(p, s.source))))
        if b == False:
            return b

def is_child(s):
    b = bool(list(prolog.query("is_child({},{})".format(s.people,s.source))))
    return b

def is_children(s):
    for child in s.people:
        b = bool(list(prolog.query("is_child({},{})".format(child,s.source))))
        if b == False:
            return b
    return b

def is_daughter(s):
    b = bool(list(prolog.query("is_daughter({}, {})".format(s.people,s.source))))
    return b

def is_son(s):
    b = bool(list(prolog.query("is_son({},{})".format(s.people,s.source))))
    return b

def is_siblings(s):
    b = bool(list(prolog.query("is_sibling({},{})".format(s.people, s.source))))
    return b

def is_grandparent(s):
    b = bool(list(prolog.query("is_grandparent({}, {})".format(s.people,s.source))))
    return b

def is_descendant(s):
    b = bool(list(prolog.query("is_descendant({}, {})".format(s.people,s.source))))
    return b

def is_relative(s):
    b = bool(list(prolog.query("is_relative({}, {})".format(s.people,s.source))))
    return b

def is_cousin(s):
    b = bool(list(prolog.query("is_cousin({}, {})".format(s.people,s.source))))
    return b

def is_father(s):
    b =  bool(list(prolog.query("is_father({}, {})".format(s.people,s.source))))
    return b

def is_mother(s):
    b =  bool(list(prolog.query("is_mother({}, {})".format(s.people,s.source))))
    return b

def is_grandfather(s):
    b =  bool(list(prolog.query("is_grandfather({}, {})".format(s.people,s.source))))
    return b

def is_grandmother(s):
    b =  bool(list(prolog.query("is_grandmother({}, {})".format(s.people,s.source))))
    return b

def is_brother(s):
    b =  bool(list(prolog.query("is_brother({}, {})".format(s.people,s.source))))
    return b

def is_sister(s):
    b =  bool(list(prolog.query("is_sister({}, {})".format(s.people,s.source))))
    return b

def is_uncle(s):
    b =  bool(list(prolog.query("is_uncle({}, {})".format(s.people,s.source))))
    return b

def is_aunt(s):
    b =  bool(list(prolog.query("is_aunt({}, {})".format(s.people,s.source))))
    return b

def get_siblings(s):
    return list(prolog.query("is_sibling(X, {})".format(s.people)))

def get_mother(s):
    return list(prolog.query("is_mother(X, {})".format(s.people)))
    
def get_father(s):
    return list(prolog.query("is_father(X, {})".format(s.people)))

def get_sister(s):
    return list(prolog.query("is_sister(X, {})".format(s.people[0])))

def get_brother(s):
    return list(prolog.query("is_brother(X, {})".format(s.people[0])))

def get_parent(s):
     return list(prolog.query("is_parent(X, {})".format(s.people)))

def get_grandparent(s):
     return list(prolog.query("is_grandparent(X, {})".format(s.people)))

def get_grandmother(s):
    return list(prolog.query("is_grandmother(X, {})".format(s.people)))
    
def get_grandfather(s):
    return list(prolog.query("is_grandfather(X, {})".format(s.people)))

def get_children(s):
    return list(prolog.query("is_child(X, {})".format(s.people)))

def get_son(s):
    return list(prolog.query("is_son(X, {})".format(s.people)))

def get_daughter(s):
    return list(prolog.query("is_daughter(X, {})".format(s.people)))

def get_relative(s):
    return list(prolog.query("is_relative(X, {})".format(s.people)))

def get_cousin(s):
    return list(prolog.query("is_cousin(X, {})".format(s.people)))

def get_uncle(s):
    return list(prolog.query("is_uncle(X, {})".format(s.people)))

def get_aunt(s):
    return list(prolog.query("is_aunt(X, {})".format(s.people)))

#statement prompts
relation_s = {
    "siblings": add_sibling,
    "brother": add_brother, "sister": add_sister, 
    "brothers": add_brother, "sisters": add_sister, 
    "parents": add_parents, "parent": add_parent,
    "mother": add_mother, "father": add_father, 
    "grandmother": add_grandmother, "grandfather": add_grandfather, 
    "child": add_child, "children": add_children, 
    "daughter": add_daughter, "son": add_son,
    "daughters": add_daughter, "sons": add_son,
    "uncle": add_uncle, "aunt": add_aunt
}

#question prompts
relation_q = {
    "sibling": is_siblings, "siblings": is_siblings,
    "brother": is_brother, "sister": is_sister, 
    "brothers": is_brother, "sisters": is_sister, 
    "parent": is_parent, "parents": are_parents,
    "mother": is_mother, "father": is_father, 
    "grandmother": is_grandmother, "grandfather": is_grandfather, 
    "child": is_child, "children": is_children, 
    "daughter": is_daughter, "son": is_son, 
    "daughters": is_daughter, "sons": is_son,
    "cousin": is_cousin, "cousins": is_cousin,
    "relative":is_relative, "relatives": is_relative, "uncle": is_uncle, "aunt": is_aunt
}

#who question prompts
relation_p = {
    "siblings": get_siblings, 
    "brother": get_brother, "sister": get_sister, 
    "brothers": get_brother, "sisters": get_sister,
    "parent": get_parent, "parents": get_parent, "mother": get_mother, "father": get_father,
    "grandparent": get_grandparent, "grandmother": get_grandmother, "grandfather": get_grandfather, 
    "children": get_children, "daughter": get_daughter, "son": get_son,
    "daughters": get_daughter, "sons": get_son,
    "cousin": get_cousin, "cousins": get_cousin,
    "relative": get_relative, "relatives": get_relative, "uncle": get_uncle, "aunt": get_aunt
}

def classify(s):
    try:
        if s.source != None:
            #question prompt
            if s.question == True:
                if relation_q[s.relation](s):
                    print("\tYES!")
                else: 
                    print("\tNO!")
                
                print("------------------------\n")
            
            #statement prompt
            else:
                b = relation_s[s.relation](s)
                if b:
                    print("\tI learned something new!")
                else:
                    print("\tI learned nothing new from this. It might be impossible, or I already know it!")
                    
                print("------------------------\n")
                
        #search prompt
        else:
            names = relation_p[s.relation](s)
            names_tmp = [list(name.values()) for name in names]
            names = []
            for name in names_tmp:
                names = names + name
            names = list(set(names))

            if len(names) > 0:
                for x in names:
                    # filter out identical names
                    if not(s.people.lower() == x):
                        print("\t", x.capitalize())
            else:
                print("\tNone")
                
            print("------------------------\n")
    except:
        print("Sorry, I couldn't read that.")