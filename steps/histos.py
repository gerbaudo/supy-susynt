import supy

class absEta(supy.steps.histos.value) :
    def wrapName(self) : return ".absEta",
    def wrap(self,val) : return abs(val[0].Eta())
