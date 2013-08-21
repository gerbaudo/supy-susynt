import supy
import ROOT as r

class Grlt(supy.wrappedChain.calculable) :
    def __init__(self, file='') :
        self.grlReader = r.Root.TGoodRunsListReader(file)
        self.grlReader.Interpret()
        self.grlIn = r.Root.TGoodRunsList(self.grlReader.GetMergedGoodRunsList())
        self.grlOut = r.Root.TGoodRunsList('outputGRL')
        self.value = self
    def update(self, _) :
        pass

masks = {  # todo: access enum from SusyDefs
    'ECut_GRL'       : 1 << 0,
    'ECut_TTC'       : 1 << 1,
    'ECut_LarErr'    : 1 << 2,
    'ECut_TileErr'   : 1 << 3,
    'ECut_GoodVtx'   : 1 << 4,
    'ECut_HotSpot'   : 1 << 5,
    'ECut_BadJet'    : 1 << 6,
    'ECut_BadMuon'   : 1 << 7,
    'ECut_Cosmic'    : 1 << 8,
    'ECut_SmartVeto' : 1 << 9,
    'ECut_TileTrip'  : 1 << 10
    }

class BitMask(supy.wrappedChain.calculable) :
    def __init__(self, bitName='') :
        self.bit = masks[bitName]
    def update(self, _) :
        NtSys_NOM = 0 # todo implement syst
        self.value = self.source['event'].cutFlags[NtSys_NOM] & self.bit
        # run = evt.run
        # event = evt.event
        # lb = evt.lb
        # print 'flag  ',"{0:b}".format(flag)
        # print 'mask  ',"{0:b}".format(ECut_GRL)
        # print 'f & l ',(flag & ECut_GRL)
        # print 'runnumber : ',run,' ',event,' ',lb
class IsGoodRun(BitMask) :
    def __init__(self, collection) : super(IsGoodRun, self).__init__('ECut_GRL')
class LarErr(BitMask) :
    def __init__(self, collection) : super(LarErr, self).__init__('ECut_LarErr')
class TileErr(BitMask) :
    def __init__(self, collection) : super(TileErr, self).__init__('ECut_TileErr')
class TtcVeto(BitMask) :
    def __init__(self, collection) : super(TtcVeto, self).__init__('ECut_TTC')
class GoodVertex(BitMask) :
    def __init__(self, collection) : super(GoodVertex, self).__init__('ECut_GoodVtx')
class TileTrip(BitMask) :
    def __init__(self, collection) : super(TileTrip, self).__init__('ECut_TileTrip')
class Lar(BitMask) :
    "No el or jet in LAr hole; obsolete"
    def update(self, _) : self.value = True
