def calculate_rfm(df):

    rfm = df[['CustomerID',
              'Recency',
              'Frequency',
              'Monetary']]

    return rfm