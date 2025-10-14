from Bio import SeqIO
import csv

Input_file = 'dna.fasta'
Output_file = 'sequence_length.csv'

# A) Load and report (use SeqIO)

# - Read all records from `dna.fasta`.
# - For each record, print the record ID and the sequence length.
# - Also print the first 10 bases of the sequence.

with open(Output_file, 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Header', 'Length', 'Start'])  # Write header row

    for record in SeqIO.parse(Input_file, "fasta"): # Iterate over each record
        header = record.id # Get record ID
        sequence = str(record.seq)  # Convert sequence to string
        count = len(sequence) # Get sequence length
        start = sequence[:10] # Get first 10 bases
        writer.writerow([header, count, start])  # Write data row
        print(f"{header} starts with {start} and has {count} nucleotides.") # Print to console

# B) Reverse complements to a new FASTA (use Seq, SeqRecord, SeqIO)

# - For each original record, create the reverse complement of its sequence.
# - Make a new SeqRecord for the reverse complement.
# - Set the new ID to "<oldid>_rc" and the description to "reverse complement of <oldid>".
# - Write all reverse-complement records to a file named `dna_rc.fasta`.

for record in SeqIO.parse(Input_file, "fasta"): # Iterate over original records
    rc_sequence = record.seq.reverse_complement() # Get reverse complement
    rc_record = SeqIO.SeqRecord( # Create new SeqRecord
        rc_sequence, # Reverse complement sequence
        id=f"{record.id}_rc", # New ID
        description=f"reverse complement of {record.id}" # New description
    )
    with open('dna_rc.fasta', 'a') as output_handle: # Append mode
        SeqIO.write(rc_record, output_handle, "fasta") # Write to file
    #print(f"Wrote reverse complement for {record.id} to dna_rc.fasta")  # Print confirmation

# C) GC% annotation to a new FASTA (use SeqRecord, SeqIO)

# - For each original record, calculate GC% = 100 * (count of 'G' + count of 'C') / length.
# - Round to 1 decimal place.
# - Create a copy of the record where the description includes "GC=<value>%".
# - Write these annotated records to `dna_with_gc.fasta`.

for record in SeqIO.parse(Input_file, "fasta"): # Iterate over original records 
    sequence = str(record.seq).upper() # Ensure case insensitivity
    gc_count = sequence.count('G') + sequence.count('C') # Count G and C
    gc_percent = round(100 * gc_count / len(sequence), 1) # Calculate GC%
    annotated_record = SeqIO.SeqRecord( # Create new SeqRecord
        record.seq, # Same sequence
        id=record.id, # Same ID
        description=f"{record.description} GC={gc_percent}%" # Annotated description with GC%
    )
    with open('dna_with_gc.fasta', 'a') as output_handle: # Append mode
        SeqIO.write(annotated_record, output_handle, "fasta") # Write to file
    #print(f"Wrote GC% annotated record for {record.id} to dna_with_gc.fasta") # Print confirmation

# D) Translation (Optional, do if you have extra time)

# - Translate each DNA sequence and print the first 10 amino acids.
# - Read `dna_rc.fasta` back in and confirm IDs/descriptions look correct.

for record in SeqIO.parse(Input_file, "fasta"): # Iterate over original records
    protein_sequence = record.seq.translate(to_stop=True) # Translate DNA to protein, stop at first stop codon
    print(f"{record.id} translates to {str(protein_sequence)[:10]}...") # Print first 10 amino acids
