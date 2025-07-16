filename ='C:\\Users\\aaronf.WISMAIN\\Downloads\\IFNalpha.fasta'
with open(filename, 'r') as fh:
    seq = fh.read()
codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP' : ['TAA', 'TAG', 'TGA']
}
atg_index = seq.find('ATG')
trimmed_seq = seq[atg_index:]
codons = [trimmed_seq[i:i+3] for i in range(0, len(trimmed_seq), 3)]
#print(atg_index)
#(codons)
# print(aa_count)



aa_count = {aa: 0 for aa in codon_table.keys()}


for codon in codons:
    found = False
    for aa, codon_list in codon_table.items():
        if codon in codon_list:
            aa_count[aa] += 1
            found = True
            if aa == 'STOP':

                print("\nAmino Acid Counts (up to first STOP):")
                for aa_out, count in aa_count.items():
                        print(f"{aa_out}: {count}")
                exit()
            break

print("\nAmino Acid Counts (no STOP codon found):")
for aa, count in aa_count.items():
    print(f"{aa}: {count}")
