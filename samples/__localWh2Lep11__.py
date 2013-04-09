from supy.samples import SampleHolder
localWh2Lep11 = SampleHolder()

xSecVal = 1.140 #pb # 1.1402753294*0.30636*0.3348500000
localWh2Lep11.add('WH_2Lep_11', '["/tmp/wA_noslep_WH_2Lep_11/NTUP_SUSY.01176858._000001.root.1"]', xs = xSecVal)

baseDir='/tmp/gerbaudo/dileptonSkim/'
brWl=0.10
localWh2Lep11.add('WH_2Lep_11_ee', "['%s/WH_2Lep_176584_1_0_skim_ee.root']"%baseDir, xs=xSecVal*brWl*brWl)
localWh2Lep11.add('WH_2Lep_11_mm', "['%s/WH_2Lep_176584_1_0_skim_mm.root']"%baseDir, xs=xSecVal*brWl*brWl)
localWh2Lep11.add('WH_2Lep_11_em', "['%s/WH_2Lep_176584_1_0_skim_em.root']"%baseDir, xs=xSecVal*2.0*brWl*brWl)


