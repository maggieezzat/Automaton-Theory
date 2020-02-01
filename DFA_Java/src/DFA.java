import java.util.ArrayList;
import java.util.Hashtable;

/*

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
 
 */


public class DFA {
	
	public int startState;
	
	public int currentState;
	
	public ArrayList <Integer> acceptStates;
	
	public Hashtable <Pair,Integer> transitionFn;
	
	
	public DFA(String dfaString)
	{
		this.startState = 0;
		this.currentState = 0;
		this.transitionFn = new Hashtable<Pair,Integer>();
		this.acceptStates = new ArrayList<Integer>();
		
		decodeDFAString(dfaString);
		
	}
	
	private void decodeDFAString(String str)
	{
		
		String [] acceptStatesStr = (str.split("#")[1]).split(",");
		for(String accStStr : acceptStatesStr) 
		{
			this.acceptStates.add( Integer.parseInt(accStStr) );
		}
		
		String [] trans = str.split("#")[0].split(";");
		for(String tuple : trans)
		{
			String [] tupleElements = tuple.split(",");
			int i = Integer.parseInt(tupleElements[0]);
			int j = Integer.parseInt(tupleElements[1]);
			int k = Integer.parseInt(tupleElements[2]);
			
			//A triple i, j, k means that trans(i, 0) = j and trans(i, 1) = k.
			
			Pair p1 = new Pair(i, 0);
			Pair p2 = new Pair(i, 1);
			
			this.transitionFn.put(p1, j);
			this.transitionFn.put(p2, k);
				
		}
		
	}
	
	public boolean run(String inputStr)
	{
		for (int i=0; i < inputStr.length(); i++)
		{
		    int currentInput = Integer.parseInt(inputStr.charAt(i)+"");
		    
		    if(this.transitionFn.containsKey(new Pair(currentState, currentInput))) 
		    {	
		    	this.currentState = this.transitionFn.get(new Pair(currentState, currentInput));
		    }
		    else
		    {
		    	return false;	
		    } 
		    
		}
		
		if(this.acceptStates.contains(this.currentState))
		{
			return true;
		}
		
		return false;
	}
	
	public static void main (String[] args) 
	{
		
		DFA dfa1 = new DFA("0,0,1;1,2,1;2,0,3;3,3,3#1,3");
		boolean dfa1_output = dfa1.run("00110010");
		System.out.println(dfa1_output);
		
		DFA dfa2 = new DFA("0,1,3;1,3,2;2,2,2;3,3,3#2");
		boolean dfa2_output = dfa2.run("011111");
		System.out.println(dfa2_output);
		
		DFA dfa3 = new DFA("0,0,1;1,2,3;2,2,4;3,2,3;4,2,5;5,2,3#5");
		boolean dfa3_output = dfa3.run("1011");
		dfa3_output = dfa3.run("10111");
		System.out.println(dfa3_output);

		
	}

}


class Pair
{
	int x;
	int y;
	
	public Pair(int x, int y)
	{
		this.x = x;
		this.y = y;
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Pair other = (Pair) obj;
		if (x != other.x)
			return false;
		if (y != other.y)
			return false;
		return true;
	} 
	
	public String toString()
	{
		return "(" + this.x + "," + this.y + ")";
	}
	
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + x;
		result = prime * result + y;
		return result;
	}
	
	
	
}


