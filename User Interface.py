# Import libraries
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import numpy as np
import os
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from dateutil.relativedelta import relativedelta  # relativedelta takes care of leap year

## Read in clean csv file
clean_csv = pd.read_csv("Clean_stockcards.csv")

# Format display float
pd.set_option('display.float_format', lambda x: '%.2f' % x)

############################# Start of Functions #####################################
def main():

    pd.to_numeric(clean_csv['Year'])
    clean_csv['Date'] = pd.to_datetime(clean_csv['Date'], format='%Y-%m-%d').dt.date
    clean_csv.sort_values('Date', inplace=True)

    print("Welcome to New Ocean Trading Transactions Program!")
    i_pref = " "
    global data

    # While loop for interface
    while i_pref != 3:
        try:
            i_pref = int(input("""Choose the time frame to analyse transactions:
1) Last 5 Years
2) Select the Start Date and End Date
3) End Program
Please choose 1, 2 or 3"""))
            if i_pref == 1:
                last_date = clean_csv['Date'].max()
                start_date = last_date - relativedelta(years=5)
                print("\n")
                data = clean_csv.loc[clean_csv.Date >= start_date]
                print(data)
                print("Here are the data you requested from {} to {}.".format(start_date, last_date))


            elif i_pref == 2:
                # Keep prompting user for min and max year till he get both inputs right
                while True:
                    try:
                        max_date = max(clean_csv.Date)
                        min_date = min(clean_csv.Date)
                        cmin = input("Choose your start date in YYYY-MM-DD format (Earliest Transaction = {})".format(min_date)).strip()
                        cmax = input("Choose your end date in YYYY-MM-DD format (Last Transaction = {})".format(max_date)).strip()
                        cmin = pd.to_datetime(cmin, format='%Y-%m-%d').date()
                        cmax = pd.to_datetime(cmax, format='%Y-%m-%d').date()
                        if cmin < min_date:
                            print("Starting date is too early, please try again")
                            continue
                        if cmax > max_date:
                            print("Ending date is too late, please try again")
                            continue
                        if cmax < cmin:
                            print(
                                "Error, please choose your dates again. Start date must be less than or equal to end date")
                            continue
                        else:
                            data = clean_csv[(clean_csv.Date >= cmin) & (clean_csv.Date <= cmax)]
                            print(data)
                            print("Here are the data you requested from {} to {}.".format(cmin, cmax))
                            break
                    except ValueError:
                        print("Please input only valid years between {} to {}".format(min_date, max_date))
                        continue


            # Exit the program
            elif i_pref == 3:
                print("Program will proceed to end!")
                break


            # Number not 1, 2 or 3
            elif i_pref not in range(1, 4):
                print("Please choose 1, 2 or 3 only.")
                continue
            # Ask user whether the data is correct
            try:
                correct_data = input("Is this the dataset you want? [Y/N]")
                if correct_data == 'n' or correct_data == 'N':
                    continue
                elif correct_data == 'y' or correct_data == 'Y':
                    print("We will proceed with this dataset.")
                    ChoosingMenu()
                    break
                elif i_pref not in (['y', 'Y', 'n', 'N']):
                    print("Please enter only y/n!")
                    continue
            except (IndexError, ValueError, TypeError):
                print("Please enter only y/n!")
                continue
        # Exception handling
        except (IndexError, ValueError, TypeError):
            print("I do not understand your input, please try again. Choose 1, 2 or 3 only.")
            continue
        break

def ChoosingMenu():
   while True:
       try:
           global mchoice
           mchoice=int(input(""" 
               [   MAIN MENU   ]  
Please choose an option:
================== FINANCE =====================
1) Financial Indicators Overview
================== CUSTOMER ====================
2) Summary
3) Transaction Trends
4) Purchase Trends
5) Financial Trends
6) Profit - Quantity Cluster Analysis
=================== STOCK ======================
7) Most Profitable Stock
8) Least Profitable Stock
9) Most Sold Stock
============ GEOGRAPHICAL REGION ===============
10) Profit & Quantity Summary by Customer Region
11) End Programme
Enter Your Input Here ->"""))
           if mchoice==1:
               financial_overview()
               break
           if mchoice ==2:
               cust_summary()
               break
           if mchoice == 3:
               transaction_trend()
               break
           if mchoice == 4:
               purchase_trend()
               break
           if mchoice == 5:
               financial_trend()
               break
           if mchoice == 6:
               cluster_analysis()
               break
           if mchoice == 7:
               topfiveprofitstocks()
               break
           if mchoice == 8:
               LeastprofitableStocks()
               break
           if mchoice == 9:
               topfivesoldstocks()
               break
           if mchoice == 10:
               regional_analysis()
               break
           if mchoice==11:
               print("Program will proceed to end.")
               break
           else:
               print("I do not understand your input please try again")
               continue
       except ValueError:
           print("Input Invalid, Please Try Again")
def graphshow():
   while True:
       try:
           choice=int(input("""Do you want to see in in graphical format?
1) Yes
2) No
Input here-> """))
           if choice==1:
               plt.show()
               break
           if choice==2:
               print("Ok")
               break
           else:
               print("Please enter 1 or 2")
               continue
       except ValueError:
           print("Please enter 1 or 2")
           continue

def returnmain():
   while True:
       try:
           choice = int(input("""Do you want to return to the Main Menu?
1) Yes
2) No
Input here-> """))
           if choice == 1:
               ChoosingMenu()
               break
           elif choice == 2:
               print("Program will proceed to end")
               break
           else:
               print("Please enter 1 or 2")
               continue
       except ValueError:
           print("Please enter 1 or 2")
           continue

# ------------------------------------ FINANCIAL OVERVIEW -----------------------------

def graph_choice():
    while True:
        try:
            g_choice = int(input("""
Do you want to see in in graphical format?
1) Yes
2) No
Input here-> """))
            if g_choice in (1, 2):
                break
            elif g_choice not in (1, 2):
                print("Please enter 1 or 2.")
        except ValueError:
            print("Please enter 1 or 2.")
            continue

    return g_choice

def group_choice():
    while True:
        try:
            choice = int(input("""
What do you want to group the dataset by?
1) Years
2) Year and Months
3) NIL
Input here-> """))
            if choice in (1, 2, 3):
                break
            elif choice not in (1, 2, 3):
                print("Please enter 1, 2 or 3.")
        except ValueError:
            print("Please enter 1, 2 or 3.")
            continue

    return choice


def cluster_choice():
    while True:
        try:
            choice = int(input("""Do you want to view the cluster analysis with Customer Code?
1) Yes
2) No
Input here-> """))
            if choice in (1, 2):
                break
            elif choice not in (1, 2):
                print("Please enter 1 or 2.")
        except ValueError:
            print("Please enter 1 or 2.")
            continue

    return choice



