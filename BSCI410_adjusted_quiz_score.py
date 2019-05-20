import numpy as np, pandas as pd
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-y','--year',type = str,required = True)
parser.add_argument('-i','--input',type =str, required =True)
parser.add_argument('-o','--output',type =str, required =True)
parser.add_argument('-n','--number_dropped',type = int, required = True)
parser.add_argument('-t','--total_adjusted_score', type = int, required = True)
args = parser.parse_args(sys.argv[1:])


df = pd.read_csv(args.input, sep = ',')
df = df[['Student']+[name for name in df.columns if args.year in name]]
df = df.drop([len(df)-1]) 
df.columns = ['Student']+ ['Quiz_{}'.format(q) for q in range (1,len(df.columns))]
df = df.set_index('Student')

# Step 1: obtain percentage
df_c = df.copy()
for i in range(1,len(df)):
    df_c.iloc[i]= df_c.iloc[i]/df_c.iloc[0]


#Step 2 first sort by percentage (high to low)
#then sort by score possible (low to high), as we prioritize dropping low percentage with high scores since they have greater influence on the final percentage
# then return adjusted percentage multilied by adjusted score 80 
def rank_by_percentage(i,df):
    df_tmp = pd.DataFrame(df.iloc[[0,i]]).T
    df_tmp.columns = ['Total','Student']
    df_tmp = df_tmp.sort_values(by= ['Student','Total'], ascending=[False,True])
    score = (sum([a*b for a,b in zip(list(df_tmp['Total']),\
        list(df_tmp['Student']))][:-args.number_dropped])/sum(list(df_tmp['Total'])[:-args.number_dropped]))\
            *args.total_adjusted_score
    return score

#Step 3 retun a list of scores
scores = [rank_by_percentage(i,df_c) for i in range(1,len(df_c))]
df_c['Adjusted_score']= [args.total_adjusted_score]+scores
pd.DataFrame(df_c['Adjusted_score']).iloc[1:,].to_csv(args.output,sep =',')
print('Adjusted score saved as {}'.format(args.output))