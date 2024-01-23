
# Most Active Cookie Finder

## Project Overview

This project consists of a Python script, `cookie_finder.py`, which processes a cookie log file in CSV format and returns the most active cookie for a specified date. The script is designed to be run from the command line, taking two parameters: the path to the CSV file (`-f`) and the date for which the most active cookie is sought (`-d`).

## Requirements

- Python 3.x

## Installation

No additional installation is required, as the script uses standard Python libraries.

## Usage

To run the script, open your terminal and navigate to the directory containing `cookie_finder.py`. Ensure that your cookie log file (in CSV format) is accessible.

The script can be executed with the following command:

```
python cookie_finder.py -f [path_to_cookie_log.csv] -d [date]
```

Replace `[path_to_cookie_log.csv]` with the path to your cookie log file and `[date]` with the date you're interested in, formatted as `YYYY-MM-DD`.

For example:

```
python cookie_finder.py -f cookie_log.csv -d 2018-12-09
```

## Sample Data

A sample cookie log file named `cookie_log.csv` is provided for testing purposes.

## Functionality

- **Parsing Command Line Arguments**: The script uses `argparse` to handle command-line arguments for the filename and date.
- **Reading the Log File**: It reads the CSV file and extracts cookie and timestamp information.
- **Filtering and Counting Cookies**: The script filters cookies based on the specified date and counts their occurrences.
- **Identifying Most Active Cookie(s)**: It identifies the cookie(s) that appear the most on the given date and prints them to stdout.
- **Error Handling**: Basic error handling is implemented for file reading and argument parsing.

## Testing

The script can be tested with different CSV files and dates to ensure it handles various scenarios correctly. A separate file for unit tests can be created as `test_cookie_finder.py`.
