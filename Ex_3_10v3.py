#take first two sequences from the ls_orchid.fasta file (from biopython.org)

from Bio import SeqIO
handle = open("ls_orchid.fasta")
record_iterator = SeqIO.parse(handle, "fasta")
rec_one = record_iterator.next()
rec_two = record_iterator.next()
handle.close()
seq_one = rec_one.seq
seq_two = rec_two.seq
################################################

#compare sequences

window = 5 # No of characters taken
#print seq_one
#print seq_two
data = []
#data.append(2+4j)
for i in range(len(seq_one)-window):
    for j in range(len(seq_two)-window):
        if str(seq_one[i:i+window]) == str(seq_two[j:j+window]):
            data.append(i+j*1j)
            #print seq_one[i:i+window],'   ',seq_two[j:j+window]
            
################################################

#plot the results

# losungen plotten funktioniert nicht, weil matplotlib ein problem hat.
# das vergleichen der sequenzen funktioniert einwandfrei
# ich weiss nicht, was ich noch mehr machen konnte, ich habe schon etwa
# 5 modul installiert, aber irgendwie stimmt im matplotlib die syntax nicht :(



#import dateutil
import matplotlib.pyplot as plt
#import pylab
pylab.gray() #black-white
plt.plot(data)
plt.xlabel("%s (length %i bp)" % (rec_one.id, len(rec_one))) #label of x-axis
plt.ylabel("%s (length %i bp)" % (rec_two.id, len(rec_two))) #label of y-axis
plt.title("Dot plot using window size %i\n(allowing no mis-matches)" % window) #title of plot
plt.show()
