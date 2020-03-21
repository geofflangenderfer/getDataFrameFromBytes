# What is this?
Convenience function to upload a csv to Google Colab

# How will this help me?
Save some time converting from [bytes][0] to [pandas.dataFrame][1]

# How do I use this?
Use something like the following in a [google colab](https://colab.research.google.com/)
```python
from getDataframeFromBytes import getDataframe
import pandas as pd
from google.colab import files


bytes_csv = files.upload()['Reduced_DataSet (1).csv']
dataframe = getDataframe(bytes_csv)
print(dataframe.head())
```
Results in:
```
   Unnamed: 0       ID       Date  Age     Sex  ... Morphine_NotHeroin Hydromorphone Other OpiateNOS AnyOpioid
0           1  13-0102  3/21/2013   48    Male  ...                  N             N     N         N         N
1           2  16-0165  3/13/2016   30  Female  ...                  N             N     N         N         Y
2           3  16-0208  3/31/2016   23    Male  ...                  N             N     N         N         Y
3           4  13-0052  2/13/2013   22    Male  ...                  N             N     N         N         N
4           5  14-0277  6/29/2014   23    Male  ...                  N             N     N         N         N

[5 rows x 26 columns]
```

[0]: https://docs.python.org/3/library/stdtypes.html#bytes-objects
[1]: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
