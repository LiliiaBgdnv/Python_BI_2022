#Task 1

import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd
import re

response = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mp_mv250')
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('tbody', {'class': 'lister-list'})
rows = table.findAll('tr')
movies = []
director=[]

for row in rows:
    title_column = row.find('td', {'class': 'titleColumn'})
    name = title_column.a.text
    year = title_column.span.text.strip('()')
    rating = float(row.find('td', {'class': 'ratingColumn 
imdbRating'}).text.strip())
    n_reviews = int(row.find('td', {'class': 'ratingColumn 
imdbRating'}).find('strong').attrs['title'].split()[3].replace(',', ''))
    director = (re.search(r'title="([^"]+)"', str(title_column)).group(1))
    director = director.split(' (dir.)')[0]
    rank = int(row.find('td', {'class': 
'titleColumn'}).text.strip().split('.')[0])
    movie = {'name': name, 'rank': rank, 'year': year, 'rating': rating, 
'n_reviews': n_reviews, 'director': director}
    movies.append(movie)
top_n_reviews = sorted(movies, key=lambda x: x['n_reviews'], 
reverse=True)[:4]
for movie in top_n_reviews:
    print(f"{movie['name']}: {movie['n_reviews']} reviews")
year_ratings = defaultdict(list)
top_years = []
for movie in movies:
    year_ratings[movie['year']].append(movie['rating'])

for year, ratings in year_ratings.items():
    avg_rating = sum(ratings) / len(ratings)
    top_years.append((year, avg_rating))

top_years = sorted(top_years, key=lambda x: x[1], reverse=True)[:4]
for year, avg_rating in top_years:
    print(f"{year}: {avg_rating:.2f}")
director_counts = defaultdict(int)
for movie in movies:
    director_counts[movie['director']] += 1
    
director_counts = {k: v for k, v in director_counts.items() if v > 2}
director_counts = {k: v for k, v in sorted(director_counts.items(), 
key=lambda x: x[1], reverse=True)}
plt.bar(director_counts.keys(), director_counts.values())
plt.xticks(rotation=90)
plt.xlabel('Режиссёр')
plt.ylabel('Количество фильмов в топ-250 IMDb')
plt.show()
pd.DataFrame(movies).to_csv('top250_full.csv', index=False)

#Task 2

import sys
import time
import os
import io
import datetime
import requests
from dotenv import load_dotenv

load_dotenv()
TG_API_TOKEN = os.environ.get('TG_API_TOKEN')
def telegram_logger(chat_id):
    def decorator(func):
        def wrapper(*args, **kwargs):
        
            start_time = time.monotonic()
            log_file = io.StringIO()
            sys.stdout = log_file
            sys.stderr = log_file
            try:
                result = func(*args, **kwargs)
                status = "Success"
            except Exception as e:
                result = e
                status = "Error"
            finally:
                end_time = time.monotonic()
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__
                elapsed_time = end_time - start_time
                if elapsed_time < 86400:
                    elapsed_time_str = 
datetime.timedelta(seconds=elapsed_time)
                else:
                    elapsed_time_str = 
datetime.timedelta(seconds=elapsed_time)
                if status == "Success":
                    message = f"<code>{func.__name__}()</code> has 
finished successfully in <code>{elapsed_time_str}</code> 😎."
                else:
                    message = f"<code>{func.__name__}()</code> has 
finished with <code>{type(result).__name__}</code> exception: 
<code>{result}</code> 😢."
                
requests.post(f"https://api.telegram.org/bot{os.environ.get('TG_API_TOKEN')}/sendMessage", 
data={
                    "chat_id": chat_id,
                    "text": message,
                    "parse_mode": "HTML",
                })
                if log_file.getvalue():
                    file_name = f"{func.__name__}.log"
                    
requests.post(f"https://api.telegram.org/bot{os.environ.get('TG_API_TOKEN')}/sendDocument", 
data={
                        "chat_id": chat_id,
                    }, files={
                        "document": (file_name, log_file.getvalue(), 
"text/plain"),
                    })
        return wrapper
    return decorator

chat_id="443641247"
@telegram_logger(chat_id)
def good_function():
    print("This goes to stdout")
    print("And this goes to stderr", file=sys.stderr)
    time.sleep(2)
    print("Wake up, Neo")

@telegram_logger(chat_id)
def bad_function():
    print("Some text to stdout")
    time.sleep(2)
    print("Some text to stderr", file=sys.stderr)
    raise RuntimeError("Ooops, exception here!")
    print("This text follows exception and should not appear in logs")
    
@telegram_logger(chat_id)
def long_lasting_function():
    time.sleep(200000000)

good_function()

try:
    bad_function()
except Exception:
    pass

#Task 3
%load_ext autoreload
%autoreload 2
from genscan import GenscanOutput

# Call the run_genscan method to obtain a GenscanOutput object
output = GenscanOutput.run_genscan(sequence=None, sequence_file='seq.txt', 
organism="Vertebrate", exon_cutoff=1.00, sequence_name="")
# Print the output
print(output)

