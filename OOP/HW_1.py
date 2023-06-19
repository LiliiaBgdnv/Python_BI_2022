# Task 1
import datetime

class User:
    def __init__(self, user):
        self.user = user

class Message(User):
    def __init__(self, user, text):
        self.text = text
        self.user = user
        self.datetime = datetime.datetime.now()

    def show(self):
        #self.datetime = datetime
        print(f"[{self.datetime}] {self.user}: {self.text}")

    def send(self):
        return (f"[{self.datetime}] {self.user}: {self.text}")

class Chat(Message):
    def __init__(self, chat_history):
        self.chat_history = chat_history
        self.datetime_history = []

    def recieve(self, message):
        self.chat_history.insert(0, message)

    def show_last_message(self):
         print(self.chat_history[0])

# get_history_from_time_period я не реализовала :(

    def show_chat(self):
        for message in self.chat_history:
            print(message)

empty_chat_history = []
chat = Chat(empty_chat_history)
user1 = User('Scott')
user2 = User('Ramona')

message1 = Message(user2.user, 'What kind of tea do you want?')
send_message1 = message1.send()
chat.recieve(send_message1)
message1.show()

message2 = Message(user1.user, "There's more than one kind?")
send_message2 = message2.send()
chat.recieve(send_message2)
message2.show()

message3 = Message(user2.user, """We have blueberry, raspberry, ginseng, sleepy time, green tea,
green tea with lemon, green tea with lemon and honey, liver disaster, ginger with
honey, ginger without honey, vanilla almond, white truffel, blueberry chamomile, 
vanilla walnut, constant comment and... earl grey.""")
send_message3 = message3.send()
chat.recieve(send_message3)
message3.show()

message4 = Message(user1.user, "Did you make some of those up?")
send_message4 = message4.send()
chat.recieve(send_message4)
message4.show()

chat.show_chat()

chat.show_last_message()

# Task 2
class Args:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __rlshift__(self, f):
        return f(*self.args, **self.kwargs)
sum << Args([1, 2])
(lambda a, b, c: a**2 + b + c) << Args(1, 2, c=50)

# Task 3

class StrangeFloat(float):
    def __getattr__(self, attr):
        if "_" in attr:
            action, number = attr.split("_")
            if action == "add":
                return StrangeFloat(self.__add__(float(number)))
            elif action == "subtract":
                return StrangeFloat(self.__sub__(float(number)))
            elif action == "multiply":
                return StrangeFloat(self.__mul__(float(number)))
            elif action == "divide":
                return StrangeFloat(self.__truediv__(float(number)))
        raise AttributeError(f"'{type(self).__attr__}' object has no attribute '{attr}'")
number = StrangeFloat(3.5)
number.add_1
number.subtract_20
number.multiply_5
number.divide_25
number.add_1.add_2.multiply_6.divide_8.subtract_9
getattr(number, "add_-2.5")   # Используем getattr, так как не можем написать number.add_-2.5 - это SyntaxError
number + 8   # Стандартные для float операции работают также
number.as_integer_ratio()   # Стандартные для float операции работают также  (это встроенный метод float, писать его НЕ НАДО)

#Task 4
# Before:
import numpy as np


matrix = []
for idx in range(0, 100, 10):
    matrix += [list(range(idx, idx + 10))]
    
selected_columns_indices = list(filter(lambda x: x in range(1, 5, 2), range(len(matrix))))
selected_columns = map(lambda x: [x[col] for col in selected_columns_indices], matrix)

arr = np.array(list(selected_columns))

mask = arr[:, 1] % 3 == 0
new_arr = arr[mask]

product = new_arr @ new_arr.T

if (product[0] < 1000).all() and (product[2] > 1000).any():
    print(product.mean())

# After

# Ваш код здесь
import numpy as np


matrix = []
for idx in range(0, 100, 10):
    matrix.__iadd__([list(range(idx, idx.__add__(10)))])
    
selected_columns_indices = list(filter(lambda x: x in range(1, 5, 2), range(matrix.__len__())))
selected_columns = map(lambda x: [x[col] for col in selected_columns_indices], matrix)

arr = np.array(list(selected_columns))

mask = arr[:, 1].__mod__(3).__eq__(0)
new_arr = arr[mask]

product = new_arr @ new_arr.T

#additional code for finding the average value of a matrix
sum_arr = np.zeros(product.shape[1])
full_sum = 0

for row in product:
    sum_arr.__iadd__(row)

for elem in sum_arr:
    full_sum += elem #here the replacement leads to an error

if (product[0].__lt__(1000)).all().__and__((product[2].__gt__(1000)).any()):
    print((full_sum).__truediv__(product.__len__().__mul__(product[0].__len__())))

#Task 5

from abc import ABC, abstractmethod

class BiologicalSequence(ABC):
    @abstractmethod
    def __len__(self):
        pass

    #ability to get elements by index and make slices of the sequence
    @abstractmethod
    def __getitem__(self, index):
        pass

    #to convert to string
    @abstractmethod
    def __str__(self):
        pass

    #to check the sequence alphabet for correctness
    @abstractmethod
    def checking(self):
        pass

class NucleicAcidSequence(BiologicalSequence):
    alphabets = {'A', 'C', 'G', 'T', 'U'}

    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        return self.sequence[index]

    def __str__(self):
        return self.sequence

    def check_alphabet(self):
        return set(self.sequence).issubset(self.alphabets)

    #a complementary sequence
    def complement(self):
        complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'U': 'A'}
        complementary_seq = [complements.get(base, base) for base in self.sequence]
        complementary_seq = ''.join(complementary_seq)
        return type(self)(complementary_seq)

    #returns the GC composition
    def gc_content(self):
        gc_bases = [base for base in self.sequence if base in {'G', 'C'}]
        return len(gc_bases) / len(self.sequence)


class DNASequence(NucleicAcidSequence):
    alphabets = {'A', 'C', 'G', 'T'}

    #the transcribed RNA sequence
    def transcribe(self):
        return RNASequence(self.sequence.replace('T', 'U'))


class RNASequence(NucleicAcidSequence):
    alphabets = {'A', 'C', 'G', 'U'}


class AminoAcidSequence(BiologicalSequence):
    alphabets = set('ACDEFGHIKLMNPQRSTVWY')

    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        return self.sequence[index]

    def __str__(self):
        return self.sequence

    def check_alphabet(self):
        return set(self.sequence).issubset(self._valid_alphabets)

    def molecular_weight(self):
        weights = {'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.15,
                   'E': 147.13, 'Q': 146.15, 'G': 75.07, 'H': 155.16, 'I': 131.17,
                   'L': 131.17, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13,
                   'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15}
        return sum(weights.get(aa, 0) for aa in self.sequence)


