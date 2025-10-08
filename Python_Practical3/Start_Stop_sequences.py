sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
#codons = ['CCA', 'TGT', 'GTA', 'TAG']
start_codon = ['ATG']
stop_codons = ['TAA', 'TAG', 'TGA']
for sequence in sequences:
  #for codon in codons:
    #if codon in sequence:
     # print(codon + " is in " + sequence)
  for codon in start_codon:
    if codon in start_codon:
      print(start_codon + " is in " + sequence)
  for stop_codon in stop_codons:
    if stop_codon in sequence:
      print(stop_codon + " is in " + sequence)
    if start_codon in sequence and stop_codon in sequence:
      print(start_codon + " and " + stop_codon + " are in " + sequence)
