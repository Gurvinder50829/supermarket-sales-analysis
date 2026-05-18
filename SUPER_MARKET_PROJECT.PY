# Write a program in which making the project on the Supermarket Data Analysics analysics data  and Visualization the data 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# then data fetch 
df =pd.read_csv(r"C:\Users\Gurvinder Singh\Desktop\INTERNSHIP_LEVEL_PROJECT\SuperMarket Analysis.csv",encoding="latin1")
print(df)

# then understand the data
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())

# then check if the data is check missing or not
print(df.isnull().sum())
# 
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (16, 8)
plt.rcParams["axes.titleweight"] = "bold"
# df.columns = df.columns.str.lower().str.strip()
# then making the multiple sunplot to find the insights from the data and pridict the data find the insights from the data 
# then subplot =1(Product_Subplots)
fig,ax =plt.subplots(3,3,figsize=(15,10),constrained_layout=True)
fig.suptitle("Product_Data_Distribution",fontweight="bold")
# plt.subplots_adjust(top=0.92, hspace=0.6, wspace=0.4)

# productline 
Product_line=df["Product line"].value_counts().reset_index(name='count')
le_product =Product_line["Product line"]+"-"+Product_line["count"].astype(str)
pr=ax[0,0].bar(le_product,Product_line["count"],color="grey",label="Product_Distribution",edgecolor="black")
ax[0,0].bar_label(pr,padding=5,color="blue",fontsize=10)
ax[0,0].set_title("Product_Distribution",fontweight="bold")
# ax[0,0].set_xlabel("Product_Type",fontweight="bold")
ax[0,0].set_ylabel("Count",fontweight="bold")
ax[0,0].grid(True)
ax[0,0].tick_params(axis="x",labelsize=4)
ax[0,0].legend(loc="lower left")
# maximum quanity of the product
Product =df["Product line"].value_counts().reset_index(name="count")
Max_product =Product.nlargest(1,"count")
Max_idx= Max_product["count"].idxmax()
Max_values = Max_product.loc[Max_idx,"Product line"]+"-"+str(Max_product.loc[Max_idx,"count"])
Max_count =Max_product.loc[Max_idx,"count"]
print(Max_product)
colors=[]
for max in Product["count"]:
    if max == Max_product["count"].iloc[0]:
        colors.append("green")
    else:
        colors.append("whitesmoke")
pr_labels =Product["Product line"]+"-"+Product["count"].astype(str)
pr=ax[0,1].bar(pr_labels,Product["count"],color=colors,label="Maximum_Product_Distribution",edgecolor="black")
ax[0,1].text(Max_values,Max_count,f"Fashion Accessories has the Maximum Count of {Max_count}",ha="center",va="bottom",fontweight="bold",color="green")
# ax[0,1].bar_label(pr,padding=2,color="blue",fontsize=10)
ax[0,1].set_title("Max Product Count",fontweight="bold")
# ax[0,1].set_xlabel("Product_Type",fontweight="bold")
ax[0,1].set_ylabel("Count",fontweight="bold")
ax[0,1].grid(True)
ax[0,1].tick_params(axis="x",labelsize=4)
ax[0,1].tick_params(axis="y",labelsize=7,pad=5)
ax[0,1].legend(loc="lower left")
# min product 
Product =df["Product line"].value_counts().reset_index(name="count")
Min_product =Product.nsmallest(1,"count")
Min_idx=Product["count"].idxmin()
Min_values =Product.loc[Min_idx,"Product line"]
Min_count =Product.loc[Min_idx,"count"]
print("Min Product",Min_product)
colors=[]
for val in Product_line["count"]:
    if val==Min_product["count"].iloc[0]:
        colors.append("red")
    else:
        colors.append("whitesmoke")
mxlabel=Product["Product line"]+"-"+Product["count"].astype(str)
mn=ax[0,2].bar(mxlabel,Product["count"],color=colors,label="Min_Product_Distribution",edgecolor="black")
ax[0,2].text(Min_idx,Min_count,f"Home and Lifestyle has the Minimum count of {Min_count}",ha="center",va="bottom",fontweight="bold",color="red")
# ax[0,2].bar_label(mn,padding=2,color="blue",fontsize=10)
ax[0,2].set_title("Min Product Count",fontweight="bold")
# ax[0,2].set_xlabel("Product_Type",fontweight="bold")
ax[0,2].set_ylabel("Count",fontweight="bold")
ax[0,2].grid(True)
ax[0,2].tick_params(axis="x",labelsize=4)
ax[0,2].tick_params(axis="y",labelsize=7,pad=5)
ax[0,2].legend(loc="lower left")
# # product vs quantity
Quantity_Product =df.groupby("Product line")["Quantity"].sum().reset_index(name="count")
print("Product_Quantity",Quantity_Product)
qn_labels=Quantity_Product["Product line"]+"-"+Quantity_Product["count"].astype(str)
mx=ax[1,0].bar(qn_labels,Quantity_Product["count"],label="Product Distributes Quantity",color="orange",edgecolor="black")
ax[1,0].bar_label(mx,padding=2,color="blue",fontsize=10)
ax[1,0].set_title("Product Distributing Quantity",fontweight="bold")
# ax[1,0].set_xlabel("Product_Type",fontweight="bold")
ax[1,0].set_ylabel("Quantity",fontweight="bold")
ax[1,0].grid(True)
ax[1,0].tick_params(axis="x",labelsize=4)
ax[1,0].tick_params(axis="y",labelsize=7,pad=5)
ax[1,0].legend(loc="lower left")
# # then check the maximum quantity of the product line 
Quantity_Product =df.groupby("Product line")["Quantity"].sum().reset_index(name="count")
Max_Quantity =Quantity_Product.nlargest(1,"count")
max_idxqn = Max_Quantity["count"].idxmax()
max_valqn =Max_Quantity.loc[max_idxqn,"Product line"]+"-"+str(Max_Quantity.loc[max_idxqn,"count"])
max_countqn=Max_Quantity.loc[max_idxqn,"count"]
bar_colors=[]
for value in Quantity_Product["count"]:
    if value ==Max_Quantity["count"].iloc[0]:
        bar_colors.append("green")
    else:
        bar_colors.append("whitesmoke")
