import calculables
import samples
import steps
import supy
import ROOT as r
import os

class cutflow_WZ(supy.analysis):
    def parameters(self) :
        return {
            'grlFile' : os.getenv('ROOTCOREDIR')+'/data/MultiLep/data12_8TeV.periodAllYear_DetStatus-v47-pro13-01_CoolRunQuery-00-04-08_Susy.xml'
            }
    def listOfSteps(self, config):
        sf = steps.filters
        return [supy.steps.printer.progressPrinter(),
                sf.GoodRun().onlyData(),
                sf.LarErr(),
                sf.TileErr(),
                sf.TtcVeto(),
                sf.GoodVertex(),
                sf.TileTrip(),
                supy.steps.filters.value('sameSign',min=1),
                supy.steps.histos.multiplicity('signalJets',8),
                supy.steps.histos.multiplicity('trueJets',8),
                supy.steps.filters.multiplicity('signalJets',min=2),
                steps.histos.absEta('signalJets',20,0.,5.,'indicesSignalJets'),
                steps.histos.absEta('trueJets',20,0.,5.,'indicesTrueJets'),
                ]

    def listOfCalculables(self, config):
        pars = self.parameters()
        cdil = calculables.dilepton
        sc = supy.calculables
        ce, cj = calculables.event, calculables.jet
        lcals =  sc.zeroArgs(supy.calculables)
        lcals += [ce.Grlt(pars['grlFile'])]
        lcals += sc.fromCollections(ce, ['event',])
        lcals += [cdil.signalLeptons(),
                  cj.signalJets(), cj.indicesSignalJets(),
                  cj.trueJets(), cj.indicesTrueJets(),
                  ]
        lcals += supy.calculables.fromCollections(calculables.dilepton, [('signalLeptons','')])

        return lcals

    def listOfSampleDictionaries(self):
        return [samples.Sherpa_CT10_lllnu_WZ]

    def listOfSamples(self, config):
        test = True
        nEventsMax=1000 if test else None
        return (supy.samples.specify(names='Sherpa_CT10_lllnu_WZ', color=r.kBlack, nEventsMax=nEventsMax)
                #+supy.samples.specify(names='WH_2Lep_11_ee', color=r.kBlue)
                )

    def conclude(self, pars):
        org = self.organizer(pars)
        org.scale(lumiToUseInAbsenceOfData=20.0)
        supy.plotter(org,
                     doLog=False,
                     pdfFileName=self.pdfFileName(org.tag),
                     ).plotAll()
