#!/bin/sh 
#SBATCH --job-name="genotype"
#SBATCH -o /data/ssmith/logs/gtype_%A_%a.out
#SBATCH -e /data/ssmith/logs/gtype_%A_%a.err
#SBATCH -N 1
#SBATCH -n 4
#"$SLURM_ARRAY_TASK_ID"
gatk GenotypeGVCFs \
-R /data/ssmith/c_l_genome/apis_c_l_genome.fa \
-V /data/ssmith/scripts/drone_analysis/combined_drone_ID.g.vcf \
-O /data/ssmith/scripts/drone_analysis/combined_genotyped.vcf
