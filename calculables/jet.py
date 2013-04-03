import supy

GeV = 1000.
GeV2MeV=1000.
MeV2GeV=0.001

#___________________________________________________________
class signalJets(supy.wrappedChain.calculable) :

    def __init__(self):
        maxEta, minPt, minJvf = 2.5, 20., 0.5
        self.maxEta = maxEta
        self.minPt  = minPt
        self.minJvf = minJvf
        self.moreName = ""
        if maxEta : self.moreName += "|eta|<%.1f"%maxEta
        if minPt  : self.moreName += "pt>%.1f"%minPt
        if minJvf : self.moreName += "JVF>%.1f"%minJvf        
    def update(self, _) :
        self.value = [j for j in self.source['jets']
                      if abs(j.Eta())<self.maxEta and j.Pt()>self.minPt and \
                      (j.jvf < 0.0 or j.jvf>self.minJvf)]

class indicesSignalJets(supy.wrappedChain.calculable) :
    def update(self, _) :
        self.value = [i for i,jj in enumerate(self.source['signalJets'])]

