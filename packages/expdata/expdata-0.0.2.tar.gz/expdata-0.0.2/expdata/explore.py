import pandas as pd


def categorical_column(dfColumn):
    """dfColumn: df.Month, df.Names etc"""
    vals_dict = dict(dfColumn.value_counts())
    x = [i for i in vals_dict.keys()]
    y = [i for i in vals_dict.values()]
    total_number = sum(dfColumn.value_counts())
    percentages = []
    for i in vals_dict.values():
        percentages.append(round((i/total_number*100),2))
    df = pd.DataFrame(index=vals_dict.keys(), columns=['occurence', '%'])
    df['occurence'] = vals_dict.values()
    df['%'] = percentages
    # sns.barplot(x, y)
    return df
