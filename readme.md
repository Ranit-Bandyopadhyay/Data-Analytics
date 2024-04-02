## 1. Approach

### Part 1: Data Extraction
- Utilizing BeautifulSoup4 and requests library for fetching data from web pages.
- Pandas library will be employed to handle file formats like `.csv` and `.xlsx`.
- A folder named `Data extraction` will be created, containing text files with extracted data in the specified format.

### Part 2: Data Analysis
- Reading through the extracted files and creating functions for each mentioned parameter.
- Appending each parameter's data to a list.

### Part 3: Output
- Employing the `to_csv()` function from Pandas to convert the lists into a dataframe.
- Outputting the dataframe to a CSV file.


## 2. Run the `.py` file
- Navigate to terminal and type `pip install requirements.txt`
- Navigate to `driver.py` file and run the file. Output will be generated in the same directory as `output.csv`