def financial_overview():
    # Change display setting of print(pandas.DataFrame)
    pd.set_option('display.max_rows', 120)
    pd.set_option('display.width', 150)
    pd.set_option('display.max_columns', 10)

    choice2 = group_choice()
    if choice2 == 1:
        dataset = data.copy()
        df = dataset.groupby(dataset.Year)["Amt", "Worth"].agg("sum").round(2)
        df["Total Profit (S$)"] = df["Amt"] - abs(df["Worth"])
        df.rename(columns={'Amt': 'Total Revenue (S$)', 'Worth': 'Total Cost of Goods Sold (S$)'}, inplace=True)
        df['Year'] = df.index
        df = df[['Year', 'Total Revenue (S$)', 'Total Cost of Goods Sold (S$)', 'Total Profit (S$)']]
        print("""Financial Overview
=============================================================================
{}""".format(df.to_string(index=False)))

        g_choice2 = graph_choice()
        if g_choice2 == 1:
            df["Total Cost of Goods Sold (S$)"] = abs(df["Total Cost of Goods Sold (S$)"])
            sns.lineplot(x="Year", y="Total Revenue (S$)", data=df, marker = "8")
            sns.lineplot(x="Year", y="Total Cost of Goods Sold (S$)", data=df, marker = "8")
            sns.lineplot(x="Year", y="Total Profit (S$)", data=df, marker = "8")
            plt.ticklabel_format(style='plain', axis='y')
            plt.legend(labels=['Total Revenue', 'Absolute Value of Total Cost of Goods Sold', 'Total Profit'], loc=1, prop={'size': 8})
            plt.ylabel("Singapore Dollars (S$)")
            plt.suptitle("Financial Overview by Year: {} to {}".format(min(dataset.Date), max(dataset.Date)), fontsize = 13)
            plt.show()
            returnmain()

        else:
            returnmain()

    elif choice2 == 2:
        dataset = data.copy()
        df = dataset.groupby([dataset.Year, dataset.Month])["Amt", "Worth"].agg("sum").round(2)
        df["Total Profit (S$)"] = df["Amt"] - abs(df["Worth"])
        df.rename(columns={'Amt': 'Total Revenue (S$)', 'Worth': 'Total Cost of Goods Sold (S$)'}, inplace=True)
        df["Year-Month"] = [str(df.index[i][0]) + '-' + str(df.index[i][1]) for i in range(len(df))]
        df = df[['Year-Month', 'Total Revenue (S$)', 'Total Cost of Goods Sold (S$)', 'Total Profit (S$)']]
        print("""Financial Overview
=============================================================================
{}""".format(df.to_string(index=False)))

        g_choice2 = graph_choice()
        if g_choice2 == 1:
            df["Total Cost of Goods Sold (S$)"] = abs(df["Total Cost of Goods Sold (S$)"])
            plt.xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Total Revenue (S$)", data=df, marker="8").set_xticklabels(df["Year-Month"])
            sns.lineplot(x=np.arange(len(df)), y="Total Cost of Goods Sold (S$)", data=df, marker="8").set_xticklabels(df["Year-Month"])
            sns.lineplot(x=np.arange(len(df)), y="Total Profit (S$)", data=df, marker="8").set_xticklabels(df["Year-Month"])
            plt.ticklabel_format(style='plain', axis='y')
            plt.legend(labels=['Total Revenue', 'Absolute Value of Total Cost of Goods Sold', 'Total Profit'], loc=1,
                       prop={'size': 8})
            plt.ylabel("Singapore Dollars (S$)")
            plt.xlabel("Year-Month")
            plt.suptitle("Financial Overview by Year-Month: {} to {}".format(min(dataset.Date), max(dataset.Date)),
                         fontsize=13)
            plt.show()
            returnmain()

        else:
            returnmain()

    elif choice2 == 3:
        dataset = data.copy()
        df = dataset[["Amt", "Worth"]].agg("sum").round(2)
        df["Total Profit (S$)"] = df["Amt"] - abs(df["Worth"])
        df.rename(index={'Amt': 'Total Revenue (S$)', 'Worth': 'Total Cost of Goods Sold (S$)'}, inplace=True)
        print("""Financial Overview
==============================================
{}""".format(df))
        returnmain()

# ------------------------------------CUSTOMER--------------------------------------------
def cust_summary():
    # Change display setting of print(pandas.DataFrame)
    pd.set_option('display.max_rows', 120)
    pd.set_option('display.width', 300)
    pd.set_option('display.max_columns', 10)

    choice2 = group_choice()
    if choice2 == 1:
        dataset = data.copy()
        # Number of Customers
        df = dataset.groupby(dataset.Year)["CustomerCode"].agg({'Unique Customers' : "nunique"})

        # Number of Transaction Type
        df2 = dataset.groupby([dataset.Year, dataset.Type])["Type"].agg({"Count" : "count"}).reset_index()
        df3 = df2.pivot(index='Year', columns='Type', values='Count')
        df4 = df.merge(df3, left_on='Year', right_on='Year')

        # Number of Cur Type
        df5 = dataset.groupby([dataset.Year, dataset.Cur])["Cur"].agg({"Count": "count"}).reset_index()
        df6 = df5.pivot(index='Year', columns='Cur', values='Count')
        df7 = df4.merge(df6, left_on='Year', right_on='Year')
        df7.rename(columns={'ICG': 'ICG Transactions',
                            'ICX': 'ICX Transactions',
                            'M$': "Transactions in M$",
                            'S$': "Transactions in S$",
                            'USD$': "Transactions in USD$"}, inplace=True)
        df7.reset_index(level=0, inplace=True)
        print("""Customer Information Summary 
                                                    Frequency Table
==========================================================================================================================
{}""".format(df7.to_string(index=False)))
        returnmain()

    elif choice2 == 2:
        dataset = data.copy()

        # Number of Customers
        df = dataset.groupby([dataset.Year, dataset.Month])["CustomerCode"].agg({'Unique Customers': "nunique"})
        df["Year-Month"] = [str(df.index[i][0]) + '-' + str(df.index[i][1]) for i in range(len(df))]
        df = df[['Year-Month', 'Unique Customers']]

        # Number of Transaction Type
        df2 = dataset.groupby([dataset.Year, dataset.Month, dataset.Type])["Type"].agg({"Count": "count"})
        df2["Year-Month"] = [str(df2.index[i][0]) + '-' + str(df2.index[i][1]) for i in range(len(df2))]
        df2['Type'] = df2.index.get_level_values('Type')
        df3 = df2.pivot(index='Year-Month', columns='Type', values='Count')
        df4 = df.merge(df3, left_on='Year-Month', right_on='Year-Month')

        # Number of Cur Type
        df5 = dataset.groupby([dataset.Year, dataset.Month, dataset.Cur])["Cur"].agg({"Count": "count"})
        df5["Year-Month"] = [str(df5.index[i][0]) + '-' + str(df5.index[i][1]) for i in range(len(df5))]
        df5['Cur'] = df5.index.get_level_values('Cur')
        df6 = df5.pivot(index='Year-Month', columns='Cur', values='Count')
        df7 = df4.merge(df6, left_on='Year-Month', right_on='Year-Month')
        df7.rename(columns={'ICG': 'ICG Transactions',
                            'ICX': 'ICX Transactions',
                            'M$': "Transactions in M$",
                            'S$': "Transactions in S$",
                            'USD$': "Transactions in USD$"}, inplace=True)
        print("""Customer Information Summary
                                                        Frequency Table
=====================================================================================================================================
        {}""".format(df7.to_string(index=False)))
        returnmain()


    elif choice2 == 3:
        dataset = data.copy()
        print("""Customer Information Summary
=======================================""")
        No_Cust = len(dataset.groupby(["CustomerCode"]))
        print("Number of Unique Customers = {}".format(No_Cust))
        print("---------------------------------------")
        No_TransCur = dataset.loc[:, ["Cur"]].groupby(["Cur"]).size().reset_index(name='Count').to_string(index=None)
        print("""Frequency of Transactions by Currency
{}""".format(No_TransCur))
        print("---------------------------------------")
        No_TransType = dataset.loc[:, ["Type"]].groupby(["Type"]).size().reset_index(name='Count').to_string(index=None)
        print("""Frequency of Transactions by Transaction Type
{}""".format(No_TransType))
        print("=======================================")
        returnmain()


