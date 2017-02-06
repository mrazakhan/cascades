''' split data by cities'''
import pandas as pd
import sys

def split_by_city(business, review, tip, user):
	bus_df=pd.read_csv(business, index_col=0)
	review_df=pd.read_csv(review,index_col=0)
	tip_df=pd.read_csv(tip, index_col=0)
	user_df=pd.read_csv(user, index_col=0)[['user_id','friends']]
	# assign review id
	tip_df['review_id']=tip_df['business_id'].astype(str)+':'+tip_df['user_id'].astype(str)+':'+tip_df['date'].astype(str)

	review_df['text']=review_df['text'].apply(lambda x:str(x).strip().replace(',',''))

	bus_df=bus_df[[each for each in bus_df.columns if 'Unnamed' not in each]]
	review_df=review_df[[each for each in review_df.columns if 'Unnamed' not in each]]
	user_df=user_df[[each for each in user_df.columns if 'Unnamed' not in each]]
	tip_df=tip_df[[each for each in tip_df.columns if 'Unnamed' not in each]]

	print 'bus_df. columns', bus_df.columns
	print 'review_df. columns', review_df.columns
	print 'user_df. columns', user_df.columns
	print 'tip_df. columns', tip_df.columns

	business_review=pd.merge(bus_df, review_df, on='business_id', suffixes=('_business','_review'))
	business_review_user=pd.merge(business_review, user_df, on='user_id')

	
	business_tip=pd.merge(bus_df, tip_df, on='business_id', suffixes=('_business','_tip'))
	business_tip_user=pd.merge(business_tip, user_df, on='user_id')

	dc={'AZ':'pheonix','NV':'vegas','ON':'waterloo','NC':'charlotte','OH':'cleveland','PA':'pittsburgh','QC':'montreal','WI':'madison','EDH':'edinburgh','BW':'karlsruhe','IL':'champaign'}
	cities=dc.values()
	for city in cities:
		tip_city=business_tip_user[business_tip_user.city==city]
		review_city=business_review_user[business_review_user.city==city]
		print city, tip_city.shape, review_city.shape

		#print 'review_city.columns', review_city.columns
		#print 'tip_city.columns', tip_city.columns
		order=['business_id', 'user_id', 'date','review_id', 'friends']
		review_city=review_city.reindex(columns=[order + list(set(list(review_city.columns))-set(order))])
		tip_city=tip_city.reindex(columns=[order + list(set(list(tip_city.columns))-set(order))])
		review_city.to_csv('business_review_user_'+city+'.csv', index=False)
		tip_city.to_csv('business_tip_user_'+city+'.csv', index=False)

if __name__=='__main__':
	if len(sys.argv)<4:
		print 'Required Args : business_filename, review_filename, tip_filename, user_filename'
		sys.exit(-1)
	
	business,review, tip, user=sys.argv[1:]
	split_by_city(business, review, tip, user)
