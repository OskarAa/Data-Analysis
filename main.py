import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


# Importing data from CSV file:



# Getting the dimensions of the dataframe
# Getting the structure of the dataframe:
# Setting column names: 

column_names = ["Date","Open","High","Low","Close","Adj Close","Volume"]

df = pd.read_csv('AAPL.csv', 
                names=column_names)

print(df.head())
print(df.info())
# Changing column names:
df.columns = ["Datums", "Atvērt", "Augsts", "Zems", "Aizvērt", "Pielāgot aizvērt", "Skaļums"]
print("List of column names: ", df.columns)



# Counting number of missing vals:
missing = df.isnull().sum().reset_index(name='Missing Values Counted')
print("Table with missing values counted: \n", missing)

# Dropping Missing:
df_complete = df.dropna() 
print("Dataframe without missing values: ", df_complete.shape)



vid_aiz = np.array(df_complete)

#vid_aizpatj.reshape[5,5]

#print(vid_aiz)



print("----------------------------------------------------------")



print("Minimala:", np.amin(vid_aiz[1:,5]))
print("Maksimala:", np.amax(vid_aiz[1:,5]))

sorted_by_price = vid_aiz[vid_aiz[1:,5].argsort()]


print("Sorted by price:", sorted_by_price)


#print(np.mean(vid_aizpatj[:, 3]))







def grafiks1():
  x = []
  y = []
  
  with open('AAPL (1).csv','r') as csvfile:
      plots = csv.reader(csvfile, delimiter = ',')
      
      for row in plots:
          x.append(row[0])
          y.append((row[2]))
  
  plt.bar(x, y, color = 'g', width = 0.72, label = "Close")
  plt.xlabel('Date')
  plt.ylabel('Close')
  plt.title('Price')
  plt.legend()
  plt.show()

def grafiks2():

  x = []
  y = []



  ko = np.arange(1,51)
  
  with open('AAPL (1).csv','r') as csvfile:
      lines = csv.reader(csvfile, delimiter=',')
      for row in lines:
          x.append(row[0])
          y.append((row[1]))
  
  plt.plot(x, y, color = 'g', linestyle = 'dashed',
          marker = 'o',label = "Price")
  
  plt.xticks(rotation = 25)
  plt.xlabel(ko)
  plt.ylabel('Close')
  plt.title('KautKO', fontsize = 20)
  plt.grid()
  plt.legend()
  plt.show()
#grafiks2()
grafiks1()