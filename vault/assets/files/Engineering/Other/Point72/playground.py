#%%
from math import prod
from typing import List
import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv('ResearchDatasetV2.0.csv')
# %%
data['Date'] = pd.to_datetime(data['Date'],format='%Y%m%d')
data.plot(x='Date',y='Signal')

# %%
def plot(df: pd.DataFrame, x: str, y_cols:List[str], name:str = 'Plot') -> pd.DataFrame:
    # PLOT
    fig = go.Figure(layout=DEFAULT_LAYOUT)
    fig.update_layout(title=f'{name}')
    for y in y_cols:
        fig.add_scatter(
            x=df[x],
            y=df[y],
            name=f'{y}',
            # line=dict(color='red')
        )
    fig.show(render='browser')
    fig.write_html(f"/home/ncuong/Programming/algorithms/Other/Point72/{name}.html")

DEFAULT_LAYOUT = dict(
    xaxis=dict(
        type='date',
        rangeselector=dict(
            buttons=list([
                dict(count=7,
                    label='1w',
                    step='day',
                    stepmode='backward'),
                dict(count=1,
                    label='1m',
                    step='month',
                    stepmode='backward'),
                dict(count=3,
                    label='3m',
                    step='month',
                    stepmode='backward'),
                dict(count=6,
                    label='6m',
                    step='month',
                    stepmode='backward'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ]),
            bgcolor = '#7792E3',
            font=dict(
                color = 'white',
                size = 13
            ),
        ),
        rangeslider=dict(
            visible=True
        ),
    ),
    height = 550
)
# %%
df = data[(data['Signal'] > 0.5) & (data['Signal'] < 300)]
df = df[df['ClosePrice'] < 300]
plot(df, 'Date', ['Signal'], 'Signal')
# plot(df, 'Date', ['ClosePrice'], 'ClosePrice')
# plot(data, 'Date', ['ClosePrice', 'Signal'], 'ClosePrice & Signal')

# %%
def remove_outliers(df:pd.DataFrame, y_col:str, alpha:float = 0.005) -> pd.DataFrame:
    df = df.drop(find_outlier_index(df, y_col, alpha))
    return df

def find_outlier_index(df:pd.DataFrame, y_col:str, alpha:float = 0.005):
    return df[(df[y_col] < df[y_col].quantile(alpha)) | (df[y_col] > df[y_col].quantile(1-alpha))].index


index = find_outlier_index(data, 'Signal')
# %%
data = remove_outliers(data, 'Signal')
data = remove_outliers(data, 'ClosePrice')
# %%
def normalise(df:pd.DataFrame, y_col:str) -> pd.DataFrame:
    df[y_col] = (df[y_col] - df[y_col].min()) / (df[y_col].max() - df[y_col].min())
    return df

def normalise_mean(df:pd.DataFrame, y_col:str) -> pd.DataFrame:
    df[y_col] = (df[y_col] - df[y_col].mean()) / df[y_col].std()
    return df

def interpolate_daily_data(df:pd.DataFrame, y_cols:List[str]) -> pd.DataFrame:
    new_df = pd.DataFrame()
    new_df['Date_Complete'] = pd.date_range(start=df['Date'].min(), end=df['Date'].max(), freq='D')
    new_df = pd.concat([new_df,df], join="outer", axis=1)
    for y_col in y_cols:
        new_df[y_col] = new_df[y_col].interpolate(method = "linear")
    return new_df[['Date_Complete']+y_cols]

#%%
df_complete =  interpolate_daily_data(data,['Signal','ClosePrice']).dropna()
df_complete = df_complete[df_complete['Date_Complete'] < '2013-11-09']
plot(df_complete, 'Date_Complete', ['Signal','ClosePrice'], 'ClosePrice & Signal')
# %%
normal_data = normalise_mean(data, 'ClosePrice')
normal_data = normalise_mean(data, 'Signal')
plot(normal_data, 'Date', ['ClosePrice','Signal'], 'Normalised Signal and ClosePrice')
# %%
def correlation(series1:pd.Series, series2:pd.Series) -> float:
    return series1.corr(series2)

def find_lag_with_max_correlation(df:pd.DataFrame, y1:str, y2:str) -> int:
    lag = 0
    print(df)
    max_corr = cross_correlation(df, y1, y2, 0)
    for i in range(len(df)):
        corr = cross_correlation(df, y1, y2, i)
        if corr > max_corr:
            max_corr = corr
            lag = i
            print(lag)
            print(corr)
            new_df = df.copy()
            new_df[y1] = new_df[y1].shift(lag)
            plot(new_df, 'Date_Complete', [y2, y1], f'{lag}-days lagged Signal')
    return lag

def plot_correlation_lag(df:pd.DataFrame, y1:str, y2:str, lag:int) -> pd.DataFrame:
    new_df = df.copy()
    new_df[y1] = new_df[y1].shift(lag)
    plot(new_df, 'Date_Complete', [y1, y2], f'Lagged ClosePrice {lag}')
    return new_df


def cross_correlation(df:pd.DataFrame, y1:str, y2:str, lag:int) -> float:
    new_df = df.copy()
    new_df[y1] = new_df[y1].shift(lag)
    return new_df[y1].corr(new_df[y2])

# %%
# cross_correlation(data, 'Signal', 'ClosePrice', 0)
find_lag_with_max_correlation(df_complete, 'Signal', 'ClosePrice')
# %%
for l in range(1,10,1):
    plot_correlation_lag(df_complete, 'Signal','ClosePrice', l)
# %%
y1 = 'Signal'
y2 = 'ClosePrice'
lag = 10
new_df = data.copy()
new_df[y1] = new_df[y1].shift(lag)
plot(new_df, 'Date', [y1, y2], 'Lagged ClosePrice')
# %%

