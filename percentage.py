import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    Present=[]
    Percentage=[]
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        
        
        for row in df:
            Present.append(float(row["Days Present"]))
            Percentage.append(float(row["Marks In Percentage"]))
        
    return{"x":Present,"y":Percentage}
    
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between the days present and percentage is",correlation[0,1])
def setup():
    data_path="percentage.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
setup()
    
