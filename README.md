# contextfreegrammar_gen
This is a text generator based on context free grammars encoded in BNF.

Productions can be added either directly or using an input file. Check the following snippet for an example of direct addition of productions:

    from cfg import ContextFreeGrammar, cleanup
   
    grammar = ContextFreeGrammar()
    grammar.add_production('S', 'NP VP')
    grammar.add_production('NP', 'Det N | Det N')
    grammar.add_production('NP', 'I | he | she | Joe')
    grammar.add_production('VP', 'V NP | VP')
    grammar.add_production('Det', 'a | the | my | his')
    grammar.add_production('N', 'elephant | cat | jeans | suit')
    grammar.add_production('V', 'kicked | followed | shot')
    
Once productions are added, a sentence based on the productions can be generated as follows:

    for i in xrange(10):
        print cleanup(grammar.gen_random_convergent('S')) 
    
This generates ten sentences such as:

    I followed Joe.
    I followed she.
    I followed he.
    My cat kicked Joe.
    Joe shot she.
    Joe shot the elephant.
    She followed my suit.
    I shot she.
    He shot Joe.
    His jeans followed she.

Reading from an input BNF productions is pretty simple:

    grammar = ContextFreeGrammar()
    grammar.add_productions_from_file('./grammars/spout.cfg')
    for i in xrange(10):
        s = cleanup(grammar.gen_random_convergent('spout'))
        print s

Which when run gives something like:

    Show that the T U- matrix of 9 is uncomputable.
    Show that the inverse determinant of 5 9 1 is 5. Include Feynman diagrams.
    Are maximal trees S-complete? Discuss. Be sure to refer to Fermat 's Theorem in your answer.
    Show that the R- path of { 9 6 } is uncomputable. Be sure to refer to Plutonium Atom Totality in your answer.
    Express { 2 4 0 9 } in canonical form.
    Are inverse matrices R E-complete? Discuss.
    Show that the inverse matrix of 5 5 is infinity. Be sure to refer to Fermat 's Theorem in your answer.
    Show that the Q- closure of 1 7 is the null set.
    Express 2 in the epsilon domain. Include flowcharts.
    Is maximal factorisation T-complete? Discuss.

There are 8 grammars in the ./grammars directory to poke arround with.

##Installation
Clone repository.

##Dependencies
None

