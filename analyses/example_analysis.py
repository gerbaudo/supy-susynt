import supy
import ROOT as r


class example_analysis(supy.analysis):
    def listOfSteps(self, config):
        return [supy.steps.printer.progressPrinter(),
                supy.steps.histos.value('Two', 10, 0, 10),
                ]

    def listOfCalculables(self, config):
        return (supy.calculables.zeroArgs(supy.calculables) +
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
                     pdfFileName=self.pdfFileName(org.tag),
                     ).plotAll()
