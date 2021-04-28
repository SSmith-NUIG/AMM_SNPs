#!/bin/sh 
#SBATCH --job-name="amm_purity"
#SBATCH -o /data/ssmith/logs/amm_purity_%A_%a.out
#SBATCH -e /data/ssmith/logs/amm_purity_%A_%a.err
#SBATCH -N 1
#SBATCH -n 4
#"$SLURM_ARRAY_TASK_ID"
vcftools \
--vcf /data/ssmith/scripts/drone_analysis/combined_genotyped.vcf \
--out /data3/ssmith/drone_amm/combined \
--positions /data/ssmith/scripts/vcftools_positions.txt \
--recode --recode-INFO-all \
--minDP 5
