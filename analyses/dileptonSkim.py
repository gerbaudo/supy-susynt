import calculables
import samples
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
        return [samples.localWh2Lep11]

    def listOfSamples(self, config):
        return (supy.samples.specify(names='WH_2Lep_11', color=r.kBlack))
