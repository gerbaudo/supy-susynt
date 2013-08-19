from supy import analysisStep

class BitMaskFilter(analysisStep) :
    def __init__(self, var='') : self.var = var
    def select(self,ev) : return ev[self.var]

class GoodRun(BitMaskFilter) :
    def __init__(self) : super(GoodRun, self).__init__('IsGoodRun')
class LarErr(BitMaskFilter) :
    def __init__(self) : super(LarErr, self).__init__('LarErr')
class TileErr(BitMaskFilter) :
    def __init__(self) : super(TileErr, self).__init__('TileErr')
class TtcVeto(BitMaskFilter) :
    def __init__(self) : super(TtcVeto, self).__init__('TtcVeto')
class GoodVertex(BitMaskFilter) :
    def __init__(self) : super(GoodVertex, self).__init__('GoodVertex')
class TileTrip(BitMaskFilter) :
    def __init__(self) : super(TileTrip, self).__init__('TileTrip')
class Lar(BitMaskFilter) :
    def __init__(self) : super(Lar, self).__init__('Lar')
