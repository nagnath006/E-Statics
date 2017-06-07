import pandas as pd

from bokeh.charts import Scatter, output_file, defaults, show,Donut
from bokeh.charts.operations import blend
from bokeh.charts.utils import df_from_json
from bokeh.layouts import gridplot
import pandas as pd
from bokeh.charts import TimeSeries, show, output_file
from bokeh.sampledata.autompg import autompg as df
from bokeh.sampledata.iris import flowers
from bokeh.sampledata.olympics2014 import data


AAPL = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])
MSFT = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=MSFT&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])
IBM = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=IBM&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])

data = pd.DataFrame(data=dict(AAPL=AAPL['Adj Close'][:1000],
                              MSFT=MSFT['Adj Close'][:1000],
                              IBM=IBM['Adj Close'][:1000],
                              Date=AAPL['Date'][:1000])).set_index('Date')
defaults.plot_width = 450
defaults.plot_height = 400
TOOLS="pan,wheel_zoom,box_zoom,reset,save"
tooltips = [("Cylinders", "@cyl"),
            ("Displacement", "@displ"),
            ("Weight", "@weight"),
            ("Acceleration", "@accel"),
            ("Horsepower", "@hp"),
            ("Miles Per Gallon", "@mpg"),
            ("Origin", "@origin")]

			
data = pd.Series([0.15,0.4,0.7,1.0], index = list('abcd'))
pie_chart = Donut(data)
				
tsline2 = TimeSeries(
    data, y=['IBM', 'MSFT', 'AAPL'], legend=True,
    color=['IBM', 'MSFT', 'AAPL'], dash=['IBM', 'MSFT', 'AAPL'],
    title="Timeseries (Line Explicit)", tools=TOOLS, ylabel='Stock Prices',
    xlabel='Date')

scatter1 = Scatter(
    df, x='mpg', y='hp', title="x='mpg', y='hp'",
    xlabel="Miles Per Gallon", ylabel="Horsepower", legend='top_right',
    tooltips=tooltips)

scatter2 = Scatter(
    df, x='mpg', y='hp', color='cyl', title="x='mpg', y='hp', color='cyl'",
    xlabel="Miles Per Gallon", ylabel="Horsepower", legend='top_right',
    tooltips=tooltips)

scatter3 = Scatter(
    df, x='mpg', y='hp', color='origin', title="x='mpg', y='hp', color='origin', with tooltips",
    xlabel="Miles Per Gallon", ylabel="Horsepower",
    legend='top_right', tooltips=tooltips)

#scatter4 = Scatter(
 #   df, x='mpg', y='hp', color='cyl', marker='origin', title="x='mpg', y='hp', color='cyl', marker='origin'",
  #  xlabel="Miles Per Gallon", ylabel="Horsepower", legend='top_right',
   # tooltips=tooltips)

# Example with nested json/dict like data, which has been pre-aggregated and pivoted
#df2 = df_from_json(data)
#df2 = df2.sort('total', ascending=False)

#df2 = df2.head(10)
#df2 = pd.melt(df2, id_vars=['abbr', 'name'])

#scatter5 = Scatter(
 #   df2, x='value', y='name', color='variable', title="x='value', y='name', color='variable'",
  #  xlabel="Medals", ylabel="Top 10 Countries", legend='bottom_right')

scatter6 = Scatter(flowers, x=blend('petal_length', 'sepal_length', name='length'),
                   y=blend('petal_width', 'sepal_width', name='width'), color='species',
                   title='x=petal_length+sepal_length, y=petal_width+sepal_width, color=species',
                   legend='top_right')

output_file("scatter_multi.html", title="scatter_multi.py example")

show(gridplot(pie_chart,tsline2, scatter2, scatter3,
              scatter6, ncols=2))