# Decision Making with Programming and Analytics Project

![0_F6QUIiDYKcqGVCF_](https://user-images.githubusercontent.com/45563371/89464486-26ded400-d7a3-11ea-9447-fbb5b147ef8f.jpg)

- [Project Statement](##-Project-Statement)
- [Heading](#heading-1)
- [Heading](#heading-2)

<!-- toc -->

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

![image](https://user-images.githubusercontent.com/45563371/91745308-58558e80-ebed-11ea-8fe1-6ba0dc726fe6.png)

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

   - Profitable Products by Periods
   
     ![image](https://user-images.githubusercontent.com/45563371/91668954-8bdbde80-eb43-11ea-9128-f96dde667b34.png)

     - Observation
       - Product with StkISN 10126 has been consistently one of the most profitable products for New Ocean Trading across the 5 periods. 
       - Other notable products with high profitability include StkISN: 10128, 41371, 41534, 41535, 41909, 43513, 44935, 44947, 46506.
     - Impact on Customer Loyalty Program
       - To increase profits, the loyalty program can encourage customers to make the switch from purchasing low-margin products to these high-margin products identified. 
       - Companies that can make use of these products in their manufacturing line or businesses should also be tagged for targeted promotions, e.g. special discounts for a clothing company to switch from low-margin wool to high-margin wool for the first few transactions. 
       - The company can also bundle these products together with other low-margin, but popular products to encourage higher sales of both.
     - Impact on Stock Up Timing
       - These products should be consistently maintained with high inventory to avoid missing out on earning high profit margins. 
       - On the other hand, the provision of products with the lowest or no profitability should be reconsidered by the company and removed from their trading lineup if feasible.

   - Most Popular and Profitable Products
   
     ![image](https://user-images.githubusercontent.com/45563371/91668981-c80f3f00-eb43-11ea-8a9c-02573b21e85f.png)
     
     - Observation
       - The most popular products such as StkISN 10074 and 45869 have a wide gap between profit and quantity sold. 
       - It is evident that quite a large number of sellable products by New Ocean Trading is not the most profitable. 
       - Hence for products such as StkISN 10074, 45869, 10631, the firm may want to consider raising prices by a tiny margin as this can result in an exponential increase in profits.
     - Impact on Stock Up Timing
       - If these products are heavy or large in size, it may be uneconomical to trade in them and incur heavy costs in shipping and delivery in exchange for low profit margins. 
       - Hence, products such as StkISN 10074 and 45869 should be dropped from the trading lineup of New Ocean Trading. 

   - Profit Generated by Country and Region
   
     ![image](https://user-images.githubusercontent.com/45563371/91668997-f42ac000-eb43-11ea-90c6-ddc27e9aa71f.png)
     
     ![image](https://user-images.githubusercontent.com/45563371/91669000-ff7deb80-eb43-11ea-98ea-123bd2553549.png)
     
     - Observation
       - From the geographical distribution of both transactions and profits generated, Indonesia, followed by Singapore then Malaysia, are the most important customer bases for New Ocean Trading. All three countries are located in Southeast Asia, showing that the goods that New Ocean Trading trades in are important and popular commodities for businesses and manufacturing industries of Southeast Asia. 
       - Finland, not shown on the map above, generates a mere profit of around $4,000. Walk in non-regular customers who take up a sizeable proportion of all transactions, are generally not profitable for New Ocean Trading to deal with.
     - Impact on Regional Focus
       - There is no doubt that the regional focus for New Ocean Trading should be Southeast Asia. Australia, although close in proximity to Southeast Asia, is a minor customer base for the company. 
       - Finland is both geographically distant from Southeast Asia and a minor customer base for the company. One possible strategy to cut operational costs drive growth may be to withdraw resources from these two countries and redirect them to Southeast Asia. 
       - New Ocean Trading should also set up a regional office in Singapore (if they have not done so already), which is a centralised location in Southeast Asia and thus ideal for interacting with their regional customer bases.
     - Impact on Customer Loyalty Program
       - The company should try to convert walk in non-regular customers, who may purchase intermittently, into registered customers who trade regularly with New Ocean Trading so as to improve their profitability. Sign-up rewards can be provided to encourage these businesses to join the loyalty program and become regular customers. Otherwise, the company can offer discounts on high-margin products for walk-in customers who pay in cash to increase the profitability of this group.
       - New Ocean Trading could provide specific shipping discounts in Southeast Asia, to further attract customers from emerging economies within the region, such as the -       Philippines, Thailand and Vietnam. Customers can also be rewarded when they introduce other businesses to deal with New Ocean Trading.
       - The rewards provided through the loyalty program should also be based on the unique culture of each country. Malaysia and Indonesia and majority Muslim populated countries, hence seasonal rewards could be introduced inline with the cultural festive celebrations such as Hari Raya Haji and Hari Raya Puasa. New Ocean Trading can also partner with third-party firms from each country to provide locally customised rewards, and to ensure speedy delivery of physical rewards to their business customers.
     - Impact on Stock Up Timing
       - New Ocean Trading should expand on their lineup of commodities and exports traded in Southeast Asia, targeting goods like palm oil which is a popular export of Malaysia and Indonesia. 
       - Additionally, as Malaysia and Indonesia are Muslim populated countries, and Singapore is a Chinese-majority country, the company can anticipate the rise in popularity of certain goods during the respective seasonal festivities in the region, such as red fabric during Chinese New Year, and honey dates during Hari Raya, thus ensure stock up of these items before the festivities.

   - Forecast of Revenue and Quantity of Stocks
     
     ![image](https://user-images.githubusercontent.com/45563371/91669075-9fd41000-eb44-11ea-8f2a-f04ff717f7ef.png)
     
     ![image](https://user-images.githubusercontent.com/45563371/91669079-ab273b80-eb44-11ea-8c1d-6fabb4cf95c6.png)
     
     - Impact on Stock Up Timing
       - Forecasted the general quantities of all stock sold for the upcoming years. 
       - From this, New Ocean Trading can observe the forecast for upcoming quantity of stocks sold in each period to estimate the general number of all items to stock up in anticipation of the upcoming demand.
       - Due to their significance and high impact on the company’s revenue and profits, forecasted the quantities of stock sold for the top 5 most sold stocks, as well as the top 5 most profitable stocks. For example, for product StkISN 10074, demand starts to peak during 2019 Q3 at 88,000 predicted quantity sold, hence the company can begin stock up in 2019 Q2. This is to avoid stock out costs of:
         - Missing out on sales of profitable products
         - Potentially losing sales or losing customers due to unavailability of popular products.
       - New Ocean Trading can follow the forecast and stock up before every peak in quantities sold.

### Command Line User Interface
- The objective of the command line user interface (UI) is to provide New Ocean Trading a platform to easily visualise and understand their transactional records. Users can utilise our UI to view information about finances, customers, geographical distribution and stock in their transactions.
- Design Process
  
  |**SNo**|**Functions Required**                                   | **Design Intention**                                                                                      |
  |-------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
  | 1     | Selection of transactional records data for examination | The program is designed for users to have flexibility in choosing their dataset by time frame             |
  | 2     | Selection of transaction variables to analyse           | The program will focus on variables useful for New Ocean Trading’s business objectives                    |
  | 3     | Summary and analysis of variables                       | Create functions that will display summary, trends and insights on important elements in variables        |
  | 4     | Different view options for the summaries and analysis   | Include additional view options that allow users better visualisation like graphs or descriptive statistic|
  
- UI menu for dataset selection by time frame

  ![image](https://user-images.githubusercontent.com/45563371/91669251-0dcd0700-eb46-11ea-9790-1053b142647d.png)
  
- UI Main Menu for exploration of transactional records

  ![image](https://user-images.githubusercontent.com/45563371/91669264-2806e500-eb46-11ea-8ad8-c1522dba82e2.png)

- Descriptive Statistic - Output for Financial Trends Function

  ![image](https://user-images.githubusercontent.com/45563371/91669272-33f2a700-eb46-11ea-9271-8fcf32590199.png)
  
- Graphical View - Output for Transaction Trends Function

  ![image](https://user-images.githubusercontent.com/45563371/91669280-44a31d00-eb46-11ea-9c67-3eefc70948ff.png)

### Conclusion

| **Insights from data analysis**                                                                         | **Application for company**                                              | 
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Customer codes IJ01, IT23, IK11 and IT04 are the top most profitable customers                                  | The company can target to increase retention and encourage repeat transactions from these customers through the customer loyalty program |
| Products with StkISN 10126, 43513, 41534 are the top most profitable products                                   | The company can maintain high stocks of these products and target to increase the sales of these products in the customer loyalty program | 
| Popular products with StkISN 10074 and 45869 have a large gap between profit and its high quantity sold         | The company can raise the prices of these products by a tiny margin since it can result in an exponential increase in profits | 
| Indonesia, Singapore and Malaysia have the most important customer base                                         | The company can redirect resources from Australia and Finland to set their regional focus in SEA instead |
| There are increases in monthly revenue from February to March, April to May, November to December               | The company should stock up on high-demand items in these high sales seasons |
| Based on current demand and revenue trends for the top 5 most sold and profitable stock, a forecast was created | The company can stock up their inventory for these top 5 most sold and profitable stock based on the forecasted demand and revenue in future time periods |

## Code and Resources Used
- Python: Version 3.6
- Packages: pandas, numpy, os, datetime, matplotlib, seaborn, sklearn, dateutil
- Tableau
