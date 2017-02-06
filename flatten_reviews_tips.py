''''flatten reviews and tips for the friends list'''
def flatten_reviews_tips():
    cities_list=['karlsruhe','edinburgh','montreal','pittsburgh','charlotte','madison','champaign','cleveland','waterloo','vegas', 'pheonix']
    for ctype in ['review','tip']:
        for city in cities_list:
            lst=['business_id;user_id;date;review_id;friends']
            print city
            with open('business_'+ctype+'_user_'+city+'.csv') as fin:
                fin.next()
                for i,each in enumerate(fin):
                    if each.strip()!='': 
                        business_id, user_id, date,review_id, friends, _=each.split(',',5)
                        friends=friends.strip().replace("[","").replace("]","").replace('"',"")
            #         print 'business_id {} , user_id {} friends {}'.format(business_id, user_id, friends)
                        month='-'.join(x for x in date.split('-')[:2])
                        prefix=';'.join(each for each in [business_id, user_id, month,review_id])
                        for f in friends.split(','):
                            lst.append(prefix+';'+f.strip())

            with open('flattened_business_'+ctype+'_user_'+city+'.csv','w') as fout:
                for each in lst:
                    fout.write(each+'\n')
                    
if __name__=='__main__':
    flatten_reviews_tips()