def transaction_trend():
    # Change display setting of print(pandas.DataFrame)
    pd.set_option('display.max_rows', 120)
    pd.set_option('display.width', 300)
    pd.set_option('display.max_columns', 10)

    choice2 = group_choice()
    if choice2 == 1:
        dataset = data.copy()
        df = pd.DataFrame(columns=["Year", "NoT", "Mean NoT", "Median NoT", "Mode NoT", "Median QP per S", "Mode QP per S"])

        list_of_data = []
        list_of_years = sorted(dataset["Year"].unique())
        for index, year in enumerate(list_of_years):
            year_data = dataset[dataset.Year == year]
            list_of_data.append(year_data)

        for each in list_of_data:
            year_NoTrans = str(each["Year"].iloc[0])
            No_Trans = str(len(each))
            mean_NoTrans = float(each.groupby(each.CustomerCode).size().mean())
            median_NoTrans = float(each.groupby(each.CustomerCode).size().median())
            mode_NoTrans = str(list(each.groupby(each.CustomerCode).size().mode())).strip('[]')

            NoTrans_Qty = each.groupby(each.CustomerCode).size().to_frame()
            NoTrans_Qty = NoTrans_Qty.rename(columns={0: 'NoTrans'})
            each_Quantity = pd.DataFrame(each.groupby("CustomerCode").Quantity.sum())
            each_Quantity = each_Quantity[each_Quantity.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1)]
            NoTrans_Qty = pd.merge(NoTrans_Qty, each_Quantity, on='CustomerCode', how='left')
            NoTrans_Qty["TransSize"] = NoTrans_Qty["Quantity"] / NoTrans_Qty["NoTrans"]
            median_TransSize = int(NoTrans_Qty.TransSize.median())
            mode_TransSize = str(list(NoTrans_Qty.TransSize.mode().astype(int))).strip('[]')

            df_row = [year_NoTrans, No_Trans, mean_NoTrans, median_NoTrans, mode_NoTrans, median_TransSize, mode_TransSize]
            df.loc[len(df)] = df_row

        print("""Customer Transaction Trends
Number of Transactions (NoT)
Transaction Size ~ Quantity Purchased per StockISN (QP per S)
===============================================================================================================
{}
===============================================================================================================""".format(df.to_string(index=False)))

        g_choice2 = graph_choice()
        if g_choice2 == 1:
            df["Year"] = df["Year"].astype(int)
            df["NoT"] = df["NoT"].astype(int)
            df["Median QP per S"] = df["Median QP per S"].astype(int)
            fig, (ax1, ax2, ax3) = plt.subplots(3)
            fig.tight_layout(w_pad=1.4, h_pad=1.6)

            sns.lineplot(x="Year", y="NoT", data=df, marker="8", ax = ax1)
            ax1.set_ylabel("Number of Transactions", fontsize = 7)
            ax1.set_title("Customer Number of Transactions across the Years: {} to {}".format(min(dataset.Date), max(dataset.Date)),fontsize=9)

            sns.lineplot(x="Year", y="Median NoT", data=df, marker="8", ax=ax2, color="tomato")
            ax2.set_ylabel("Median Number of Transactions", fontsize = 7)
            ax2.set_title("The Average Customer's Number of Transactions across the Years: {} to {}".format(min(dataset.Date), max(dataset.Date)),fontsize=9)

            sns.lineplot(x="Year", y="Median QP per S", data=df, marker="8", ax=ax3, color="darkturquoise")
            ax3.set_ylabel("Median Quantity Purchased per StockISN", fontsize = 7)
            ax3.set_title(
                "The Average Customer's Transaction Size across the Years: {} to {}".format(min(dataset.Date),
                                                                                                  max(dataset.Date)),
                fontsize=9)


            plt.show()
            returnmain()

        else:
            returnmain()


    elif choice2 == 2:
        dataset = data.copy()
        df = pd.DataFrame(columns=["Year", "Month", "NoT", "Mean NoT", "Median NoT", "Mode NoT", "Median QP per S", "Mode QP per S"])

        list_of_data = []
        list_of_years = sorted(dataset["Year"].unique())
        for index, year in enumerate(list_of_years):
            year_data = dataset[dataset.Year == year]
            list_of_months = sorted(year_data["Month"].unique())
            for index, month in enumerate(list_of_months):
                month_data = year_data[year_data.Month == month]
                list_of_data.append(month_data)

        for each in list_of_data:
            year_NoTrans = str(each["Year"].iloc[0])
            month_NoTrans = str(each["Month"].iloc[0])
            No_Trans = str(len(each))
            mean_NoTrans = float(each.groupby(each.CustomerCode).size().mean())
            median_NoTrans = float(each.groupby(each.CustomerCode).size().median())
            mode_NoTrans = str(list(each.groupby(each.CustomerCode).size().mode())).strip('[]')

            NoTrans_Qty = each.groupby(each.CustomerCode).size().to_frame()
            NoTrans_Qty = NoTrans_Qty.rename(columns={0: 'NoTrans'})
            each_Quantity = pd.DataFrame(each.groupby("CustomerCode").Quantity.sum())
            each_Quantity = each_Quantity[each_Quantity.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1)]
            NoTrans_Qty = pd.merge(NoTrans_Qty, each_Quantity, on='CustomerCode', how='left')
            NoTrans_Qty["TransSize"] = NoTrans_Qty["Quantity"] / NoTrans_Qty["NoTrans"]
            median_TransSize = int(NoTrans_Qty.TransSize.median())
            mode_TransSize = str(list(NoTrans_Qty.TransSize.mode().astype(int))).strip('[]')

            df_row = [year_NoTrans, month_NoTrans, No_Trans, mean_NoTrans, median_NoTrans, mode_NoTrans, median_TransSize, mode_TransSize]
            df.loc[len(df)] = df_row

        print("""Customer Transaction Trends
Number of Transactions (NoT)
Transaction Size ~ Quantity Purchased per StockISN (QP per S)
===================================================================================================================
{}
===================================================================================================================""".format(df.to_string(index=False)))

        g_choice2 = graph_choice()
        if g_choice2 == 1:
            df["Year-Month"] = df["Year"] + "-" + df["Month"]
            df["NoT"] = df["NoT"].astype(int)
            df["Median QP per S"] = df["Median QP per S"].astype(int)

            fig, (ax1, ax2, ax3) = plt.subplots(3)
            fig.tight_layout(w_pad=1.4, h_pad=1.6)

            ax1.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="NoT", data=df, marker="8", ax=ax1).set_xticklabels(df["Year-Month"])
            ax1.set_ylabel("Number of Transactions", fontsize=7)
            ax1.set_title("Customer Number of Transactions across the Year-Months: {} to {}".format(min(dataset.Date), max(dataset.Date)), fontsize=9)

            ax2.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Median NoT", data=df, marker="8", ax=ax2, color="tomato").set_xticklabels(df["Year-Month"])
            ax2.set_ylabel("Median Number of Transactions", fontsize=7)
            ax2.set_title(
                "The Average Customer's Number of Transactions across the Year-Months: {} to {}".format(min(dataset.Date),
                                                                                                  max(dataset.Date)),
                fontsize=9)

            ax3.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Median QP per S", data=df, marker="8", ax=ax3,color="darkturquoise").set_xticklabels(df["Year-Month"])
            ax3.set_ylabel("Median Quantity Purchased per StockISN", fontsize=7)
            ax3.set_title("The Average Customer's Transaction Size across the Year-Months: {} to {}".format(min(dataset.Date), max(dataset.Date)), fontsize=9)

            plt.show()
            returnmain()

        else:
            returnmain()


    elif choice2 == 3:
        dataset = data.copy()
        print("""Customer Transaction Trends
===============================================""")
        No_Trans = len(dataset)
        print("Total Number of Transactions = {}".format(No_Trans))
        print("-----------------------------------------------")
        mean_NoTrans = dataset.groupby(dataset.CustomerCode).size().mean()
        median_NoTrans = dataset.groupby(dataset.CustomerCode).size().median()
        mode_NoTrans = list(dataset.groupby(dataset.CustomerCode).size().mode())
        print("""Across the Customers,
Mean Number of Transactions = {}
Median Number of Transactions = {}
Mode Number of Transactions: {}""".format(mean_NoTrans, median_NoTrans, mode_NoTrans))
        print("===============================================")
        returnmain()


