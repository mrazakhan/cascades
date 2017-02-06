for fname in yelp_academic_dataset_business.json  yelp_academic_dataset_review.json  yelp_academic_dataset_user.json yelp_academic_dataset_checkin.json   yelp_academic_dataset_tip.json
do
	
	echo $fname
	LANG=C sed -i 's/[\d128-\d255]//g' $fname

done
