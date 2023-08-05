import pandas as pd
def word_freq(data, keyword):
    freq_factor = 10
    list_freq = []
    for d in data:
        d_split = d.split()
        count = 0
        for s in d_split:
            if s == keyword:
                count+=1
        list_freq.append(count/freq_factor)
    return list_freq

def transform(data, fit_dataframe):
    target_keys = fit_dataframe.columns
    df = {}
    for tk in target_keys:
        df[tk] = word_freq([data], tk)
    df = pd.DataFrame(df)
    #return df
    df = pd.DataFrame(df.values*fit_dataframe.values, index = fit_dataframe.index)
    #return df
    df = pd.DataFrame(df.sum(axis = 1, skipna = True), columns=["sum"])
    #return df

    get_max = df.loc[df['sum'].idxmax()]

    if(type(get_max) == pd.core.series.Series):
        return get_max.name
    else:
        return list(get_max.index)
    
    