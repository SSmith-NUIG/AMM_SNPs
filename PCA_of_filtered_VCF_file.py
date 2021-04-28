import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler


# previous file was then used to recode the combined VCF file
# filtered_vcf contains only the SNPs of interest
# the following script will pull out the first value of each cell in the sample
# columns. A 0 means it is the same as the reference
# A 1 or 2 means there is a SNP there and it matches the first or second ALT allele

# Read in the vcf and drop unneeded columns
filtered_vcf = pd.read_csv("/home/stephen/combined.recode.vcf", sep="\t", skiprows=217)
filtered_vcf.drop(columns=["ID", "QUAL", "FILTER", "INFO", "FORMAT","#CHROM","REF","ALT"], inplace=True)

samples = ['S1', 'S12', 'S13', 'S14', 'S15', 'S17',
       'S18', 'S19', 'S2', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26',
       'S29', 'S3', 'S30', 'S31', 'S32', 'S4', 'S5', 'S6', 'S7', 'S9']

# remove everything from the cell except the first value, these are haploid so we only need the first allele call
for i in samples:
    filtered_vcf[i] = filtered_vcf[i].str.slice(stop=1)

filtered_vcf.to_csv("/home/stephen/filtered_vcf.csv", sep=",", index=False)

# transform the data
filtered_vcf = filtered_vcf.T

# set the column names as the first row
filtered_vcf.columns = filtered_vcf.iloc[0]

#remove the now duplicated first row
filtered_vcf = filtered_vcf[1:]

# get the shape of the dataframe
filtered_vcf.shape

#get all of the data into one array
x = filtered_vcf[:].values

# get the labels of the dataframe
y = filtered_vcf.index

# scale and standardise the data
x_std = StandardScaler().fit_transform(x)

# produce the covariate matrix
cov_mat = np.cov(x_std.T)

# get the eigenvalues and eigenvectors
eig_vals, eig_vecs = np.linalg.eig(cov_mat)

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort(key=lambda x: x[0], reverse=True)

tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

matrix_w = np.hstack((eig_pairs[0][1].reshape(104,1),
                      eig_pairs[1][1].reshape(104,1)))

Y = x_std.dot(matrix_w)

marker2 = []
for i in y:
    marker2.append('$' + i + "$")


with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(6, 4))
    for lab, marker in zip(y, marker2):
        plt.scatter(Y[y==lab, 0],
                    Y[y==lab, 1],
                    label=lab,
                    marker=marker,
                    s=150)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title("PCA from dora SNPs")
    plt.legend(title='Samples', bbox_to_anchor=(1.05, 1), loc='best', fontsize='x-small')
    #plt.legend(loc='right')
    plt.show()
