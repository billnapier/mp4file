#!/usr/bin/python
'''
Created on Dec 6, 2009

@author: napier
'''

from mp4file.mp4file import Mp4File

def print_atoms(parent, indent=0):
    for atom in parent.get_atoms():
        print "%s %s/%s %d" % (("-" * indent), atom.type, atom.name, atom.size)
        print_atoms(atom, indent=indent+1)

def find_metadata_atom(file, name):
    atom = file.find('.//%s//data' % name)
    return atom.get_attribute('data')

def print_all_metadata_atoms(file):
    atoms = file.findall('.//data')
    for atom in atoms:
        data = atom.get_attribute('data')
        print atom.parent.name, data

if __name__ == '__main__':
    file = Mp4File("/home/napier/bill.mp4")

    title = find_metadata_atom(file, 'title')
    tvshow = find_metadata_atom(file, 'tvsh')
    tvepisodenum = find_metadata_atom(file, 'tvepisode')
    tvseason = find_metadata_atom(file, 'tvseason')
    #track = find_metadata_atom(file, 'trkn')
    print title, tvshow, tvepisodenum, tvseason
    #print_atoms(file)
