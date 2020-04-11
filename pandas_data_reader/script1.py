import datetime
from pandas.util.testing import assert_frame_equal

from pandas_datareader import data

start=datetime.datetime(2016,3,1)
end=datetime.datetime(2016,3,10)

df=data.DataReader(name='AAPL', data_source="yahoo", start = start, end=end)


print(df)

