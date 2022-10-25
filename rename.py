import os
import glob
import shutil



method = 'SR'

path = '/home/marxt/phd/comparison_paper/analysis/std_res-analysis/results'

filenames = glob.glob(path + '/*.tif')

for in_file in filenames:
    in_bname = os.path.basename(in_file)
    print(in_bname)

    if 'hm' in in_bname:
        ref = 'HDOY'
    elif 'rm_' in in_bname:
        ref = 'MEAN'
    elif 'sg2' in in_bname:
        ref = 'PRI'
    else:
        continue

    if 'otsu' in in_bname:
        thres = 'OTSU'
    elif 'ki' in in_bname:
        thres = 'KI'
    elif 'fixed' in in_bname:
        thres = 'FIX'

    if 'nofilt' in in_bname:
        hfilt = 'NONE'
    else:
        hfilt = 'HAND'


    out_bname = '{}_{}_{}_{}.tif'.format(method, ref, thres, hfilt)
    out_file = in_file.replace(in_bname, out_bname)
    print(in_file)
    print(out_file)
    shutil.copyfile(in_file, out_file)

    hfilt = None
    ref = None
    thres = None

