# -*- coding: utf-8 -*-
"""Копия блокнота "HW_2.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1euEn6zYDb60UDX9sO0eKnfLLIBUBQVXD

# Задание 1 (2 балла)

Напишите класс `MyDict`, который будет полностью повторять поведение обычного словаря, за исключением того, что при итерации мы должны получать и ключи, и значения.

**Модули использовать нельзя**
"""

class MyDict(dict):
    def __iter__(self):
        for key in self.keys():
            yield (key, self[key])

dct = MyDict({"a": 1, "b": 2, "c": 3, "d": 25})
for key, value in dct:
    print(key, value)

for key, value in dct.items():
    print(key, value)

for key in dct.keys():
    print(key)

dct["c"] + dct["d"]

"""# Задание 2 (2 балла)

Напишите функцию `iter_append`, которая "добавляет" новый элемент в конец итератора, возвращая итератор, который включает изначальные элементы и новый элемент. Итерироваться по итератору внутри функции нельзя, то есть вот такая штука не принимается
```python
def iter_append(iterator, item):
    lst = list(iterator) + [item]
    return iter(lst)
```

**Модули использовать нельзя**
"""

def iter_append(iterator, item):
    yield from iterator
    yield item 
    pass

my_iterator = iter([1, 2, 3])
new_iterator = iter_append(my_iterator, 4)

for element in new_iterator:
    print(element)

"""# Задание 3 (5 баллов)

Представим, что мы установили себе некотурую библиотеку, которая содержит в себе два класса `MyString` и `MySet`, которые являются наследниками `str` и `set`, но также несут и дополнительные методы.

Проблема заключается в том, что библиотеку писали не очень аккуратные люди, поэтому получилось так, что некоторые методы возвращают не тот тип данных, который мы ожидаем. Например, `MyString().reverse()` возвращает объект класса `str`, хотя логичнее было бы ожидать объект класса `MyString`.

Найдите и реализуйте удобный способ сделать так, чтобы подобные методы возвращали экземпляр текущего класса, а не родительского. При этом **код методов изменять нельзя**

**+3 дополнительных балла** за реализацию того, чтобы **унаследованные от `str` и `set` методы** также возвращали объект интересующего нас класса (то есть `MyString.replace(..., ...)` должен возвращать `MyString`). **Переопределять методы нельзя**

**Модули использовать нельзя**
"""

def return_other_type(method):
    def wrapper(*args, **kwargs):
        result = method(*args, **kwargs)
        if isinstance(result, str):
            return args[0].__class__(result)
        elif isinstance(result, set):
            return args[0].__class__(result)
        return result
    return wrapper

class MyString(str):
    @return_other_type
    def reverse(self):
        return self[::-1]
    
    @return_other_type
    def make_uppercase(self):
        return "".join([chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char for char in self])
    
    @return_other_type
    def make_lowercase(self):
        return "".join([chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char for char in self])
    
    @return_other_type
    def capitalize_words(self):
        return " ".join([word.capitalize() for word in self.split()])
    
    
class MySet(set):
    @return_other_type
    def is_empty(self):
        return len(self) == 0
    
    @return_other_type
    def has_duplicates(self):
        return len(self) != len(set(self))
    
    @return_other_type
    def union_with(self, other):
        return self.union(other)
    
    @return_other_type
    def intersection_with(self, other):
        return self.intersection(other)
    
    @return_other_type
    def difference_with(self, other):
        return self.difference(other)

string_example = MyString("Aa Bb Cc")
set_example_1 = MySet({1, 2, 3, 4})
set_example_2 = MySet({3, 4, 5, 6, 6})

print(type(string_example.reverse()))
print(type(string_example.make_uppercase()))
print(type(string_example.make_lowercase()))
print(type(string_example.capitalize_words()))
print()
print(type(set_example_1.is_empty()))
print(type(set_example_2.has_duplicates()))
print(type(set_example_1.union_with(set_example_2)))
print(type(set_example_1.difference_with(set_example_2)))

"""# Задание 4 (5 баллов)

Напишите декоратор `switch_privacy`:
1. Делает все публичные **методы** класса приватными
2. Делает все приватные методы класса публичными
3. Dunder методы и защищённые методы остаются без изменений
4. Должен работать тестовый код ниже, в теле класса писать код нельзя

**Модули использовать нельзя**
"""

def switch_privacy(cls):
    keys_to_modify = []
    
    for name in vars(cls):
        if callable(getattr(cls, name)) and not name.startswith('_') and not name.startswith(f'_{cls.__name__}__') and not name.endswith('__'):
            keys_to_modify.append(name)
        elif callable(getattr(cls, name)) and name.startswith(f'_{cls.__name__}__') and not name.endswith('__'):
            keys_to_modify.append(name)
    for name in keys_to_modify:
        method = getattr(cls, name)
        if not name.startswith('_'):
            setattr(cls, f'_{cls.__name__}__' + name, method)
        else:
            setattr(cls, name[len(cls.__name__)+3:], method)
        delattr(cls, name)
    return cls

