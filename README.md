# AutoTrading-Template

## RSI 

RSI 是 Relative Strength Index 的縮寫，1978年由Wells Wilder發明，是用來衡量過去一段時間內，投資標的漲跌趨勢的相對指標，Relative這個字代表的是，它是以過去這段時間內的上漲量對比下跌量，或者我們也可以說是買盤與賣盤的相對強弱，因此是一個相對的概念。

### RSI 的計算公式 :

> RSI = 100 × 前N日漲幅的平均值 ÷ ( 前N日漲幅的平均值 + 前N日跌幅的平均值 )

- 前N日漲幅的平均值 < 前N日跌幅的平均值：RSI小於50，代表買盤較賣盤弱
- 前N日漲幅的平均值 > 前N日跌幅的平均值：RSI大於50，代表買盤較賣盤強。

因此，在經過 training_data 線性回歸後，我們取 : 

- BUY		REI < 25
- SELL		RSI > 65

## Requirments

python : 3.10.4

numpy : 1.20.3

pandas : 1.4.4

scikit-learn : 1.1.1

matplotlib : 3.5.1

## Use

    python trade.py [training_data.csv] [testing_data.csv] [output.csv]
