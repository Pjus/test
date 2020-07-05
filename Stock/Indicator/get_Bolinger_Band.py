"""
중심선: n기간 동안의 이동평균(SMA)

상단선: 중심선 + Kσ(일반적으로 K는 2배를 많이 사용함)

하단선: 중심선 - Kσ(일반적으로 K는 2배를 많이 사용함)

"""

def fnBolingerBand(m_DF, n=20, k=2):
    m_DF['20d_ma'] = pd.rolling_mean(m_DF['Adj Close'], window=n)
    m_DF['Bol_upper'] = pd.rolling_mean(m_DF['Adj Close'], window=n) + k* pd.rolling_std(m_DF['Adj Close'], n, min_periods=n)
    m_DF['Bol_lower'] = pd.rolling_mean(m_DF['Adj Close'], window=n) - k* pd.rolling_std(m_DF['Adj Close'], n, min_periods=n)
    return m_DF