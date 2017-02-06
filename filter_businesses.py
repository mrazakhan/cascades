''' Filter Data by cities'''
import pandas as pd
import sys

def filter_business(fname):

	df=pd.read_csv(fname)
	state_to_city={'AZ':'pheonix','NV':'vegas','ON':'waterloo','NC':'charlotte','OH':'cleveland','PA':'pittsburgh','QC':'montreal','WI':'madison','EDH':'edinburgh','BW':'karlsruhe','IL':'champaign'}
	keys=state_to_city.keys()
	df2=df[df.state.apply(lambda x:x in keys)]
	df2['city']=df2['state'].apply(lambda x:state_to_city[x])
	df2.to_csv('yelp_academic_dataset_business_filtered.csv')

if __name__=='__main__':
	if len(sys.argv)<2:
		print 'Input File Required'
		sys.exit(-1)

	fname=sys.argv[1]
	filter_business(fname)