def purchase_trend():
    # Change display setting of print(pandas.DataFrame)
    pd.set_option('display.max_rows', 120)
    pd.set_option('display.width', 300)
    pd.set_option('display.max_columns', 10)

    choice2 = group_choice()
    if choice2 == 1:
        dataset1 = data.copy()
        df = pd.DataFrame(columns=["Year", "Total Quantity Purchased", "Median QP",
                                   "Total Number of Unique StockISN", "Median NoUS",
                                   "Mode NoUS", "Median QP per StockISN"])

        list_of_data = []
        list_of_years = sorted(dataset1["Year"].unique())
        for index, year in enumerate(list_of_years):
            year_data = dataset1[dataset1.Year == year]
            list_of_data.append(year_data)

        for dataset in list_of_data:
            # Year
            year_purchase = str(dataset["Year"].iloc[0])

            # Quantity Purchased
            dataset_Quantity = pd.DataFrame(dataset.groupby("CustomerCode").Quantity.sum())
            dataset_Quantity = dataset_Quantity[
                dataset_Quantity.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1)]
            total_Qty = int(dataset_Quantity.Quantity.sum())
            median_Qty = int(dataset_Quantity.Quantity.median())

            # Number of Unique StockISN
            total_NoStkType = dataset["StockISN"].nunique()
            median_NoStkType = int(dataset.groupby(dataset.CustomerCode).StockISN.nunique().median())
            mode_NoStkType = str(list(dataset.groupby(dataset.CustomerCode).StockISN.nunique().mode())).strip('[]')

            # Purchase Variety: Quantity Purchased per StockISN
            NoStkType_Qty = dataset.groupby("CustomerCode").StockISN.nunique().to_frame()
            NoStkType_Qty = NoStkType_Qty.rename(columns={"StockISN": 'NoStkType'})
            dataset_Quantity = pd.DataFrame(dataset.groupby("CustomerCode").Quantity.sum())
            dataset_Quantity = dataset_Quantity[
                dataset_Quantity.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1)]
            NoStkType_Qty = pd.merge(NoStkType_Qty, dataset_Quantity, on='CustomerCode', how='left')
            NoStkType_Qty["PurchaseVariety"] = NoStkType_Qty["Quantity"] / NoStkType_Qty["NoStkType"]
            median_PurchaseVariety = int(NoStkType_Qty.PurchaseVariety.median())

            df_row = [year_purchase, total_Qty, median_Qty, total_NoStkType,
                      median_NoStkType, mode_NoStkType, median_PurchaseVariety]
            df.loc[len(df)] = df_row

        print("""Customer Purchase Trends
Quantity Purchased (QP)
Number of Unique StockISN (NoUS)
Purchase Variety ~ Quantity Purchased Per StockISN (QP per StockISN)
=====================================================================================================================
{}
=====================================================================================================================""".format(
            df.to_string(index=False)))

        g_choice2 = graph_choice()
        if g_choice2 == 1:
            df["Year"] = df["Year"].astype(int)
            df["Total Quantity Purchased"] = df["Total Quantity Purchased"].astype(int)
            df["Median QP"] = df["Median QP"].astype(int)
            df["Total Number of Unique StockISN"] = df["Total Number of Unique StockISN"].astype(int)
            df["Median NoUS"] = df["Median NoUS"].astype(int)
            df["Median QP per StockISN"] = df["Median QP per StockISN"].astype(int)
            fig, ([ax1, ax2], [ax3, ax4], [ax5, ax6]) = plt.subplots(3, 2)
            fig.tight_layout(w_pad=1.4, h_pad=1.4)

            sns.lineplot(x="Year", y="Total Quantity Purchased", data=df, marker="8", ax=ax1)
            ax1.set_ylabel("Total Quantity Purchased", fontsize=6)
            ax1.set_title("Total Quantity Customer Purchased across the Years: {} to {}".format(min(dataset1.Date),
                                                                                                max(dataset1.Date)),
                          fontsize=9)

            sns.lineplot(x="Year", y="Median QP", data=df, marker="8", ax=ax2)
            ax2.set_ylabel("Median Quantity Purchased", fontsize=6)
            ax2.set_title(
                "The Average Customer's Quantity Purchased across the Years: {} to {}".format(min(dataset1.Date),
                                                                                              max(dataset1.Date)),
                fontsize=9)

            sns.lineplot(x="Year", y="Total Number of Unique StockISN", data=df, marker="8", ax=ax3, color="tomato")
            ax3.set_ylabel("Total Number of Unique StockISN", fontsize=6)
            ax3.set_title(
                "Number of Unique StockISN Customer Purchased across the Years: {} to {}".format(min(dataset1.Date),
                                                                                                 max(dataset1.Date)),
                fontsize=9)

            sns.lineplot(x="Year", y="Median NoUS", data=df, marker="8", ax=ax4, color="tomato")
            ax4.set_ylabel("Median Number of StockISN", fontsize=6)
            ax4.set_title("The Average Customer's Number of StockISN Purchased across the Years: {} to {}".format(
                min(dataset1.Date), max(dataset1.Date)), fontsize=9)

            sns.lineplot(x="Year", y="Median QP per StockISN", data=df, marker="8", ax=ax5, color="darkturquoise")
            ax5.set_ylabel("Median Quantity Purchased per StockISN", fontsize=6)
            ax5.set_title("The Average Customer's Purchase Variety across the Years: {} to {}".format(min(dataset1.Date),
                                                                                                      max(
                                                                                                          dataset1.Date)),
                          fontsize=9)

            plt.show()
            returnmain()
        else:
            returnmain()

    elif choice2 == 2:
        dataset1 = data.copy()
        df = pd.DataFrame(columns=["Year", "Month", "Total Quantity Purchased", "Median QP",
                                   "Total Number of Unique StockISN", "Median NoUS",
                                   "Mode NoUS", "Median QP per StockISN"])

        list_of_data = []
        list_of_years = sorted(dataset1["Year"].unique())
        for index, year in enumerate(list_of_years):
            year_data = dataset1[dataset1.Year == year]
            list_of_months = sorted(year_data["Month"].unique())
            for index, month in enumerate(list_of_months):
                month_data = year_data[year_data.Month == month]
                list_of_data.append(month_data)

        for dataset in list_of_data:
            # Year, Month
            year_purchase = str(dataset["Year"].iloc[0])
            month_purchase = str(dataset["Month"].iloc[0])

            # Quantity Purchased
            dataset_Quantity = pd.DataFrame(dataset.groupby("CustomerCode").Quantity.sum())
            dataset_Quantity = dataset_Quantity[
                dataset_Quantity.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1)]
            total_Qty = int(dataset_Quantity.Quantity.sum())
            median_Qty = int(dataset_Quantity.Quantity.median())

            # Number of Unique StockISN
            total_NoStkType = dataset["StockISN"].nunique()
            median_NoStkType = int(dataset.groupby(dataset.CustomerCode).StockISN.nunique().median())
            mode_NoStkType = str(list(dataset.groupby(dataset.CustomerCode).StockISN.nunique().mode())).strip('[]')

            # Purchase Variety: Quantity Purchased per StockISN
            NoStkType_Qty = dataset.groupby("CustomerCode").StockISN.nunique().to_frame()
            NoStkType_Qty = NoStkType_Qty.rename(columns={"StockISN": 'NoStkType'})
            dataset_Quantity = pd.DataFrame(dataset.groupby("CustomerCode").Quantity.sum())
            dataset_Quantity = dataset_Quantity[
                dataset_Quantity.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1)]
            NoStkType_Qty = pd.merge(NoStkType_Qty, dataset_Quantity, on='CustomerCode', how='left')
            NoStkType_Qty["PurchaseVariety"] = NoStkType_Qty["Quantity"] / NoStkType_Qty["NoStkType"]
            median_PurchaseVariety = int(NoStkType_Qty.PurchaseVariety.median())
            df_row = [year_purchase, month_purchase, total_Qty, median_Qty, total_NoStkType,
                      median_NoStkType, mode_NoStkType, median_PurchaseVariety]
            df.loc[len(df)] = df_row

        print("""Customer Purchase Trends
Quantity Purchased (QP)
Number of Unique StockISN (NoUS)
Purchase Variety ~ Quantity Purchased Per StockISN (QP per StockISN)
===============================================================================================================================
{}
===============================================================================================================================""".format(
            df.to_string(index=False)))

        g_choice2 = graph_choice()
        if g_choice2 == 1:
            df["Year-Month"] = df["Year"] + "-" + df["Month"]
            df["Total Quantity Purchased"] = df["Total Quantity Purchased"].astype(int)
            df["Median QP"] = df["Median QP"].astype(int)
            df["Total Number of Unique StockISN"] = df["Total Number of Unique StockISN"].astype(int)
            df["Median NoUS"] = df["Median NoUS"].astype(int)
            df["Median QP per StockISN"] = df["Median QP per StockISN"].astype(int)
            fig, ([ax1, ax2], [ax3, ax4], [ax5, ax6]) = plt.subplots(3, 2)
            fig.tight_layout(w_pad=1.4, h_pad=1.4)

            ax1.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Total Quantity Purchased", data=df, marker="8",
                         ax=ax1).set_xticklabels(df["Year-Month"])
            ax1.set_ylabel("Total Quantity Purchased", fontsize=6)
            ax1.set_title("Total Quantity Customer Purchased across the Years: {} to {}".format(min(dataset1.Date),
                                                                                                max(dataset1.Date)),
                          fontsize=9)

            ax2.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Median QP", data=df, marker="8", ax=ax2).set_xticklabels(
                df["Year-Month"])
            ax2.set_ylabel("Median Quantity Purchased", fontsize=6)
            ax2.set_title(
                "The Average Customer's Quantity Purchased across the Years: {} to {}".format(min(dataset1.Date),
                                                                                              max(dataset1.Date)),
                fontsize=9)

            ax3.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Total Number of Unique StockISN", data=df, marker="8", ax=ax3,
                         color="tomato").set_xticklabels(df["Year-Month"])
            ax3.set_ylabel("Total Number of Unique StockISN", fontsize=6)
            ax3.set_title(
                "Number of Unique StockISN Customer Purchased across the Years: {} to {}".format(min(dataset1.Date),
                                                                                                 max(dataset1.Date)),
                fontsize=9)

            ax4.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Median NoUS", data=df, marker="8", ax=ax4,
                         color="tomato").set_xticklabels(df["Year-Month"])
            ax4.set_ylabel("Median Number of StockISN", fontsize=6)
            ax4.set_title("The Average Customer's Number of StockISN Purchased across the Years: {} to {}".format(
                min(dataset1.Date), max(dataset1.Date)), fontsize=9)

            ax5.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Median QP per StockISN", data=df, marker="8", ax=ax5,
                         color="darkturquoise").set_xticklabels(df["Year-Month"])
            ax5.set_ylabel("Median Quantity Purchased per StockISN", fontsize=6)
            ax5.set_title("The Average Customer's Purchase Variety across the Years: {} to {}".format(min(dataset1.Date),
                                                                                                      max(
                                                                                                          dataset1.Date)),
                          fontsize=9)

            plt.show()
            returnmain()
        else:
            returnmain()

    elif choice2 == 3:
        dataset = data.copy()
        print("""Customer Purchase Trends
===============================================""")
        dataset = dataset[dataset.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1)]
        total_Qty = int(dataset["Quantity"].sum())
        median_Qty = int(dataset.groupby(dataset.CustomerCode)["Quantity"].sum().median())
        mode_Qty = list(dataset.groupby(dataset.CustomerCode)["Quantity"].sum().mode())

        total_NoUS = dataset["StockISN"].nunique()
        median_NoUS = int(dataset.groupby(dataset.CustomerCode).StockISN.nunique().median())
        mode_NoUS = list(dataset.groupby(dataset.CustomerCode).StockISN.nunique().mode())

        NoStkType_Qty = dataset.groupby("CustomerCode").StockISN.nunique().to_frame()
        NoStkType_Qty = NoStkType_Qty.rename(columns={"StockISN": 'NoStkType'})
        dataset_Quantity = pd.DataFrame(dataset.groupby("CustomerCode").Quantity.sum())
        dataset_Quantity = dataset_Quantity[dataset_Quantity.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1)]
        NoStkType_Qty = pd.merge(NoStkType_Qty, dataset_Quantity, on='CustomerCode', how='left')
        NoStkType_Qty["PurchaseVariety"] = NoStkType_Qty["Quantity"] / NoStkType_Qty["NoStkType"]
        median_PurchaseVariety = int(NoStkType_Qty.PurchaseVariety.median())
        mode_PurchaseVariety = list(NoStkType_Qty.PurchaseVariety.mode())

        print("Total Quantity Purchased = {}".format(total_Qty))
        print("""Across the Customers,
Median of Quantity Purchased = {}
Mode of Quantity Purchased: {}""".format(median_Qty, mode_Qty))
        print("-----------------------------------------------")
        print("Total Number of Unique Stock Purchased = {}".format(total_NoUS))
        print("""Across the Customers,
Median Number of Unique Stock Purchased = {}
Mode Number of Unique Stock Purchased: {}""".format(median_NoUS, mode_NoUS))
        print("-----------------------------------------------")
        print("""Across the Customers,
Median Purchase Variety (Quantity Purchased per StockISN) = {}
Mode Number of Unique Stock Purchased: {}""".format(median_PurchaseVariety, mode_PurchaseVariety))
        returnmain()


