#Pritish Chugh
#B19187
#Data science Lab assignment 6
#Part 1 (a)
import pandas as pd
import matplotlib.pyplot as plt
datafile= pd.read_excel ("Covid19IndiaData_30032020.xlsx") 
age=[]
for i in datafile["Age"]:
    age.append(i)
uniqueage=list(set(age))
prob=[]
for i in uniqueage:
    prob.append(age.count(i)/len(age))
Ans=pd.DataFrame({"Age of the person affected": uniqueage, "Prabability of being infected": prob})
print(Ans)
plt.scatter(uniqueage,prob,c="b")
plt.xlabel("Age of the infected person")
plt.ylabel("Probability of person being infected")
plt.xticks(range(1,100,10))
plt.show()
Expectance=0
for i in range(len(uniqueage)):
    Expectance+=uniqueage[i]*prob[i]
print("Expected age of infected person is",Expectance)
var=0
for i in range(len(uniqueage)):
    var+=((uniqueage[i]**2)*prob[i])
Var=var-(Expectance**2)
print("Variance of the PMF is",Var, "and is too high")
print("It is clear that the data points are not close to expected value i.e. the probability is widely ditributed")
#Part1 (b)
data1=datafile[(datafile["StatusCode"]=="Recovered")]["Age"] #ages of people who got recovered
age2=[]
for i in data1:
    age2.append(i)
uniqueage2=list(set(age2))
dic1={}
for i in uniqueage2:
    dic1[i]=age2.count(i)/len(age2)
prob2=list(dic1.values())
uniqueage2=list(dic1.keys())
Ans2=pd.DataFrame({"Age of the person affected": uniqueage2, "Prabability of recovered": prob2})
print(Ans2)
plt.scatter(uniqueage2,prob2,c="b")
plt.xlabel("Age of the infected person")
plt.ylabel("Probability of person being infected but recovered")
plt.xticks(range(1,100,10))
plt.show()
Expectance2=0
for i in range(len(uniqueage2)):
    Expectance2+=uniqueage2[i]*prob2[i]
print("Expected age of infected person that was recovered is",Expectance2)
var2=0
for i in range(len(uniqueage2)):
    var2+=((uniqueage2[i]**2)*prob2[i])
Var2=var2-(Expectance2**2)
print("Variance is",Var2)

data2=datafile[(datafile["StatusCode"]=="Dead")]["Age"] #ages of people who died
age3=[]
for i in data2:
    age3.append(i)
uniqueage3=list(set(age3))
dic2={}
for i in uniqueage3:
    dic2[i]=age3.count(i)/len(age3)
prob3=list(dic2.values())
uniqueage3=list(dic2.keys())
Ans3=pd.DataFrame({"Age of the person affected": uniqueage3, "Prabability of dead": prob3})
print(Ans3)
plt.scatter(uniqueage3,prob3,c="b")
plt.xlabel("Age of the infected person")
plt.ylabel("Probability of person being infected and died")
plt.xticks(range(1,100,10))
plt.show()
Expectance3=0
for i in range(len(uniqueage3)):
    Expectance3+=uniqueage3[i]*prob3[i]
print("Expected age of infected person that was recovered is",Expectance2)
var3=0
for i in range(len(uniqueage3)):
    var3+=((uniqueage3[i]**2)*prob3[i])
Var3=var3-(Expectance3**2)
print("Variance is",Var3)
print("No, the expectations are not the same as case(1)")

print("People of age 38-40 have more probability of recovering from Corona virus and people of age 65-70 have more probability of dieing from corona")


# Part 1 (c)

data3=datafile[(datafile["GenderCode0F1M"]==0)]["Age"] 
age4=[]
for i in data3:
    age4.append(i)
uniqueage4=list(set(age4))
dic3={}
for i in uniqueage4:
    dic3[i]=age4.count(i)/len(age4)
