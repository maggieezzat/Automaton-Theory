import copy

class DFA:

    def __init__(self, start_state, accept_states, transition_fn, current_state):
        
        '''
            Inputs:
                - accept_states: a list of integers representing the accept states of the DFA
                - transition_fn: a dictionary with key as state, and 
                value as [ 0-trans, 1-trans ]
                - current_state: the start state of the DFA which is the epsilon closure of the 
                start state of the NFA

        '''
        self.start_state = start_state
        self.current_state = current_state
        self.accept_states = accept_states
        self.transition_fn = transition_fn



    def run_DFA(self, binary_str):
        ''''
            Inputs: 
                - binary_str: a String input to the NFA
                
        '''
        self.current_state = self.start_state

        for elem in binary_str:
            current_input = int(elem)
            self.current_state = self.transition_fn[self.current_state][current_input]
 
        if self.current_state in self.accept_states:
            return True
        
        return False


    

def get_all_nfa_states(z,o,e,f):

    states = []

    for i in range(len(z)):
        item = z[i].split(",")
        states.append(item[0])
        states.append(item[1])
    
    for i in range(len(o)):
        item = o[i].split(",")
        states.append(item[0])
        states.append(item[1])

    for i in range(len(e)):
        item = e[i].split(",")
        states.append(item[0])
        states.append(item[1])
    
    for i in range(len(f)):
        states.append(f[i])
    
    s = set(states)
    states = list(s)
    states.sort()

    return states



def construct_nfa_table(z, o, e, states):

    nfa_table = {} #construct an empty dictionary

    for state in states: # {state: [ [0-trans], [1-trans], [e-trans] ]}
        nfa_table[state] = [ [], [], [] ]

    #fill the [0-trans]
    for i in range(len(z)):
        item = z[i].split(",")
        current_state = item[0]
        new_state = item[1]
        nfa_table[current_state][0].append(new_state)
    
    #fill the [1-trans]
    for i in range(len(o)):
        item = o[i].split(",")
        current_state = item[0]
        new_state = item[1]
        nfa_table[current_state][1].append(new_state)
    
    #fill the [e-trans]
    for i in range(len(e)):
        item = e[i].split(",")
        current_state = item[0]
        new_state = item[1]
        nfa_table[current_state][2].append(new_state)
    
    nfa_table_with_closure = copy.deepcopy(nfa_table)

    #get epsilon closure
    for state in states:
        eps_closure = get_epsilon_closure(state , nfa_table)
        nfa_table_with_closure[state][2].append(state)
        nfa_table_with_closure[state][2].extend(eps_closure)
        
        unique_set = set(nfa_table_with_closure[state][2])
        unique_list = list(unique_set)
        unique_list.sort()
        nfa_table_with_closure[state][2] = unique_list

    return nfa_table_with_closure



def get_epsilon_closure(state, nfa_table):

    e_trans = nfa_table[state][2]
    
    if len(e_trans) == 0:
        return []
    
    for state in e_trans:
        return e_trans + get_epsilon_closure(state, nfa_table)
    


def get_union_transition_zero(state_list, nfa_table):
    
    zero_trans = []

    for state in state_list:
        zero_trans.extend( nfa_table[state][0] )
        next_states = nfa_table[state][0]
        for next_state in next_states:
            zero_trans.extend( nfa_table[next_state][2] )
    
    if len(zero_trans) == 0:
        return "Dead", ["Dead"]
    
    zero_trans_set = set(zero_trans)
    zero_trans_list = list(zero_trans_set)
    zero_trans_list.sort()

    z = ""
    
    for i in range(len(zero_trans_list)):
        z+= "," + zero_trans_list[i]

    z_str = z[1:]

    return z_str, zero_trans_list




def get_union_transition_one(state_list, nfa_table):

    one_trans = []

    for state in state_list:
        one_trans.extend( nfa_table[state][1] )
        next_states = nfa_table[state][1]
        for next_state in next_states:
            one_trans.extend( nfa_table[next_state][2] )
    
    if len(one_trans) == 0:
        return "Dead", ["Dead"]
    
    one_trans_set = set(one_trans)
    one_trans_list = list(one_trans_set)
    one_trans_list.sort()

    o = ""
    
    for j in range(len(one_trans_list)):
        o+= "," + one_trans_list[j]

    o_str = o[1:]

    return o_str, one_trans_list




def get_state_string(state_list):

    state_str = ""
    for i in range(len(state_list)):
        state_str += "," + state_list[i]
    
    state_str = state_str[1:]
    
    return state_str




