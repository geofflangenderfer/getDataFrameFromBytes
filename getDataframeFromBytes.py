import pandas as pd
from google.colab import files
from io import StringIO

def getDataframe(bytes):
  dataframe = pd.read_csv(
    StringIO(
      str(bytes, "utf-8")
    )
  )
  return dataframe

bytes_csv = files.upload()['Reduced_DataSet (1).csv']
dataframe = getDataframe(bytes_csv)
dataframe.head()
