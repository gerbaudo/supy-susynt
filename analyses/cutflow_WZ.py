import calculables
import samples
import steps
import supy
import ROOT as r


class cutflow_WZ(supy.analysis):
    def listOfSteps(self, config):
        return [supy.steps.printer.progressPrinter(),
                supy.steps.filters.value('sameSign',min=1),
                supy.steps.histos.multiplicity('signalJets',8),
                supy.steps.histos.multiplicity('trueJets',8),
                supy.steps.filters.multiplicity('signalJets',min=2),
                steps.histos.absEta('signalJets',20,0.,5.,'indicesSignalJets'),
                steps.histos.absEta('trueJets',20,0.,5.,'indicesTrueJets'),
                ]

    def listOfCalculables(self, config):
        cdil = calculables.dilepton
        cj = calculables.jet
        lcals =  supy.calculables.zeroArgs(supy.calculables)
        lcals += [cdil.signalLeptons(),
                  cj.signalJets(), cj.indicesSignalJets(),
                  cj.trueJets(), cj.indicesTrueJets(),
                  ]
        lcals += supy.calculables.fromCollections(calculables.dilepton, [('signalLeptons','')])

        return lcals

    def listOfSampleDictionaries(self):
        return [samples.Sherpa_CT10_lllnu_WZ]

    def listOfSamples(self, config):
        return (supy.samples.specify(names='Sherpa_CT10_lllnu_WZ', color=r.kBlack)
                #+supy.samples.specify(names='WH_2Lep_11_ee', color=r.kBlue)
                )

    def conclude(self, pars):
        #make a pdf file with plots from the histograms created above
        org = self.organizer(pars)
        org.scale(lumiToUseInAbsenceOfData=20.0)
        supy.plotter(org,
                     doLog=False,
                     pdfFileName=self.pdfFileName(org.tag),
                     ).plotAll()
