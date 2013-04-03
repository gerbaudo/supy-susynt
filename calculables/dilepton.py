import supy


#___________________________________________________________
class signalLeptons(supy.wrappedChain.calculable) :
    def update(self, _) :
        el = self.source['electrons']
        mu = self.source['muons']
        self.value = sorted([e for e in el] + [m for m in mu], key=lambda x: x.Pt(), reverse=True)
#___________________________________________________________
class sameSign(supy.wrappedChain.calculable) :
    def __init__(self, collection = 'signalLeptons'):
        self.coll = collection
    def update(self, _) :
        leptons = self.source[self.coll]
        self.value = False if len(leptons)<2 else leptons[0].q*leptons[1].q > 0
#___________________________________________________________
class oppositeSign(supy.wrappedChain.calculable) :
    def update(self, _) :
        self.value = not self.source['sameSign']
#___________________________________________________________
class sameFlavor(supy.wrappedChain.calculable) :
    def __init__(self, collection = 'signalLeptons'):
        self.coll = collection
    def update(self, _) :
        leptons = self.source[self.coll]
        self.value = False if len(leptons)<2 else leptons[0].isMu()==leptons[1].isMu()
#___________________________________________________________
class oppositeFlavor(supy.wrappedChain.calculable) :
    def update(self, _) :
        self.value = not self.source['sameFlavor']
#___________________________________________________________