max_qn =Quantity_Product["Product line"]+"-"+Quantity_Product["count"].astype(str)
mx=ax[1,1].bar(max_qn,Quantity_Product["count"],label="Maximum Product Distributes Quantity",color=bar_colors,edgecolor="black")
# ax[1,1].bar_label(mx,padding=2,color="blue",fontsize=10)
ax[1,1].text(max_valqn,max_countqn,f"Fashion Accessories has the maximum Quantity And Count  is: {max_countqn}",ha="center",va="bottom",fontweight="bold",color="green")
ax[1,1].set_title("Maximum Product Distributing Quantity",fontweight="bold")
# ax[1,1].set_xlabel("Product_Type",fontweight="bold")
ax[1,1].set_ylabel("Quantity",fontweight="bold")
ax[1,1].grid(True)
ax[1,1].tick_params(axis="x",labelsize=4)
ax[1,1].tick_params(axis="y",labelsize=7,pad=3)
ax[1,1].legend(loc="lower left")
# quantity vs less product
Quantity_Product =df.groupby("Product line")["Quantity"].sum().reset_index(name="count")
Min_Quantity =Quantity_Product.nsmallest(1,"count")
min_idxqn = Min_Quantity["count"].idxmin()
min_valqn =Min_Quantity.loc[min_idxqn,"Product line"]+"-"+str(Min_Quantity.loc[min_idxqn,"count"])
min_countqn=Min_Quantity.loc[min_idxqn,"count"]
bar_colors=[]
for value in Quantity_Product["count"]:
    if value ==Min_Quantity["count"].iloc[0]:
        bar_colors.append("red")
    else:
        bar_colors.append("whitesmoke")
labels =Quantity_Product["Product line"]+ "-" +Quantity_Product["count"].astype(str)
mx=ax[1,2].bar(labels,Quantity_Product["count"],label=" Minimum Product Distributes Quantity",color=bar_colors,edgecolor="black")
# ax[1,1].bar_label(mx,padding=2,color="blue",fontsize=10)
ax[1,2].text(min_valqn,min_countqn,f"Home and lifestyle has the Minimum Quantity And Count is:{min_countqn}",ha="center",va="bottom",fontweight="bold",color="red")
ax[1,2].set_title("Minimum Product Distributing Quantity",fontweight="bold")
# ax[1,2].set_xlabel("Product_Type",fontweight="bold")
ax[1,2].set_ylabel("Quantity",fontweight="bold")
ax[1,2].grid(True)
ax[1,2].tick_params(axis="x",labelsize=5)
ax[1,2].tick_params(axis="y",labelsize=7,pad=3)
ax[1,2].legend(loc="lower left")
# product vs city
Product_city =df.groupby("Product line")["City"].value_counts().reset_index(name="Count")
print("Product Vs City",Product_city)
# # max product  vs city
Max_Product_city =Product_city.nlargest(1,"Count")
print("Max Product vs City",Max_Product_city)
# Min product vs city
Min_Product_city =Product_city.nsmallest(1,"Count")
print("Min Product vs City",Min_Product_city)
# then making the plot of city vs product
ax[2,0].bar(Product_city["Product line"]+"-"+Product_city["City"],Product_city["Count"],label="Min Product vs City")
ax[2,0].set_title("City vs Product",fontweight="bold")
ax[2,0].grid(True)
ax[2,0].set_xlabel("Product line",fontweight="bold",fontsize=8)
ax[2,0].set_ylabel("Count",fontweight="bold",fontsize=8)
ax[2,0].legend(title="City vs Product_Line")
ax[2,0].tick_params(axis='x',labelsize=6,rotation=90)
ax[2,0].tick_params(axis='y',labelsize=4)
# max city vs product line
Product_city =df.groupby("Product line")["City"].value_counts().reset_index(name="Count")
print(Product_city)
Max_Product_city =Product_city.nlargest(1,"Count")
Max_city_idx =Max_Product_city["Count"].idxmax()
max_city_values =Max_Product_city.loc[Max_city_idx,"Product line"] +"-"+Max_Product_city.loc[Max_city_idx,"City"]
max_city_count =Max_Product_city.loc[Max_city_idx,"Count"]
max_bar_color =[]
for bar in Product_city["Count"]:
    if bar == Max_Product_city["Count"].iloc[0]:
        max_bar_color.append("green")
    else:
        max_bar_color.append("whitesmoke")
mx=ax[2,1].bar(Product_city["Product line"] +"-"+Product_city["City"],Product_city["Count"],label="Product by City ",color=max_bar_color,edgecolor="black")
# ax[1,1].bar_label(mx,padding=2,color="blue",fontsize=10)
ax[2,1].text(max_city_values,max_city_count,f"{max_city_count}",ha="center",va="bottom",fontweight="bold",color="green")
ax[2,1].set_title("Maximum Product By City",fontweight="bold")
ax[2,1].set_xlabel("Product line",fontweight="bold")
ax[2,1].set_ylabel("Count",fontweight="bold")
ax[2,1].grid(True)
ax[2,1].tick_params(axis="x",labelsize=4,rotation=90)
ax[2,1].tick_params(axis="y",labelsize=7,pad=3)
ax[2,1].legend(loc="lower left")
# # min city product
# Min_Product_city =Product_city["Count"].min()
Min_city_idx =Min_Product_city.index[0]
Min_city_values =Min_Product_city.loc[Min_city_idx,"Product line"] +"-"+Min_Product_city.loc[Min_city_idx,"City"]
Min_city_count =Min_Product_city.loc[Min_city_idx,"Count"]
Min_bar_color =[]
for bar in Product_city["Count"]:
    if bar == Product_city["Count"].min():
        Min_bar_color.append("red")
    else:
        Min_bar_color.append("whitesmoke")
mx=ax[2,2].bar(Product_city["Product line"] +"-"+Product_city["City"],Product_city["Count"],label="Product by City ",color=Min_bar_color,edgecolor="black")
# ax[1,1].bar_label(mx,padding=2,color="blue",fontsize=10,label=Min_Product_city,color="red")
ax[2,2].text(Min_city_values,Min_city_count+2,f"{Min_city_count}",ha="center",va="bottom",fontweight="bold",color="red")
ax[2,2].set_title("Minimum Product By City",fontweight="bold")
ax[2,2].set_xlabel("Product line",fontweight="bold")
ax[2,2].set_ylabel("Count",fontweight="bold")
ax[2,2].grid(True)
ax[2,2].tick_params(axis="x",labelsize=4,rotation=90)
ax[2,2].tick_params(axis="y",labelsize=7)
ax[2,2].legend(loc="lower left")

