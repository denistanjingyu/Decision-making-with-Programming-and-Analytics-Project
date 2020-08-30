# Decision Making with Programming and Analytics Project

![0_F6QUIiDYKcqGVCF_](https://user-images.githubusercontent.com/45563371/89464486-26ded400-d7a3-11ea-9447-fbb5b147ef8f.jpg)

## Project Statement
Mike, CFO from New Ocean Trading, has long struggled to make sense out of the lengthy transactional records. The internal team who attempts to analyse the data often delivers outcomes that contradict with his anticipation. As such, he relies on his long-established business instinct to make business decision instead. Mike heard that you are good at analysing lengthy data and are well versed in Python Programming. He wishes to engage you to see what can be done to improve his department and understand the reason why the internal team may not be delivering what is expected. 

### He has brought with him 2 items for your analysis: 

 (1) The json file (cat_class.json) containing categorical classification information about their products, there are 8090 lines of stock internal serial number (StockISN) with its corresponding category codes. The following illustrates the first 10 lines of data. 
 
 (2) The second file (stockcards.xlsx) contains transactional records with more than 56000 lines of data covers the period from Jan 2011 to Apr 2019. The header information and first 10 records are shown below:
 
 1. Standardise and store all data into one consistent format (either csv/json/database/others) instead of the current forms of excel spreadsheet, json, and csv. Data transformation and conversion should be done programmatically instead of manually. Choose appropriate format and justify your decision.  
 2. Perform any appropriate cleaning activities to ensure that the data is accurate and consistent to be used for analysis. Remove irrelevant data that is not within the scope of this project. Make reasonable judgement to remove or replace data with suitable value. 
 3. Analyse the data appropriately to help with understanding customer buying patterns, geographical distribution of transactions, stocks item analysis and forecast. Mike would like to use these understanding to establish appropriate customer loyalty program, decide upon regional focus, and guide future stock up timing. Mike would like to see analysis based on the last 5 years of data. 
 4. Create a command line user interface which allows user to query data from stockcards data file. The query should allow user to extract information related to certain variable(s). The query results from data file are then displayed on the command prompt. The view option 
summarizes the data appropriate for reading, statistical summary could also be adopted to summarize the data. The program allows for viewing up to 5 years’ data. You can decide on appropriate views that may be relevant to Mike.  

## Approach
- Problem Understanding
- Data Format
- Data Cleaning/Preprocessing
- Data Analysis
- Command Line User Interface
- Conclusion

### Problem Understanding
- Presented with a set of transactional record data from New Ocean Trading, a company that has not been relying on programming analytics to make business decisions
- Make use of Python Programming to create an interactive program that can analyse the transactional records and present the company, through a simple user interface, with analysis and insights to guide their business decisions
- Company’s business focus would be to establish a customer loyalty program to retain customers and encourage higher spending, decide upon regional focus and forecast stock up timings
- Analysis was done on data 5 years from the last transaction date, from 2014-04-27 to 2019-04-27

### Data Format
- CSV
  - Compact and storage savings can be significant for large datasets
  - More accessible to a majority of business users
  - Dataset that we are dealing with has a strict tabular structure and data types are always known beforehand
  
### Data Cleaning/Preprocessing
- Many inconsistencies such as zero values and missing values
- Join ‘stockcards.csv’ and ‘cat_class.json’ datasets on the Stock Internal serial number information
- Removed spaces from the column names
- Replaced all other forms of currency inputs such as ‘SIN’, ‘US’, ‘US$’, and ‘USD’ to the respective standard codes, and filled in missing values of ‘Cur’ with ‘S$’
- For the ‘CustomerCode’ column, missing values were filled with ‘CASH’, referring to walk in non-regular customers, and capitalised the whole column to resolve wrong inputs of lower cases
- After removing null values of 547 rows, 55,539 rows of transactions were left 
- Extracted the year, month, and day information from ‘Date’ into separate columns for easier analysis
- Standardised the values for ‘TUPrice’, ‘ODAmt’ and ‘Amt’ to contain only positive values
- Created a quantity (by taking ‘ODAmt’ / ‘TUPrice’) and profit (‘Amt’ - ‘Worth’) column 
- Trimmed whitespace from data elements to avoid any potential problems with seemingly similar values being polluted by trailing whitespace, which would then be parsed and wrongly used as input to something else
- Created a class CheckColumns() to check for the number of unique values in each column and their suitability to be converted to categorical types
- Deleted all transactions with all 4 values of ‘TUPrice’, ‘ODAmt’, ‘Amt’ and ‘Worth’ being equal to zero, as we could not meaningfully substitute these values for the mean or median, without at least one other present dollar value
- Final clean dataset is then saved and exported as ‘Clean_stockcards.csv’ with a total of 55,169 transactions

#### Interesting Findings from Data Cleaning
- Presence of transactions with ‘TUPrice’, ‘ODAmt’ and ‘Amt’ = 0 with a negative worth value
  - These transactions might be an indication of an existing customer loyalty program, and that these goods were gifts redeemed by customers for free
  - This deduction would later be corroborated by the findings under analysis of customer profitability, where those highly profitable business customers would be the same companies that redeemed the free gifts (matching the ‘CustomerCode’ of these transactions)
  
### Data Analysis
- Objective of Analysis
  - Customer Buying Pattern
    - To understand the buying patterns of the customers, in each time period, that are most likely to increase profits with the implementation of a customer loyalty program.
  - Geographical Distribution
    - To locate the geographical distribution of customers, in each time period, by profitability so as to decide upon a regional focus for the company.
  - Stock Up Timings
    - To identify the ideal stock up timings to increase profits based on seasonality and customer buying pattern.

- Analysis Charts & Visualisation
  - To fulfil the data analysis for the last 5 years, the periods were grouped as follows, based on the last transaction date on 27 April 2019
    
     |**Period**|    **From Date - To Date**    |
     |----------|-------------------------------|
     | Period 1 | 28 April 2014 - 27 April 2015 |
     | Period 2 | 28 April 2015 - 27 April 2016 |
     | Period 3 | 28 April 2016 - 27 April 2017 | 
     | Period 4 | 28 April 2017 - 27 April 2018 |
     | Period 5 | 28 April 2018 - 27 April 2019 |
     
   - Profit Analysis by Periods
   
     ![image](https://user-images.githubusercontent.com/45563371/91668741-82517700-eb41-11ea-99f7-4b8c1bcb1492.png)

