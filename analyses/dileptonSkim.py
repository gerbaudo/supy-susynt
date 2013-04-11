import calculables
import steps
import supy
import ROOT as r


class dileptonSkim(supy.analysis):
    def parameters(self) :
        selections = self.vary()
        selections['skim_ee'] = {'flag' : 'diElectron'    }
        selections['skim_em'] = {'flag' : 'oppositeFlavor'}
        selections['skim_mm'] = {'flag' : 'diMuon'        }
        return {'selections' : selections}
    def listOfSteps(self, config):
        skim = config['selections']['flag']
        return [supy.steps.printer.progressPrinter(),
                supy.steps.filters.value(skim,min=1),
                supy.steps.other.skimmer(),
                ]

    def listOfCalculables(self, config):
        lcals =  supy.calculables.zeroArgs(supy.calculables)
        lcals += [calculables.dilepton.signalLeptons(), ]
        lcals += supy.calculables.fromCollections(calculables.dilepton, [('signalLeptons','')])
        return lcals

    def listOfSampleDictionaries(self):
        dir = '/gdata/atlas/ucintprod/SusyNt/susy_n0135'
        holder = supy.samples.SampleHolder()
        holder.add("WH_2Lep_176584",
                   '["%s/user.zgecse.mc12_8TeV.176584.Herwigpp_simplifiedModel_wA_noslep_WH_2Lep_11.SusyNt.e1702_s1581_s1586_r3658_r3549_p1328_n0135/user.zgecse.026706._00001.susyNt.root"]'%dir,
                   xs=1.140,  # /pb
                   )
        return [holder]

    def listOfSamples(self, config):
        return (supy.samples.specify(names="WH_2Lep_176584", color=r.kBlack))
