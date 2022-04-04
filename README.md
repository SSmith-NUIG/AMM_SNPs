# AMM_SNPs
Workflow for updating SNP locations from old genome to new genome

This workflow uses the VCF files created from GATKs haplotype caller using the clpipeline.sh script

It is designed to look for a list of SNPs as detailed in pinto et al 2016.
This paper used the old honeybee genome and as such, the locations are not correct in the new 3.1 genome

dora.snps is a file with the information of the SNPs identified in pinto et al.
This file has a column which contains the SNP and 60bp of flanking region either side of the SNP.

We will be using BLAST to search the new genome for this ~122bp sequence. This will give us the location
of the SNP in the new genome.

First we need to create a file to submit to BLAST, this is in the FASTA format.
Run the Create_BLAST_input_file.py to create this file.

Then go to BLAST https://blast.ncbi.nlm.nih.gov/Blast.cgi and enter apis mellifera in the BLAST genomes input box
Hit search and the new 3.1 genome should appear in the database dropdown box.

Upload the blast_file.fa which you have created.

Once the analysis has completed, download the hit_table.csv

Run BLAST_output_filtering.py on this file to create a filtered dataframe which contains (most) of the correct hits

These new SNP locations were manually checked using the tablet genome browser https://ics.hutton.ac.uk/tablet/ though
any genome browser should be perfectly fine.

Each new SNP location was entered by jumping to that location and looking to see if the SNP location matches the sequence in 
the original dora_snps.csv file. Some were a few bases off due to gaps etc.

Some SNPS (four) were missing completely from the new genome location file and had to be entered manually. This was due to their
flanking regions being quite different in the new genome compared to the old genome and so the matched length from BLAST was a lot
shorter than ~122bp.

Once we have the correct genome locations we use genome_positions_for_VCFtools.py to create the positions.txt file required by
VCFtools.


To create the combined VCF file which we will use as input for VCFtools we can run combining_gvcfs.sh to create a single joint VCF.
We can also annotate this VCF using annotate_VCF.sh (useful for STRUCTURE input).

Now we can run VCFtools to filter our combined VCF file so that it only contains the information relating to the
pinto et al list of SNPs.

Use amm_snp_filtering.sh for this.

To visualise our VCF file we can run PCA_of_filtered_VCF_file.py. This creates a rough PCA plot to allow some initial visualisation
and analysis before more stringent methods are used (STRUCTURE etc.)
