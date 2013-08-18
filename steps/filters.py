from supy import analysisStep

class GoodRun(analysisStep) :
    def select(self,ev) : return ev[self.var]
    def __init__(self, var='IsGoodRun') : self.var = var
class LarErr(analysisStep) :
    def select(self,ev) : return ev[self.var]
    def __init__(self, var='LarErr') : self.var = var

