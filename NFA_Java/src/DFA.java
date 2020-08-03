import java.util.ArrayList;
import java.util.Hashtable;


public class DFA {
	
	public int startState;
	public int currentState;
	public ArrayList <Integer> acceptStates;
	public Hashtable <Pair,Integer> transitionFn;
	
	Hashtable <Pair,ArrayList<Integer>> nfaTransFn;
	ArrayList <Integer> nfaStates;
	
	
	public DFA(String nfaDescription)
	{
		this.startState = 0;
		this.currentState = 0;
		this.transitionFn = new Hashtable<Pair,Integer>();
		this.acceptStates = new ArrayList<Integer>();
		
		this.nfaTransFn = new Hashtable<Pair, ArrayList<Integer>>();
		this.nfaStates = new ArrayList<Integer>();
		
		decodeNfaDescription(nfaDescription);
		
	}
	
	
	public void decodeNfaDescription(String desc)
	{
		String z = desc.split("#")[0];
		String o = desc.split("#")[1];
		String e = desc.split("#")[2];
		String f = desc.split("#")[3];
		
		String [] zeroTrans = z.split(";");
		String [] oneTrans = o.split(";");
		String [] epsilonTrans = e.split(";");
		//f is a comma separated set of accept states
		//String [] accept_states = f.split(",");
		
		getAllStates(zeroTrans, oneTrans, epsilonTrans);
		
		decodeTrans(zeroTrans, 0);
		decodeTrans(oneTrans, 1);
		decodeTrans(epsilonTrans, -1);	//-1 means epsilon
		
		getEpsilonClosure();
		
		

		
	}
	
	public void getAllStates(String [] zeroTrans, String [] oneTrans, String [] epsilonTrans)
	{
		for(String tuple : zeroTrans)
		{
			String [] tupleElements = tuple.split(",");
			int i = Integer.parseInt(tupleElements[0]); //current state
			int j = Integer.parseInt(tupleElements[1]); //new state
			
			if(! this.nfaStates.contains(i))
				this.nfaStates.add(i);
			
			if(! this.nfaStates.contains(j))
				this.nfaStates.add(j);
		}
		
		for(String tuple : oneTrans)
		{
			String [] tupleElements = tuple.split(",");
			int i = Integer.parseInt(tupleElements[0]); //current state
			int j = Integer.parseInt(tupleElements[1]); //new state
			
			if(! this.nfaStates.contains(i))
				this.nfaStates.add(i);
			
			if(! this.nfaStates.contains(j))
				this.nfaStates.add(j);
		}
		
		for(String tuple : epsilonTrans)
		{
			String [] tupleElements = tuple.split(",");
			int i = Integer.parseInt(tupleElements[0]); //current state
			int j = Integer.parseInt(tupleElements[1]); //new state
			
			if(! this.nfaStates.contains(i))
				this.nfaStates.add(i);
			
			if(! this.nfaStates.contains(j))
				this.nfaStates.add(j);
		}
		
		this.nfaStates.sort(null);
		
	}
	
	
	public void decodeTrans(String [] trans, int val)
	{
			
		for(String tuple : trans)
		{
			String [] tupleElements = tuple.split(",");
			int i = Integer.parseInt(tupleElements[0]); //current state
			int j = Integer.parseInt(tupleElements[1]); //new state
			
			//A tuple i, j means that trans(i, val) = j
			
			if(! this.nfaStates.contains(i))
				this.nfaStates.add(i);
			
			if(! this.nfaStates.contains(j))
				this.nfaStates.add(j);
			
			
			Pair p = new Pair(i, val);
			ArrayList <Integer>st;
			
			if (this.nfaTransFn.containsKey(p)) 
				st = nfaTransFn.get(p);
			else 
				st = new ArrayList<Integer>();

			st.add(j);
			this.nfaTransFn.put(p, st);
				
		}
		

		
	}
	
	
	public void getEpsilonClosure()
	{
		//make sure each state is there, with at least itself as the epsilon transition
		for (int state : this.nfaStates)
		{
			Pair p = new Pair(state, -1);
			
			if( ! this.nfaTransFn.contains(p)) //if not there, add it with itself as the target state
			{	
				ArrayList<Integer> epsTrans = new ArrayList<Integer>();
				epsTrans.add(state);
				nfaTransFn.put(p, epsTrans);
			}
			else //if it's there, make sure it exists in the list of targets
			{
				ArrayList<Integer> epsTrans =  nfaTransFn.get(p);
				if ( !epsTrans.contains(state))
				{
					epsTrans.add(state);
					nfaTransFn.put(p, epsTrans);
				}
				
			}
			
		}
		
		//get the actual epsilon closures

		
		
	}
	
	
	/**************************************************************************************/
	/**************************************************************************************/
	/**************************************************************************************/
	public static ArrayList<String> getEpsilonClosure(String state,Transition[]transitions){
		ArrayList<String> result = new ArrayList<>();
		result.add(state);
		for(int i = 0 ; i<transitions.length;i++) {
			if(transitions[i].alphabet.equals("$") && transitions[i].from.equals(state)&&!result.contains(transitions[i].to)) {
				result.add(transitions[i].to);
			}
		}
		return result;
	}
	
	public static ArrayList<String> getAllEpsilonClosure(String state,Transition[]transitions){
		ArrayList<String> result = getEpsilonClosure(state, transitions);
		for(int i = 0 ; i < result.size();i++) {
			ArrayList<String> newOutcome = getEpsilonClosure(result.get(i), transitions);
			for(int j = 0 ; j<newOutcome.size();j++) {
				if (!result.contains(newOutcome.get(j))) {
					result.add(newOutcome.get(j));
				}
			}
		}
		return result;
	}
	/**************************************************************************************/
	/**************************************************************************************/
	/**************************************************************************************/
	
	
	
	
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
		
		//DFA dfa_1 = new DFA("0,0,1;1,2,1;2,0,3;3,3,3#1,3");
		//System.out.println(dfa_1.run("1100"));
		
		//DFA dfa_2 = new DFA("0,0,1;1,1,2;2,2,2#2");
		//System.out.println(dfa_2.run("111"));
		
		ArrayList<Integer> a = new ArrayList<Integer>();
		a.add(10);
		a.add(15);
		a.add(5);
		
		a.sort(null);
		System.out.println(a);

		
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
