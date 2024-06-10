import requests
import pandas as pd

df = pd.read_csv('input.csv',header=None)

output_df = pd.DataFrame()

for index, row in df.iterrows():
    try:
        response = requests.get("http://" + row[0], timeout=5)
        print(f"{row[0]} is reachable")
        output_df=output_df.append({"site":row[0],"status":"Reachable"},ignore_index=True)
    except requests.ConnectionError:
        print(f"Failed to reach {row[0]}")
        output_df=output_df.append({"site":row[0],"status":"Unreachable"},ignore_index=True)


print(output_df)
output_df.to_csv("output.csv",header=False,index=False)

