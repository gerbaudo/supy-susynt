import calculables
import samples
import steps
import supy
import ROOT as r


class example_analysis(supy.analysis):
    def listOfSteps(self, config):
        return [supy.steps.printer.progressPrinter(),
                supy.steps.filters.value('sameSign',min=1),
                supy.steps.histos.multiplicity('signalJets',8),
                supy.steps.filters.multiplicity('signalJets',min=2),
                steps.histos.absEta('signalJets',20,0.,5.,'indicesSignalJets'),
                ]

    def listOfCalculables(self, config):
        cdil = calculables.dilepton
        cj = calculables.jet
        lcals =  supy.calculables.zeroArgs(supy.calculables)
        lcals += [cdil.signalLeptons(),
                  cj.signalJets(), cj.indicesSignalJets(),
                  ]
        lcals += supy.calculables.fromCollections(calculables.dilepton, [('signalLeptons','')])

        return lcals

    def listOfSampleDictionaries(self):
        return [samples.localWh2Lep11]

    def listOfSamples(self, config):
        return (supy.samples.specify(names='WH_2Lep_11_ee', color=r.kBlack)
                +supy.samples.specify(names='WH_2Lep_11_em', color=r.kViolet)
                +supy.samples.specify(names='WH_2Lep_11_mm', color=r.kRed)
                )

    def conclude(self, pars):
        #make a pdf file with plots from the histograms created above
        org = self.organizer(pars)
        org.scale(lumiToUseInAbsenceOfData=20.0)
        supy.plotter(org,
                     doLog=False,
                     pdfFileName=self.pdfFileName(org.tag),
                     ).plotAll()
