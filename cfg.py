import random
from collections import defaultdict



class ContextFreeGrammar(object):
    """
    Models a context free grammar construct. Based on code from:
    http://eli.thegreenplace.net/2010/01/28/generating-random-sentences-from-a-context-free-grammar/
    """

    def __init__(self):
        self.prod = {}


    def add_production(self, lhs, rhs):
        """ Add production to the grammar. 'rhs' can
            be several productions separated by '|'.
            Each production is a sequence of symbols
            separated by whitespace.

            Usage:
                grammar = ContextFreeGrammar()
                grammar.add_production('NT', 'VP PP')
                grammar.add_production('Digit', '1|2|3|4')
        """
        if lhs not in self.prod: self.prod[lhs] = []
        for prod in rhs.split('|'):
            tmp = prod.split('"')
            terms = []
            for t1, t2 in zip(tmp[::2] + [''], tmp[1::2] + ['']):
                if t1.strip(): terms += t1.split()
                if t2.strip(): terms.append('"' + t2 + '"')
            self.prod[lhs].append(tuple(terms))

        
    def add_productions_from_file(self, grammar_file_path):
        """ Add productions to the grammar from a grammar file.
            Usage:
                grammar = ContextFreeGrammar()
                grammar.add_productions_from_file('./grammars/exam.cfg')
        """        
        grammar = u''
        with open(grammar_file_path) as f:
            for line in f.read().splitlines():
                if not line.lstrip().startswith('//'):
                    grammar += ' ' + line
                    
        
        rules = grammar.strip().split(u';')
        
        for r in rules:
            if not r: continue
            lhs, rhs = r.split(u':')
            lhs = lhs.strip()
            if lhs not in self.prod: self.prod[lhs] = []
            for prod in rhs.split('|'):
                tmp = prod.split('"')
                terms = []
                for t1, t2 in zip(tmp[::2] + [''], tmp[1::2] + ['']):
                    if t1.strip(): terms += t1.split()
                    if t2.strip(): terms.append('"' + t2 + '"')
                self.prod[lhs].append(tuple(terms))
            

    def gen_random(self, symbol):
        """ Generate a random sentence from the
            grammar, starting with the given
            symbol.
        """
        sentence = ''

        # select one production of this symbol randomly
        rand_prod = random.choice(self.prod[symbol])

        for sym in rand_prod:
            # for non-terminals, recurse
            if sym in self.prod:
                sentence += self.gen_random(sym)
            else:
                sentence += sym + ' '

        return sentence


    def gen_random_convergent(self,
                              symbol,
                              cfactor=0.25,
                              pcount=defaultdict(int)
                              ):
        """ Generate a random sentence from the
            grammar, starting with the given symbol.
        
            Uses a convergent algorithm - productions
            that have already appeared in the
            derivation on each branch have a smaller
            chance to be selected.
    
            cfactor - controls how tight the
            convergence is. 0 < cfactor < 1.0
    
            pcount is used internally by the
            recursive calls to pass on the
            productions that have been used in the
            branch.
        """
        sentence = ''
    
        # The possible productions of this symbol are weighted
        # by their appearance in the branch that has led to this
        # symbol in the derivation
        #
        weights = []
        for prod in self.prod[symbol]:
            if prod in pcount:
                weights.append(cfactor ** (pcount[prod]))
            else:
                weights.append(1.0)
        rand_prod = self.prod[symbol][weighted_choice(weights)]
    
        # pcount is a single object (created in the first call to
        # this method) that's being passed around into recursive
        # calls to count how many times productions have been
        # used.
        # Before recursive calls the count is updated, and after
        # the sentence for this call is ready, it is rolled-back
        # to avoid modifying the parent's pcount.
        #
        pcount[rand_prod] += 1
    
        for sym in rand_prod:
            # for non-terminals, recurse
            if sym in self.prod:
                sentence += self.gen_random_convergent(
                                  sym,
                                  cfactor=cfactor,
                                  pcount=pcount)
            else:
                sentence += sym + ' '
    
        # backtracking: clear the modification to pcount
        pcount[rand_prod] -= 1
        return sentence


def weighted_choice(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i

def cleanup(sentence):
    s = u" ".join(s.strip() for s in sentence.split('"') if s.strip())
    for p in ('.', '!' ,'?', ',', '-'):
        s = s.replace(' ' + p, p)
    s = s.replace('\\n', '\n')
    return s[0].upper() + s[1:]
     

