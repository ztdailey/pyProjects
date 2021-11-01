import pandas as pd
import xlsxwriter
import datetime

    #Import data from fcm cloud
inc_st = pd.read_json("https://fmpcloud.io/api/v3/income-statement/AAPL?limit=120&apikey=6562b55c10cc4519f6de03db8f12da7f")
fcf = pd.read_json("https://fmpcloud.io/api/v3/cash-flow-statement/AAPL?limit=120&apikey=6562b55c10cc4519f6de03db8f12da7f")

    #Set date as index
inc_st.set_index('date', inplace = True)
fcf.set_index('date', inplace = True)

    #Create data frame with Revenue, EPS and FCF
data = inc_st[['revenue', 'eps']].copy()
data['fcf'] = fcf['freeCashFlow']

    #Sort data frame by year ascending
data = data.sort_index()
data['rev % change'] = data['revenue'].pct_change()
data['eps % change'] = data['eps'].pct_change()
data['fcf % change'] = data['fcf'].pct_change()

    #Set current year and trailing ten year start date
date = datetime.date.today()
year = date.strftime("%Y")
tenyrback = int(year) - 10

    #Filter down to only the past ten years
data = data.loc[str(tenyrback) + '-01-01':]
data.index = data.index.year

    #Create three separate data frames for the three sheets
rev = data[['revenue', 'rev % change']].copy()
eps = data[['eps', 'eps % change']].copy()
fcf = data[['fcf', 'fcf % change']].copy()

    #Create writer function to send data frames to the workbook
def create_sheet(writer, df, sheet_name):
    df.to_excel(writer, sheet_name=sheet_name)
    worksheet = writer.sheets[sheet_name]
    wb = writer.book

        #Create line chart for $ amount column
    chart = wb.add_chart({'type': 'line'})

    chart.add_series({
        'name': sheet_name,
        'categories': [sheet_name, 1, 0, 11, 0],
        'values': [sheet_name, 1, 1, 11, 1]
    })
        #Create bar chart for % change column
    column_chart = wb.add_chart({'type': 'column'})

    column_chart.add_series({
        'name': sheet_name,
        'categories': [sheet_name, 1, 0, 11, 0],
        'values': [sheet_name, 1, 2, 11, 2],
        'y2_axis': True
    })
        #Combine both charts into one visual
    chart.combine(column_chart)

    worksheet.insert_chart('E2', chart)

    #Write data and charts to workbook in each respective sheet
writer = pd.ExcelWriter('finAnalysis.xlsx', engine='xlsxwriter')
wb = writer.book

create_sheet(writer, rev, 'Revenue')
create_sheet(writer, eps, 'EPS')
create_sheet(writer, fcf, "FCF")

writer.save()