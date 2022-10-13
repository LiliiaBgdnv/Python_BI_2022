#**Insertion**.
This program is designed to filter the readings in a fastq file. The filtering is performed immediately by GC composition, read quality and length parameters. You can read more about quality coding [here](https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm). 


In the output you get two files with reads that passed and failed or a comment about why the files could not be saved.

# **Description**
The program is implemented using four functions. The three functions responsible for checking the parameters *GC composition*, *quality* and *reading length* are nested within the **main** function. 

To execute the program, the user must call the main function with the arguments:

1. **input_fastq** - the path to the file that is fed to the program.  
2. **output_file_prefix** - path prefix to the file in which the result will be written. To the prefix is added **"_passed.fastq"** for files with filtered reads and **"_failed.fastq"** for files and filtered reads.
3. **gc_bounds** - GC composition interval *(percentage)* or maximum value for filtering (default is (0, 100).
4. **length_bounds** - length interval for filtering (default is (0, 2**32).
5. **quality_threshold** - The threshold value of the average quality of the read for filtering (the default is 0). Reads with a quality lower than this will be filtered out.
6. **save_filtered** - whether to save the filtered readings (the default is False). You should set it to True to save the filtered reeds.


**If you don't want to filter readings by any parameter (3, 4, 5), don't specify them in the main function.**


### Description of the operation of the main function
The main function is implemented with a counter that takes a read from the list created from **input_file**, checks it for GC composition. If the percentage of guanine and cytosine is not in the specified interval, the file is written to the *failed file*, but if it is, the next check takes place. At the next step the quality line is checked for each reading. If the check fails, the reading is written to the *failed file*, otherwise a length check takes place. Only after all three checks are passed, the reading is written to the *passed file*.
