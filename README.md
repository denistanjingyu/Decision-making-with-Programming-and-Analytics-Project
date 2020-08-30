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
     
     - Observation
       - There was a significant decrease in profits of $557,667 from period 3 to 4, and a decrease of $137,141 from period 4 to 5. This is despite the increasing revenue amounts, which grew from $10m in period 4 to more than $11m in period 5. 
       - Moreover, from period 3 onwards, there was a declining trend in profit percentages from 18.83% to 13.88% which indicates that customers are purchasing more products that have lower profitability margin while purchasing lower quantities of high-margin products. Products could also have rising overall costs to sell.
     - Impact on Customer Loyalty Program
       - New Ocean Trading can encourage the sales of higher margin products to customers through trade and shipping discounts or promotions, provide higher tier rewards to customers who purchase high-margin products and lower tier rewards to customers who purchase low-margin products.
       
   - Revenue by Month
     
     ![image](https://user-images.githubusercontent.com/45563371/91668795-060b6380-eb42-11ea-8b82-96372a7af61f.png)

     - Observation
       - Across the 5 periods, there are three significant increases in monthly revenue in every period, namely from February to March, April to May and from November to December, whereas there is a significant decrease in each period from January to February.
     - Impact on Customer Loyalty Program
       - Time-specific promotions can be offered to encourage businesses to transact more during February to increase revenue. 
       - High-margin products can also be promoted more during March, May and December to take advantage of the high spending behaviour of customers.
     - Impact on Stock Up Timing
       - March, May and December are high revenue months, hence the company should begin stocking up popular items in the prior months during February, April and November, in preparation for upcoming high demand.

   - Profit by Customer and Period
   
     ![image](https://user-images.githubusercontent.com/45563371/91668838-72866280-eb42-11ea-81e2-abd4ff58a86d.png)
     
     - Observation
       - Customers IJ01, IT23, IK11 and IT04 etc. are consistently the most profitable customers for New Ocean Trading.
     - Impact on Customer Loyalty Program
       - Highly customised rewards can be provided for these customers, such as a VIP tier. 
       - Preferential treatment should be conferred such as priority of shipping order and delivery to these customers. This will help to increase retention and maintain a close and intimate relationship with them, encouraging repeat and higher volume transactions.
    
   - Cluster Analysis
     
     ![image](https://user-images.githubusercontent.com/45563371/91668858-9e094d00-eb42-11ea-8f75-4282b5d264e2.png)
     
     ![image](https://user-images.githubusercontent.com/45563371/91668879-d872ea00-eb42-11ea-96a8-dfde91d44d01.png)
     
     - Observation 1 
       - Across the 5 periods, the two biggest clusters of customers are always centered around quantity of less than 10,000 and profit of around $50,000. 
       - The majority of customers are low quantity and low profit customers which implies that they are buying a relatively small number of stocks that bring low levels of profit to the company. 
     - Impact on Customer Loyalty Program
       - The customer loyalty program can be targeted at these customers to increase both quantity and profits generated from them. 
       - To increase profits, the company can promote the sales of higher profitability stocks
     - Observation 2
       - Presence of an outlier cluster: walk in non-regular customers (CASH). Walk in non-regular customers generally have quantity of less than 50,000 and loss of more than $300,000. They are low quantity and negative profit customers which implies that they are buying a relatively small quantity of stock that does not lead to profits for the company.          - The customers are purchasing stocks that are sold at a loss, where the selling price does not cover the cost price. 
     - Impact on Customer Loyalty Program
       - The company can also implement sign-up rewards to encourage these businesses to join the loyalty program and become regular customers. 
       - The customer loyalty program can then be targeted to increase sales of more profitable products amongst this group of customers. 
       - Discounts on the more profitable products may help to convert customers who are already purchasing similar items to these products instead.
     - Observation 3
       - Presence of another outlier cluster: customers with customer code IJ01. 
       - Customers with code IJ01 are from Indonesia and generally have quantity of more than 500,000 and profits of more than $450,000. They are high quantity and high profit customers which implies that they are buying relatively high quantity of stock and that leads to high profits for the company. 
     - Impact on Customer Loyalty Program 
       - One of the goals of the customer loyalty program would be to lead more customers into this high quantity and high profits cluster. 
       - Through active engagement and promotion of the benefits of the VIP tier, existing customers could be incentivised to increase their purchase and reach the VIP tier.

