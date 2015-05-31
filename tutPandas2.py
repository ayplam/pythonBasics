__author__ = 'goldenxradian'

from pandas import *
import scipy
import pandas
import numpy as np
import matplotlib.pyplot as plt
import string

def get_max_record(group):
    return group.ix[group.prop.idxmax()]

def get_rank_of_name(group,name='Wes'):
    df = group.sort_index(by='prop',ascending=False)
    if df[df.name == name].empty:
        return NaN
    else:
        return int(df[df.name == name].index.tolist())


def get_quantile_count(group, quantile = 0.5):
    # Optional if you want to combine the "John" and "Jon"
    # This groups all the names that SOUND like each other, and takes the SUM of it all
    # I wonder how it knows which columns to take the sum of.
    # group = group.groupby('soundex').sum()
    # First sort the data by descending order of proportion
    df = group.sort_index(by='prop',ascending=False)
    # So I think searchsorted returns an object, you need to turn it into an int.
    return int(df.prop.cumsum().searchsorted(quantile))

def readData(fname):
    return read_csv(fname)

def birthdata(names):

    # print names.head()                # Useful for just looking at a few of them

    # Get everyone in 1880
    # print names[names.year == 1880]
    boys = names[names.sex == 'boy']        # Can also do names['sex']
    girls = names[names.sex == 'girl']

    print boys.head()
    # Compute most popular boys name for each year
    print "\n Get most popular boys name for each year"
    # So all of the sudden, groupby makes ALL your columns into the years.
    # So you can use .apply(f'n) to apply that function to all the rows.
    result = boys.groupby('year').apply(get_max_record)
    print boys.groupby('year').apply(get_max_record)
    print "^^ Get most popular boys name for each year"

    # So clearly, name diversity goes up as time goes on.
    # result.prop.plot()
    # plt.show()

    # argmax/idxmax are interchangeable. This basic definition went into get_max_record
    # print boys.name[boys[boys.year == 2000].prop.argmax()]
    # This little snippet was used to help write get_max_record

    # So in this dataset, all the names /years are unique.
    # IF THEY ARE UNIQUE, YOU CAN USE THEM TO INDEX! This saves TIME over constantly using ==
    # Find all Travis'
    # print boys[boys.name == 'Travis']
    # But if this dataset is HUGE, this means that you have to search every element multiple times!

    # Re-index your data
    idf = boys.set_index(['name','year'])
    # # So now you can actually index FOR Travis
    # print idf.ix['Travis']
    # # Can plot popularity too
    # print idf.ix['Travis'].prop.plot()

    # print df_boys['prop']

    # Hierchical index. This creates a series, but the index has multiple levels
    # print names.groupby(['year','sex']).size()
    # print names.groupby(['year', 'sex']).size().ix[2000] # Selects out year 2000

    print "\n Overall mean popularity"
    print boys.groupby('name')['prop'].mean().order()
    print  "^^  Overall mean popularity \n"

    # describe() gives count, mean, std, min, quartile ranges and max
    # Can't also do .prop bc groupby doesn't give you attributes
    # results = boys.groupby('name')['prop'].describe()
    # print results[-50:]
    # # print boys['prop'].describe()


    # Diversity of names.
    df = boys[boys.year==2008].sort_index(by='prop',ascending=False)
    # print df
    # Sort by prop, descending order
    print df

    # If you sorted all the baby names, how many names did it take to reach 50%?
    # Use searchsorted to search sorted data, and looking when it gets past 0.5
    print df.prop.cumsum().searchsorted(0.5)
    print df.prop.cumsum()[120:130]

    # Ok, so you want to do this for EVERY year.
    print "\n Do this for EVERY year now with a function"
    print boys.groupby('year').apply(get_quantile_count)

    q = 0.25
    boyCount = boys.groupby('year').apply(get_quantile_count,q)
    girlCount = girls.groupby('year').apply(get_quantile_count,q)
    # # Can't get the labels to work. Need to place inside legend.
    # boyCount.plot(label='boy')
    # girlCount.plot(label='girl')
    # plt.legend(['boy', 'girl'], loc='best')
    # plt.show()

    print "\n Q: Given that names are becoming more diverse, what's the rank of your name every year?"

    # Break down the problem. Start first with a year. Is prop already sorted?
    grouped = boys.groupby('year')['prop']

    # transform is same as apply, but RIGID, the size of the input and the output must be the same!
    # Adding a column
    boys['year_rank'] = grouped.transform(Series.rank)
    # Different things you COULD do with transform - pass in a lambda function that applies it on the whole thing
    result = grouped.transform(lambda x: x - x.mean())
    # Result is a SERIES now.
    print result[:10]
    # Need to pass in boys.year (sort of as an array?) to know how to group everything and calculatethe means.
    print result.groupby(boys.year).mean()

    # Notice that you don't get the years on the x-axis if you do things this way
    # Could explicitly pass x,y
    # boys[boys.name == 'Wesley'].year_rank.plot()

    # Looks like boys is already sorted by prop. Is this because of something earlier...?
    print boys[:20]

    # Since you set the index, you must use "ix"
    idf = boys.set_index(['name','year'])
    print idf.ix['John'].year_rank.plot()
    plt.show()

    # print df[df.name == 'John']

    # Ok, now build the method and use the groupby
    # print boys.groupby('year').apply(get_rank_of_name,'John')

def mergeDataAndStuff(names,births):

    # births has year, number of births, and sex
    # Can do many-many, many-one, one-one joins
    # many-many compute cartesian product of duplicated keys on SQL ll

    # If no merge keys, it will merge on the intersection/common set of columns
    # Important to merge on sex because Leslie can be boy or girl.
    merged = merge(names, births, on=['year', 'sex'])
    print merged[:5]
    # Number of people with the actual name
    # So sometimes, using [] works, and something that uses . works.
    # Can't assign by attribute (merged.persons = ... ) does not work
    merged['persons'] = np.floor(merged.prop * merged.births)
    print merged.head()
    # To get most popular names over the entire sample
    print merged.groupby(['name','sex'])['persons'].sum().order()

    mboys = merged[merged.sex == 'boy']
    # There are names that are shared between sexes which is why you can't set_index on "merged"
    # but you can on mboys
    idf = mboys.set_index(['year', 'name'])['persons']
    # Get all years, name is Christopher
    print idf.ix[:,'Christopher']   #.plot(kind='bar',rot=90)

    # pivot this up to create a data frame whose columns are the unique names
    # Row Names = years
    # Col Names = all unique names
    # Actual values = # of persons in each graph

    result = idf.unstack('name')
    print result['Wesley'].plot()
    plt.show()


def main():

    names = readData('baby-names2.csv')
    births = readData('births.csv')
    # basics()
    # birthdata(names)
    mergeDataAndStuff(names,births)

if __name__ == "__main__":
    main()