def financial_trend():
    # Change display setting of print(pandas.DataFrame)
    pd.set_option('display.max_rows', 120)
    pd.set_option('display.width', 300)
    pd.set_option('display.max_columns', 10)

    choice2 = group_choice()
    if choice2 == 1:
        dataset1 = data.copy()
        df = pd.DataFrame(columns=["Year", "Median Revenue",
                                   "Median Cost of Goods Sold",
                                   "Median Profit"])

        list_of_data = []
        list_of_years = sorted(dataset1["Year"].unique())
        for index, year in enumerate(list_of_years):
            year_data = dataset1[dataset1.Year == year]
            list_of_data.append(year_data)

        for dataset in list_of_data:
            # Year
            year_finance = str(dataset["Year"].iloc[0])

            # Revenue
            median_Rev = round(dataset.groupby(dataset.CustomerCode).Amt.sum().median(), 2)

            # Cost
            median_Cost = round(dataset.groupby(dataset.CustomerCode).Worth.sum().median(), 2)

            # Profit
            median_Profit = round(dataset.groupby(dataset.CustomerCode).Profit.sum().median(), 2)

            df_row = [year_finance, median_Rev, median_Cost, median_Profit]
            df.loc[len(df)] = df_row

        print("""Customer Financial Trends
==========================================================================
{}
==========================================================================""".format(df.to_string(index=False)))

        g_choice2 = graph_choice()
        if g_choice2 == 1:
            df["Year"] = df["Year"].astype(int)
            df["Median Revenue"] = df["Median Revenue"].astype(float)
            df["Median Cost of Goods Sold"] = abs(df["Median Cost of Goods Sold"].astype(float))
            df["Median Profit"] = df["Median Profit"].astype(float)
            fig, (ax1, ax2, ax3) = plt.subplots(3)
            fig.tight_layout(w_pad=1.4, h_pad=1.6)

            sns.lineplot(x="Year", y="Median Revenue", data=df, marker="8", ax=ax1)
            ax1.set_ylabel("Median Revenue", fontsize=9)
            ax1.set_title("The Average Customer's Revenue across the Years: {} to {}".format(min(dataset1.Date),
                                                                                             max(dataset1.Date)),
                          fontsize=10)

            sns.lineplot(x="Year", y="Median Cost of Goods Sold", data=df, marker="8", ax=ax2, color="tomato")
            ax2.set_ylabel("Median Customer Absolute Cost of Goods Sold", fontsize=7)
            ax2.set_title(
                "The Average Customer's Cost of Goods Sold across the Years: {} to {}".format(min(dataset1.Date),
                                                                                              max(dataset1.Date)),
                fontsize=10)

            sns.lineplot(x="Year", y="Median Profit", data=df, marker="8", ax=ax3, color="darkturquoise")
            ax3.set_ylabel("Median Customer Profit", fontsize=9)
            ax3.set_title("The Average Customer's Profit across the Years: {} to {}".format(min(dataset1.Date),
                                                                                            max(dataset1.Date)),
                          fontsize=10)

            plt.show()
            returnmain()
        else:
            returnmain()


    elif choice2 == 2:
        dataset1 = data.copy()
        df = pd.DataFrame(columns=["Year", "Month", "Median Revenue",
                                   "Median Cost of Goods Sold",
                                   "Median Profit"])

        list_of_data = []
        list_of_years = sorted(dataset1["Year"].unique())
        for index, year in enumerate(list_of_years):
            year_data = dataset1[dataset1.Year == year]
            list_of_months = sorted(year_data["Month"].unique())
            for index, month in enumerate(list_of_months):
                month_data = year_data[year_data.Month == month]
                list_of_data.append(month_data)

        for dataset in list_of_data:
            # Year, Month
            year_finance = str(dataset["Year"].iloc[0])
            month_finance = str(dataset["Month"].iloc[0])

            # Revenue
            median_Rev = dataset.groupby(dataset.CustomerCode).Amt.sum().median().round(2)

            # Cost
            median_Cost = dataset.groupby(dataset.CustomerCode).Worth.sum().median().round(2)

            # Profit
            median_Profit = dataset.groupby(dataset.CustomerCode).Profit.sum().median().round(2)

            df_row = [year_finance, month_finance, median_Rev, median_Cost, median_Profit]
            df.loc[len(df)] = df_row

        print("""Customer Financial Trends
==========================================================================
{}
==========================================================================""".format(df.to_string(index=False)))

        g_choice2 = graph_choice()
        if g_choice2 == 1:
            df["Year-Month"] = df["Year"] + "-" + df["Month"]
            df["Median Revenue"] = df["Median Revenue"].astype(float)
            df["Median Cost of Goods Sold"] = abs(df["Median Cost of Goods Sold"].astype(float))
            df["Median Profit"] = df["Median Profit"].astype(float)
            fig, (ax1, ax2, ax3) = plt.subplots(3)
            fig.tight_layout(w_pad=1.4, h_pad=1.6)

            ax1.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Median Revenue", data=df, marker="8", ax=ax1).set_xticklabels(
                df["Year-Month"])
            ax1.set_ylabel("Median Revenue", fontsize=9)
            ax1.set_xlabel("Year-Month", fontsize=9)
            ax1.set_title("The Average Customer's Revenue across the Year-Months: {} to {}".format(min(dataset1.Date),
                                                                                                   max(dataset1.Date)),
                          fontsize=10)

            ax2.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Median Cost of Goods Sold", data=df, marker="8", ax=ax2,
                         color="tomato").set_xticklabels(df["Year-Month"])
            ax2.set_ylabel("Median Customer Absolute Cost of Goods Sold", fontsize=7)
            ax2.set_xlabel("Year-Month", fontsize=9)
            ax2.set_title(
                "The Average Customer's Cost of Goods Sold across the Year-Months: {} to {}".format(min(dataset1.Date),
                                                                                                    max(dataset1.Date)),
                fontsize=10)

            ax3.set_xticks(np.arange(len(df)))
            sns.lineplot(x=np.arange(len(df)), y="Median Profit", data=df, marker="8", ax=ax3,
                         color="darkturquoise").set_xticklabels(df["Year-Month"])
            ax3.set_ylabel("Median Customer Profit", fontsize=9)
            ax3.set_xlabel("Year-Month", fontsize=9)
            ax3.set_title("The Average Customer's Profit across the Year-Month: {} to {}".format(min(dataset1.Date),
                                                                                                 max(dataset1.Date)),
                          fontsize=10)

            plt.show()
            returnmain()
        else:
            returnmain()


    elif choice2 == 3:
        dataset = data.copy()
        print("""Customer Financial Trends
===============================================""")
        # Revenue
        median_Rev = dataset.groupby(dataset.CustomerCode).Amt.sum().median().round(2)
        mode_Rev = str(list(dataset.groupby(dataset.CustomerCode).Amt.sum().mode().round(2)))

        # Cost
        median_Cost = dataset.groupby(dataset.CustomerCode).Worth.sum().median().round(2)
        mode_Cost = str(list(dataset.groupby(dataset.CustomerCode).Worth.sum().mode().round(2)))

        # Profit
        median_Profit = dataset.groupby(dataset.CustomerCode).Profit.sum().median().round(2)
        mode_Profit = str(list(dataset.groupby(dataset.CustomerCode).Profit.sum().mode().round(2)))

        print("""Across the Customers,
Median Revenue = {}
Mode Revenue: {}""".format(median_Rev, mode_Rev))
        print("-----------------------------------------------")
        print("""Across the Customers,
Median Cost of Goods Sold = {}
Mode Cost of Goods Sold: {}""".format(median_Cost, mode_Cost))
        print("-----------------------------------------------")
        print("""Across the Customers,
Median Profit = {}
Mode Profit: {}""".format(median_Profit, mode_Profit))
        print("-----------------------------------------------")
        returnmain()

