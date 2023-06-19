# Task 1

from joblib import Parallel, delayed
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
import numpy as np

class RandomForestClassifierCustom:
    def __init__(self, n_estimators: int = 100, max_depth: int = None, 
max_features: int = 'auto',
                 random_state: int = None):
        self.n_estimators: int = n_estimators
        self.max_depth: int = max_depth
        self.max_features: int = max_features
        self.random_state: int = random_state
        self.trees: list = []
        self.feat_ids_by_tree: list = []
        self.classes_: np.ndarray = None
        self.X: np.ndarray = None
        self.y: np.ndarray = None

    def _fitting_model(self, idx: int) -> tuple:
        rng: np.random.Generator = np.random.default_rng(self.random_state 
+ idx)
        features_ids: np.ndarray = rng.choice(self.X.shape[1], 
size=self.max_features, replace=False)
        pseudosampling_ids: np.ndarray = rng.choice(self.X.shape[0], 
size=self.X.shape[0], replace=True)
        pseudo_X: np.ndarray = self.X[pseudosampling_ids][:, features_ids]
        pseudo_y: np.ndarray = self.y[pseudosampling_ids]

        tree_class: DecisionTreeClassifier = 
DecisionTreeClassifier(max_depth=self.max_depth,
                                            
max_features=self.max_features,
                                            
random_state=self.random_state,
                                            )
        fitted_tree: DecisionTreeClassifier = tree_class.fit(pseudo_X, 
pseudo_y)
        return fitted_tree, features_ids

    def fit(self, X: np.ndarray, y: np.ndarray, n_jobs: int = 1) -> 
object:
        self.X: np.ndarray = X
        self.y: np.ndarray = y
        self.classes_: np.ndarray = sorted(np.unique(self.y))
        processes = 
Parallel(n_jobs=n_jobs)(delayed(self._fitting_model)(idx) for idx in 
range(self.n_estimators))
        self.trees, self.feat_ids_by_tree = zip(*processes)
        return self

    def _prediction_calc(self, tree_and_feat_ids: tuple) -> np.ndarray:
        tree, feat_ids = tree_and_feat_ids
        pred: np.ndarray = tree.predict_proba(self.X[:, feat_ids])
        return pred

    def predict_proba(self, X: np.ndarray, n_jobs: int = 1) -> np.ndarray:
        self.X: np.ndarray = X
        y_pred: np.ndarray = np.zeros((self.X.shape[0], 
len(self.classes_)))
        processes = 
Parallel(n_jobs=n_jobs)(delayed(self._prediction_calc)(tf) for tf in 
zip(self.trees, self.feat_ids_by_tree))
        y_pred: np.ndarray = sum(processes)
        return y_pred

    def predict(self, X: np.ndarray, n_jobs: int = 1) -> np.ndarray:
        probas: np.ndarray = self.predict_proba(X, n_jobs)
        predictions: np.ndarray = np.argmax(probas, axis=1)
        return predictions


X, y = make_classification(n_samples=100000)
random_forest = RandomForestClassifierCustom(max_depth=30, n_estimators=10, max_features=2, random_state=42)
%%time

_ = random_forest.fit(X, y, n_jobs=1)
%%time

preds_1 = random_forest.predict(X, n_jobs=1)
random_forest = RandomForestClassifierCustom(max_depth=30, n_estimators=10, max_features=2, random_state=42)
%%time

_ = random_forest.fit(X, y, n_jobs=2)
%%time

preds_2 = random_forest.predict(X, n_jobs=2)
(preds_1 == preds_2).all()   # Количество worker'ов не должно влиять на 
предсказания

#Task 2

import os
import psutil
import time
import warnings

def get_memory_usage() -> int:    # Показывает текущее потребление памяти 
процессом
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def bytes_to_human_readable(n_bytes:int) -> str:
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for idx, s in enumerate(symbols):
        prefix[s] = 1 << (idx + 1) * 10
    for s in reversed(symbols):
        if n_bytes >= prefix[s]:
            value = float(n_bytes) / prefix[s]
            return f"{value:.2f}{s}"
    return f"{n_bytes}B"

