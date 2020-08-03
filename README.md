# DFA
* A basic Implementation of a Deterministic Finite State Automaton (DFA)
* A DFA is a quintuple ( <img src="https://render.githubusercontent.com/render/math?math=Q"> , <img src="https://render.githubusercontent.com/render/math?math=\Sigma">, <img src="https://render.githubusercontent.com/render/math?math=\delta">, <img src="https://render.githubusercontent.com/render/math?math=q_0">, <img src="https://render.githubusercontent.com/render/math?math=F">): 
  * <img src="https://render.githubusercontent.com/render/math?math=Q"> is a non-empty, finite set of states. 
  * <img src="https://render.githubusercontent.com/render/math?math=\Sigma"> is non-empty, finite set of symbols (an alphabet).
  * <img src="https://render.githubusercontent.com/render/math?math=\delta : Q \times \Sigma"> &#8594; <img src="https://render.githubusercontent.com/render/math?math=Q"> is the transition function.
  * <img src="https://render.githubusercontent.com/render/math?math=q_0 \in Q"> is the start state.
  * <img src="https://render.githubusercontent.com/render/math?math=F \in Q"> is the set of accept states. 
* A DFA accepts a string <img src="https://render.githubusercontent.com/render/math?math=w = w_1 w_2 ... w_n \in \Sigma^*"> if there is a sequence <img src="https://render.githubusercontent.com/render/math?math=r_0, r_1, ..., r_n"> of states such that 
  * <img src="https://render.githubusercontent.com/render/math?math=r_0 = q_0">
  * <img src="https://render.githubusercontent.com/render/math?math=r_n \in F">
  *  <img src="https://render.githubusercontent.com/render/math?math=\delta"> (r<sub>i</sub>,w<sub>i+1</sub>) = r<sub>i+1</sub>"> for every <img src="https://render.githubusercontent.com/render/math?math=0 <= i < n">

We make the following assumptions for simplicity.
1. The alphabet <img src="https://render.githubusercontent.com/render/math?math=\Sigma"> is always the binary alphabet {0,1}
2. The set of states <img src="https://render.githubusercontent.com/render/math?math=Q"> is always of the form The set of states {0, . . . , n}, for some <img src="https://render.githubusercontent.com/render/math?math=n \in N">.
3. The start state is always state 0.

An object DFA is implemented, where:
* DFA is created by calling the function `construct_DFA` which takes one parameter that is a string description of a DFA and returns a DFA instance.
* A string describing a DFA is of the form `P#S`, where `P` is a prefix representing the transition function <img src="https://render.githubusercontent.com/render/math?math=\delta"> and `S` is a suffix representing the set <img src="https://render.githubusercontent.com/render/math?math=F">) of accept state.
* `P` is a semicolon-separated sequence of triples of states: each triple is a comma-separated sequence of states. 
A triple i, j, k means that <img src="https://render.githubusercontent.com/render/math?math=\delta"> (i,0) = j and <img src="https://render.githubusercontent.com/render/math?math=\delta">  (i,1) = k
* `S` is a comma-separated sequence of states.
* For example, the DFA for which the state diagram appears below may have the following
string representation: `0,0,1;1,2,1;2,0,3;3,3,3#1,3`