plt.tight_layout()
plt.show()
# SALES SUBPLOT THEN ANAYLICS THE DATA AND VISUALIZATION THE DATA\
fig,ax=plt.subplots(4,3,figsize=(15,10),constrained_layout=True)
fig.suptitle("Sales Distribution",fontweight="bold",fontsize=10)
plt.subplots_adjust(hspace=0.5, wspace=0.3)
Total_Sales =df["Sales"].sum()
print(Total_Sales)
sns.kdeplot(x="Sales",data=df,ax=ax[0,0],fill=True)
ax[0,0].set_title("Sales Distribution",fontweight="bold")
ax[0,0].legend(title="Sales Distribution")
ax[0,0].grid(True,linestyle="--")
# gender distribution by sales
Gender_Sales =df.groupby("Gender")["Sales"].sum().reset_index(name="count")
print("Gender Distributions",Gender_Sales)
max_gender =Gender_Sales.nlargest(1,"count")
max_idx =Gender_Sales.index[0]
max_valuesgn =Gender_Sales.loc[max_idx,"Gender"]
max_countgn=round(Gender_Sales.loc[max_idx,"count"],2)
color_bar =[]
for col in Gender_Sales["count"]:
    if col ==max_gender["count"].iloc[0]:
        color_bar.append("green")
    else :
        color_bar.append("whitesmoke")
ax[0,1].bar(Gender_Sales["Gender"],Gender_Sales["count"],label="Gender Distributing Max and Min Sales",color=color_bar,edgecolor="black",width=0.3)
ax[0,1].text(max_valuesgn,max_countgn,f"Female category has the highest count:{(max_countgn)}",ha="center",va="bottom",fontweight="bold",color="green",fontsize=8)
ax[0,1].set_title("Gender Distributing Max and Min Sales",fontweight="bold")
ax[0,1].set_xlabel("Gender",fontweight="bold")
ax[0,1].set_ylabel("Sales",fontweight="bold")
ax[0,1].grid(True)
ax[0,1].tick_params(axis="x",labelsize=8)
ax[0,1].tick_params(axis="y",labelsize=7)
ax[0,1].legend(loc="lower left")
# quantity Vs Sales Distributions
quantity_vs_sales = df.groupby("Quantity")["Sales"].sum().reset_index(name="count")
quantity_vs_sales_max =quantity_vs_sales.nlargest(1,"count")
quantity_Sales_idx =quantity_vs_sales.loc[quantity_vs_sales["count"].idxmax()]
quantity_Sales_Values =quantity_Sales_idx["Quantity"]               
quantity_Sales_count =quantity_Sales_idx["count"]
Sales_bar_color =[]
for col in quantity_vs_sales["count"]:
    if col ==quantity_vs_sales_max["count"].iloc[0]:
        Sales_bar_color.append("green")
    else :
        Sales_bar_color.append("whitesmoke")
ax[0,2].bar(quantity_vs_sales["Quantity"],quantity_vs_sales["count"],label="Quantity Vs Sales",edgecolor="black",color=Sales_bar_color)
ax[0,2].text(quantity_Sales_Values,quantity_Sales_count+2,f"Maximum Sales occurred at quantity 10 with value {round(quantity_Sales_count),2}",ha="center",va="bottom",fontweight="bold",fontsize=8,color="green")
ax[0,2].set_title("Quantity Vs Sales",fontweight="bold")
ax[0,2].set_xlabel("Quantity",fontweight="bold")
ax[0,2].set_ylabel("Sales",fontweight="bold")
ax[0,2].grid(True)
ax[0,2].legend(loc="lower left")
ax[0,2].tick_params(axis="x",labelsize=6)
ax[0,2].tick_params(axis="y",labelsize=6)
# Product line vs Sales
Product_Sales =df.groupby("Product line")["Sales"].sum().reset_index(name="count")
print("Product_Vs_City_Distributions",Product_city)
mx=ax[1,0].bar(Product_Sales["Product line"],Product_Sales["count"],color="brown",edgecolor="black",label="Product_VS_Sales",width=0.3)
ax[1,0].bar_label(mx,padding=5,fontweight="bold",color="blue",fontsize=8)
ax[1,0].set_title("Product Distributes Sales",fontweight="bold")
ax[1,0].set_xlabel("Product line")
ax[1,0].set_ylabel("Sales",fontweight="bold")
ax[1,0].grid(True)
ax[1,0].tick_params(axis="x",labelsize=4)
ax[1,0].legend(loc="lower left")

# max_sales product
Product_Sales =df.groupby("Product line")["Sales"].sum().reset_index(name="count")
Product_Sales_max =Product_Sales.nlargest(1,"count")
Product_idx = Product_Sales.loc[Product_Sales["count"].idxmax()]
Product_Sales_Values =Product_idx["Product line"]
max_idx = Product_Sales["count"].idxmax()
Product_Sales_count= Product_idx["count"]
mx_color=[]
for max_bar in Product_Sales["count"]:
    if max_bar==Product_idx["count"]:
        mx_color.append("green")
    else:
        mx_color.append("whitesmoke")
ax[1,1].bar(Product_Sales["Product line"],Product_Sales["count"],color=mx_color,edgecolor="black",label="Maximum Product Sale",width=0.3)
ax[1,1].text(max_idx,Product_Sales_count+2,f"Food and Beverages recorded the Maximum Sales of{round(Product_Sales_count),2}",ha="center",va="bottom",fontweight="bold",color="green",fontsize=8)
ax[1,1].set_title("Maximum Sales Product",fontweight="bold")
ax[1,1].set_xlabel("Product",fontweight="bold")
ax[1,1].set_ylabel("Sales",fontweight="bold")
ax[1,1].grid(True)
ax[1,1].legend(loc="lower left")
ax[1,1].tick_params(axis="x",labelsize=5)
ax[1,1].tick_params(axis="y",labelsize=6)

# Min  Product  Sales
Product_Sales =df.groupby("Product line")["Sales"].sum().reset_index(name="count")
Product_Sales_min =Product_Sales.nsmallest(1,"count")
min_idx = Product_Sales["count"].idxmin()
# use for the text at top
Product_idx = Product_Sales.loc[Product_Sales["count"].idxmin()]
Product_Sales_Values =Product_idx["Product line"]
Product_Sales_count= Product_idx["count"]
mx_color=[]
for max_bar in Product_Sales["count"]:
    if max_bar==Product_idx["count"]:
        mx_color.append("red")
    else:
        mx_color.append("whitesmoke")
ax[1,2].bar(Product_Sales["Product line"],Product_Sales["count"],color=mx_color,edgecolor="black",label="Minimum Product Sale",width=0.3)
ax[1,2].text(min_idx,Product_Sales_count+2,f"Health And Beauty recorded the Minimum Sales of :{round(Product_Sales_count),2}",ha="center",va="bottom",fontweight="bold",color="red",fontsize=8)
ax[1,2].set_title("Minimum Sales Product",fontweight="bold")
ax[1,2].set_xlabel("Product",fontweight="bold")
ax[1,2].set_ylabel("Sales",fontweight="bold")
ax[1,2].grid(True)
ax[1,2].legend(loc="lower left")
ax[1,2].tick_params(axis="x",labelsize=5)
ax[1,2].tick_params(axis="y",labelsize=6)

