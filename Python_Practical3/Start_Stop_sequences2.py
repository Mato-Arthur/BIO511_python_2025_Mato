sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']

start_codons = ['ATG']
stop_codons = ['TAA', 'TAG', 'TGA']

for sequence in sequences:
    print(f"\nAnalyzing sequence: {sequence}")
    flag = True
#Checking for start codons and defining position of start codon
    for start in start_codons:
        if start in sequence:
            print(start + " is in " + sequence)
            position_start = sequence.index(start) 
#Checking for stop codons and defining position of stop codon
    for stop in stop_codons:
        if stop in sequence:
            print(stop + " is in " + sequence)
            position_stop = sequence.index(stop)
#Checking if both start and stop codons are in the same sequence
            if start in sequence and stop in sequence and flag == True:
                flag = False
                print(start + " and " + stop + " are in " + sequence)
#Checking if start codon is before stop codon
            if position_start < position_stop: 
                print("The start codon is before the " + stop + " in " + sequence)
            else :
                print("The start codon is not before the " + stop + " in " + sequence)  
