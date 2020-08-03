# DFA
* A basic Implementation of a Deterministic Finite State Automaton (DFA)
* A DFA is a quintuple ( <img src="https://render.githubusercontent.com/render/math?math=Q"> , <img src="https://render.githubusercontent.com/render/math?math=\Sigma">, <img src="https://render.githubusercontent.com/render/math?math=\delta">, <img src="https://render.githubusercontent.com/render/math?math=q_0">, <img src="https://render.githubusercontent.com/render/math?math=F">): 
  * <img src="https://render.githubusercontent.com/render/math?math=Q"> is a non-empty, finite set of states. 
  * <img src="https://render.githubusercontent.com/render/math?math=\Sigma"> is non-empty, finite set of symbols (an alphabet).
  * <img src="https://render.githubusercontent.com/render/math?math=\delta : Q \times \Sigma \in Q"> is the transition function.
  * <img src="https://render.githubusercontent.com/render/math?math=q_0 \in Q"> is the start state.
  * <img src="https://render.githubusercontent.com/render/math?math=F \in Q"> is the set of accept states. 
* A DFA accepts a string <img src="https://render.githubusercontent.com/render/math?math=w = w_1 w_2 ... w_n \in \Sigma^*"> if there is a sequence <img src="https://render.githubusercontent.com/render/math?math=r_0, r_1, ..., r_n"> of states such that 
  * <img src="https://render.githubusercontent.com/render/math?math=r_0 = q_0">
  * <img src="https://render.githubusercontent.com/render/math?math=r_n \in F">
  * <img src="https://render.githubusercontent.com/render/math?math= \delta(r_i,w_{i+1}) = r_{i+1}"> for every <img src="https://render.githubusercontent.com/render/math?math=0 <= i < n">

We make the following assumptions for simplicity.
1. The alphabet <img src="https://render.githubusercontent.com/render/math?math=\Sigma"> is always the binary alphabet {0,1}
2. The set of states <img src="https://render.githubusercontent.com/render/math?math=Q"> is always of the form The set of states {0, . . . , n}, for some <img src="https://render.githubusercontent.com/render/math?math=n \in N">.
3. The start state is always state 0.

An object DFA is implemented, where:
* DFA is created by calling the function `construct_DFA` which takes one parameter that is a string description of a DFA and returns a DFA instance.
* A string describing a DFA is of the form P#S, where P is a prefix representing the
transition function ± and S is a suffix representing the set F of accept state.
* P is a semicolon-separated sequence of triples of states; each triple is a comma-separated
sequence of states. A triple i, j, k means that ±(i, 0) = j and ±(i, 1) = k.
* S is a comma-separated sequence of states.
* For example, the DFA for which the state diagram appears below may have the following
string representation.
0,0,1;1,2,1;2,0,3;3,3,3#1,3
1
* run simulates the operation of the constructed DFA on a given binary string. It returns
true if the string is accepted by the DFA and false otherwise.
