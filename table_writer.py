import numpy as numpy
import pandas as pd


df = pd.read_csv("June-General-Ranking.csv")

headers = list(df.columns)

f = open("HTNLRankingTable.txt", "w")
f.write("<table>\n")

f.write("<tr>\n")
for val in headers:
    f.write("<th>" + str(val) + "</th>")
f.write("\n</tr>")

for i in range(len(df)):
    f.write("\n<tr>\n")
    values = list(df.loc[i])
    for val in values:
        f.write("<td>" + str(val) + "</td>")
    f.write("\n</tr>")

f.write("\n</table>")
f.close()