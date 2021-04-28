import pandas as pd

# processing output hit file from BLAST
# BLAST against the 3.1 genome using the blast_file.fa created previously
hit_df = pd.read_csv("/home/stephen/dora_snps_hit_table.csv", sep=",")

hit_df_filtered = hit_df[(hit_df["alignment_length"]>120)]

filter = list(hit_df_filtered["query_name"])
original = list(hit_df["query_name"])

# checking why some sequences are outside of the filter criteria
# these will have to be manually dealt with in excel
for i in original:
    if i not in filter:
        print(i)

hit_df_filtered["genomic_start"] = hit_df_filtered[["subject_start","subject_end"]].min(axis=1)

# adding 60 bp to the genomic start, this is because the flanking region
# is 60bps, this is not 100% accurate as there are gaps and different starting
# positions to deal with but it gives a good approximation
# this will be edited manually when these positions are checked using a genome viewer
hit_df_filtered["new genomic location"] = hit_df_filtered["genomic_start"] + 60

hit_df_filtered.to_csv("/home/stephen/dora_snps_new_location.csv",sep=",", index=False)
