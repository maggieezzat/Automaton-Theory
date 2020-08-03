
def LRE(CFG):
    
    rules = CFG.split(";")
    vars = []
    
    cfg = {}
    for rule in rules:
        vars.append(rule[0])
        r = rule.split(",")
        cfg[r[0]] = r[1:]
    
    new_CFG = {}

    i=0
    while i<len(vars):
        Ai = vars[i]
        Ai_rules = cfg[Ai]
        
        j=0
        while j<i:
            Ai_rules = cfg[Ai]
            Aj = vars[j]
            Aj_rules = cfg[vars[j]]
            
            Ai_new_rules = get_new_productions(Ai, Ai_rules, Aj, Aj_rules)
            cfg[Ai] = Ai_new_rules
            
            j+=1
        
        beta_rules, alpha_rules = eliminate_left_rec(Ai, cfg[Ai])

        if beta_rules == None and alpha_rules == None:
            new_CFG[Ai] = cfg[Ai]
        else:
            new_CFG[Ai] = beta_rules
            new_CFG[Ai + "'"] = alpha_rules
            cfg[Ai] = beta_rules

        
        i+=1
    
    str_CFG = get_cfg_string(new_CFG)
    return str_CFG
    




def get_new_productions(Ai, Ai_rules, Aj, Aj_rules):
    
    new_prod_rules = []

    for Ai_rule in Ai_rules:
        if Ai_rule[0] == Aj:
            for Aj_rule in Aj_rules:
                r = Ai_rule.replace(Aj, Aj_rule)
                new_prod_rules.append(r)
        else:
            new_prod_rules.append(Ai_rule)
    
    return new_prod_rules





def eliminate_left_rec(Ai, Ai_rules):
    
    #Get alphas, betas, identify if left recursive
    left_recursive = False
    alphas = []
    betas = []
    for Ai_rule in Ai_rules:
        if Ai_rule[0] == Ai:
            alphas.append(Ai_rule[1:])
            left_recursive = True
        else:
            betas.append(Ai_rule)
    
    if left_recursive:
        #eliminate direct left recursion
        beta_rules = []
        alpha_rules = []
        
        for beta in betas:
            beta_rules.append(beta+Ai+"'")
        for alpha in alphas:
            alpha_rules.append(alpha+Ai+"'")
        
        #epsilon production
        alpha_rules.append("")
        
        return beta_rules, alpha_rules
    else:
        return None,None





def get_cfg_string(cfg):
    
    cfg_str = ""
    
    for var in cfg:
        cfg_str += ";" + var
        rules = cfg[var]
        for rule in rules:
            cfg_str += "," + rule
        
    cfg_str = cfg_str[1:]

    return cfg_str





def main():

    input = "S,ScT,T;T,aSb,iaLb,i;L,SdL,S"
    true_output = "S,TS';S',cTS',;T,aSb,iaLb,i;L,aSbS'dL,iaLbS'dL,iS'dL,aSbS',iaLbS',iS'"
    output = LRE(input)
    print(output)
    assert output == true_output, "Wrong Answer"
    

    input = "S,Sa,b"
    true_output = "S,bS';S',aS',"
    output = LRE(input)
    print(output)
    assert output == true_output, "Wrong Answer"

    input = "S,Sab,cd"
    true_output = "S,cdS';S',abS',"
    output = LRE(input)
    print(output)
    assert output == true_output, "Wrong Answer"

    input = "S,SuS,SS,Ss,lSr,a"
    true_output = "S,lSrS',aS';S',uSS',SS',sS',"
    output = LRE(input)
    print(output)
    assert output == true_output, "Wrong Answer"

    input = "S,SuT,T;T,TF,F;F,Fs,P;P,a,b"
    true_output = "S,TS';S',uTS',;T,FT';T',FT',;F,PF';F',sF',;P,a,b"
    output = LRE(input)
    print(output)
    assert output == true_output, "Wrong Answer"

    input = "S,z,To;T,o,Sz"
    true_output = "S,z,To;T,oT',zzT';T',ozT',"
    output = LRE(input)
    print(output)
    assert output == true_output, "Wrong Answer"

    input = "S,lLr,a;L,LbS,S"
    true_output = "S,lLr,a;L,lLrL',aL';L',bSL',"
    output = LRE(input)
    print(output)
    assert output == true_output, "Wrong Answer"

    input = "S,BC,C;B,Bb,b;C,SC,a"
    true_output = "S,BC,C;B,bB';B',bB',;C,bB'CCC',aC';C',CC',"
    output = LRE(input)
    print(output)
    assert output == true_output, "Wrong Answer"


    
    
if __name__ == "__main__":
    main() 