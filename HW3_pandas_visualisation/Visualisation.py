import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

df = pd.read_table('diffexpr_data.tsv.gz')
print(df)

df

conditions = [
    (df['pval_corr'] < 0.05) & (df['logFC'] < 0),
    (df['pval_corr'] < 0.05) & (df['logFC'] >= 0),
    (df['pval_corr'] >= 0.05) & (df['logFC'] < 0),
    (df['pval_corr'] >= 0.05) & (df['logFC'] >= 0)

]

values = ['Non-significantly upregulated', 'Non-significantly downregulated',
            'Significantly downregulated', 'Significantly upregulated']

df['labels'] = np.select(conditions, values)

largest = df[df['labels'].str.startswith('S')].nlargest(2, 'logFC')
smallest  = df[df['labels'].str.startswith('S')].nsmallest(2, 'logFC')

labels = {'Significantly downregulated':'blue', 'Significantly upregulated':'orange',
            'Non-significantly downregulated':'green', 'Non-significantly upregulated':'red'}



fig, ax = plt.subplots(figsize=(11,6))
plt.setp(ax.spines.values(), linewidth=1.5)
plt.scatter(df['logFC'], df['log_pval'] )


plt.axvline(x = 0, color='gray', linestyle='--')
plt.axhline(-np.log10(0.05), color='gray', linestyle='--')
plt.text(8, -np.log10(0.05), 'p value=0.05', weight='bold', c='gray', alpha = 0.6)


plt.xlabel(r'$\mathbf{\bf{log_2(fold \ change)}}$', size=12)
plt.ylabel(r"$\mathbf{\bf{-log_{10}(p \ value \ corrected)}}$", size=12)
plt.title(r'$\mathbf{\bf{Volcano \ plot}}$', size=14)

plt.minorticks_on()
plt.xticks(weight='bold')
plt.yticks(weight='bold')
plt.xlim(df.logFC.min() - 0.8, df.logFC.max() + 0.8)
plt.ylim(df.log_pval.min() - 6, df.log_pval.max() + 6)

plt.autoscale()

plt.savefig('volcplot.png', dpi = 300, bbox_inches = 'tight', edgecolor = 'b')


