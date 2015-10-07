from cfg import ContextFreeGrammar, cleanup

if __name__ == "__main__":
    
    print "Strating...\n\n"
    
    
#     grammar = ContextFreeGrammar()
#     grammar.add_production('S', 'NP VP')
#     grammar.add_production('NP', 'Det N | Det N')
#     grammar.add_production('NP', 'I | he | she | Joe')
#     grammar.add_production('VP', 'V NP | VP')
#     grammar.add_production('Det', 'a | the | my | his')
#     grammar.add_production('N', 'elephant | cat | jeans | suit')
#     grammar.add_production('V', 'kicked | followed | shot')
#  
#     for i in xrange(10):
#         print cleanup(grammar.gen_random_convergent('S'))   
          
          
          
    grammar = ContextFreeGrammar()
    grammar.add_productions_from_file('./grammars/exam.cfg')
    for i in xrange(10):
        s = cleanup(grammar.gen_random_convergent('question'))
        print s
        
        
    print "\n\nDone."
    
    
    
    
    
    
