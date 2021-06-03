import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/GOOG.csv")

#df["Date"]
#df["Close"]-df["Open"])/df["Open"]

df["Tauxdevar"]=(df["Close"]-df["Open"])/df["Open"]
df.to_csv("OutputData/output_panda.csv")

#graph (2 curves on the same graph)
plt.plot(df["Date"],df["Tauxdevar"])
plt.plot(df["Date"],df["Open"])