@switch_privacy
class ExampleClass:
    # Но не здесь
    def public_method(self):
        return 1
    
    def _protected_method(self):
        return 2
    
    def __private_method(self):
        return 3
    
    def __dunder_method__(self):
        pass

test_object = ExampleClass()

test_object._ExampleClass__public_method()   # Публичный метод стал приватным

test_object.private_method()   # Приватный метод стал публичным

test_object._protected_method()   # Защищённый метод остался защищённым

test_object.__dunder_method__()   # Дандер метод не изменился

hasattr(test_object, "public_method"), hasattr(test_object, "private")   # Изначальные варианты изменённых методов не сохраняются

"""# Задание 5 (7 баллов)

Напишите [контекстный менеджер](https://docs.python.org/3/library/stdtypes.html#context-manager-types) `OpenFasta`

Контекстные менеджеры это специальные объекты, которые могут работать с конструкцией `with ... as ...:`. В них нет ничего сложного, для их реализации как обычно нужно только определить только пару dunder методов. Изучите этот вопрос самостоятельно

1. Объект должен работать как обычные файлы в питоне (наследоваться не надо, здесь лучше будет использовать **композицию**), но:
    + При итерации по объекту мы должны будем получать не строку из файла, а специальный объект `FastaRecord`. Он будет хранить в себе информацию о последовательности. Важно, **не строки, а именно последовательности**, в fasta файлах последовательность часто разбивают на много строк
    + Нужно написать методы `read_record` и `read_records`, которые по смыслу соответствуют `readline()` и `readlines()` в обычных файлах, но они должны выдавать не строки, а объект(ы) `FastaRecord`
2. Конструктор должен принимать один аргумент - **путь к файлу**
3. Класс должен эффективно распоряжаться памятью, с расчётом на работу с очень большими файлами
    
Объект `FastaRecord`. Это должен быть **датакласс** (см. про примеры декораторов в соответствующей лекции) с тремя полями:
+ `seq` - последовательность
+ `id_` - ID последовательности (это то, что в фаста файле в строке, которая начинается с `>` до первого пробела. Например, >**GTD326487.1** Species anonymous 24 chromosome) 
+ `description` - то, что осталось после ID (Например, >GTD326487.1 **Species anonymous 24 chromosome**)


Напишите демонстрацию работы кода с использованием всех написанных методов, обязательно добавьте файл с тестовыми данными в репозиторий (не обязательно большой)

**Можно использовать модули из стандартной библиотеки**
"""

from typing import List
from dataclasses import dataclass
import os

@dataclass
class FastaRecord:
    seq: str
    id_: str
    description: str


class OpenFasta:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

    def __iter__(self):
        record_lines = []
        for line in self.file:
            line = line.strip()
            if line.startswith(">"):
                if record_lines:
                    yield self._create_record(record_lines)
                record_lines = [line]
            else:
                record_lines.append(line)
        if record_lines:
            yield self._create_record(record_lines)

    def _create_record(self, lines) -> FastaRecord:
        # Extract the ID and description from the header line
        header_parts = lines[0][1:].split(maxsplit=1)
        record_id = header_parts[0]
        description = header_parts[1] if len(header_parts) > 1 else ""
        
        # Join the sequence lines together and return the record
        return FastaRecord(seq="".join(lines[1:]), id_=record_id, description=description)
    
    def read_records(self) -> List[FastaRecord]:
        """
        Reads all records in the file and returns them as a list of FastaRecord objects.
        """
        records = []
        for record in self:
            records.append(record)
        return records

with OpenFasta(os.path.join("/content", "sequence.fasta")) as fasta:
    for record in fasta:
        print(record)

"""# Задание 6 (7 баллов)

1. Напишите код, который позволит получать все возможные (неуникальные) генотипы при скрещивании двух организмов. Это может быть функция или класс, что вам кажется более удобным.

Например, все возможные исходы скрещивания "Aabb" и "Aabb" (неуникальные) это

```
AAbb
AAbb
AAbb
AAbb
Aabb
Aabb
Aabb
Aabb
Aabb
Aabb
Aabb
Aabb
aabb
aabb
aabb
aabb
```

2. Напишите функцию, которая вычисляет вероятность появления определённого генотипа (его ожидаемую долю в потомстве).
Например,

```python
get_offspting_genotype_probability(parent1="Aabb", parent2="Aabb", target_genotype="Аabb")   # 0.5

```

3. Напишите код, который выводит все уникальные генотипы при скрещивании `'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'` и `'АаббВвГгДДЕеЖжЗзИиЙйКкЛлМмНН'`, которые содержат в себе следующую комбинацию аллелей `'АаБбВвГгДдЕеЖжЗзИиЙйКкЛл'`
4. Напишите код, который расчитывает вероятность появления генотипа `'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'` при скрещивании `АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн` и `АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн`

Важные замечания:
1. Порядок следования аллелей в случае гетерозигот всегда должен быть следующим: сначала большая буква, затем маленькая (вариант `AaBb` допустим, но `aAbB` быть не должно)
2. Подзадачи 3 и 4 могут потребовать много вычислительного времени (до 15+ минут в зависимости от железа), поэтому убедитесь, что вы хорошо протестировали написанный вами код на малых данных перед выполнением этих задач. Если ваш код работает **дольше 20 мин**, то скорее всего ваше решение не оптимально, попытайтесь что-нибудь оптимизировать. Если оптимальное решение совсем не получается, то попробуйте из входных данных во всех заданиях убрать последний ген (это должно уменьшить время выполнения примерно в 4 раза), но **за такое решение будет снято 2 балла**
3. Несмотря на то, что подзадания 2, 3 и 4 возможно решить математически, не прибегая к непосредственному получению всех возможных генотипов, от вас требуется именно brute-force вариант алгоритма

**Можно использовать модули из стандартной библиотеки питона**, но **за выполнение задания без использования модулей придусмотрено +3 дополнительных балла**
"""

