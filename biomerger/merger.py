from Bio import SeqIO
import os
import sys
import itertools
import gzip
import shutil
from itertools import zip_longest

def merge(files, f_out, compress=True):

    #p1 = os.path.join(location, f1)
    #p2 = os.path.join(location, f1)
    #out = os.path.join(location, f_out)

    outfile = open(f_out,"w")
    fastq_iters = []
    for f in files:
        try:
            fastq_iters.append(SeqIO.parse(open(f),"fastq"))
        except:
            fastq_iters.append(SeqIO.parse(gzip.open(f), "fastq"))

    for t in zip_longest(fastq_iters):
        add = []
        for rec in t:
            if(rec != None):
                add.append(rec)
        SeqIO.write(add, outfile, "fastq")
    outfile.close()

    #compress
    if compress:
        with open(f_out, 'rb') as f_in, gzip.open("{}.gz".format(f_out), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

