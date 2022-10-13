trans = str.maketrans("Tt", "Uu")    # symbols to transcribe
comp = str.maketrans("GgCcTtAa", "CcGgAaTt")    # symbols to complement
base = "AaCcGgTtUu"    # list of allowed characters

def complement(x):
      return(seq.translate(comp))
def reverse(x):
      return(x [::-1])

while True:
    command = input("Enter command: ").lower()    # please enter the command of interest
    if command == "exit":
      print("Good luck! :) ")
      break
    else:
      seq = input("Enter sequence: ")    # please enter the sequence of interest

      # sequence check
      if (not(all(ch in base for ch in seq))):
        print("Invalid alphabet. Try again!")
      elif (("T" in seq.upper()) == True) and (("U" in seq.upper()) == True):
        print("Uracil and Thymine cannot be in the same sequence. Try again!")
      else:
        # transcribe — print the transcribed sequence
        if command == "transcribe":
          print(seq.translate(trans))

        # complement — print the complementary sequence
        if command == "complement":
          print(complement(seq))

        # reverse - print the inverted sequence
        if command == "reverse":
          print(reverse(seq))

        # reverse complement - print the reverse complementary sequence
        if command == "reverse complement":
          print(reverse(complement(seq)))