#Task 1
class GenotypeCalculator:
    def __init__(self, parent1, parent2):
        self.parent1 = parent1
        self.parent2 = parent2
        self.a_alleles = []
        self.b_alleles = []
        self.combinations = []
        self.result = []

    def get_alleles(self):
        for allele in self.parent1 + self.parent2:
            if allele.upper() == self.parent1[0].upper():
                self.a_alleles.append(allele)
            elif allele.upper() == self.parent1[3].upper():
                self.b_alleles.append(allele)

    def generate_combinations(self):
        self.get_alleles()
        for a_allele in self.a_alleles[0:2]:
            for b_allele in self.b_alleles[0:2]:
                self.combinations.append(a_allele + b_allele)
        for a_allele in self.a_alleles[2:4]:
            for b_allele in self.b_alleles[2:4]:
                self.combinations.append(a_allele + b_allele)
    def get_all_genotypes(self):
        self.generate_combinations()
        for combination_from_parent1 in self.combinations[0:4]:
            for combination_from_parent2 in self.combinations[4:8]:
                genotype = ''.join(sorted(combination_from_parent1 + combination_from_parent2, key=str.lower))
                self.result.append(''.join(sorted(sorted(genotype[0:2]) + sorted(genotype[2:4]), key=str.lower)))
        return self.result

genotype_calculator = GenotypeCalculator('Aabb', 'Aabb')
for genotypes in genotype_calculator.get_all_genotypes():
    print(genotypes)

#Task 2
def get_offspting_genotype_probability(parent1, parent2, target_genotype):
    genotype_calculator = GenotypeCalculator(parent1, parent2)
    all_genotypes = genotype_calculator.get_all_genotypes()
    return  all_genotypes.count(target_genotype) / len(all_genotypes)

probability = get_offspting_genotype_probability(parent1="Aabb", parent2="Aabb", target_genotype='Aabb')
print(f"Вероятность генотипа: {probability}")

#Task 3
def get_combinations(alphabet, length):
    def _get_combinations(alphabet, length, index, current, generated):
        if len(current) == length:
            if current not in generated:
                generated.add(current)
                yield current
            return

        for i in range(index, len(alphabet)):
            if alphabet[i] not in current.lower() and alphabet[i].lower() not in current and alphabet[i] not in current.upper() and alphabet[i].upper() not in current:
                yield from _get_combinations(alphabet, length, i + 1, current + alphabet[i], generated)
    generated = set()
    return _get_combinations(alphabet, length, 0, "", generated)

combinations = set() 
combinations_1 = list(get_combinations("АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн", 14))
combinations_2 = list(get_combinations("АаббВвГгДДЕеЖжЗзИиЙйКкЛлМмНН", 14))
for elem1 in combinations_1:
    for elem2 in combinations_2:
        merged = elem1 + elem2
        if set('АаБбВвГгДдЕеЖжЗзИиЙйКкЛл').issubset(set(merged)):
            sorted_merged = ''.join(sorted(merged, key=lambda x: (x.lower(), x.islower())))
            combinations.add(sorted_merged)
for combination in combinations:
    print(combination)

# Task 4
def get_combinations(alphabet, length):
    def _get_combinations(alphabet, length, index, current, generated):
        if len(current) == length:
            if current not in generated:
                generated.add(current)
                yield current
            return

        for i in range(index, len(alphabet)):
            if alphabet[i] not in current.lower() and alphabet[i].lower() not in current and alphabet[i] not in current.upper() and alphabet[i].upper() not in current:
                yield from _get_combinations(alphabet, length, i + 1, current + alphabet[i], generated)
    generated = set()
    return _get_combinations(alphabet, length, 0, "", generated)

combinations = set() 
combinations_1 = list(get_combinations("АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн", 14))
combinations_2 = list(get_combinations("АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн", 14))
for elem1 in combinations_1:
    for elem2 in combinations_2:
        merged = elem1 + elem2
        sorted_merged = ''.join(sorted(merged, key=lambda x: (x.lower(), x.islower())))
        combinations.add(sorted_merged)
combinations_list = list(combinations)
count = combinations_list.count('АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн')
probability = count / len(combinations_list)
print(probability)