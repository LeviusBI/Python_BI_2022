import pandas as pd
import numpy as np

# function to read gff files
def read_gff(gfffile):
    df = pd.read_csv(gfffile, sep='\t', comment='t', header = 0, names=['Chromosome', 'source',
                                                                        'type', 'start',
                                                                        'end', 'score',
                                                                        'strand', 'phase', 'atributes'])
    return df

# function to read bed files
def read_bed6(bedfile):
    df = pd.read_csv(bedfile, sep='\t', header = 0, names = ['Chromosome', 'start',
                                                             'end', 'name', 
                                                             'score', 'strand'])
    return df


table_bed = read_bed6('alignment.bed')
print(table_bed)
table_gff = read_gff('rrna_annotation.gff')
print(table_gff)

table_gff['atributes']=table_gff['atributes'].replace(['Name=16S_rRNA;produc', 
                                                       'Name=5S_rRNA;produc', 
                                                       'Name=23S_rRNA;produc'], 
                                                       ['16S', '5S', '23S'])


table_gff['atributes']

table_gff['atributes']

rna_p_chr = table_gff.groupby(by=['Chromosome', 'atributes']).size() #size is used, 'cause .groupby returns pandas 
                                                                     #object

print(rna_p_chr) 

rna_p_chr.unstack().plot.bar(figsize=(13,5), color={'16S':'pink', '23S':'yellow', '5S':'cyan'})

suc_rna = pd.merge(table_gff,table_bed, on="Chromosome", how="outer")
suc_rna[(suc_rna['start_x'] >= suc_rna['start_y']) & (suc_rna['end_x'] <= suc_rna['end_y'])]