prob4=list(dic3.values())
uniqueage4=list(dic3.keys())
Ans4=pd.DataFrame({"Age of the female affected": uniqueage4, "Prabability of Infected given that Female": prob4})
print(Ans4)
plt.scatter(uniqueage4,prob4,c="b")
plt.xlabel("Age of the infected female")
plt.ylabel("Probability of people being infected given female")
plt.xticks(range(1,100,10))
plt.show()
Expectance4=0
for i in range(len(uniqueage4)):
    Expectance4+=uniqueage4[i]*prob4[i]
print("Expected age of infected person given female",Expectance4)
var4=0
for i in range(len(uniqueage4)):
    var4+=((uniqueage4[i]**2)*prob4[i])
Var4=var4-(Expectance4**2)
print("Variance is",Var4)


data4=datafile[(datafile["GenderCode0F1M"]==1)]["Age"] 
age5=[]
for i in data4:
    age5.append(i)
uniqueage5=list(set(age5))
dic4={}
for i in uniqueage5:
    dic4[i]=age5.count(i)/len(age5)
prob5=list(dic4.values())
uniqueage5=list(dic4.keys())
Ans5=pd.DataFrame({"Age of the male affected": uniqueage5, "Prabability of Infected given that Male": prob5})
print(Ans5)
plt.scatter(uniqueage5,prob5,c="b")
plt.xlabel("Age of the infected male")
plt.ylabel("Probability of people being infected given male ")
plt.xticks(range(1,100,10))
plt.show()
Expectance5=0
for i in range(len(uniqueage5)):
    Expectance5+=uniqueage5[i]*prob5[i]
print("Expected age of infected person given male",Expectance5)
var5=0
for i in range(len(uniqueage5)):
    var5+=((uniqueage5[i]**2)*prob5[i])
Var5=var5-(Expectance5**2)
print("Variance is",Var5)
print("expected age in male and female is almost the same approximately 39 \n")
print("No the PMFs are not identically distributed. In male the infected people are more in 20-60 age group while in female no. of infected are almost equally distributed")

print("\n The differnce is because mostly females remain in households and hence are less exposed to the virus")



# Part 2 
import datetime
datafile2=pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx",header= 1, sheet_name= "TableS1")
  #(b)
# NON WUHAN RESIDENTS
Incubation2=[]
listnw2=[]
data5= datafile2[(datafile2["ExposureType"]!="Lives-works-studies in Wuhan")]
Expl2= []
Expr2= []

onset2= []

for i in data5["ExposureL"]:
    Expl2.append(i)
for i in data5["Onset"]:
    onset2.append(i)
for i in data5["ExposureR"]:
    Expr2.append(i)
# Acc. to the word file in the link we consider that in those cases, where onset data is not present, ExposureR+1day is used 
for i in range(len(onset2)):
    if str(onset2[i])=="NaT":
        onset2[i]= Expr2[i]+ datetime.timedelta(days=1)
        
for i in range(0,len(Expl2)):
    listnw2.append((onset2[i]-Expl2[i]))

for i in range(len(listnw2)):
    listnw2[i]= str(listnw2[i])
    listnw2[i]= listnw2[i][:2]
for i in range(len(listnw2)):
    if listnw2[i]!="Na":
       if int(listnw2[i])>0:
           Incubation2.append(int(listnw2[i]))
        
unique1= list(set(Incubation2))


dic1= {}
for i in unique1:
    dic1[i]= Incubation2.count(i)/(len(Incubation2))
prob1= list(dic1.values())
unique1=list(dic1.keys())
result1= pd.DataFrame({"No. of days in Incubation Period": unique1, "PMF of the given Incubation Period for Non WR": prob1})

dic2= {}  # To calculate the count
for i in unique1:
    dic2[i]= Incubation2.count(i)

Mean1= 0
for i in dic1:
    Mean1+=(i*dic1[i])


variance1= 0
for i in dic1:
    variance1=(i*i*dic1[i])
Variance1=variance1-(Mean1**2)    
print(Mean1,Variance1)