# Sales VS city
Sales_city =df.groupby("City")["Sales"].sum().reset_index(name="count")
print(Sales_city)
sl =ax[2,0].bar(Sales_city["City"],Sales_city["count"],label="City Distribution By Sales",edgecolor="black",width=0.3,color="royalblue")
ax[2,0].bar_label(sl,padding=5,color="blue",fontsize=8)
ax[2,0].set_title("City Distribution By Sales",fontweight="bold")
ax[2,0].set_xlabel("Sales",fontweight="bold")
ax[2,0].set_ylabel("City",fontweight="bold")
ax[2,0].grid(True)
ax[2,0].legend(loc="lower left")
ax[2,0].tick_params(axis="x",labelsize=8)
ax[2,0].tick_params(axis="y",labelsize=8)
# maximum city by sales
Sales_city =df.groupby("City")["Sales"].sum().reset_index(name="count")
Max_Sales_city =Sales_city.nlargest(1,"count")
print(Max_Sales_city)
mx_City_idx= Sales_city.loc[Sales_city["count"].idxmax()]
mx_idx=Sales_city["count"].idxmax()
mx_sales_values =mx_City_idx["City"]
mx_sales_count=mx_City_idx["count"]
colorss =[]
for MX_col in Sales_city["count"]:
    if MX_col==Max_Sales_city["count"].iloc[0]:
        colorss.append("green")
    else:
        colorss.append("whitesmoke")
mx=ax[2,1].bar(Sales_city["City"],Sales_city["count"],label="Maximum Sales Distribution By City",edgecolor="black",width=0.3,color=colorss)
# ax[2,1].bar_label(mx,padding=5,color="blue")
ax[2,1].text(mx_idx,mx_sales_count,f"Naypyitaw has the maximum sales :{mx_sales_count}",va="bottom",ha="center",fontweight="bold",color="green")
ax[2,1].set_title("Maximum Sales Distribution By City",fontweight="bold")
ax[2,1].set_xlabel("Sales",fontweight="bold")
ax[2,1].set_ylabel("City",fontweight="bold")
ax[2,1].grid(True)
ax[2,1].legend(loc="lower left")
ax[2,1].tick_params(axis="x",labelsize=8)
ax[2,1].tick_params(axis="y",labelsize=8)
# minimum sales by city
Sales_city =df.groupby("City")["Sales"].sum().reset_index(name="count")
Min_Sales_city =Sales_city.nsmallest(1,"count")
print(Min_Sales_city)
mn_City_idx= Sales_city.loc[Sales_city["count"].idxmin()]
mn_idx=Sales_city["count"].idxmin()
mn_sales_values =mn_City_idx["City"]
mn_sales_count=mn_City_idx["count"]
colorss =[]
for Mn_col in Sales_city["count"]:
    if Mn_col==Min_Sales_city["count"].iloc[0]:
        colorss.append("red")
    else:
        colorss.append("whitesmoke")
mx=ax[2,2].bar(Sales_city["City"],Sales_city["count"],label="Minimum Sales Distribution By City",edgecolor="black",width=0.3,color=colorss)
# ax[2,1].bar_label(mx,padding=5,color="blue")
ax[2,2].text(mn_idx,mn_sales_count,f"Mandalay has the minimum sales :{mn_sales_count}",va="bottom",ha="center",fontweight="bold",color="red")
ax[2,2].set_title("Minimum Sales Distribution By City",fontweight="bold",pad=10)
ax[2,2].set_xlabel("Sales",fontweight="bold")
ax[2,2].set_ylabel("City",fontweight="bold")
ax[2,2].grid(True)
ax[2,2].legend(loc="lower left")
ax[2,2].tick_params(axis="x",labelsize=8)
ax[2,2].tick_params(axis="y",labelsize=8)
# branch vs sales
branch_Sales =df.groupby("Branch")["Sales"].sum().reset_index()
print("banch Vs Sales",branch_Sales)
br =ax[3,0].bar(branch_Sales["Branch"],branch_Sales["Sales"],color="crimson",label="Branch Vs Sales",edgecolor="black",width=0.3)
ax[3,0].bar_label(br,padding=3,color="blue",fontsize=8)
ax[3,0].set_title("Branch Distributing By Sales",fontweight="bold")
# ax[3,0].set_xlabel("Branch")
ax[3,0].set_ylabel("Sales Count")
ax[3,0].grid(True)
ax[3,0].legend(loc="lower right")
# then find check the which branch having maximum sales
branch_Sales =df.groupby("Branch")["Sales"].sum().reset_index(name="count")
branch_Sales_max =branch_Sales.max()
max_idx = branch_Sales["count"].max()
# use for the text at top
branch_idx = branch_Sales.loc[branch_Sales["count"].idxmax()]
Branch_Sales_Values =branch_idx["Branch"]
Branch_Sales_count= branch_idx["count"]
mx_branch_color =[]
for br_max in branch_Sales["count"]:
    if br_max ==branch_Sales_max["count"]:
        mx_branch_color.append("green")
    else:
        mx_branch_color.append("whitesmoke")
ax[3,1].bar(branch_Sales["Branch"],branch_Sales["count"],color=mx_branch_color,edgecolor="black",label="Maximum Branch VS Sales",width=0.3)
ax[3,1].text(Branch_Sales_Values,Branch_Sales_count,f"Giza{Branch_Sales_count} is the branch with Maximum sales.",ha="center",va="bottom",color="green",fontsize=8,fontweight="bold")
ax[3,1].set_title("Maximum Branch Distrbution By Sales",fontweight="bold")
ax[3,1].set_xlabel("Branch")
ax[3,1].set_ylabel("Sales")
ax[3,2].legend(loc="lower left")
ax[3,1].grid(True)
# min branch sales
branch_Sales =df.groupby("Branch")["Sales"].sum().reset_index(name="count")
branch_Sales_max =branch_Sales.min()
branch_idx = branch_Sales.loc[branch_Sales["count"].idxmin()]
Branch_Sales_Values =branch_idx["Branch"]
Branch_Sales_count= branch_idx["count"]
mn_branch_color =[]
for br_max in branch_Sales["count"]:
    if br_max ==branch_Sales_max["count"]:
        mn_branch_color.append("red")
    else:
        mn_branch_color.append("whitesmoke")
