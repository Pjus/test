import pandas as pd
import numpy as np
import plotly.graph_objects as go

path_dir = './data'
data = np.loadtxt(path_dir + '/' + '000660_from_2010.csv', delimiter = ',')
data = pd.DataFrame(data)
data.columns = ['Open', 'High', "Low", "Close", "Volumn", "Adj"]

def cal_dmi(data, n=14, n_ADX=14) :
    i = 0
    UpI = [0]
    DoI = [0]

    while i + 1 <= data.index[-1] :
        UpMove = data.loc[i + 1, "High"] - data.loc[i, "High"]
        DoMove = data.loc[i, "Low"] - data.loc[i+1, "Low"]
        if UpMove > DoMove and UpMove > 0 :
            UpD = UpMove
        else :
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0 :
            DoD = DoMove
        else :
            DoD = 0
        DoI.append(DoD)
        i = i + 1

    i = 0
    TR_l = [0]
    while i < data.index[-1]:
        TR = max(data.loc[i + 1, 'High'], data.loc[i, 'Close']) - min(data.loc[i + 1, 'Low'], data.loc[i, 'Close'])
        TR_l.append(TR)
        i = i + 1
    TR_s = pd.Series(TR_l)
    ATR = pd.Series(TR_s.ewm(span=n, min_periods=1).mean())
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(UpI.ewm(span=n, min_periods=1).mean() / ATR)
    NegDI = pd.Series(DoI.ewm(span=n, min_periods=1).mean() / ATR)
    ADX = pd.Series((abs(PosDI - NegDI) / (PosDI + NegDI)).ewm(span=n_ADX, min_periods=1).mean(),
                    name='ADX_' + str(n) + '_' + str(n_ADX))

    return PosDI, NegDI, ADX
    
    data["PDI"],data["MDI"],data["ADX"] = cal_dmi(data)
 

fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index[20:], y=data["PDI"][20:],
                        mode='lines',
                        name="PDI"))
fig.add_trace(go.Scatter(x=data.index[20:], y=data["MDI"][20:],
                        mode='lines',
                        name="MDI"))
fig.add_trace(go.Scatter(x=data.index[20:], y=data["ADX"][20:],
                        mode='lines',
                        name="ADX"))

fig.update_layout(title='DMI and ADX',
                   xaxis_title='days',
                   yaxis_title='Value')

fig.show()