import pandas as pd
import numpy as np
import matplotlib.pyplot as py
import seaborn as sns


# Read the file

customers = pd.read_csv("Ecommerce Customers.csv")

# Let’s checkout the data -

print(customers.head())
print(customers.shape)
print(customers.describe())

g = sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=customers)
g.savefig("jointplot.png")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
 
# Read the file
 
cust = pd.read_csv("Ecommerce Customers.csv")
 
# Let’s checkout the data -
 
print(cust.head())
 
print("No of Rows =" , cust.shape)
 
sns.jointplot(x='Time on Website',y='Yearly Amount Spent', data=cust)
plt.show()