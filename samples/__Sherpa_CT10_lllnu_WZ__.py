from supy.samples import SampleHolder
Sherpa_CT10_lllnu_WZ = SampleHolder()

xSecVal = 9.7508 # fb


baseDir = '/gdata/atlas/ucintprod/SusyNt/mc12_n0145/'
baseDir += 'user.sfarrell.mc12_8TeV.126893.Sherpa_CT10_lllnu_WZ.SusyNt.e1434_s1499_s1504_r3658_r3549_p1512_n0145/'
Sherpa_CT10_lllnu_WZ.add('Sherpa_CT10_lllnu_WZ',
                         "utils.fileListFromDisk(location = '%s/*.root*', isDirectory = False)"%baseDir,
                         xs=xSecVal)
