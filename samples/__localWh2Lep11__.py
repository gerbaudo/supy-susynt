from supy.samples import SampleHolder
localWh2Lep11 = SampleHolder()

xSecVal = 1.140 #pb # 1.1402753294*0.30636*0.3348500000
# brWl=0.10 # don't know whether the br is already included; for now just put in the ee/em/mm comb.
baseDir='/gdata/atlas/ucintprod/SusyNt/susy_n0139'
localWh2Lep11.add('WH_2Lep_11',
                  "['%s/user.gerbaudo.mc12_8TeV.176584.Herwigpp_simplifiedModel_wA_noslep_WH_2Lep_11.SusyNt.e1702_s1581_s1586_r3658_r3549_p1328_n0139/user.gerbaudo.014081._00001.susyNt.root']"%baseDir,
                  xs = xSecVal*4.0/4.0)

baseDir='/tmp/gerbaudo/dileptonSkim/'
localWh2Lep11.add('WH_2Lep_11_ee', "['%s/skim_ee/WH_2Lep_11_1_0_skim.root']"%baseDir, xs=xSecVal*1.0/4.0)
localWh2Lep11.add('WH_2Lep_11_mm', "['%s/skim_mm/WH_2Lep_11_1_0_skim.root']"%baseDir, xs=xSecVal*1.0/4.0)
localWh2Lep11.add('WH_2Lep_11_em', "['%s/skim_em/WH_2Lep_11_1_0_skim.root']"%baseDir, xs=xSecVal*2.0/4.0)
