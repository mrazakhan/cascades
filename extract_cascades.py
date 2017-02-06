import pandas as pd
import numpy as np
import sys

cities_list=['karlsruhe','edinburgh','montreal','pittsburgh','charlotte','madison','champaign','cleveland','waterloo','vegas', 'pheonix']

def extract_graph():
    for city in cities_list:
        print 'extract_graph', city
        df1=pd.read_csv('flattened_business_review_user_'+city+'.csv',delimiter=';')
        df1['type']='review'
        df2=pd.read_csv('flattened_business_tip_user_'+city+'.csv',delimiter=';')
        df1['type']='tip'
        df=df1.append(df2)
        dfc=pd.DataFrame(df.groupby(['business_id']).apply(lambda x:np.intersect1d(x['user_id'].values, x['friends'].values)))
        dfc.columns=['common']
        dfc['len_common']=dfc['common'].apply(lambda x:len(x))
        df_merged=pd.merge(dfc.reset_index(), df, on='business_id')
        df_merged=df_merged[df_merged.len_common>=1]
        print df_merged.shape
        # res = pd.DataFrame(df_merged.set_index(['business_id','friends','review_id','user_id'])['common'].apply(
        #         pd.Series).stack())
        res=df_merged
        res['common_friends']=res.friends
        #res=res.reset_index()
        res.drop('common',axis=1, inplace=True)
        res=res[res.common_friends==res.friends]
        print res.shape
        res[[each for each in res.columns if 'level' not in each and each!='friends']].to_csv('graph_review_tip_'+city+'.csv')


def extract_monthly_reviews():
    for city in cities_list:
        print 'extract_monthly_reviews', city
        df1=pd.read_csv('business_review_user_{}.csv'.format(city))[['business_id','user_id','review_id','date']]
        df1['type']='review'
        df2=pd.read_csv('business_tip_user_{}.csv'.format(city))[['business_id','user_id','review_id','date']]
        df2['type']='tip'
        df=df1.append(df2)

        filters=['2015-01-01','2015-02-01','2015-03-01','2015-04-01','2015-05-01','2015-06-01','2015-07-01','2015-08-01',
                '2015-09-01','2015-10-01','2015-11-01','2015-12-01']
        # df.set_index('date',inplace=True)
        for i in range(12):
            if i==0:
                df_current=df[df.date<filters[0]]
            else:
                df_current=df[(df.date<filters[i])&((df.date>filters[i-1]))]
            #df_current=df.ix[cfilter]
            export_name='{}_{}_review_tip.csv'.format(city,filters[i])
#             print export_name,df_current.shape
            df_current.to_csv(export_name)



if __name__=='__main__':

    extract_graph()
    extract_monthly_reviews()