def cluster_analysis():
    dataset = data.copy()
    startyear = dataset.iloc[0].Year
    endyear = dataset.iloc[-1].Year
    num_of_plots = endyear - startyear
    start = startyear
    fig, ax = plt.subplots(3, 3, sharex=True, sharey=True)
    fig.set_size_inches(5.5, 3)
    fig.tight_layout(w_pad=1.5, h_pad=1.5)
    fig.suptitle('Customer Profit-Quantity Cluster Analysis across the Years: {} to {}'.format(min(dataset.Date),
                                                                                                 max(dataset.Date)), fontsize=12)
    fig.subplots_adjust(top=0.88)
    c_choice = cluster_choice()

    for i in range(num_of_plots + 1):
        #Based on user input, subset the df with only those years and group by customer code
        #Sum up the profit and quantity for each customer for the year
        #Remove customers with profit/quantity = 0. This is probably because they do not exist during that year. Possible that customer legit had profit of 0 but the chances are very low.
        #Given that profit and quantity subsets eventually have the same length, no customers were wrongly removed. i.e. customer exists but 0 profit
        cust_profit = dataset.loc[dataset.Year == start].groupby('CustomerCode').Profit.sum()
        cust_profit = cust_profit[cust_profit != 0]
        cust_profit.head()

        cust_quantity = dataset.loc[dataset.Year == start].groupby('CustomerCode').Quantity.sum()
        cust_quantity = cust_quantity[cust_quantity != 0]
        cust_quantity.head()

        #Create a dataframe combining both profit and quantity
        profit_quantity = pd.DataFrame({'Profit':cust_profit, 'Quantity': cust_quantity})
        profit_quantity['CustomerCode'] = profit_quantity.index
        profit_quantity

        #Remove all infinity and nan values. These are mostly caused by division by zero errors.
        profit_quantity = profit_quantity[profit_quantity.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1)]
        profit_quantity

        #Instantiate kmeans and fit the dataframe
        #Number of clusters can be based on the elbow graph or based on domain knowledge instead of statistical opinions
        kmeans = KMeans(n_clusters = 4, random_state = 0).fit(profit_quantity[["Profit", "Quantity"]])

        #View the label for each customer
        #View the cluster center coordinates for each cluster
        kmeans.labels_
        kmeans.cluster_centers_

        if c_choice == 1:
        #Plot the final clustering
            row, col = int(i / 3), i % 3
            ax[row,col].scatter(profit_quantity.Profit, profit_quantity.Quantity, s = 3, c = kmeans.labels_, cmap = 'rainbow', marker= "D")
            ax[row,col].set_xlabel("Profit")
            ax[row,col].set_ylabel("Quantity")
            ax[row,col].set_title("Cluster Plot for Year {}".format(start))
            ax[row,col].xaxis.set_tick_params(which='both', labelbottom=True)
            ax[row, col].yaxis.set_tick_params(which='both', labelbottom=True)
            # Label Customer Code on each scatter point
            for i, txt in enumerate(profit_quantity.CustomerCode):
                ax[row, col].annotate(txt, (profit_quantity.Profit[i], profit_quantity.Quantity[i]))
            #Update next plot title by increasing 1 year
            start += 1

        elif c_choice == 2:
            row, col = int(i / 3), i % 3
            ax[row, col].scatter(profit_quantity.Profit, profit_quantity.Quantity, s=3, c=kmeans.labels_,
                                 cmap='rainbow', marker="D")
            ax[row, col].set_xlabel("Profit")
            ax[row, col].set_ylabel("Quantity")
            ax[row, col].set_title("Cluster Plot for Year {}".format(start))
            ax[row, col].xaxis.set_tick_params(which='both', labelbottom=True)
            ax[row, col].yaxis.set_tick_params(which='both', labelbottom=True)
            # Update next plot title by increasing 1 year
            start += 1

    plt.show()
    returnmain()

