from Bio import SeqIO
import os
import sys
import itertools
import gzip
import shutil

def merge(f1, f2, f_out, compress=True):

    #p1 = os.path.join(location, f1)
    #p2 = os.path.join(location, f1)
    #out = os.path.join(location, f_out)

    outfile = open(f_out,"w")
    fastq_iter1 = SeqIO.parse(open(f1),"fastq")
    fastq_iter2 = SeqIO.parse(open(f2),"fastq")
    for rec1, rec2 in zip(fastq_iter1, fastq_iter2):
        SeqIO.write([rec1,rec2], outfile, "fastq")
    outfile.close()

    #compress
    if compress:
        with open(f_out, 'rb') as f_in, gzip.open("{}.gz".format(f_out), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

