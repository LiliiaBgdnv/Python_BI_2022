The script is written based on Python 3.9 in Google Colab using the libraries `pandas 1.5.1`, `numpy 1.23.4`, `matplotlib 3.6.2`.

The first part of the script opens two files `.gff` and `.bed`. The **read_gff** function reads the `.gff` file and then the attribute column is edited, leaving only the rRNA type data.

The function **read_bed6** reads the `.bed` file.

Next, the amount of each rRNA type for each chromosome and visualize the data visualized.

The last part of this task selects only those rRNAs that have successfully assembled.

The second part of the script is about visualizing differential gene expression data, imitating the volcano plot.

The data are preprocessed before plotting.  The gene category depending on the `p-value` and log from `fold change` determined and entered in a new column. We select the data to display the top 2 genes that significantly decreased expression, and the top 2 genes that significantly increased expression.

The graph contains edits: 
> - 1. Four segments on the graph
> - 2. Axes and labels.
    
    a. xlabel, ylabel and title - in bold italics, sized +- as in the picture
    
    b. The base of the logarithm in lower case
    
    с. Size and thickness of the ticks on the X and Y axes (minor ticks must be displayed)
    
    d. Thickness of axes.
> - 3. Legend.
    
    a. Size and font of letters in the legend
    
    b. Size of the markers in the legend
    
    с. A small shadow from the legend to the right down
> - 4. Pronounce the top 2 genes that significantly decreased expression and the top 2 genes that significantly increased expression
    
    a. Arrows
    
    b. Text at the arrows
      
