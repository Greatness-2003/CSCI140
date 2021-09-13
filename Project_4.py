import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def make_subset(df, region = None, vaccine = None, year = None):
    df = df.copy()
    if region == None:
        region = df['Region']
    if vaccine == None:
        vaccine = df['Vaccine']
    if year == None:
        year = df['Year']
    df = df.loc[(df['Region'].isin(region)) & (df['Vaccine'].isin(vaccine)) & (df['Year'].isin(year))]
    return df


def make_plot(series_object, title ='', bar = True):
    if bar == False:
        plot_series = sns.lineplot(x= series_object.index, y = series_object.values, ci=None)
        plt.xticks(rotation=90)
        plt.title(title)
    else:
        plot_series= sns.barplot(y = series_object.index, x = series_object.values, orient = 'h', ci=None)
        plt.ylabel(series_object.index.name)
    return plot_series