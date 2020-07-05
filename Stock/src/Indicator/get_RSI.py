import numpy as np
import pandas as pd

# 30이하면 과매도, 70 이상이면 과매수
def fnRSI(m_Df, m_N=7):
    close = m_Df[['Close']]

    U = np.where(close.diff(1) > 0, close.diff(1), 0)
    D = np.where(close.diff(1) < 0, close.diff(1) *(-1), 0)

    AU = pd.DataFrame(U).rolling( window=m_N, min_periods=m_N).mean()
    AD = pd.DataFrame(D).rolling( window=m_N, min_periods=m_N).mean()
    RSI = AU.div(AD+AU) *100

    m_Df['RSI'] = RSI

    return m_Df