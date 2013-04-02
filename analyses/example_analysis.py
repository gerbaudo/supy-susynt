import supy
import ROOT as r


class example_analysis(supy.analysis):
    def listOfSteps(self, config):
        return [supy.steps.printer.progressPrinter(),
 #                supy.steps.histos.value('run', 20, 0, 1e4),
#                 supy.steps.histos.value('bx', 3564, 0., 3564.),
                supy.steps.histos.value('Two', 10, 0, 10),
                supy.steps.printer.printstuff(['event'])
                ]

    def listOfCalculables(self, config):
        return (supy.calculables.zeroArgs(supy.calculables) +
                [supy.calculables.other.fixedValue('Two', 2)]
                )

    def listOfSampleDictionaries(self):
        dir = "/afs/cern.ch/user/e/elaird/public/susypvt/framework_take3/"
        dir = '/tmp/gerbaudo/supy-minimal-example/data/'
        holder = supy.samples.SampleHolder()

        holder.add("Data",
#                   '["%s/skimmed_900_GeV_Data.root"]' % dir,
                   '["/gdata/atlas/ucintprod/SusyNt/susy_n0115/user.sfarrell.mc12_8TeV.176584.Herwigpp_simplifiedModel_wA_noslep_WH_2Lep_11.SusyNt.e1702_s1581_s1586_r3658_r3549_p1181_n0115/user.sfarrell.096947._00001.susyNt.root"]',
                   lumi=1.0e-5,  # /pb
                   )
        holder.add("MC",
                   '["%s/skimmed_900_GeV_MC.root"]' % dir,
                   xs=1.0e8,  # pb
                   )
        return [holder]

    def listOfSamples(self, config):
        return (supy.samples.specify(names="Data",
                                     color=r.kBlack,
                                     markerStyle=20)
 #                supy.samples.specify(names="MC",
#                                      color=r.kRed,
#                                      effectiveLumi=0.5)
                )

    def conclude(self, pars):
        #make a pdf file with plots from the histograms created above
        org = self.organizer(pars)
        org.scale()
        supy.plotter(org,
                     pdfFileName=self.pdfFileName(org.tag),
 #                     samplesForRatios=("Data", "MC"),
#                      sampleLabelsForRatios=("data", "sim"),
                     ).plotAll()