# WUHAN RESIDENTS
Incubation1=[]
listw=[]
data6= datafile2[(datafile2["ExposureType"]=="Lives-works-studies in Wuhan")]
Expl1= []
onset1=[]
for i in data6["ExposureL"]:
    Expl1.append(i)
for i in data6["Onset"]:
    onset1.append(i)
for i in range(len(Expl1)):
    if str(Expl1[i])=="NaT":
        Expl1[i]= pd.Timestamp(datetime.date(2019,12,1))
# AS per the word file in the link exposure L Date has been set to 1/12/2019 for missing data 
for i in range(0,len(Expl1)):
    for j in range(0,len(onset1)):
        if i==j:
                listw.append((onset1[i]-Expl1[i]))


for i in range(len(listw)):
    listw[i]= str(listw[i])
    listw[i]= listw[i][:2]
for i in range(len(listw)):
    if listw[i]!="Na":
       if int(listw[i])>0:
           Incubation1.append(int(listw[i]))
        
unique2= list(set(Incubation1))
unique2.sort()
dic3= {}
for i in unique2:
    dic3[i]= Incubation1.count(i)

#     Both WUHAN's and NON WUHAN's

for i in dic3:
    if i in dic2:
        dic2[i]+=dic3[i]
    else:
        dic2[i]= dic3[i]
length= len(Incubation2)+ len(Incubation1)
for i in dic2:
    dic2[i]= dic2[i]/length
    
x=  list(dic2.keys())
x.sort()
dic= {}
for i in x:
    dic[i]= dic2[i]
X= list(dic.keys())
Y= list(dic.values())


result= pd.DataFrame({"No. of days in Incubation Period":X, "PMF of the given Incubation Period":Y})
print(result)
plt.scatter(X, Y, c= "b")
plt.xlabel("No. of days in Incubation Period")
plt.ylabel("PMF for given Incubation Period")
plt.show()

Mean= 0
for i in dic:
    Mean+=(i*dic[i])
print("Expected value of Incubation Period is ", Mean, "days")

variance= 0
for i in dic:
    variance=((i**2)*dic[i])
Variance=variance-(Mean**2)
print("Variance is", Variance)   

print(result1)
plt.scatter(unique1, prob1, c= "b")
plt.xlabel("No. of days in Incubation Period")
plt.ylabel("PMF of the given Incubation Period for Non WAHAN RESIDENTS")
plt.xticks(range(1,40,2))
plt.show()
print("Expected Incubation Period in case of Non WAHAN RESIDENTS is", Mean1, "days")
print("Variance is", Variance1)

print("Expected Incubation Period is quite different in the two cases.")



#Part 2 (c)

import pandas as pd
import matplotlib.pyplot as plt
datafile= pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx",header= 1, sheet_name= "TableS2")
data1= datafile["Onset"]
Onsetl= []
for i in data1:
    Onsetl.append(i)
data2= datafile["Hospitalization/Isolation"]
Hosp= []
for i in data2:
    Hosp.append(i)
listdif1= []
for i in range(0,len(Onsetl)):
    listdif1.append((Onsetl[i]-Hosp[i]))
for i in range(len(listdif1)):
    listdif1[i]= str(listdif1[i])
    listdif1[i]= listdif1[i][:2]
HOlist= []
for i in range(len(listdif1)):
    if listdif1[i]!="Na":
        HOlist.append(abs(int(listdif1[i])))
HOunique= list(set(HOlist))
HOunique.sort()
dic1= {}
for i in HOunique:
    dic1[i]= (HOlist.count(i))/(len(HOlist))
prob= list(dic1.values())    
Ans= pd.DataFrame({"Time from Onset to Hospitalization (in days)": HOunique, "PMF for period": prob})
print("Data For Dead Patients")  
print(Ans)
plt.scatter(HOunique, prob, c= "b")
plt.xlabel("Time from Onset to Hospitalization (in days)")
plt.xticks(range(0,11,1))
plt.ylabel("PMF for period")
plt.show()

Deathl= []
data3= datafile["Death"]
for i in data3:
    Deathl.append(i)
