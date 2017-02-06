#'''Converts Json data to Csv'''


import sys
import pandas as pd

def _read1(filename):
    lst=[]
    with open(filename) as fin:
        count=0
        for i,each in enumerate(fin):
            print i,  
            if each.strip()!='':
                each=eval(each.strip())
                if type(each)==dict:
                    lst.append(each)
                    count+=1
        df=pd.DataFrame(lst)
        print ' ************ Warning : Still may have to replace \r and quotes in the text through sed *********'
    return df


def readFromJson(filename, sep=','):
    if 'review' not in filename and 'tip' not in filename:
    	data_df = pd.read_json(filename, lines=True,encoding='utf-8')
    else:
        data_df=_read1(filename)
    if 'text' in data_df.columns:
		data_df['text']=data_df['text'].apply(lambda x:x.encode('ascii','ignore').strip().replace(',' ,' '))
    return data_df


if __name__=='__main__':
	if len(sys.argv)<2:
		print 'Pass the Json file as the input argument'
		sys.exit(-1)
	fname=sys.argv[1]
	df=readFromJson(fname)
	df.to_csv(fname.replace('json','csv'),encoding='utf-8')
