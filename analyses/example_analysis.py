import calculables
import steps
import supy
import ROOT as r


class example_analysis(supy.analysis):
    def listOfSteps(self, config):
        return [supy.steps.printer.progressPrinter(),
                supy.steps.histos.value('Two', 10, 0, 10),
                supy.steps.filters.value('sameSign',min=1),
                #supy.steps.filters.value('oppositeFlavor',min=1),
                supy.steps.filters.value('diMuon',min=1),
                supy.steps.histos.multiplicity('signalJets',8),
                supy.steps.filters.multiplicity('signalJets',min=2),
                steps.histos.absEta('signalJets',20,0.,5.,'indicesSignalJets'),
#                 supy.steps.printer.printstuff(['sameSign','oppositeSign',
#                                                'sameFlavor','oppositeFlavor',
#                                                #'signalpts'
#                                                ]),
                ]

    def listOfCalculables(self, config):
        cdil = calculables.dilepton
        cj = calculables.jet
        return (supy.calculables.zeroArgs(supy.calculables) +
                [cdil.signalLeptons(),
                 cdil.sameSign(), cdil.oppositeSign(),
                 cdil.sameFlavor(), cdil.oppositeFlavor(),
                 cdil.diMuon(), cdil.diElectron(),
                 cj.signalJets(), cj.indicesSignalJets(),
                 ] +
                [supy.calculables.other.fixedValue('Two', 2)]
                )

    def listOfSampleDictionaries(self):
        dir = '/gdata/atlas/ucintprod/SusyNt/susy_n0135'
        holder = supy.samples.SampleHolder()
        holder.add("WH_2Lep_176584",
                   '["%s/user.zgecse.mc12_8TeV.176584.Herwigpp_simplifiedModel_wA_noslep_WH_2Lep_11.SusyNt.e1702_s1581_s1586_r3658_r3549_p1328_n0135/user.zgecse.026706._00001.susyNt.root"]'%dir,
                   xs=1.140,  # /pb
                   )
        return [holder]

    def listOfSamples(self, config):
        return (supy.samples.specify(names="WH_2Lep_176584",
                                     color=r.kBlack)
                )

    def conclude(self, pars):
        #make a pdf file with plots from the histograms created above
        org = self.organizer(pars)
        org.scale(lumiToUseInAbsenceOfData=20.0)
        supy.plotter(org,
                     doLog=False,
                     pdfFileName=self.pdfFileName(org.tag),
                     ).plotAll()
