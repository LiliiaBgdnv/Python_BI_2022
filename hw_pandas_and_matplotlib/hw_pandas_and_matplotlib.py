#Download data from google disk if you work in Colab, insert your path to the file 
# "rrna_annotation.gff" and "alignment.bed"!!!

#!gdown --id 1fbxXxumB1rDNTLkAfhajSLJcqwGBdwG7 # rrna_annotation.gff
#!gdown --id 1UaQ51vAi8CFzISJYsJKzdH4TaG5ndWzo # alignment.bed

path_rrna_annotation = 'C://jupyter//rrna_annotation.gff'
path_alignment = 'C://jupyter//alignment.bed'
import pandas as pd
#function to read a gff file
def read_gff(gff_file):
    gff_table = pd.read_csv(
        gff_file,
        sep="\t",
        header=None,
        comment="#",
        names=("chromosome", "source", "type", "start",
               "end", "score", "strand", "phase", "attribute"))
    return(gff_table)
gff_table = read_gff(path_rrna_annotation)

#leave only rRNA type data (16S, 23S, 5S)
gff_table['attribute'] = gff_table['attribute'].str[5:8].str.replace(r'_','')
gff_table
#function to read a bed file
def read_bed6(bed_file):
    bed_table = pd.read_csv(
        bed_file,
        sep='\t',
        comment='#',
        header=None,
        names = ("chromosome", "start", "end", "name", "score", "strand"))
    return bed_table
bed_table = read_bed6(path_alignment)
bed_table
# table showing for each chromosome the number of rRNAs of each type

table_for_rRNA = gff_table.groupby(['chromosome', 'attribute'])["attribute"].count().unstack().fillna(0)
a = table_for_rRNA.index.to_series().str.rsplit('_').str[-1].astype(int).sort_values()
table_for_rRNA = table_for_rRNA.reindex(index=a.index)
table_for_rRNA
#visualization
table_for_rRNA.plot.bar(xlabel='Sequence', ylabel='Count', figsize=(15, 7));
#table containing the initial records of the rRNAs that are fully included in the assembly,
# as well as a record of the contig in which this rRNA is included

merge_table = pd.merge(gff_table,bed_table, on="chromosome", how="outer")
merge_table[(merge_table['start_x'] >= merge_table['start_y']) & (merge_table['end_x'] <= merge_table['end_y'])]


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

#Download data from google disk if you work in Colab, insert your path to the file "diffexpr_data.tsv.gz"!!!

#!gdown --id 1TcZWPE2vd4M7JAMHLp5bQHvyg08sK1qY
diffexpr = 'C://jupyter//diffexpr_data.tsv.gz'
diffexpr_data = pd.read_csv(diffexpr,
                           sep='\t',
                           comment='#')
diffexpr_data
#function to determine the gene category depending on the p-value and log "fold change"
def label_maker(p, fold):
    if fold < 0:
        if p < 0.05:
            return 'Significantly downregulated'
        else:
            return 'Non-significantly downregulated'
    else:
        if p >= 0.05:
            return 'Non-significantly upregulated'
        else:
            return 'Significantly upregulated'
#create a new column to display the category
diffexpr_data['Lable'] = diffexpr_data.apply(lambda x: label_maker(x['pval_corr'], x['logFC']), axis=1)
#select the data with the min log "fold change" and p-value > 0.05
Sd = diffexpr_data[diffexpr_data['Lable'] == 'Significantly downregulated']
Sd = Sd.sort_values(by='logFC')
#select the data with the max log "fold change" and p-value > 0.05
Su = diffexpr_data[diffexpr_data['Lable'] == 'Significantly upregulated']
Su = Su.sort_values(by='logFC', ascending=False)
#Set boundaries for the X-axis
x_min = round(diffexpr_data['logFC'].min(), 1) - 1
x_max = round(diffexpr_data['logFC'].max(), 1) + 1.5

#set graph size
fig, ax = plt.subplots(figsize=(15, 10))

#install the font
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.bf'] = 'Arial:italic:bold'

#add title and lables
plt.title('Volcano plot', weight='bold', style='italic', size=25)
plt.xlabel(r'$\mathbf{\bf{log_2(fold\ change)}}$', size=14)
plt.ylabel(r"$\mathbf{-log_{10}(p \ value \ corrected)}$", size=14)

#divide the data into 4 groups and visualize
label_names = list(set(diffexpr_data['Lable']))
for i in range(4):
  l = diffexpr_data[diffexpr_data['Lable'] == label_names[i]]
  plt.scatter(l['logFC'], l['log_pval'], label=label_names[i], s=9)

#add legend
legend_properties = {'weight':'bold'} #add a bold typeface
plt.legend(shadow=True, markerscale=3, prop=legend_properties)

#set the boundaries of the X-axis
plt.xlim(x_min, x_max)
 
#add ticks on X and Y lable
fig.gca().yaxis.set_minor_locator(ticker.MultipleLocator(5))
fig.gca().xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.tick_params(which='major', width=2, length=7, labelsize=12)
ax.tick_params(which='minor', width=1.2, length=3)
#add a dashed gray line
ax.axhline(y=-np.log10(0.05), linestyle= '--', color='gray', linewidth=2)
ax.axvline(x=0, linestyle= '--', color='gray', linewidth=2)

#change the border width
for axis in ['top','bottom','left','right']:
    fig.gca().spines[axis].set_linewidth(2)

#add the phrase "p value"
ax.annotate('p value = 0.05',
            xy=(770, 85), xycoords='figure points', color = 'gray', weight='semibold', size = 12)

#add arrows and signatures for the top 2 genes that significantly decreased expression and the
#top 2 genes that significantly increased expression
ax.annotate(Sd.iloc[0][0], xy=(Sd.iloc[0][1], Sd.iloc[0][4]), xytext=(Sd.iloc[0][1] - 0.9, Sd.iloc[0][4] + 8),
            arrowprops=dict(arrowstyle="simple", facecolor='red'), weight='semibold', size=10)
ax.annotate(Sd.iloc[1][0], xy=(Sd.iloc[1][1], Sd.iloc[1][4]), xytext=(Sd.iloc[1][1] - 1, Sd.iloc[1][4] + 8),
            arrowprops=dict(arrowstyle="simple", facecolor='red'), weight='semibold', size=10)
ax.annotate(Su.iloc[0][0], xy=(Su.iloc[0][1], Su.iloc[0][4]), xytext=(Su.iloc[0][1] - 1, Su.iloc[0][4] + 8),
            arrowprops=dict(arrowstyle="simple", facecolor='red'), weight='semibold', size=10)
ax.annotate(Su.iloc[1][0], xy=(Su.iloc[1][1], Su.iloc[1][4]), xytext=(Su.iloc[1][1] - 1, Su.iloc[1][4] + 8),
            arrowprops=dict(arrowstyle="simple", facecolor='red'), weight='semibold', size=10);
