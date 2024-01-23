import argparse
import csv
from collections import Counter
from datetime import datetime

def parse_arguments():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description='Find the most active cookie from a log file for a given date.')
    parser.add_argument('-f', '--filename', required=True, help='Log file name')
    parser.add_argument('-d', '--date', required=True, help='Date in YYYY-MM-DD format')
    return parser.parse_args()

def read_log_file(filename):
    """ Generator to read log file """
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            yield row

def get_most_active_cookie(log_file, date):
    """ Find the most active cookie for a given date """
    cookie_counter = Counter()
    for cookie, timestamp in log_file:
        log_date = datetime.fromisoformat(timestamp).date()
        if str(log_date) == date:
            cookie_counter[cookie] += 1
        elif log_date < datetime.fromisoformat(date).date():
            break
    max_count = max(cookie_counter.values(), default=0)
    return [cookie for cookie, count in cookie_counter.items() if count == max_count]

def main():
    """ Main function """
    args = parse_arguments()
    log_file = read_log_file(args.filename)
    most_active_cookies = get_most_active_cookie(log_file, args.date)
    for cookie in most_active_cookies:
        print(cookie)

if __name__ == "__main__":
    main()
