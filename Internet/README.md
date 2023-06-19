Task 1: IMDb Movie Data Analysis
The code in this task fetches data from the IMDb website's top 250 movies 
chart. It retrieves information such as movie title, year, rating, number 
of reviews, and director. The code then performs various analyses on the 
data, including finding movies with the highest number of reviews, 
calculating average ratings by year, and determining the directors with 
the most movies in the top 250. Finally, it visualizes the director counts 
using a bar chart and exports the movie data to a CSV file.

Task 2: Telegram Logger
This task involves a logging decorator for functions, which sends logs and 
status updates to a specified Telegram chat. The decorator measures the 
execution time of the decorated function, captures standard output and 
error messages, and posts them to the chat along with the elapsed time. If 
an exception occurs during function execution, the decorator captures the 
exception details and includes them in the log. Additionally, if there is 
any log content, it can be sent as a separate log file.

To use this functionality, you need to set up a Telegram bot and obtain an 
API token. The token should be stored as an environment variable named 
TG_API_TOKEN.

Task 3: Genscan Output Parser
The code in this task demonstrates how to use the GenscanOutput class to 
parse and analyze the output of the Genscan gene prediction program. It 
provides a simple example where the run_genscan method is called with a 
DNA sequence file (seq.txt). The method returns a GenscanOutput object, 
which can be further processed or analyzed as needed.

To use the GenscanOutput class, make sure you have the genscan.py file in 
the same directory as your code or set the correct path to it.

Additional Notes
* Make sure to install the required dependencies (beautifulsoup4, 
matplotlib, pandas, requests, python-dotenv) before running the code.
* For Task 2, you need to set up a Telegram bot and obtain an API token. 
The 
token should be stored as an environment variable named TG_API_TOKEN.
* In Task 3, the genscan.py file is referenced. Please make sure you have 
the correct path to the file or place it in the same directory as your 
code.