# ----------------------------------STOCK ------------------------------------------------
def LeastprofitableStocks():
   stock_profit32 = data[data['Profit'].replace([np.inf, -np.inf], np.nan).notnull()]
   stock_profit32 = stock_profit32[stock_profit32['Quantity'].replace([np.inf, -np.inf], np.nan).notnull()]
   while True:
       try:
           choice = int(input("""What do you want to group the dataset by?
1) Years
2) Months
3) NIL
Input here-> """))
           if choice == 1:
               stock_profit32 = stock_profit32.groupby(['StockISN','Year'], as_index=False)[['Quantity','Profit']].sum()
               for i in stock_profit32.Year.unique():
                   print("For Year {} the bottom 5 stocks are:".format(i))
                   print(stock_profit32[stock_profit32.Year == i].nsmallest(5, 'Profit'))
               break
           elif choice == 2:
               stock_profit32 = stock_profit32.groupby(['StockISN','Month'], as_index=False)[['Quantity','Profit']].sum()
               for i in stock_profit32.Month.unique():
                   print("For Month {} the top 5 stocks are:".format(i))
                   print(stock_profit32[stock_profit32.Month == i].nsmallest(5, 'Profit'))
               break
           elif choice == 3:
               stock_profit32=stock_profit32.groupby('StockISN',as_index=False)[['Quantity','Profit']].sum()
               print("The top 10 most sold items in the timeframe is:")
               print(stock_profit32.nsmallest(10, "Profit"))
               break
           else:
               print("Please enter 1, 2 or 3")
               continue
       except ValueError:
           print("Please enter 1, 2 or 3")
           continue
   returnmain()