![DFA](https://github.com/maggieezzat/Automaton-Theory/blob/master/DFA_Python/dfa%20diagram.PNG)

* `run` simulates the operation of the constructed DFA on a given binary string. It returns `true` if the string is accepted by the DFA and `false` otherwise.


# NFA

* An implementation of the classical algorithm for constructing a deterministic finite automaton (DFA) equivalent to a non-deterministic finite automaton (NFA).
* A NFA is a quintuple  ( <img src="https://render.githubusercontent.com/render/math?math=Q"> , <img src="https://render.githubusercontent.com/render/math?math=\Sigma">, <img src="https://render.githubusercontent.com/render/math?math=\delta">, <img src="https://render.githubusercontent.com/render/math?math=q_0">, <img src="https://render.githubusercontent.com/render/math?math=F">):
  * <img src="https://render.githubusercontent.com/render/math?math=Q"> is a non-empty, finite set of states. 
  * <img src="https://render.githubusercontent.com/render/math?math=\Sigma"> is non-empty, finite set of symbols (an alphabet).
  * <img src="https://render.githubusercontent.com/render/math?math=\delta : Q \times {\Sigma \cup \epsilon} "> &#8594; <img src="https://render.githubusercontent.com/render/math?math=P(Q)"> is the transition function.
  * <img src="https://render.githubusercontent.com/render/math?math=q_0 \in Q"> is the start state.
  * <img src="https://render.githubusercontent.com/render/math?math=F \in Q"> is the set of accept states. 
* Given a description of an NFA, we will construct an equivalent DFA.
* Same assumptions followed in DFA will hold in NFA

An object DFA is implemented, where:
* DFA is created by calling the function `decode_NFA` which takes one parameter that is a string description of a NFA and returns a DFA instance.
* A string describing an NFA is of the form `Z#O#E#F`, where `Z`, `O`, and `E`, respectively, represent the 0-transitions, the 1-transitions, and the <img src="https://render.githubusercontent.com/render/math?math=\epsilon">-transitions. `F` represents the set of accept state.
* `Z`, `O`, and `E` are semicolon-separated sequences of pairs of states. Each pair is a comma-separated sequence of two states. A pair i, j represents a transition from state i to state j. For Z this means that <img src="https://render.githubusercontent.com/render/math?math=\delta">(i, 0) = j, similarly for O and E.
* `F` is a comma-separated sequence of states.
* For example, the NFA for which the state diagram appears below may have the following string representation: `0,0;1,2;3,3#0,0;0,1;2,3;3,3#1,2#3`
![NFA](https://github.com/maggieezzat/Automaton-Theory/blob/master/NFA/nfa.PNG)
* `run` simulates the operation of the constructed DFA on a given binary string. It returns `true` if the string is accepted by the DFA and `false` otherwise.


# FDFA

* An implementation of a fallback deterministic finite automaton with actions (FDFA) abstract data type. 
* A FDFA is a sextuple  ( <img src="https://render.githubusercontent.com/render/math?math=Q"> , <img src="https://render.githubusercontent.com/render/math?math=\Sigma">, <img src="https://render.githubusercontent.com/render/math?math=\delta">, <img src="https://render.githubusercontent.com/render/math?math=q_0">, <img src="https://render.githubusercontent.com/render/math?math=F">, <img src="https://render.githubusercontent.com/render/math?math=A">): 
  * <img src="https://render.githubusercontent.com/render/math?math=Q"> is a non-empty, finite set of states. 
  * <img src="https://render.githubusercontent.com/render/math?math=\Sigma"> is non-empty, finite set of symbols (an alphabet).
  * <img src="https://render.githubusercontent.com/render/math?math=\delta : Q \times \Sigma"> &#8594; <img src="https://render.githubusercontent.com/render/math?math=Q"> is the transition function.
  * <img src="https://render.githubusercontent.com/render/math?math=q_0 \in Q"> is the start state.
  * <img src="https://render.githubusercontent.com/render/math?math=F \in Q"> is the set of accept states. 
  * <img src="https://render.githubusercontent.com/render/math?math=A"> is function that maps every state in Q to an action. 
* Same assumptions followed in DFA will hold in FDFA

An object FDFA is implemented, where:
* FDFA is created by calling the function `construct_fdfa` which takes one parameter that is a string description of a FDFA and returns a FDFA instance.
* A string describing an FDFA is of the form `P#S`, where `P` is a prefix representing both the transition function <img src="https://render.githubusercontent.com/render/math?math=\delta"> and the action function <img src="https://render.githubusercontent.com/render/math?math=A"> and `S` is a suffix representing the set <img src="https://render.githubusercontent.com/render/math?math=F"> of accept state.
* `P` is a semicolon-separated sequence of quadruples. Each quadruple is a comma-separated sequence of items: the first three items are states and the fourth is a binary string. A quadruple i, j, k, s means that <img src="https://render.githubusercontent.com/render/math?math=\delta">(i, 0) = j, <img src="https://render.githubusercontent.com/render/math?math=\delta">(i, 1) = k, and <img src="https://render.githubusercontent.com/render/math?math=A">(i) = s.
* `S` is a comma-separated sequence of states.
* For example, consider the FDFA for which the state diagram appears below. Suppose
that, for state i, A(i) is the two-bit binary representation of i. Thus, such an FDFA may have the following string representation: `0,0,1,00;1,2,1,01;2,0,3,10;3,3,3,11#0,1,2`

![FDFA](https://github.com/maggieezzat/DFA/blob/master/FDFA/fdfa.PNG)

* `run` simulates the operation of the constructed FDFA on a given binary string. For example, running the above FDFA on the string `1011100` produces the output `1000`.

# CFG Left Recursion Elimination

* An implementation of the Context Free Grammar (CFG) Left Recursion Elimination Algorithm.
* a CFG is a quadruple (<img src="https://render.githubusercontent.com/render/math?math=V">, <img src="https://render.githubusercontent.com/render/math?math=\Sigma">, <img src="https://render.githubusercontent.com/render/math?math=R">, <img src="https://render.githubusercontent.com/render/math?math=S">)
where:
  * <img src="https://render.githubusercontent.com/render/math?math=V"> and <img src="https://render.githubusercontent.com/render/math?math=\Sigma"> are disjoint alphabets (respectively, containing variables and terminals).
  * <img src="https://render.githubusercontent.com/render/math?math=R \subset V \times (V \cup \Sigma)^*"> is a set of rules.
  * <img src="https://render.githubusercontent.com/render/math?math=S \in V"> is the start variable.

We make the following assumptions for simplicity:
1. The set <img src="https://render.githubusercontent.com/render/math?math=V"> of variables consists of upper-case English symbols.
2. The start variable is the symbol <img src="https://render.githubusercontent.com/render/math?math=S">.
3. The set <img src="https://render.githubusercontent.com/render/math?math=\Sigma"> of terminals consists of lower-case English symbols.
4. We only consider CFGs with no cycles and no <img src="https://render.githubusercontent.com/render/math?math=\epsilon">-rules.
