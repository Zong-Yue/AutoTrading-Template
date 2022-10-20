import sklearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# You can write code above the if-main block.

def RSI(Close, ind, period=6):
    # 整理資料
    Chg = Close - Close.shift(1)
    Chg_pos = pd.Series(index=Chg.index, data=Chg[Chg>0])
    Chg_pos = Chg_pos.fillna(0)
    Chg_neg = pd.Series(index=Chg.index, data=-Chg[Chg<0])
    Chg_neg = Chg_neg.fillna(0)
    
    # 計算6日平均漲跌幅度
    import numpy as np
    up_mean = np.mean(Chg_pos.values[ind-period:ind])
    down_mean = np.mean(Chg_neg.values[ind-period:ind])
    
    
    # 計算 RSI
    rsi = ( 100 * up_mean / ( up_mean + down_mean ) )
    
    return rsi


if __name__ == "__main__":
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--training", default="training_data.csv", help="input training data file name")
    parser.add_argument("--testing", default="testing_data.csv", help="input testing data file name")
    parser.add_argument("--output", default="output.csv", help="output file name")
    args = parser.parse_args()

    # Data Reading
    training_data = pd.read_csv(args.training, header=0)
    testing_data= pd.read_csv(args.testing, header=0)

    # Testing Data Adjustment
    testing_data = pd.read_csv('testing_data.csv', header=0)
    testDataR1 = testing_data.columns.values
    testData = testing_data.values

    ftestDataR1 = testDataR1.astype(float)
    ftestData = testData.astype(float)

    Close = []

    import csv
    count = 0       # Stock we hold
    dn = 0          # Data index
    delta = 0.005   # Action Parameter 1


    with open(args.output, "w", encoding='utf-8' ,newline='') as csvfile:
        writer = csv.writer(csvfile)
        # First Day
        # BUY if the difference between Close & Open > delta
        if ((ftestDataR1[3] - ftestDataR1[0])/ftestDataR1[3]) > delta :
            if count < 1 :
                writer.writerows('1')
                count +=1
        
        # SELL if the difference between Close & Open < -delta
        elif ((ftestDataR1[0] - ftestDataR1[3])/ftestDataR1[3]) > delta :
            if count >= 0 :
                writer.writerow([-1])
                count -=1
        else :
            writer.writerows('0')

        Close.append(ftestDataR1[3])

        # Second Day and so on
        for row in ftestData :
            if dn < 5:
                if ((ftestData[dn][3] - ftestData[dn][0])/ftestData[dn][3]) > delta :
                    if count < 1 :
                        writer.writerows('1')
                        count +=1
                    else :
                        writer.writerows('0')
                elif ((ftestData[dn][0] - ftestData[dn][3])/ftestData[dn][3]) > delta :
                    if count >= 0 :
                        writer.writerow([-1])
                        count -=1
                    else :
                        writer.writerows('0')
                else :
                    writer.writerows('0')

            # From the 7th dat, Use RSI to make decision 
            elif dn <  len(ftestData)-1:
                Close_series = pd.Series(Close)
                Close_index = dn + 2

                # BUY if RSI < 25
                if RSI(Close_series, Close_index) < 25 :
                    if count < 1 :
                        writer.writerows('1')
                        count +=1
                    else :
                        writer.writerows('0')

                # Sell if RSI > 65
                elif RSI(Close_series, Close_index) > 65 :
                    if count >= 0 :
                        writer.writerow([-1])
                        count -=1
                    else :
                        writer.writerows('0')
                else :
                    writer.writerows('0')
            
            Close.append(ftestData[dn][3])
            dn+=1