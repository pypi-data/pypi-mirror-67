import pandas as pd


def onehot(df, dfColumnList):
    df1 = df
    for dfColumn in dfColumnList:
        dummy_df = pd.get_dummies(dfColumn)
        column_names = dummy_df.columns
        for col in column_names:
            df1[col] = dummy_df[col]
    return df1
