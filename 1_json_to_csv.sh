#for fname in yelp_academic_dataset_business.json  yelp_academic_dataset_review.json  yelp_academic_dataset_user.json yelp_academic_dataset_checkin.json   yelp_academic_dataset_tip.json
for fname in yelp_academic_dataset_tip.json3
do
	echo $fname
	python json_to_csv.py $fname 

done
