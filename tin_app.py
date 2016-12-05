import requests, HTMLParser, boto3, os, time
from pyquery import PyQuery as pq

def tincheck(content):
		d = pq(content)
		arr=[]
		for mytd in d("body > div > table > tr > td"):
			arr.append(pq(mytd).text())

		s3 = boto3.resource('s3')
		for bucket in s3.buckets.all():
		        print(bucket.name)

		str=""
		for i in range(1,len(arr)-2,2) :
			str=str+arr[i]+" : "+arr[i+1]+os.linesep
			i

		keyfile = time.strftime("%H:%M:%S")+'/data.txt'
		s3.Bucket('kartikey').put_object(Key=keyfile, Body=str)

		s31 = boto3.client('s3')

		url = s31.generate_presigned_url(
		    ClientMethod='get_object',
		    Params={
		        'Bucket': 'kartikey',
		        'Key': keyfile
		    }
		)
		return url

def check(tin):
	w=tin
	r = requests.get("http://www.tinxsys.com/TinxsysInternetWeb/dealerControllerServlet?tinNumber="+w+"&searchBy=TIN&backPage=searchByTin_Inter.jsp")

	if (r.content).find('Dealer Not Found for the entered') is -1:
		return r.content
	else :
		return False