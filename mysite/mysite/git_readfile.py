from github import Github
import csv
import os
import pandas as pd
import io
github = Github('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')
repository = github.get_user().get_repo('Python_RD_Git')
filename = 'files/download_8.csv'
file = repository.get_contents(filename)
data = file.decoded_content.decode()
nmlist = ['資料日期', '證券代號', '持股分級', '持股數量分級', '人數', '股數', '占集保庫存數比例%']
df = pd.read_csv(io.StringIO(data),names=nmlist)

st_lists=df.values.tolist()
print("st_lists:",st_lists)

for st_list in st_lists:
    print("st_list:",st_list)
    


context={"st_own_lists" : []} 
#my_context={"st_own_list" : []} 

with open("d:\\test\\download_8.csv", "r", newline="") as fr:
    st_own_lists = csv.reader(fr,delimiter=',')  
         
    for st_own_list in st_own_lists :
        context["st_own_lists"].append(st_own_list)
        print(st_own_list)
            