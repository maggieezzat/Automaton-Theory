
class FDFA:

    def __init__(self, start_state, accept_states, transition_fn, actions_fn, current_state):

        self.start_state = start_state
        self.current_state = current_state
        self.accept_states = accept_states
        self.transition_fn = transition_fn
        self.actions_fn = actions_fn



    def run(self, binary_str):

        action_str = ""
        self.current_state = self.start_state

        stack = []
        L=0
        R=0
        stack.append(self.current_state)
        
        while True:

            for i in range(len(binary_str)):
                current_input = int(binary_str[i])
                self.current_state = self.transition_fn[self.current_state][current_input]
                stack.append(self.current_state)
                L+=1
            
            if self.current_state in self.accept_states:
                action_str+= self.actions_fn[self.current_state]
                return action_str
            else:
                q_r = self.current_state
                found_accept_state = False
                while len(stack) != 0:
                    self.current_state = stack.pop()
                    L-=1
                    if self.current_state in self.accept_states:
                        found_accept_state = True
                        break
                
                if found_accept_state == False:
                    action_str += self.actions_fn[q_r]
                    return action_str
                else:
                    action_str+= self.actions_fn[self.current_state]
                    L+=1
                    R=L
                    binary_str = binary_str[R:]
                    stack = []
                    self.current_state = self.start_state
                    stack.append(self.current_state)



def construct_fdfa(fdfa_description):

    states = fdfa_description.split("#")[0].split(";")
    accept_states = fdfa_description.split("#")[1].split(",")
    
    transition_fn = {}
    actions_fn = {}

    for state in states:
        state = state.split(",")
        state_name = state[0]
        zero_trans = state[1]
        one_trans = state[2]
        action = state[3]
        transition_fn[state_name] = [zero_trans, one_trans]
        actions_fn[state_name] = action

    fdfa = FDFA("0", accept_states, transition_fn, actions_fn, "0")

    return fdfa



def main():

    
    fdfa1 = construct_fdfa("0,1,0,00;1,1,2,01;2,3,2,10;3,3,3,11#1,2")
    print(fdfa1.run("0001101"))
    
if __name__ == "__main__":
    main()