def memory_limit(soft_limit: Optional[str] = None, hard_limit: 
Optional[str] = None, poll_interval: float = 1) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            def print_warning() -> int:
                mem = get_memory_usage()
                if mem > soft_limit_bytes and not warning_printed[0]:
                    warnings.warn(f"Memory usage 
({bytes_to_human_readable(mem)}) is above the soft limit 
({bytes_to_human_readable(soft_limit_bytes)})")
                    warning_printed[0] = True
                return mem
            
            def check_hard_limit():
                mem = get_memory_usage()
                if mem > hard_limit_bytes:
                    raise MemoryError(f"Memory usage 
({bytes_to_human_readable(mem)}) is above the hard limit 
({bytes_to_human_readable(hard_limit_bytes)})")

            warning_printed = [False]   # Флаг, показывающий, было ли уже 
напечатано warning при превышении soft_limit
            soft_limit_bytes = None if soft_limit is None else 
int(soft_limit[:-1]) * (1024 ** "BKMGT".index(soft_limit[-1]))
            hard_limit_bytes = None if hard_limit is None else 
int(float(hard_limit[:-1]) * (1024 ** "BKMGT".index(hard_limit[-1])))
            
            t = time.time()
            max_mem = 0
            while True:
                try:
                    mem = print_warning()
                    check_hard_limit()
                    max_mem = max(max_mem, mem)
                    result = func(*args, **kwargs)
                    return result
                finally:
                    time.sleep(poll_interval)
                    if time.time() - t > 60:  # Если функция выполняется 
более 60 секунд, перестаём отслеживать память
                        break
            raise Exception(f"Memory usage 
({bytes_to_human_readable(max_mem)}) exceeded the soft limit 
({bytes_to_human_readable(soft_limit_bytes)})")
        return wrapper
    return decorator

@memory_limit(soft_limit="512M", hard_limit="1.5G", poll_interval=0.1)
def memory_increment():
    """
    Функция для тестирования
    
    В течение нескольких секунд достигает использования памяти 1.89G
    Потребление памяти и скорость накопления можно варьировать, изменяя 
код
    """
    lst = []
    for i in range(50000000):
        if i % 500000 == 0:
            time.sleep(0.1)
        lst.append(i)
    return lst
result = memory_increment()
print(memory_limit(result))

# Task 3
from typing import Union, Optional, Callable, List, Tuple, Dict, Any
import time
import concurrent.futures

class Parallel_Running:
    def __init__(self,
                 target_func: Union[Callable, List[Callable]],
                 args_container: Optional[Union[List[Tuple], Tuple]] = 
None,
                 kwargs_container: Optional[List[Dict[str, Any]]] = None,
                 n_jobs: int = None) -> None:
        self.target_funcs = target_func
        self.args_container = args_container
        self.kwargs_container = kwargs_container
        self.n_jobs = n_jobs
        self.counter = 0

    def compare_containers_len(self):
        if self.args_container is not None and self.kwargs_container is 
not None and len(
                self.args_container) != len(self.kwargs_container):
            raise ValueError(
                f'Numbers of positional arguments and keyword arguments do 
not match: {len(self.args_container)} and {len(self.kwargs_container)}')

    def check_n_funcs(self):
        if isinstance(self.target_funcs, list):
            self.target_funcs = self.target_funcs
        else:
            self.target_funcs = [self.target_funcs]

    def fill_args_kwargs(self):
        if self.args_container is None:
            if self.kwargs_container is None:
                self.args_container = [tuple() for _ in 
range(self.n_jobs)]
                self.kwargs_container = [dict() for _ in 
range(self.n_jobs)]
            else:
                self.args_container = [tuple() for _ in 
range(len(self.kwargs_container))]
        elif self.kwargs_container is None:
            self.kwargs_container = [dict() for _ in 
range(len(self.args_container))]


    def check_n_jobs(self):
        if self.n_jobs is None:
            self.n_jobs = multiprocessing.cpu_count()
        self.fill_args_kwargs()
        self.n_jobs = min(self.n_jobs, len(self.args_container))

    def add_tasks_in_queue(self, queue: multiprocessing.Queue) -> 
multiprocessing.Queue:
        counter = 0
        for arg, kwarg in zip(self.args_container, self.kwargs_container):
            queue.put((counter, arg, kwarg))
            counter += 1
        return queue

    def process_tasks(self, func: Callable, args: Tuple, kwargs: Dict) -> 
Any:
        if not isinstance(args, tuple):
            args = (args,)
        return func(*args, **kwargs)

    def parallel_map(self) -> List[list]:
        self.compare_containers_len()
        self.check_n_funcs()
        self.check_n_jobs()

        with 
concurrent.futures.ThreadPoolExecutor(max_workers=self.n_jobs) as 
executor:
            results = []
            for func in self.target_funcs:
                arg_list = [(args, kwargs) for args, kwargs in 
zip(self.args_container, self.kwargs_container)]
                interm_res = list(executor.map(lambda x: 
self.process_tasks(func, *x), arg_list))
                results.append(interm_res)

        return results

import time


# Это только один пример тестовой функции, ваша parallel_map должна уметь 
эффективно работать с ЛЮБЫМИ функциями
# Поэтому обязательно протестируйте код на чём-нибудбь ещё
def test_func(x=1, s=2, a=1, b=1, c=1):
    time.sleep(s)
    return a*x**2 + b*x + c

%%time

# Пример 2.1
# Отдельные значения в args_container передаются в качестве позиционных 
аргументов 
#parallel_map(test_func, args_container=[1, 2.0, 3j-1, 4]) (test_func, 
args_container=[1, 2.0, )  # Здесь происходят параллельные вызовы: 
test_func(1) test_func(2.0) test_func(3j-1) test_func(4)
pr = Parallel_Running(test_func, args_container=[(1,), (2.0,), (3j-1,), 
(4,)])
results = pr.parallel_map()
print(results)

%%time

# Пример 2.2
# Элементы типа tuple в args_container распаковываются в качестве 
позиционных аргументов
pr = Parallel_Running(test_func, [(1, 1), (2.0, 2), (3j-1, 3), 4])    # 
Здесь происходят параллельные вызовы: test_func(1, 1) test_func(2.0, 2) 
test_func(3j-1, 3) test_func(4)
results = pr.parallel_map()
print(results)

%%time

# Пример 3.1
# Возможна одновременная передача args_container и kwargs_container, но 
количества элементов в них должны быть равны
pr = Parallel_Running(test_func,
             args_container=[1, 2, 3, 4],
             kwargs_container=[{"s": 3}, {"s": 3}, {"s": 3}, {"s": 3}])
results = pr.parallel_map()
print(results)
# Здесь происходят параллельные вызовы: test_func(1, s=3) test_func(2, 
s=3) test_func(3, s=3) test_func(4, s=3)

%%time

# Пример 3.2
# args_container может быть None, а kwargs_container задан явно
pr = Parallel_Running(test_func,
             kwargs_container=[{"s": 3}, {"s": 3}, {"s": 3}, {"s": 3}])
results = pr.parallel_map()
print(results)

%%time

# Пример 3.3
# kwargs_container может быть None, а args_container задан явно
pr = Parallel_Running(test_func,
             args_container=[1, 2, 3, 4])
results = pr.parallel_map()
print(results)

%%time

# Пример 3.4
# И kwargs_container, и args_container могут быть не заданы
pr = Parallel_Running(test_func)
results = pr.parallel_map()
print(results)

%%time

# Пример 3.4
# И kwargs_container, и args_container могут быть не заданы
pr = Parallel_Running(test_func)
results = pr.parallel_map()
print(results)

%%time

# Пример 3.5
# При несовпадении количеств позиционных и именованных аргументов кидается 
ошибка
pr = Parallel_Running(test_func,
             args_container=[1, 2, 3, 4],
             kwargs_container=[{"s": 3}, {"s": 3}, {"s": 3}])
results = pr.parallel_map()
print(results)

%%time

# Пример 4.1
# Если функция не имеет обязательных аргументов и аргумент n_jobs не был 
передан, то она выполняется параллельно столько раз, сколько ваш CPU имеет 
логических ядер
# В моём случае это 24, у вас может быть больше или меньше
pr = Parallel_Running(test_func)
results = pr.parallel_map()
print(results)

%%time

# Пример 4.2
# Если функция не имеет обязательных аргументов и передан только аргумент 
n_jobs, то она выполняется параллельно n_jobs раз
pr = Parallel_Running(test_func, n_jobs=2)
results = pr.parallel_map()
print(results)

%%time

# Пример 4.3
# Если аргументов для target_func указано МЕНЬШЕ, чем n_jobs, то 
используется такое же количество worker'ов, сколько было передано 
аргументов
pr = Parallel_Running(test_func,
             args_container=[1, 2, 3],
             n_jobs=5)   # Здесь используется 3 worker'a
results = pr.parallel_map()
print(results)

%%time

# Пример 4.4
# Аналогичный предыдущему случай, но с именованными аргументами
pr = Parallel_Running(test_func,
             kwargs_container=[{"s": 3}, {"s": 3}, {"s": 3}],
             n_jobs=5)   # Здесь используется 3 worker'a
results = pr.parallel_map()
print(results)

%%time

# Пример 4.5
# Комбинация примеров 4.3 и 4.4 (переданы и позиционные и именованные 
аргументы)
pr = Parallel_Running(test_func,
             args_container=[1, 2, 3],
             kwargs_container=[{"s": 3}, {"s": 3}, {"s": 3}],
             n_jobs=5)   # Здесь используется 3 worker'a
results = pr.parallel_map()
print(results)

%%time

# Пример 4.6
# Если аргументов для target_func указано БОЛЬШЕ, чем n_jobs, то 
используется n_jobs worker'ов
pr = Parallel_Running(test_func,
             args_container=[1, 2, 3, 4],
             kwargs_container=None,
             n_jobs=2)   # Здесь используется 2 worker'a
results = pr.parallel_map()
print(results)

%%time

# Пример 4.7
# Время выполнения оптимизируется, данный код должен отрабатывать за 5 
секунд
pr = Parallel_Running(test_func,
             kwargs_container=[{"s": 5}, {"s": 1}, {"s": 2}, {"s": 1}],
             n_jobs=2)
results = pr.parallel_map()
print(results)

def test_func2(string, sleep_time=1):
    time.sleep(sleep_time)
    return string

# Пример 5
# Результаты возвращаются в том же порядке, в котором были переданы 
соответствующие аргументы вне зависимости от того, когда завершился worker
arguments = ["first", "second", "third", "fourth", "fifth"]
pr = Parallel_Running(test_func2,
             args_container=arguments,
             kwargs_container=[{"sleep_time": 5}, {"sleep_time": 4}, 
{"sleep_time": 3}, {"sleep_time": 2}, {"sleep_time": 1}])
results = pr.parallel_map()
print(results)

%%time


def test_func3():
    def inner_test_func(sleep_time):
        time.sleep(sleep_time)
    pr = Parallel_Running(inner_test_func, args_container=[1, 2, 3])
    return pr.parallel_map()

# Пример 6
# Работает с функциями, созданными внутри других функций
test_func3()


