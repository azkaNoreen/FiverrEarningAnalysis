import pandas as pd
import numpy as np
import seaborn as sns
if __name__ == "__main__":

    file=input("Enter File Name: ")

    data=pd.read_csv(file+".csv")
    #canceled orders
    data=data[data['Buyer']!="bodhivida"]
    data=data[data['Buyer']!="kareembrown799"]

    data=data[data['Type']=="Order Revenue"]

    #extracting year
    month = data["Date"].values
    month = [my_str.split("-")[1] for my_str in month]
    data["Month"] = month
    sns_plot=sns.barplot(x='Month',y='Amount',data=data,estimator=np.sum, ci = None)#,hue=data['Month'])
    fig = sns_plot.get_figure()
    fig.savefig('outGraph.jpg') 