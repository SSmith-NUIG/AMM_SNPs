#!/bin/sh 
#SBATCH --job-name="combine"
#SBATCH -o /data/ssmith/logs/combine_%A_%a.out
#SBATCH -e /data/ssmith/logs/combine_%A_%a.err
#SBATCH -N 1
#SBATCH -n 8
#SBATCH -p MSC

gatk CombineGVCFs \
-R /data/ssmith/c_l_genome/apis_c_l_genome.fa \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S1.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S2.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S3.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S4.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S5.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S6.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S7.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S9.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S12.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S13.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S14.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S15.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S17.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S18.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S19.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S20.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S21.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S22.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S23.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S24.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S25.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S26.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S29.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S30.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S31.g.vcf \
--variant /data/ssmith/drone_data/cldata/GATK_c_l_output/S32.g.vcf \
-O combined_drone.g.vcf
