# python script to convert a NASA Horizons Ephemerides download to a format that Stellarium can consume

import sys
import os
import json


def processFile(filename):
    here = os.path.split(os.path.abspath(__file__))[0]
    outfname = os.path.join(here, os.path.splitext(os.path.basename(filename))[0] + '.inc')
    currentf = os.path.join(here, 'current_object.inc')

    # obtain the data
    flines = open(filename, 'r').readlines()

    objname = [f for f in flines if 'Target body name:' in f]
    if len(objname) > 0:
        objname = objname[0].split(':')[1]
        objname = objname.split('(')[0]
        objname = objname.strip().replace(' ','_')
    else:
        objname = 'MyObject'

    datablock = []
    startdata = False
    labelpoint = 0
    for li in flines:
        if li[:5] == '$$SOE':
            startdata = True
        if li[:5] == '$$EOE':
            break
        if startdata and li[:5] != '$$SOE':
            if not labelpoint %10:
                label = li[:18].strip().replace(' ', '_')
            else:
                label = ' '
            labelpoint += 1
            ra = li[23:34]
            dec = li[35:46]
            outl = {'label': label, 'ra': ra, 'dec': dec}
            datablock.append(outl)

    with open(outfname,'w') as outf:
        outf.write(f'var objname = "{objname}";\n\n')
        outf.write('var currentobject = \n')
        outf.write(json.dumps(datablock).replace('}, {', '}, \n{'))
        outf.write(';\n')

    with open(currentf,'w') as outf:
        outf.write(f'var objname = "{objname}";\n\n')
        outf.write('var currentobject = \n')
        outf.write(json.dumps(datablock).replace('}, {', '}, \n{'))
        outf.write(';\n')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python convertHorizons.py srcfile\n')
    else:
        processFile(sys.argv[1])
