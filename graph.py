import csv
from matplotlib import pyplot as plt
import numpy as np
def main():
    file_name = "speedtest_data.csv"
    rows = []
    with open(file_name,"r") as rfile:
        reader = csv.reader(rfile)
        for row in reader:
            if row:
                rows.append(row)
    head = rows[0]
    downloads = np.array(rows[1],dtype=float)
    uploads = np.array(rows[2],dtype=float)
    fig = plt.figure(figsize=(15,12))
    plt.plot(np.arange(0,5*len(downloads),5),downloads)
    plt.plot(np.arange(0,5*len(downloads),5),uploads)
    plt.title("mb/s internet test")
    plt.legend(("Downloads", "Uploads"))
    plt.xlabel("minutes since start")
    plt.ylabel("mb/s")
    plt.show()

if __name__ =="__main__":
    main()