ax[3,2].bar(branch_Sales["Branch"],branch_Sales["count"],color=mn_branch_color,edgecolor="black",label="Minimum Branch VS Sales",width=0.3)
ax[3,2].text(Branch_Sales_Values,Branch_Sales_count,f"Cario {Branch_Sales_count} is the branch with Minimum sales.",ha="center",va="bottom",color="red",fontsize=8,fontweight="bold")
ax[3,2].set_title("Minimum Branch Distrbution By Sales",fontweight="bold")
ax[3,2].set_xlabel("Branch")
ax[3,2].set_ylabel("Sales")
ax[3,2].legend(loc="lower left")
# ax[3,2].grid(True)
plt.tight_layout()
plt.show()
# Find the Sales accordingly Day month and year wish
df["Date"] =pd.to_datetime(df["Date"])
df["Month"] =df["Date"].dt.month
df["Year"] =df["Date"].dt.year
df["Day"] =df["Date"].dt.day
print(df.columns)
# then Sales vs day
Day_Sales =df.groupby("Day")["Sales"].sum().reset_index()
print("Day Sales",Day_Sales)
Month_Sales =df.groupby("Month")["Sales"].sum().reset_index()
print("Month Sales",Month_Sales)
Year_Sales =df.groupby("Year")["Sales"].sum().reset_index()
print("Year Sales",Year_Sales)
# Sales Distribution by Time
fig,ax =plt.subplots(1,3,figsize=(15,5))
fig.suptitle("Sales Distribution By Time Taken",fontweight="bold",fontsize=15)
# colors = plt.cm.viridis(np.linspace(0, 1, len("Day")))
ax[0].bar(Day_Sales["Day"],Day_Sales["Sales"],color="#6A0DAD",label="Sales Distribution by Day",edgecolor="black",width=0.2)
ax[0].set_title("Sales Distribution By Day",fontweight="bold",pad=10)
ax[0].set_xlabel("Day",fontweight="bold")
ax[0].set_ylabel("Sales",fontweight="bold")
ax[0].grid(True)
ax[0].legend(loc="lower left")
ax[0].tick_params(axis="x",labelsize=8)
ax[0].tick_params(axis="y",labelsize=8)
# Sales Distribution by Month
Month_Sales =df.groupby("Month")["Sales"].sum().reset_index()
print("Month Sales",Month_Sales)
Max_Month_Sales_idx =Month_Sales.loc[Month_Sales["Sales"].idxmax()]
Min_Month_Sales_idx =Month_Sales.loc[Month_Sales["Sales"].idxmin()]
# Values both min & max 
Max_Month_Sales_Values=Max_Month_Sales_idx["Month"]
Min_Month_Sales_Values =Min_Month_Sales_idx["Month"]
# count of the Min max
Max_Month_Sales_Count=Max_Month_Sales_idx["Sales"]
Min_Month_Sales_Count =Min_Month_Sales_idx["Sales"]
month_color =[]
for br_max in Month_Sales["Sales"]:
    if br_max ==Month_Sales["Sales"].max():
        month_color.append("green")
    elif br_max==Month_Sales["Sales"].min():
        month_color.append("red")
    else:
        month_color.append("#2F5597")
ax[1].bar(Month_Sales["Month"],Month_Sales["Sales"],color=month_color ,label="Sales Distribution by Month",edgecolor="black",width=0.8)
ax[1].text(Max_Month_Sales_Values,Max_Month_Sales_Count,f"The Highest Sales in a Month is {Max_Month_Sales_Count}",ha="center",va="bottom",color="green",fontsize=8,fontweight="bold")
ax[1].text(Min_Month_Sales_Values,Min_Month_Sales_Count,f"The Lowest Sales in a Month is {Min_Month_Sales_Count}",ha="center",va="bottom",color="red",fontsize=8,fontweight="bold")
ax[1].set_title("Sales Distribution By Month Maximum &Minimum",fontweight="bold",pad=10)
ax[1].set_xlabel("Month",fontweight="bold")
ax[1].set_ylabel("Sales",fontweight="bold")
ax[1].grid(True)
ax[1].legend(loc="lower left")
ax[1].tick_params(axis="x",labelsize=8)
ax[1].tick_params(axis="y",labelsize=8)
# making the plot of that in which Sales distribution by Year and MAximum Sales in the year
yr=ax[2].bar(Year_Sales["Year"],Year_Sales["Sales"],color="grey",edgecolor="black",label="Sales Distribution By Yearly")
ax[2].bar_label(yr,padding=5,color="blue",fontsize=8,fmt="Yearly Sales: %d",fontweight="bold")
ax[2].set_title("Sales Distribution By Year",fontweight="bold",pad=10)
ax[2].set_xlabel("Year",fontweight="bold")
ax[2].set_ylabel("Sales",fontweight="bold")
ax[2].grid(True)
ax[2].legend(loc="lower left")
ax[2].tick_params(axis="x",labelsize=8)
ax[2].tick_params(axis="y",labelsize=8)
plt.tight_layout()
plt.show()
# check the rating  
fig,ax=plt.subplots(2,3,figsize=(25,15))
fig.suptitle("Rating Distribution",fontweight="bold")
sns.countplot(x="Rating",data=df,color="blue",ax=ax[0,0])
ax[0,0].set_title("Rating Distribution",fontweight="bold",pad=10)
ax[0,0].legend(title="Rating Distributions")
ax[0,0].set_xlabel("Rating")
ax[0,0].set_ylabel("Count")
ax[0,0].tick_params(axis="x",rotation=90,labelsize=5)
ax[0,0].grid(True)
# check the maximum Rating
rating_data=df["Rating"].value_counts().reset_index(name="count")
Mx_Rating=rating_data["count"].max()
Mx_rating_indx= rating_data.loc[rating_data["count"].idxmax()]
Mx_rating_Values  =Mx_rating_indx["Rating"]
Mx_rating_count =Mx_rating_indx["count"]
rating_color =[]
for rate in rating_data["count"]:
    if rate ==rating_data["count"].max():
        rating_color.append("green")
    else :
        rating_color.append("whitesmoke")
ax[0,1].bar(rating_data["Rating"],rating_data["count"],color=rating_color,edgecolor="black",label=" Maximum Rating Distribution",width=0.1)
ax[0,1].text(Mx_rating_Values,Mx_rating_count,f"6 is the Maximum rating among all ratings Count is :{Mx_rating_count}",ha="center",va="bottom",color="green",fontsize=8,fontweight="bold")
ax[0,1].set_title(" Maximum Rating Distributions",fontweight="bold")
ax[0,1].set_xlabel("Rating",fontweight="bold")
ax[0,1].set_ylabel("Count",fontweight="bold")
ax[0,1].grid(True)
ax[0,1].legend(loc="lower left")
ax[1,0].tick_params(axis="x",labelsize=8)
ax[1,0].tick_params(axis="y",labelsize=8)
# min rating count
rating_data=df["Rating"].value_counts().reset_index(name="count")
Mn_Rating=rating_data["count"].min()
Mn_rating_indx= rating_data.loc[rating_data["count"].idxmin()]
Mn_rating_Values  =Mn_rating_indx["Rating"]
Mn_rating_count =Mn_rating_indx["count"]
rating_color_mn =[]
for rate in rating_data["count"]:
    if rate ==rating_data["count"].min():
        rating_color_mn.append("red")
    else :
        rating_color_mn.append("whitesmoke")
