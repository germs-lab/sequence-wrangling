import screed
import sys

#python subset-by-start-stop.py [fasta_file] [start - min 1] [end]

start = int(sys.argv[2])
end = int(sys.argv[3])
for record in screed.open(sys.argv[1]):
    id = record.name
    genome = record.sequence
    print genome[start-1:end]
