"""GC-check function"""
def gc_count_fun(f, gc_bounds=(0, 100)):
  cnt=0
  #Counting the amount of cytosine and guanine in a string
  for nucl in f:
    if (nucl == 'C') or (nucl == 'G'):
      cnt += 1
  #Checking and defining boundaries
  if type(gc_bounds) == tuple:
    right_margin = gc_bounds[1]
    left_margin = gc_bounds[0]
  else:
    right_margin = gc_bounds
    left_margin = 0

  if right_margin >= ((cnt/len(f))*100) >= left_margin:
     return 1
  else:
    return 0

"""Read quality check function"""
def quality_fun(f, quality_threshold = 0):
  phred_value=0
  for symbol in f:
    phred_value += (ord(symbol) - 33)
  if quality_threshold <= (phred_value/len(f)):
    return 1
  else:
    return 0

"""Length check function"""
def len_fun(f, length_bounds = (0, 2**32)):
  #Checking and defining boundaries
  if type(length_bounds) == tuple:
    right_margin = length_bounds[1]
    left_margin = length_bounds[0]
  else:
    right_margin = length_bounds
    left_margin = 0

  if right_margin >= len(f) >= left_margin:
      return 1
  else:
      return 0

"""Main function"""
def main(input_fastq, output_file_prefix, gc_bounds = (0, 100), length_bounds =  (0, 2**32), quality_threshold = 0, save_filtered = False):
  #Opening an input file and writing it to the variable f with removing \n at the ends
  with open(input_fastq, 'r') as input:
      f = input.read().split('\n')
      #Checking whether files need to be saved
      if save_filtered == True:
        with open((str(output_file_prefix) + "_passed.fastq"), 'w') as output_passed, open((str(output_file_prefix) + "_failed.fastq"), 'w') as output_failed:

          for i in range(1, len(f), 4):
            if GC_count_fun(f[i], gc_bounds) == 1:
              if quality_fun(f[i+2], quality_threshold) == 1:
                if len_fun(f[i], length_bounds) == 1:
                  #If the reading passes all the checks, it is written to the file passed
                  for j in range(-1, 3, 1):
                    output_passed.write(f[i+j]+'\n')
                else:
                  #If a reading passes the length check, it is written to the missed file
                  for j in range(-1, 3, 1):
                    output_failed.write(f[i+j]+'\n')
              else:
                #If a reading passes the quality check, it is written to the missing file
                for j in range(-1, 3, 1):
                  output_failed.write(f[i+j]+'\n')
            else:
              #If a reading passes the GC-check in %, it is written to the missing file
              for j in range(-1, 3, 1):
                output_failed.write(f[i+j]+'\n')
      else:
        print('The parameter "save_filtered" is specified as False, so there are no output files.')
