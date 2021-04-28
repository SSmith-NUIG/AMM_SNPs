import pandas as pd

# creating input file for BLAST
# dora_snps.csv contains flanking regions used during SNP assays
df = pd.read_csv("/home/stephen/dora_snps.csv")

# SNPs are surrounded by [] brackets, remove these
seq_to_blast = df["Flanking regions and [SNP]"].str.replace('[^a-zA-Z]','')
gene_id = df["Gene_ID"]

outfile = open("/home/stephen/blast_file.fa", "w")

# write each flanking sequence to a new file in FASTA format
for i,j in zip(gene_id, seq_to_blast):
    outfile.write(">" + i + "\n" + j + "\n")
outfile.close()
