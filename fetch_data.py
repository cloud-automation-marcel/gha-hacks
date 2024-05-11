import sys
import requests

# Get the run number from command line argument passed by the GitHub Action
run_number = sys.argv[1]
if int(run_number) > 10:
    print("Run number exceeds 10, exiting.")
    sys.exit()

# Formulate the URL with the current run number
url = f"https://jsonplaceholder.typicode.com/todos/{run_number}"

# Fetch the data from the URL
response = requests.get(url)
data = response.json()

# Append the fetched data to a file
with open("results.txt", "a") as file:
    file.write(f"Run {run_number}: {data}\n")

print(f"Data for run {run_number} appended to file.")
