# Scraparser

A generic PDF table scraper and parser for data analysis.

[![CI Status][ci-image]][ci-link] [![PyPi][pypi-image]][pypi-link]

Originally written for scraping and parsing Hong Kong government
[COVID-19](https://en.wikipedia.org/wiki/Coronavirus_disease_2019)
related public data. Now generalize for hopefully other research
purposes as well.

Package is available on [pypi.org][pypi-link]. The development is
on [GitLab](https://gitlab.com/yookoala/scraparser). You are welcome
to submit
[issue](https://gitlab.com/yookoala/scraparser/-/issues) and
[merge request](https://gitlab.com/yookoala/scraparser/-/merge_requests).
And should you want to contribute, please read the
[Development](#development) section.

[ci-image]: https://gitlab.com/yookoala/scraparser/badges/master/pipeline.svg
[ci-link]: https://gitlab.com/yookoala/scraparser/pipelines
[pypi-image]: https://img.shields.io/badge/dynamic/json?color=blue&label=pypi%20version&query=%24.info.version&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fscraparser%2Fjson&prefix=v
[pypi-link]: https://pypi.org/project/scraparser/


## Prerequisites

To use scraparser, you need [Python 3](https://www.python.org/)
installed to your system. You will also need to know how to use
terminal commands on your system.

The instructions below assumes that Python 3 is available to
you through the command `python3`. If it is only available to
you as command `python` or other name, simply use `python` or
the available name for the commands `python3` described below.


## Install

The recommended way is to install
[the PyPi package](https://pypi.org/project/scraparser/) with
the [pip] module:

```
python3 -m pip install --upgrade scraparser
```


## Example Use

### Basic Scraping

To scrap the latest location situation report:

```
python3 -m scraparser scrap "https://www.chp.gov.hk/files/pdf/local_situation_covid19_tc.pdf" \
| python3 -m scraparser parse-pdf-to-csv --headers="個案編號,報告日期,發病日期,性別,年齡,入住醫院名稱,住院/出院/死亡,香港/非香港居民,個案分類,確診/疑似個案"
```

The downloaded PDF file and the parsed CSV file will be stored in:

```
./data/local_situation_covid19_tc.<time-string>.pdf
./data/local_situation_covid19_tc.<time-string>.csv
```

The `time-string` will be formated as `YYYY-MM-DD-HHmmss`.


### Parse Previously Downloaded PDF Report

To parse pre-exist PDF file from your local computer:

```
python3 -m scraparser scrap-location-situation-pdf --file=path/to/somename.pdf
```

The parsed CSV file will be stored to "`path/to/somename.csv`"


### Utility to Fix or Modify Parsed CSV

Its highly difficult to correctly read tables from PDF files. Common errors include:

* **Column underflow / overflow**

  The content of a cell spilled over to the last or next cell

* **Row overflow**

  The content of a cell (usually with line wraped into multiple lines), spilled over
  to create a phantom row with only 1 content-filled cell.

To fix these issue, please use the following subcommands:

#### `sort`

The command takes CSV filenames either from arguments or from `STDIN` (one filename)
per line:

```
python3 -m scraparser sort --column=0 --sort-as-number --in-place ./data/local_situation_covid19_tc.<time-string>.csv
```

This command will:

1. Read the file and parse 1st column (parameter `--column`
   accepts column definition start with 0, like in Python list index)
2. Sort all rows by the 1st column.
3. Save the fix result back to the input file.


#### `fix-column-underflow`

The command takes CSV filenames either from arguments or from `STDIN` (one filename)
per line:

```
python3 -m scraparser fix-column-underflow --column=5 --in-place ./data/local_situation_covid19_tc.<time-string>.csv
```

This command will:

1. Automatically read all the valid contents in the 6th column (parameter `--column`
   accepts column definition start with 0, like in Python list index).
2. Read every row and check if a cell in that column is empty (`math.isnan()`).
3. If so, check the column before it (6th column for our case) and see if it is 
   suffixed by any valid content found in step (1).
4. Split the content correctly for the 6th and 7th column.
5. Save the fix result back to the input file.

#### `fix-date-column-underflow`

The command takes CSV filenames either from arguments or from `STDIN` (one filename)
per line:

```
python3 -m scraparser fix-date-column-underflow --column=1 --format=DD/MM/YYYY --in-place ./data/local_situation_covid19_tc.<time-string>.csv
```

This command will:

1. Read every row and check if a cell in the 2nd column is empty (`math.isnan()`).
2. If so, check the column before it (1st column for our case) and see if it is 
   suffixed by string that matches our specified date format.
3. Split the content correctly for the 1st and 2nd column.
4. Save the fix result back to the input file.

#### `fix-empty-rows`

The command takes CSV filenames either from arguments or from `STDIN` (one filename)
per line:

```
python3 -m scraparser fix-empty-rows --in-place ./data/local_situation_covid19_tc.<time-string>.csv
```

This command will:

1. Read every row and find all rows with all but 1 cell empty (`math.isnan()`).
2. If so, append the content of that 1 cell to the cell directly above it.
3. Drop all "phantom rows" found in step (1).
4. Save the fix result back to the input file.

## Advanced Piping usage

### Parse and Show Result Data

To correctly fix all the issue created from the parsed CSV file in local situation report:

**Linux**

```
python3 -m scraparser scrap "https://www.chp.gov.hk/files/pdf/local_situation_covid19_tc.pdf" \
| python3 -m scraparser parse-pdf-to-csv --headers="個案編號,報告日期,發病日期,性別,年齡,入住醫院名稱,住院/出院/死亡,香港/非香港居民,個案分類,確診/疑似個案" \
| python3 -m scraparser fix-date-column-underflow --column=1 --in-place \
| python3 -m scraparser fix-column-underflow --column=6 --in-place \
| python3 -m scraparser fix-column-underflow --column=5 --in-place \
| python3 -m scraparser fix-empty-rows --in-place \
| python3 -m scraparser sort --in-place \
| xargs -i xdg-open "{}"
```

**macos**

```
python3 ./scraparser scrap "https://www.chp.gov.hk/files/pdf/local_situation_covid19_tc.pdf" \
| python3 -m scraparser parse-pdf-to-csv --headers="個案編號,報告日期,發病日期,性別,年齡,入住醫院名稱,住院/出院/死亡,香港/非香港居民,個案分類,確診/疑似個案" \
| python3 -m scraparser fix-date-column-underflow --column=1 --in-place \
| python3 -m scraparser fix-column-underflow --column=6 --in-place \
| python3 -m scraparser fix-column-underflow --column=5 --in-place \
| python3 -m scraparser fix-empty-rows --in-place \
| python3 -m scraparser sort --in-place
| xargs -I{} open "{}"
```

### Parse Data then Update Google Sheet

This will overwrite the current data specified in the range. If there are not enough rows in
the Google Sheet, the file will be expanded automatically.

Presume you have defined the string `$GOOGLE_SHEET_ID` and the target sheet
'CHP/DH Local Situation Input' exists:

```
python3 -m scraparser scrap "https://www.chp.gov.hk/files/pdf/local_situation_covid19_tc.pdf" \
| python3 -m scraparser parse-pdf-to-csv --headers="個案編號,報告日期,發病日期,性別,年齡,入住醫院名稱,住院/出院/死亡,香港/非香港居民,個案分類,確診/疑似個案" \
| python3 -m scraparser fix-date-column-underflow --column=1 --in-place \
| python3 -m scraparser fix-column-underflow --column=6 --in-place \
| python3 -m scraparser fix-column-underflow --column=5 --in-place \
| python3 -m scraparser fix-empty-rows --in-place \
| python3 -m scraparser sort --in-place \
| python3 -m scraparser googlesheet "$GOOGLE_SHEET_ID" update --range="'CHP/DH Local Situation Input'!A2:Z" 
```

## Development

First clone this repository by:

```
git clone https://gitlab.com/yookoala/scraparser.git
cd scraparser
```

You are recommended to use [venv](https://docs.python.org/3/library/venv.html)
for the development environment.

First you would need to initialize venv and install all the packages specified
in the [requirements.txt](requirements.txt):

```
pip -m venv .venv
. ./bin/activate.sh
pip install -r requirements.txt
```

Once this is done, you are ready to run the package in the repository folder
as if the module was installed locally:
```
python3 -m scraparser <command>
```

You can change the [scraparser](scraparser) folder in this repository and this
command will run correctly.

### Build and Submit

Should you want to fork and create your own `scraparser` package on Python Package index,
you may build and release your package (requires
[make](https://www.gnu.org/software/make/manual/make.html)) with commands.

#### Building

To build the package for upload, you need to rename the package to something other
than `scraparser`. Let's say you would suffix the package with `YOURNAME`:

```
PYPI_PKG_NAME=scraparser-YOURNAME make clean dist
```

The default version is specified by git commands. If it fails to work, you may
force a version string on it:

```
PYPI_PKG_VERSION=0.5.0 PYPI_PKG_NAME=scraparser-YOURNAME make clean dist
```

Please note that the version string **MUST** follow the
[PEP 440](https://www.python.org/dev/peps/pep-0440/#version-scheme) convension
or it cannot be submitted.

#### Submitting to test.pypi.org

```
PYPI_TEST_PASSWORD=<your-pypi-test-token> make upload-test
```

#### Submitting to pypi.org

```
PYPI_PASSWORD=<your-pypi-test-token> make upload
```

## License

License under [the MIT License](LICENSE). You may obtain the license in this repository.
