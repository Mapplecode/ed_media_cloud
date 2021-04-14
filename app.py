from script2 import feeds
from flask import Flask,render_template,request,Response
import json
import datetime
from datetime import date
import pprint
app = Flask(__name__)
my_key = 'c803be725711cdedd89941f2ff63a95c07457583f0ed355e50b58fc4d0ca3969'
value1 = 'phone'
value2 = 'India'
media_Id = 'AND media_id:'+(str(1))
no_of_stories = 20
from_date_start =  datetime.date(2019,1,1)
till_date_end =  datetime.date(2020,1,1)


@app.route('/')
def hello_world():
    return 'Hello'
@app.route('/get_data',methods = ['GET','POST'])
def get_data():
    param = ''
    if request.method == 'GET':
        param = request.args
    if request.method == 'POST':
        param = request.form
    try:
        to_ = param.get('to')
        from_ = param.get('from')
        key1 = param.get('key1')
        key2 = param.get('key2')
        count = param.get('key2')
        response_type =param.get('response_type')

        print(to_,from_)
        if count == '' or count == None:
            try:
                count = int(count)
            except:
                count = no_of_stories
        else:
            count = no_of_stories
        if to_ == '' or to_ == None:
            to_ = datetime.datetime.now().date()
        else:
            to_ = datetime.datetime.strptime(to_,'%Y-%m-%d')

        if from_ == '' or from_ == None:
            from_ = date(date.today().year, 1, 1)
        else:
            from_ = datetime.datetime.strptime(from_,'%Y-%m-%d')
        stories = feeds(my_key,key1,key2,media_Id,count,from_,to_)
        # return render_template('index.html',context=json.dump(stories))
        url_list = []
        for i in stories:
            print(i['url'])
            if 'Rss' in i['url'] or 'rss' in i['url'] or 'RSS' in i['url'] :
                url_list.append(i['url'])
        # url_string = ''.join([str(n+'\n') for n in url_list])
        # print(Response(url_string, mimetype='text/xml'))
        # return Response(url_string, mimetype='text/xml')
        # return url_string
        if response_type == 'json':
            return json.dumps({'data':url_list})
        else:
            return render_template('index.html', context=url_list,key1=key1,key2=key2,
                                   to_=str(to_)[0:10],from_=str(from_)[0:10])
    except:
        return render_template('index.html')