ax[0,2].bar(rating_data["Rating"],rating_data["count"],color=rating_color_mn,edgecolor="black",label=" Minimum Rating Distribution",width=0.1)
ax[0,2].text(Mn_rating_Values,Mn_rating_count,f"10 is the Minimum rating among all ratings Count is :{Mn_rating_count}",ha="center",va="bottom",color="red",fontsize=8,fontweight="bold")
ax[0,2].set_title("Minimum Rating Distributions",fontweight="bold")
ax[0,2].set_xlabel("Rating",fontweight="bold")
ax[0,2].set_ylabel("Count",fontweight="bold")
ax[0,2].grid(True)
ax[0,2].legend(loc="lower left")
ax[0,2].tick_params(axis="x",labelsize=8)
ax[0,2].tick_params(axis="y",labelsize=8)
# Rating by Product

container= sns.barplot(data=df,x="Product line",y="Rating",color="royalblue",ax=ax[1,0])
for c in ax[1,0].containers:
    ax[1,0].bar_label(c,padding=5,color="blue",fontsize=5)
ax[1,0].set_title("Rating Distribution By Product",fontweight="bold")
ax[1,0].set_xlabel("Product",fontweight="bold")
ax[1,0].set_ylabel("Rating",fontweight="bold")
ax[1,0].grid(True)
ax[1,0].legend(loc="lower left")
ax[1,0].tick_params(axis="x",labelsize=8,rotation=90)
ax[1,0].tick_params(axis="y",labelsize=8,rotation=90)
# check the maximum rating in which product type 
Product_rating=df.groupby("Product line")["Rating"].count().reset_index(name="Counts")
print("Product Rating",Product_rating)
Max_Product_Rating=Product_rating["Counts"].max()
Max_Prdouct_idx=Product_rating.loc[Product_rating["Counts"].idxmax()]
Max_Product_values =Max_Prdouct_idx["Product line"]
Max_Product_count =Max_Prdouct_idx["Counts"]
Rating_Product_color =[]
for Mx_product_color in Product_rating["Counts"]:
    if Mx_product_color==Product_rating["Counts"].max():
        Rating_Product_color.append("green")
    else:
        Rating_Product_color.append("whitesmoke")
ax[1,1].bar(Product_rating["Product line"],Product_rating["Counts"],color=Rating_Product_color,label="Maximum Product Rating",edgecolor="black")
ax[1,1].set_title("Maximum Product Rating",fontweight="bold")
ax[1,1].text(Max_Product_values,Max_Product_count,f"Fashion accessories{Max_Product_count} received the highest rating among all product categories",ha="center",va="bottom",color="green",fontsize=8,fontweight="bold")
ax[1,1].set_xlabel("Product",fontweight="bold")
ax[1,1].set_ylabel("Rating",fontweight="bold")
ax[1,1].grid(True)
ax[1,1].legend(loc="lower left")
ax[1,1].tick_params(axis="x",labelsize=8,rotation=90)
ax[1,1].tick_params(axis="y",labelsize=8,rotation=90)
# mimimum rating check which color
Product_rating=df.groupby("Product line")["Rating"].count().reset_index(name="Counts")
print("Product Rating",Product_rating)
Min_Prdouct_idx=Product_rating.loc[Product_rating["Counts"].idxmin()]
Min_Product_values =Min_Prdouct_idx["Product line"]
Min_Product_count =Min_Prdouct_idx["Counts"]
Min_Rating_Product_color =[]
for Min_product_color in Product_rating["Counts"]:
    if Min_product_color==Product_rating["Counts"].min():
        Min_Rating_Product_color.append("red")
    else:
        Min_Rating_Product_color.append("whitesmoke")
ax[1,2].bar(Product_rating["Product line"],Product_rating["Counts"],color=Min_Rating_Product_color,label="Minimum Product Rating",edgecolor="black")
ax[1,2].set_title("Maximum Product Rating",fontweight="bold")
ax[1,2].text(Min_Product_values,Min_Product_count,f"Health and beauty{Min_Product_count} recorded the lowest average rating among all product categories.",ha="center",va="bottom",color="red",fontsize=8,fontweight="bold")
ax[1,2].set_xlabel("Product",fontweight="bold")
ax[1,2].set_ylabel("Rating",fontweight="bold")
ax[1,2].grid(True)
ax[1,2].legend(loc="lower left")
ax[1,2].tick_params(axis="x",labelsize=8,rotation=90)
ax[1,2].tick_params(axis="y",labelsize=8,rotation=90)
plt.tight_layout()
plt.show()
# then making the subplot of the profit table
fig,ax =plt.subplots(3,3,figsize=(15,10))
fig.suptitle("Profit Distribution",fontweight="bold",fontsize=15)
df["Profit"] =df["Sales"]-df["cogs"]
Total_profit =df["Profit"].sum()
print("Total_Profit",Total_profit)
sns.kdeplot(data=df,x="Profit",fill=True,ax=ax[0,0])
ax[0,0].set_title("Profit Distributions",fontweight="bold")
ax[0,0].grid(True)
ax[0,0].legend(title="Profit Distributions")
ax[0,0].tick_params(axis="x",labelsize=8,rotation=90)
ax[0,0].tick_params(axis="y",labelsize=8,rotation=90)
# max_profit by city
Profit_city = df.groupby("City")["Profit"].sum().reset_index(name="Values")
print("Max_Profit City",Profit_city)
Max_Profit_City_idx =Profit_city.loc[Profit_city["Values"].idxmax()]
Max_Profit_city_Values =Max_Profit_City_idx["City"]
Max_Profit_city_count =Max_Profit_City_idx["Values"]
color_max_city =[]
for Color_bar in Profit_city["Values"]:
    if Color_bar == Profit_city["Values"].max():
        color_max_city.append("green")
    else:
        color_max_city.append("whitesmoke")
