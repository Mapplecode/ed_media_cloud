import mediacloud.api, json, datetime

# ID KEYWORDS AND KEY TO BE ADDED HERE

my_key = 'c803be725711cdedd89941f2ff63a95c07457583f0ed355e50b58fc4d0ca3969'
value1 = 'SOAT'
value2 = 'Colombia'
media_Id = 'AND media_id:'+(str(1))
no_of_stories = 10

from_date_start =  datetime.date(2020,1,1)
till_date_end =  datetime.date(2021,1,28)
###################


def feeds(my_key,value1,value2,media_Id,no_of_stories,from_date_start,till_date_end):
    mc = mediacloud.api.MediaCloud(my_key)
    fetch_size = 500
    stories = []
    last_processed_stories_id = 0
    while len(stories) < no_of_stories:
        fetched_stories = mc.storyList(value1+' AND "'+value2+'" ',
                                       solr_filter=mc.dates_as_query_clause(from_date_start,till_date_end),
                                       last_processed_stories_id=last_processed_stories_id, rows= fetch_size)
        stories.extend(fetched_stories)
        if len( fetched_stories) < fetch_size:
            break
        last_processed_stories_id = stories[-1]['processed_stories_id']


    return stories



stories = feeds(my_key,value1,value2,media_Id,no_of_stories,from_date_start,till_date_end)
# print(type(stories))




file1 = open(str(value1)+'_'+str(value2)+'_feeds.txt','w')
for i in stories:
    print (i['url'])
    try:
        file1.write(i['url'])
        file1.write(' \n ')
        # print(str(key) + " is  --- -- " + str(value))
    except:
        pass

    file1.write("____________________")
    file1.write('\n  ')
    file1.write('\n  ')


#
# file1.close()