def get_dfa_accept_states(dfa_transition_fn, nfa_accept_states):

    dfa_accept_states = []

    for state in dfa_transition_fn:
        for nfa_accept_state in nfa_accept_states:
            if nfa_accept_state in state:
                dfa_accept_states.append(state)

    return dfa_accept_states


def construct_DFA(nfa_table, nfa_accept_states):

    done_states = []
    pending_states = []

    dfa_transition_fn = {}
    dfa_transition_fn["Dead"] = [ "Dead", "Dead"]
    done_states.append(["Dead"])


    #First, we get the start state 0-transitions and 1-transitions
    #The start state of DFA is the epsilon-closure of the start state in NFA
    dfa_start_state = ""
    current_state = []
    for i in range(len(nfa_table["0"][2])):
        dfa_start_state += ","+nfa_table["0"][2][i]
        current_state.append(nfa_table["0"][2][i])
    
    dfa_start_state = dfa_start_state[1:]
    
    done_states.append(current_state)

    zero_trans_str, zero_trans_list = get_union_transition_zero(current_state, nfa_table)
    one_trans_str, one_trans_list = get_union_transition_one(current_state, nfa_table)
    
    dfa_transition_fn[dfa_start_state] = [zero_trans_str, one_trans_str]

    if not(zero_trans_list in done_states):
        pending_states.append(zero_trans_list)
    if not(one_trans_list in done_states):
        pending_states.append(one_trans_list)

    while len(pending_states) != 0:

        current_state = pending_states[0]
        pending_states = pending_states[1:]
        done_states.append(current_state)

        zero_trans_str, zero_trans_list = get_union_transition_zero(current_state, nfa_table)
        one_trans_str, one_trans_list = get_union_transition_one(current_state, nfa_table)
    
        current_state_str = get_state_string(current_state)
        dfa_transition_fn[current_state_str] = [zero_trans_str, one_trans_str]

        if not(zero_trans_list in done_states):
            pending_states.append(zero_trans_list)
        if not(one_trans_list in done_states):
            pending_states.append(one_trans_list)


    dfa_accept_states = get_dfa_accept_states(dfa_transition_fn, nfa_accept_states)

    dfa = DFA(dfa_start_state, dfa_accept_states, dfa_transition_fn, dfa_start_state)

    return dfa




def decode_NFA(nfa_description):

    z = nfa_description.split("#")[0].split(";")
    o = nfa_description.split("#")[1].split(";")
    e = nfa_description.split("#")[2].split(";")
    f = nfa_description.split("#")[3].split(",")

    states = get_all_nfa_states(z,o,e,f)

    nfa_table = construct_nfa_table(z, o, e, states)

    dfa = construct_DFA(nfa_table, f)
    
    return dfa





def main():

    dfa1 = decode_NFA("0,0;0,1#0,0;1,2#1,2#2")
    print(dfa1.run_DFA("0000"))
    print(dfa1.run_DFA("0101"))
    print(dfa1.run_DFA("1111"))
    print(dfa1.run_DFA("1000"))
    print(dfa1.run_DFA("111111"))

    dfa2 = decode_NFA("0,2;1,0;2,1#2,1;2,2#0,1#1") 
    print(dfa2.run_DFA("10110"))    
    print(dfa2.run_DFA("01110"))    
    print(dfa2.run_DFA("100100"))   
    print(dfa2.run_DFA("0001"))     
    print(dfa2.run_DFA("010"))  
    
    dfa3 = decode_NFA("0,1;1,2;2,3#0,0;1,1;2,3;3,3#1,0;2,1;3,2#1,2,3")
    print(dfa3.run_DFA("0100"))
    print(dfa3.run_DFA("1111"))
    print(dfa3.run_DFA("01000"))
    print(dfa3.run_DFA("00"))
    print(dfa3.run_DFA("1101100"))

    dfa4 = decode_NFA("0,1;1,3;3,3#0,2;2,3;3,3#1,2;3,2#3")
    print(dfa4.run_DFA("0101100"))
    print(dfa4.run_DFA("010101"))
    print(dfa4.run_DFA("111010"))
    print(dfa4.run_DFA("10100"))
    print(dfa4.run_DFA("10101"))

    dfa5 = decode_NFA("0,0;0,1;0,4;4,4#0,0;1,2;2,3;4,5#3,4;3,1#3,5")
    print(dfa5.run_DFA("001011"))       
    print(dfa5.run_DFA("011000"))       
    print(dfa5.run_DFA("1101001"))      
    print(dfa5.run_DFA("011011010"))    
    print(dfa5.run_DFA("110010"))    
    
    
if __name__ == "__main__":
    main()

