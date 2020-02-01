'''

A basic implementation of a Deterministic Finite Automaton (DFA).

A DFA is a quintuple (Q, sigma, gamma, q0, F): 
    - Q is a non-empty, finite set of states
    - sigma is non-empty, finite set of symbols (an alphabet)
    - gamma is the transition function
    - q0 (belong to Q)  is the start state
    - F (subset of Q) is the set of accept states. 
    
A DFA accepts a string w = w1w2 · · ·wn belong to (sigma*) if: 
there is a sequence r0, r1, . . . , rn of states such that:
    (i) r0 = q0, 
    (ii) rn belong to F, and 
    (iii) gamma(ri,wi+1) = ri+1, for every 0 <= i < n.


For simplicity, we assume:
    a) The alphabet sigma is always the binary alphabet {0, 1}.
    b) The set of states Q is always of the form {0, . . . , n}, for some n belong to N.
    c) The start state is always state 0.

'''

class DFA:

    def __init__(self, accept_states, transition_fn, current_state = 0 ):
        
        '''
            Inputs:
                - accept_states: a list of integers representing the accept states of the DFA
                - transition_fn: a dictionary with keys as (current state, current input) pair, and 
                value as the new current state
                - current_state: the start state of the DFA which is always initially 0 (start state)

        '''
        self.start_state = 0
        self.current_state = current_state
        self.accept_states = accept_states
        self.transition_fn = transition_fn



    def run_DFA(self, binary_str):
        
        ''''
            Inputs: 
                - binary_str: a String in the form P#S, where:
                    P is a prefix representing the transition function gamma,
                    S is a suffix representing the set F of accept state. 

                    * P is a semicolon-separated sequence of triples of states,
                    each triple is a comma-separated sequence of states. 
                    A triple i, j, k means that gamma(i, 0) = j and gamma(i, 1) = k.
                    * S is a comma-separated sequence of states.
                
        '''
        for elem in binary_str:
            current_input = int(elem)

            if (self.current_state, current_input) in self.transition_fn:
                self.current_state = self.transition_fn[(self.current_state, current_input)]
            else:
                return False
            
        if self.current_state in self.accept_states:
            return True
        
        return False



def construct_DFA(dfa_description):

    trans_desc = dfa_description.split("#")[0].split(";")
    transitionFn = {} #construct an empty dictionary

    for trans_item in trans_desc:
        trans_item = trans_item.split(",")

        i = int(trans_item[0])
        j = int(trans_item[1])
        k = int(trans_item[2])
        
        #i,0,j
        #i,1,k
 
        p1 = (i,0)
        p2 = (i,1)

        transitionFn[p1] = j
        transitionFn[p2] = k


    acc_strings = dfa_description.split("#")[1].split(",")
    accept_states = []

    for acc_string in acc_strings:
        accept_states.append(int(acc_string))


    dfa = DFA(accept_states, transitionFn)
    return dfa


def main():

    dfa1 = construct_DFA("0,0,1;1,2,1;2,0,3;3,3,3#1,3")
    dfa1_output = dfa1.run_DFA("0011010")
    print(dfa1_output)

    dfa2 = construct_DFA("0,1,3;1,3,2;2,2,2;3,3,3#2")
    dfa2_output = dfa2.run_DFA("011111")
    print(dfa2_output)
    
    dfa3 = construct_DFA("0,0,1;1,2,3;2,2,4;3,2,3;4,2,5;5,2,3#5")
    dfa3_output = dfa3.run_DFA("1011")
    dfa3_output = dfa3.run_DFA("10111")
    print(dfa3_output)
    
if __name__ == "__main__":
    main()

