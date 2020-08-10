# Section 1 - Loading our Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Section 2 - Loading and Selecting Data
df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
countries = ['US', 'India', 'France', 'China', 'Brazil']
df = df[df['Country'].isin(countries)]
df['Total Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)
df = df.pivot(index='Date', columns='Country', values='Total Cases')
countries = list(df.columns)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries

# Section 5 - Calculating Rates per 100,000
populations = {'India':37664517, 'US': 330548815, 'France': 65239883, 'China':1438027228, 'Brazil':209500000 }
percapita = covid.copy()
for country in list(percapita.columns):
    percapita[country] = percapita[country]/populations[country]*100000


# Section 6 - Generating Colours and Style
colors = {'India':'blue',  'US':'purple', 'France':'green', 'China':'black', 'Brazil':'red'}
plt.style.use('fivethirtyeight')

# Section 7 - Creating the Visualization
plot = covid.plot(figsize=(12,10), color=list(colors.values()), linewidth=5, legend=False)
# plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
# plot.grid(color='#d4d4d4')
# plot.set_xlabel('Date')
# plot.set_ylabel('# of Cases')

# Section 8 - Assigning Colour
for country in list(colors.keys()):
    plot.text(x = covid.index[-1], y = covid[country].max(), color = colors[country], s = country, weight = 'bold')

# Section 9 - Adding Labels
plot.text(x = covid.index[1], y = int(covid.max().max())+45000, s = "COVID-19 Cases by Country", fontsize = 23, weight = 'bold', alpha = .75)
# plot.text(x = covid.index[1], y = int(covid.max().max())+15000, s = "For the USA, China, Germany, France, United Kingdom, and India\nIncludes Current Cases, Recoveries, and Deaths", fontsize = 16, alpha = .75)
# plot.text(x = percapita.index[1], y = -100000,s = 'datagy.io')

percapitaplot = percapita.plot(figsize=(12,10), color=list(colors.values()), linewidth=5, legend=False)
percapitaplot.grid(color='#d4d4d4')
percapitaplot.set_xlabel('Date')
percapitaplot.set_ylabel('# of Cases per 100,000 People')
for country in list(colors.keys()):
    percapitaplot.text(x = percapita.index[-1], y = percapita[country].max(), color = colors[country], s = country, weight = 'bold')
# percapitaplot.text(x = percapita.index[1], y = percapita.max().max()+25, s = "Per Capita COVID-19 Cases by Country", fontsize = 23, weight = 'bold', alpha = .75)
# percapitaplot.text(x = percapita.index[1], y = percapita.max().max()+10, s = "For the USA, China, Germany, France, United Kingdom, and India\nIncludes Current Cases, Recoveries, and Deaths", fontsize = 16, alpha = .75)
# percapitaplot.text(x = percapita.index[1], y = -55,s = 'datagy.io')

plt.show()