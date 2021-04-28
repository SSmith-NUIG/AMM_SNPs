import pandas as pd

# this script will create a positions file needed for VCFtools
# it is in the form Chromosome {tab} position

# read in the snp file which has now has an update column containing
# the positions of the SNPs in the new genome
dora_snp_file = pd.read_csv("/home/stephen/dora_snps.csv")

LGs = dora_snp_file["Linkage group"]
positions = dora_snp_file["New genomic position"]

outfile = open("/home/stephen/vcftools_positions.txt", "w")

for i, j in zip(LGs, positions):
   outfile.write(i + "\t" + str(j) + "\n")

outfile.close()