ax[0,1].bar(Profit_city["City"],Profit_city["Values"],color=color_max_city,label="Max_City_Profit",edgecolor="black",width=0.3)
ax[0,1].set_title("Max Profit by City",fontweight="bold")
ax[0,1].text(Max_Profit_city_Values,Max_Profit_city_count,f"Naypyitaw {Max_Profit_city_count}has the highest profit contribution",ha="center",va="bottom",color="green",fontweight="bold")
ax[0,1].set_xlabel("City",fontweight="bold")
ax[0,1].set_ylabel("Profit",fontweight="bold")
ax[0,1].grid(True)
ax[0,1].legend(loc="lower left")
ax[0,1].tick_params(axis="x",labelsize=8)
ax[0,1].tick_params(axis="y",labelsize=8,rotation=90)
# Min Profit given City 
Profit_city = df.groupby("City")["Profit"].sum().reset_index(name="Values")
print("Max_Profit City",Profit_city)
Min_Profit_City_idx =Profit_city.loc[Profit_city["Values"].idxmin()]
Min_Profit_city_Values =Min_Profit_City_idx["City"]
Min_Profit_city_count =Min_Profit_City_idx["Values"].round(2)
color_min_city =[]
for Color_bar in Profit_city["Values"]:
    if Color_bar == Profit_city["Values"].min():
        color_min_city.append("red")
    else:
        color_min_city.append("whitesmoke")
ax[0,2].bar(Profit_city["City"],Profit_city["Values"],color=color_min_city,label="Min_City_Profit",edgecolor="black",width=0.3)
ax[0,2].set_title("Min Profit by City",fontweight="bold")
ax[0,2].text(Min_Profit_city_Values,Min_Profit_city_count,f"Mandalay {Min_Profit_city_count}has the Lowest profit contribution",ha="center",va="bottom",color="red",fontweight="bold")
ax[0,2].set_xlabel("City",fontweight="bold")
ax[0,2].set_ylabel("Profit",fontweight="bold")
ax[0,2].grid(True)
ax[0,2].legend(loc="lower left")
ax[0,2].tick_params(axis="x",labelsize=8)
ax[0,2].tick_params(axis="y",labelsize=8,rotation=90)
# product vs profit
Product_Profit =df.groupby("Product line")["Profit"].sum().reset_index(name="Product_count")
Product_Profit_idx =Product_Profit.loc[Product_Profit["Product_count"].idxmax()]
Product_Profit_Values =Product_Profit_idx["Product line"]
Product_Profit_Count=Product_Profit_idx["Product_count"]
pr=ax[1,0].bar(Product_Profit["Product line"],Product_Profit["Product_count"],color="grey",edgecolor="black",label="Product Distribution By Profits")
ax[1,0].bar_label(pr,padding=5,fontsize=8,color="blue")
ax[1,0].set_title("Product Distribution By Profit",fontweight="bold")
ax[1,0].set_xlabel("Product",fontweight="bold")
ax[1,0].set_ylabel("Profit",fontweight="bold")
ax[1,0].legend(loc="lower left")
ax[1,0].tick_params(axis="x",labelsize=5)
ax[1,0].tick_params(axis="y",labelsize=8)
# maximum Profit gives which  product 
Product_Profit =df.groupby("Product line")["Profit"].sum().reset_index(name="Product_count")
Max_Product_Profit_idx =Product_Profit.loc[Product_Profit["Product_count"].idxmax()]
Max_Product_Profit_Values =Max_Product_Profit_idx["Product line"]
Max_Product_Profit_Count=Max_Product_Profit_idx["Product_count"]
Product_bar_color=[]
for bars in Product_Profit["Product_count"]:
    if bars ==Product_Profit["Product_count"].max():
        Product_bar_color.append("green")
    else:
        Product_bar_color.append("whitesmoke")
ax[1,1].bar(Product_Profit["Product line"],Product_Profit["Product_count"],color=Product_bar_color,edgecolor="black",label="Maximum Profit Distribution By Product")
ax[1,1].text(Max_Product_Profit_Values,Max_Product_Profit_Count,f"Food and beverages Product Distributes Maximum Profit :{Max_Product_Profit_Count}",ha="center",va="bottom",color="green",fontweight="bold")
ax[1,1].set_title("Maximum Profit Distribution By Product",fontweight="bold")
ax[1,1].set_xlabel("Product",fontweight="bold")
ax[1,1].set_ylabel("Profit",fontweight="bold")
ax[1,1].tick_params(axis="x",labelsize=5)
ax[1,1].legend(loc="lower left")
ax[1,1].tick_params(axis="y",labelsize=8)
# minimum Profit Distribution by product
Product_Profit =df.groupby("Product line")["Profit"].sum().reset_index(name="Product_count")
Min_Product_Profit_idx =Product_Profit.loc[Product_Profit["Product_count"].idxmin()]
Min_Product_Profit_Values =Min_Product_Profit_idx["Product line"]
Min_Product_Profit_Count=Min_Product_Profit_idx["Product_count"].round(2)
Product_bar_color=[]
for bars in Product_Profit["Product_count"]:
    if bars ==Product_Profit["Product_count"].min():
        Product_bar_color.append("red")
    else:
        Product_bar_color.append("whitesmoke")
ax[1,2].bar(Product_Profit["Product line"],Product_Profit["Product_count"],color=Product_bar_color,edgecolor="black",label="Minimum Profit Distribution By Product")
ax[1,2].text(Min_Product_Profit_Values,Min_Product_Profit_Count,f"Health And Beauty Product Distrbutes the Minimum Profit :{Min_Product_Profit_Count}",ha="center",va="bottom",color="red",fontweight="bold")
ax[1,2].set_title("Minimum Profit Distribution By Product",fontweight="bold")
ax[1,2].set_xlabel("Product",fontweight="bold")
ax[1,2].set_ylabel("Profit",fontweight="bold")
ax[1,2].tick_params(axis="x",labelsize=5)
ax[1,2].legend(loc="lower left")
ax[1,2].tick_params(axis="y",labelsize=8)
# check the branch having profit
Branch_Profit =df.groupby("Branch")["Profit"].sum().reset_index(name="count")
print(Branch_Profit)
Branch_Profit_idx=Branch_Profit.loc[Branch_Profit["count"].idxmax()]
Branch_Profit_values =Branch_Profit_idx["Branch"]
Branch_Profit_count=Branch_Profit_idx["count"]
br=ax[2,0].bar(Branch_Profit["Branch"],Branch_Profit["count"],edgecolor="black",color="skyblue",label="Profit Distributing By Branch",width=0.3)
ax[2,0].bar_label(br,padding=5,fontsize=8)
ax[2,0].set_title("Profit Distribution By Branch",fontweight="bold")
ax[2,0].set_xlabel("Branch",fontweight="bold")
ax[2,0].set_ylabel("Profit",fontweight="bold")
ax[2,0].legend(loc="lower left")
ax[2,0].tick_params(axis="x",labelsize=8)
ax[2,0].tick_params(axis="y",labelsize=8)
# check the branch Having Maximum Profits
Branch_Profit =df.groupby("Branch")["Profit"].sum().reset_index(name="count")
print(Branch_Profit)
Max_Branch_Profit_idx=Branch_Profit.loc[Branch_Profit["count"].idxmax()]
Max_Branch_Profit_values =Max_Branch_Profit_idx["Branch"]
Max_Branch_Profit_count=Max_Branch_Profit_idx["count"]
branch_bar_color=[]
for branch_bar in Branch_Profit["count"]:
    if branch_bar==Max_Branch_Profit_idx["count"].max():
        branch_bar_color.append("green")
    else:
        branch_bar_color.append("whitesmoke")

