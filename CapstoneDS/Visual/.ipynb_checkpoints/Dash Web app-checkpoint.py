#Part 3
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

data = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv")

app = Dash(__name__)

app.layout = [
    html.H1(children='Automobile Sales Statistics Dashboard', style={'textAlign':'center', 'color':'#503D36', 'font-size': 24}),
    dcc.Dropdown(id='dropdown-statistics',
    options=[
            {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
            {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}],
    placeholder='Select a report type',
    ),
    dcc.Dropdown(id='select-year', 
    options=[{'label': i, 'value': i} for i in list(map(str, range(1980,2024)))],
    placeholder='Select-year'),
    html.Div([
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
    ]),
    dcc.Graph(id='graph-content')
]

@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics',component_property='value'))
    
def update_input_container(option):
    if option =='Yearly Statistics': 
        return False
    else: 
        return True

@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), Input(component_id='select-year', component_property='value')])

def update_output_container(selected_statistics,input_year):
    print(f"Selected year: {input_year}, Selected statistics: {selected_statistics}")
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        #Plot 1 Automobile sales fluctuate over Recession Period (year wise) using line chart
         # grouping data for plotting
        yearly_rec=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        print(recession_data)
        # Plotting the line graph
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Automobile sales over the Recession Period"))
#Plot 2 Calculate the average number of vehicles sold by vehicle type and represent as a Bar chart
 # use groupby to create relevant data for plotting. 
 #Hint:Use Vehicle_Type and Automobile_Sales columns
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        print(average_sales)                
        R_chart2  = dcc.Graph(
            figure=px.bar(average_sales,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title="Average number of vehicles sold by vehicle type"))
# Plot 3 : Pie chart for total expenditure share by vehicle type during recessions
            # grouping data for plotting
            # Hint:Use Vehicle_Type and Advertising_Expenditure columns
        exp_rec= recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()
        print(exp_rec)
        labels = exp_rec.values
        R_chart3 = dcc.Graph(
                figure=px.pie(exp_rec,
                values=labels,
                names=['Executivecar', 'Mediumfamilycar', 'Smallfamiliycar', 'Sports','Supperminicar'],
                title="Total expenditure share by vehicle type during recessions"
                )
        )
# Plot 4 Develop a Bar chart for the effect of unemployment rate on vehicle type and sales
       #grouping data for plotting
       # Hint:Use unemployment_rate,Vehicle_Type and Automobile_Sales columns
        unemp_data= recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(figure=px.bar(unemp_data,
        x='Vehicle_Type',
        y='Automobile_Sales',
        #color='.............',
        labels={'unemployment_rate': 'Unemployment Rate', 'Automobile_Sales': 'Average Automobile Sales'},
        title='Effect of Unemployment Rate on Vehicle Type and Sales'))
        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1),html.Div(children=R_chart2)],style={'display': 'flex','flex-wrap': 'wrap','justify-content': 'space-around'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3),html.Div(children=R_chart4)],style={'display': 'flex','flex-wrap': 'wrap','justify-content': 'space-around'})
            ]
        # Yearly Statistic Report Plots 
     # Check for Yearly Statistics.
    elif selected_statistics=='Yearly Statistics':
        yearly_data = data[data['Year'] == int(input_year)]
        print(data['Year'].dtype)
# Plot 1 :Yearly Automobile sales using line chart for the whole period.
        # grouping data for plotting.
        # Hint:Use the columns Year and Automobile_Sales.
        yas= data.groupby('Year')['Automobile_Sales'].sum().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas, 
                x='Year',
                y='Automobile_Sales',
                title="Yearly Automobile sales"))

# Plot 2 :Total Monthly Automobile sales using line chart.
         # grouping data for plotting.
        # Hint:Use the columns Month and Automobile_Sales.
        mas=yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(mas,
            x='Month',
            y='Automobile_Sales',
            title='Total Monthly Automobile Sales'))
# Plot bar chart for average number of vehicles sold during the given year
         # grouping data for plotting.
         # Hint:Use the columns Year and Automobile_Sales
        avr_vdata=yearly_data.groupby(['Year', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata,
            x='Year',
            y='Automobile_Sales',
            title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))
# Plot 4 Total Advertisement Expenditure for each vehicle using pie chart
          # grouping data for plotting.
          # Hint:Use the columns Vehicle_Type and Advertising_Expenditure
        exp_data=yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()
        labels = exp_data.values
        names=exp_data.index
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data, 
            values=labels,
            names=names,
            title='Total Advertisment Expenditure for Each Vehicle'))
        return [
                html.Div(className='chart-item', children=[html.Div(children=Y_chart1),html.Div(children=Y_chart2)],style={'display':'flex','flex-wrap': 'wrap','justify-content': 'space-around'}),
                html.Div(className='chart-item', children=[html.Div(children=Y_chart3),html.Div(children=Y_chart4)],style={'display': 'flex','flex-wrap': 'wrap','justify-content': 'space-around'})
                ]
    
if __name__ == '__main__':
    app.run(debug=True,port='8008')