def topfivesoldstocks():
   stock_isn3=data[data['Quantity'].replace([np.inf, -np.inf], np.nan).notnull()]
   stock_isn3=stock_isn3[stock_isn3['Profit'].replace([np.inf, -np.inf], np.nan).notnull()]
   while True:
       try:
           choice = int(input("""What do you want to group the dataset by?
1) Years
2) Months
3) NIL
Input here-> """))
           if choice == 1:
               fig, ax = plt.subplots(3, 3)
               fig.set_size_inches(5.5, 3)
               fig.tight_layout(w_pad=1.5, h_pad=1.5)
               stock_isn3 = stock_isn3.groupby(['StockISN','Year'], as_index=False)[['Quantity','Profit']].sum()
               a=0
               for i in stock_isn3.Year.unique():
                   print("For Year {} the top 5 stocks are:".format(i))
                   print(stock_isn3[stock_isn3.Year == i].nlargest(5, 'Quantity'))
                   tempprint=stock_isn3[stock_isn3.Year == i].nlargest(5, 'Quantity')
                   a+=1
                   row, col = int(a / 3), a% 3
                   ax[row, col].bar(tempprint.StockISN,tempprint.Quantity,color="#00BFC4")
                   ax[row, col].set_xticks(tempprint.StockISN)
               graphshow()
               break
           elif choice == 2:
               stock_isn3 = stock_isn3.groupby(['StockISN', 'Month'],as_index=False)[['Quantity', 'Profit']].sum()
               for i in stock_isn3.Month.unique():
                   print("For Month {} the top 5 stocks are:".format(i))
                   print(stock_isn3[stock_isn3.Month == i].nlargest(5, 'Quantity'))
               break
           elif choice == 3:
               stock_isn3=stock_isn3.groupby('StockISN',as_index=False)[['Quantity','Profit']].sum()
               print("The top 10 most sold items in the timeframe is:")
               print(stock_isn3.nlargest(10, "Quantity"))
               tempprint = stock_isn3.nlargest(10, 'Quantity')
               plt.scatter(tempprint.StockISN,tempprint.Quantity,color="#00BFC4")
               graphshow()
               break
           else:
               print("Please enter 1, 2 or 3")
               continue
       except ValueError:
           print("Please enter 1, 2 or 3")
           continue
   returnmain()


def topfiveprofitstocks():
   stock_profit3 = data[data['Profit'].replace([np.inf, -np.inf], np.nan).notnull()]
   stock_profit3 = stock_profit3[stock_profit3['Quantity'].replace([np.inf, -np.inf], np.nan).notnull()]
   while True:
       try:
           choice = int(input("""What do you want to group the dataset by?
1) Years
2) Months
3) NIL
Input here-> """))
           if choice == 1:
               stock_profit3 = stock_profit3.groupby(['StockISN','Year'], as_index=False)[['Quantity','Profit']].sum()
               for i in stock_profit3.Year.unique():
                   print("For Year {} the top 5 stocks are:".format(i))
                   print(stock_profit3[stock_profit3.Year == i].nlargest(5, 'Profit'))
               break
           elif choice == 2:
               stock_profit3 = stock_profit3.groupby(['StockISN','Month'], as_index=False)[['Quantity','Profit']].sum()
               for i in stock_profit3.Month.unique():
                   print("For Month {} the top 5 stocks are:".format(i))
                   print(stock_profit3[stock_profit3.Month == i].nlargest(5, 'Profit'))
               break
           elif choice == 3:
               stock_profit3=stock_profit3.groupby('StockISN',as_index=False)[['Quantity','Profit']].sum()
               print("The top 10 most sold items in the timeframe is:")
               print(stock_profit3.nlargest(10, "Profit"))
               break
           else:
               print("Please enter 1, 2 or 3")
               continue
       except ValueError:
           print("Please enter 1, 2 or 3")
           continue
   returnmain()

# ------------------------------------ CUSTOMER REGION -------------------------------------

def regional_analysis():
    # Convert all inf to nan values and remove those nans
    regional_data = data[data.replace([np.inf, -np.inf], np.nan).notnull()]

    while True:
        try:
            regional = regional_data.loc[:, ['CustomerRegion', 'Year', 'Month', 'Profit', 'Quantity']].sort_values(
                ['CustomerRegion', 'Year', 'Month'])
            choice = int(input("""What do you want to group the dataset by?
1) Year
2) Year and Month
3) NIL
Input -> """))
            if choice == 1:
                rp_cust_reg_year = regional.groupby(['CustomerRegion', 'Year'])[['Profit', 'Quantity']].sum()
                rp_cust_reg_year = pd.DataFrame(rp_cust_reg_year)
                rp_cust_reg_year.reset_index(inplace=True)
                print(rp_cust_reg_year)
                returnmain()
                break
            elif choice == 2:
                rp_cust_reg_ymonth = regional.groupby(['CustomerRegion', 'Year', 'Month'])[['Profit', 'Quantity']].sum()
                rp_cust_reg_ymonth = pd.DataFrame(rp_cust_reg_ymonth)
                rp_cust_reg_ymonth.reset_index(inplace=True)
                print(rp_cust_reg_ymonth)
                returnmain()
                break
            else:
                rp_cust_reg = regional.groupby('CustomerRegion')[['Profit', 'Quantity']].sum()
                rp_cust_reg = pd.DataFrame(rp_cust_reg)
                rp_cust_reg.reset_index(inplace=True)
                print(rp_cust_reg)
                returnmain()
                break
        except ValueError:
            print("Please enter 1, 2 or 3.")
            continue


###################################### End of Functions ###################################

main()