br=ax[2,1].bar(Branch_Profit["Branch"],Branch_Profit["count"],edgecolor="black",color=branch_bar_color,label=" Maximum Profit Distributing By Branch",width=0.3)
ax[2,1].text(Max_Branch_Profit_values,Max_Branch_Profit_count,f"Giza Branch Distibutes the Maximum Profits :{Max_Branch_Profit_count}",ha="center",va="bottom",color="green",fontsize=8,fontweight="bold")
# ax[2,1].bar_label(br,padding=5,fontsize=8)
ax[2,1].set_title("Maximum Profit Distribution By Branch",fontweight="bold")
ax[2,1].set_xlabel("Branch",fontweight="bold")
ax[2,1].set_ylabel("Profit",fontweight="bold")
ax[2,1].legend(loc="lower left")
ax[2,1].tick_params(axis="x",labelsize=8)
ax[2,1].tick_params(axis="y",labelsize=8)
# minimum Profit distibution by branch
Branch_Profit =df.groupby("Branch")["Profit"].sum().reset_index(name="count")
print(Branch_Profit)
Min_Branch_Profit_idx=Branch_Profit.loc[Branch_Profit["count"].idxmin()]
Min_Branch_Profit_values =Min_Branch_Profit_idx["Branch"]
Min_Branch_Profit_count=Min_Branch_Profit_idx["count"]
branch_bar_color=[]
for branch_bar in Branch_Profit["count"]:
    if branch_bar==Min_Branch_Profit_idx["count"].min():
        branch_bar_color.append("red")
    else:
        branch_bar_color.append("whitesmoke")

br=ax[2,2].bar(Branch_Profit["Branch"],Branch_Profit["count"],edgecolor="black",color=branch_bar_color,label=" Minimum Profit Distributing By Branch",width=0.3)
ax[2,2].text(Min_Branch_Profit_values,Min_Branch_Profit_count,f"Cario Branch Distributes Minimum Profit :{Min_Branch_Profit_count}",ha="center",va="bottom",color="red",fontsize=8,fontweight="bold")
# ax[2,1].bar_label(br,padding=5,fontsize=8)
ax[2,2].set_title("Minimum Profit Distribution By Branch",fontweight="bold")
ax[2,2].set_xlabel("Branch",fontweight="bold")
ax[2,2].set_ylabel("Profit",fontweight="bold")
ax[2,2].legend(loc="lower left")
ax[2,2].tick_params(axis="x",labelsize=8)
ax[2,2].tick_params(axis="y",labelsize=8)
plt.tight_layout()
plt.show()
# then analysics the sales
print("Total Quantity",df["Quantity"].sum())
print("Total_Cogs",df["cogs"].sum())
print("Total_Unit Price",df["Unit price"].sum())
print("Total_Sales Of 2023",df["Sales"].sum())
# then in program using Linear Regression then Predict the Sales and Profit for the future
# making the Prdicting Subplot

# import the important libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score,mean_squared_error

# import data 
X=df[["Quantity","cogs","Unit price","Year"]]
y=df["Sales"]

#train test split
X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=42)

# standarization data
Scaler =StandardScaler()
X_train =Scaler.fit_transform(X_train)
X_test=Scaler.transform(X_test)

# model train
model_ridge=Ridge(alpha=1.0)
model_ridge.fit(X_train,y_train)

# predict
y_pred_rd =model_ridge.predict(X_test)
print("Pricted_Ridge Regression",y_pred_rd)
# check the accuracy
print("R2_Score",r2_score(y_test,y_pred_rd))
print("MSE",mean_squared_error(y_test,y_pred_rd))
# check the score of the model
X_train =model_ridge.score(X_train,y_train)
X_test=model_ridge.score(X_test,y_test)
# print the score
print("X_train Score",X_train)
print("X_test",X_test)

# # then Predict the Sales 
new_data =pd.DataFrame([[5600,312592,59360,2025]],columns=["Quantity","cogs","Unit price","Year"])
new_data_scaler =Scaler.transform(new_data)
y_pred_rdn =model_ridge.predict(new_data_scaler)
print("Predicted Ridge",y_pred_rdn)
# [5600,312592,59360,2025]
# visualization the data 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

fig, ax = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Prediction Analysics",fontweight="bold",fontsize=15)
# =========================
# 1. Residual Plot (Sales Model Error)
# =========================
residual = y_test - y_pred_rd

ax[0,0].hist(residual, bins=20)
ax[0,0].axvline(0, color='red', linestyle='--')
ax[0,0].set_title("Residual Plot (Error Analysis)")
ax[0,0].set_xlabel("Error (Actual - Predicted)")
ax[0,0].grid()


# =========================
# 2. Actual vs Predicted (Sales)
# =========================
sns.scatterplot(x=y_test, y=y_pred_rd, ax=ax[0,1])

ax[0,1].plot([y_test.min(), y_test.max()],
             [y_test.min(), y_test.max()],
             'r--')

ax[0,1].set_title("Actual vs Predicted Sales")
ax[0,1].set_xlabel("Actual Sales")
ax[0,1].set_ylabel("Predicted Sales")
ax[0,1].grid()


# =========================
# 3. Profit Residual Plot (Optional Insight)
# =========================
profit_residual = y_test - y_pred_rd

ax[1,0].hist(profit_residual, bins=20)
ax[1,0].axvline(0, color='red', linestyle='--')
ax[1,0].set_title("Profit Error Analysis")
ax[1,0].set_xlabel("Error")
ax[1,0].grid()


# =========================
# 4. Actual vs Predicted Profit
# =========================
ax[1,1].scatter(y_test, y_pred_rd, color="orange")

ax[1,1].plot([y_test.min(), y_test.max()],
             [y_test.min(), y_test.max()],
             'g--')

ax[1,1].set_title("Actual vs Predicted Profit")
ax[1,1].set_xlabel("Actual Profit")
ax[1,1].set_ylabel("Predicted Profit")
ax[1,1].grid()


plt.tight_layout()
plt.show()