listdif2= []
for i in range(0,len(Onsetl)):
    listdif2.append((Onsetl[i]-Deathl[i]))
for i in range(len(listdif2)):
    listdif2[i]= str(listdif2[i])
    listdif2[i]= listdif2[i][:3]
XOlist= []
for i in range(len(listdif2)):
    if listdif2[i]!="NaT":
        XOlist.append(abs(int(listdif2[i])))
XOunique= list(set(XOlist))
XOunique.sort()       
dic2= {}
for i in XOunique:
    dic2[i]= (XOlist.count(i))/(len(XOlist))
prob2= list(dic2.values())    
Ans2= pd.DataFrame({"Time between Onset to Death (in days)": XOunique, "PMF for period": prob2})
print(Ans2)
plt.scatter(XOunique, prob2, c= "b")
plt.xlabel("Time between Onset to Death (in days)")
plt.xticks(range(0,50,2))
plt.ylabel("PMF for period")
plt.show()

listdif3= []
for i in range(0,len(Hosp)):
    listdif3.append((Hosp[i]-Deathl[i]))
for i in range(len(listdif3)):
    listdif3[i]= str(listdif3[i])
    listdif3[i]= listdif3[i][:3]
XHlist= []
for i in range(len(listdif3)):
    if listdif3[i]!="NaT":
        XHlist.append(abs(int(listdif3[i])))
XHunique= list(set(XHlist))
XHunique.sort()       
dic3= {}
for i in XHunique:
    dic3[i]= (XHlist.count(i))/(len(XHlist))
prob3= list(dic3.values())    
Ans3= pd.DataFrame({"Time from Hospitalization to Death (in days)": XHunique, "PMF for period": prob3})
print(Ans3)
plt.scatter(XHunique, prob3, c= "b")
plt.xlabel("Time for Hospitalization to Death (in days)")
plt.xticks(range(0,26,2))
plt.ylabel("PMF for period")
plt.show()
print("There is no similarity in the distribution in the three cases")
print("By looking at HO plot, we see that large number of patients were hospitalized/isolated after more than 3-4 days")
print("By looking at XH plot, we see that maximum number of isolated patients died within 5- 15 days")
print("By looking at XO plot, we see that maximum patients suffering died within 10-20 days after observation of corona symptoms.")



datafile2= pd.read_excel("linton_supp_tableS1_S2_8Feb2020.xlsx",header= 1, sheet_name= "TableS1")
data5= datafile2["Onset"]
data6= datafile2["DateHospitalizedIsolated"]
onset= []
isolated= []
for i in data5:
    onset.append(i)
for i in data6:
    isolated.append(i)
listdif4= []
for i in range(0,len(onset)):
    listdif4.append((onset[i]-isolated[i]))
for i in range(len(listdif4)):
    listdif4[i]= str(listdif4[i])
    listdif4[i]= listdif4[i][:3]
for i in range(len(listdif4)):
    if listdif4[i][2]=="d":
        listdif4[i]= listdif4[i][:2]
XHlistsur= []
for i in range(len(listdif4)):
    if listdif4[i]!="NaT":
        XHlistsur.append(abs(int(listdif4[i])))
XHuniquesur= list(set(XHlistsur))
XHuniquesur.sort()       
dic4= {}
for i in XHuniquesur:
    dic4[i]= (XHlistsur.count(i))/(len(XHlistsur))
prob4= list(dic4.values()) 
print("Data For Surviving Patients")   
Ans4= pd.DataFrame({"Time onset to hospitalization (in days)": XHuniquesur, "PMF for period": prob4})
print(Ans4)
plt.scatter(XHuniquesur, prob4, c= "b")
plt.xlabel("Time for onset to hospitalization (in days) (in case of surviving patients)")
plt.xticks(range(0,26,2))
plt.ylabel("PMF for period")
plt.show()

print("On comparing the HO plots for the two, surviving and death patients, we see that the ones who survied are those who isolated them early (3-4 days) \n while those who isolated them late died (i.e. more probability)  ")






