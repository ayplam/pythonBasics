__author__ = 'goldenxradian'

from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
import string


def side_by_side (*objs, **kwds):
    from pandas.core.common import adjoin
    space = kwds.get('space',4)
    reprs = [repr(obj).split('\n') for obj in objs]
    print adjoin(space,*reprs)

def peak_date(series):
    return series.idxmax()

def basics():

    labels = list(string.ascii_lowercase)
    nums = np.random.random(len(labels))
    # Intentionally leave one value out
    s = pandas.Series(nums[0:5], index = labels[0:5])

    print s.index                                       # Prints array of all the indices/keys
    print 'b' in s                                      # True
    # mapping = s.to_dict()                               # Create dictionary from series
    # print mapping                                       # Keep in mind a dictionary has no sorting
    # s2 = Series(mapping)                                # Create series from dictionary
    # print s2                                            # However, a series automatically sorts the keys

    # The video gives an example of what happens if you have a key that has no value (NaN). Can use isnull/notnull
    # to determine this.
    print s.isnull(), s.notnull()

    # Series object works like a numpy array
    s*2                                                     # Multiplies all the values by 2
    print s[:2]                                             # Prints [0:2) of the list

    print

    df = DataFrame({'a': np.random.randn(6),             # Creating a dataframe
                    'b': ['foo', 'bar'] * 3,                # Note that for list operations, multiple by a number repeats it
                    'c': np.random.randn(6)},
                   index = date_range('10/13/2010',periods=6,freq='H')) # If no index is specified, it's automatically an integer that increments

    df['d'] = 5                                             # Creating an array of all 5s

    print "DataFrame: \n", df

    print "\n How to get the dataframe row/column names \n"
    print df.index, "\n", list(df.columns.values)

    # df.ix allows you to index the DataFrame just like a numpy array. Can pass numbers AND labels
    print "\n Indexing parts of the dataframe: \n" , df.ix[2:3,'b':'d']
    # get_value does the same thing, but you only get ONE value. But you actually need to use the row name.
    # print df.get_value(3,'c')
    # Can also pass in booleans similar to MATLAB
    print "\n Using boolean arrays to help index the dataframe: "
    print df.ix[df['c'] > 0.5, 'a':'c']

    # Creating a nested dict:
    data = {}
    for col in ['foo','bar','baz']:
        for row in ['a','b','c','d']:
            data.setdefault(col,{})[row] = np.random.randn()

    # Note that nested dicts have multiple curly brackets
    # Delete a random item for fun
    del data['foo']['c']

    print "\n Example of a nested dict. See multiple curly brackets"
    print data

    print "\n A nested dict is essentially a dataframe"
    df2 = DataFrame(data)
    print df2
    print df2.isnull()


def readInStockData():

    # Use first column as index and they are dates so want to parse dates
    close_px = read_csv('stock_data.csv', index_col = 0, parse_dates=True)
    s1 = close_px['AAPL'][-20:]
    s2 = close_px['AAPL'][-25:-10]

    # Viewing things side by side
    side_by_side(s1,s2)
    # s1: Dates from 9-19 to 10-14
    # s2: Dates from 9-12 to 9-30

    # Adding two series forms a union between the two.
    # print s1 + s2                   # Actually ADDS the values in which there are the same keys. Otherwise NaN
    s12 = (s1+s2).dropna()
    print ('\n Comparison of adding two series\n ')
    side_by_side(s1+s2, s12)
    print ("\n Adding series in a way which you wouldn't get NaNs. Note that it does NOT change s1. \n")
    side_by_side( s1, s1.add(s2, fill_value = 0) )
    print ("\n What if you wanted to reindex s1 based on another series' keys? \n")
    side_by_side(s1.reindex(s2.index), s2)
    # side_by_side(s1.ix[s2.index],s2)                <-- Does the same thing. I like the one above better

    # Performing joins:
    b,c = s1.align(s2, join='inner')
    print ("\n Inner Join AKA only show intersection: \n")
    side_by_side(b,c)
    b,c = s1.align(s2, join='outer')
    print ("\n Outer Join AKA union, show everything: \n")
    side_by_side(b,c)
    b,c = s1.align(s2, join='right')
    print ("\n Right join AKA use only keys from s2: \n")
    side_by_side(b,c)               # This is the same as the s1.ix[s2.index], did this a couple lines ago
    b,c = s1.align(s2, join='left')
    print ("\n Left join AKA use only keys from s1: \n")
    side_by_side(b,c)

    # how to print the index and the column names/values
    print close_px.index, "\n", list(close_px.columns.values)

    # Ok, so apparently for this dataframe, ix cannot handle the column titles as inputs. I don't know why.
    df = close_px.ix[-10:,:4]
    # It automatically skips NaN, but if you don't want to , df.mean(0,skipna=false)
    # Essentially you get out a series
    print df.mean(), "\n", df.mean(1)
    a = df.mean()
    # Does same thing as above
    # print df.apply(np.mean,axis=1)

    # Find day where maximum occurred
    print "\n Day where max occured: "
    print close_px.AA.argmax(), "," , close_px.AA[close_px.AA.argmax()]
    # idxmax is shorter than argmax I guess.
    # print close_px.AAPL.idxmax(), ", ", close_px.AAPL.index[0]
    # df.apply applies the function to each and every column
    # In the tutorial, a "peak_date" function was created, though you can also use argmax.
    print close_px.apply(np.argmax)

    print("\n Find peak-to-peak data")
    print df.apply(lambda x: x.max() - x.min() )

    # Plotting integration
    # Don't HAVE to use ix, can pass in a list of column names
    print ("Simple line plots")
    close_px[['AAPL','IBM','MSFT','XOM']].plot()
    plt.show()

    close_px.ix[-1].plot(kind='bar')            # This works best if you have a series, not so hot with a df
    plt.show()



def main():

    # basics()
    readInStockData()

if __name__ == "__main__":
    main()