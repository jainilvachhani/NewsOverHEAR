from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
import urllib2
from bs4 import BeautifulSoup
from hear1.models import Subscribe
from django.views.generic import TemplateView;
from django.conf import settings

#email lib
from django.core.mail import send_mail
import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import base64


def res(a):
	a = a.replace('\'','')
	a = a.replace('"','')
	return a

class AboutView(View):
	def get(self, request, *args, **kwargs):
		return render(request,'about.html',)

class TestView(View):
	def get(self, request, *args, **kwargs):
		return render(request,'test.html',)

class ContactView(View):
	def get(self, request, *args, **kwargs):
		return render(request,'contact.html',)

class HomeView(View):
	def get(self, request, *args, **kwargs):

		print "yyyyyyy : ",self.kwargs.get('slug')

		news_title = []
		news_disp = []
		img = []
		timestamp = []
		link = []
		speakable = []

		context = {
		'news_list' : []

		}
		print "*******************************************88888888"

		wiki = "https://www.inshorts.com/en/read/"+self.kwargs.get('slug','')
		print wiki
		page = urllib2.urlopen(wiki)
		soup = BeautifulSoup(page,"html5lib")
		titles = soup.findAll("span", {"itemprop": "headline"})
		timestamps = soup.findAll("div", {"class": "news-card-author-time news-card-author-time-in-title"})
		cont = soup.findAll("div", {"itemprop": "articleBody"})
		imgs = soup.findAll("div", {"class": "news-card-image"})
		links = soup.findAll("div", {"class": "read-more"})

		for i in titles:
			news_title.append(i.text)

		for i in cont:
			news_disp.append(i.text)
			speakable.append(res(i.text))

		for i in imgs:
			img.append(i['style'][23:-17])

		for i in timestamps:
			timestamp.append(i.text.split('/')[1][8:])

		for i in links:
			link.append(i.a['href'])
		
		context['news_list'] = zip(news_title,timestamp,news_disp,speakable,img,link)

		return render(request,'index.html',context)

	def post(self, request, *args, **kwargs):

		if 's' in request.POST:
			path = "/hear1/index/"+request.POST.get('s')
			return HttpResponseRedirect(path)

		else:
			print request.POST.get('email')
			subsci = Subscribe(email_id = request.POST.get('email'))
			subsci.save()
			return HttpResponseRedirect('/hear1/index/')


class EmailView(View):

	def get(self, request, *args, **kwargs):
		emails=[]

		temp = Subscribe.objects.all()
		for i in temp:
			emails.append(i.email_id)

		print "------------",emails
		sender = settings.EMAIL_HOST_USER
		receiver = emails

		msg = MIMEMultipart()
		msg['from'] = sender;
		msg['Subject'] = "News_overHEAR News"


		wiki = "https://www.inshorts.com/en/read/"+self.kwargs.get('slug','')
		page = urllib2.urlopen(wiki)
		soup = BeautifulSoup(page,"html5lib")
		titles = soup.findAll("span", {"itemprop": "headline"})
		cont = soup.findAll("div", {"itemprop": "articleBody"})
		
		body = ""

		i=0
		while(i<=5):
			body = body+"( "+str(i+1)+" )  "+titles[i].text+"\n"
			body = body+"-->"+cont[i].text+"\n\n"
			
			i+=1


		print body
		msg.attach(MIMEText(body, 'plain'))

		text = msg.as_string()

		try:
			s=smtplib.SMTP()
			s.connect("smtp.gmail.com",587)
			s.ehlo()
			s.starttls()
			s.ehlo()
			s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
			s.sendmail(sender, receiver, text)

		except Exception, e:
			print e

		return HttpResponseRedirect('/hear1/index/')




class TextView(View):
	def get(self, request, *args, **kwargs):

		print "yyyyyyyyyyyyyyy : ",self.kwargs.get('slug')

		news_title = []
		news_disp = []
		img = []
		timestamp = []
		link = []
		speakable = []

		context = {
		'news_list' : []

		}
		print "*******************************************88888888"

		wiki = "https://www.inshorts.com/en/read/"+self.kwargs.get('slug','')
		print wiki
		page = urllib2.urlopen(wiki)
		soup = BeautifulSoup(page,"html5lib")
		titles = soup.findAll("span", {"itemprop": "headline"})
		timestamps = soup.findAll("div", {"class": "news-card-author-time news-card-author-time-in-title"})
		cont = soup.findAll("div", {"itemprop": "articleBody"})
		imgs = soup.findAll("div", {"class": "news-card-image"})
		links = soup.findAll("div", {"class": "read-more"})

		for i in titles:
			news_title.append(i.text)

		for i in cont:
			news_disp.append(i.text)
			speakable.append(res(i.text))

		for i in imgs:
			img.append(i['style'][23:-17])

		for i in timestamps:
			timestamp.append(i.text.split('/')[1][8:])

		for i in links:
			link.append(i.a['href'])

		# i=0
		# while(i<=5):
		# 	news_title.append(titles[i].text)
		# 	news_disp.append(cont[i].text)
		# 	speakable.append(res(cont[i].text))
		# 	img.append(imgs[i]['style'][23:-17])
		# 	timestamp.append(timestamps[i].text.split('/')[1][8:])
		# 	link.append(links[i].a['href'])
		# 	i+=1
		
		context['news_list'] = zip(news_title,timestamp,news_disp,speakable,img,link)

		# for ih in imgs:
		# 	print ih

		print "*******************************************8"


		return render(request,'index.html',context)

	def post(self, request, *args, **kwargs):
		print request.POST.get('email')

		subsci = Subscribe(email_id = request.POST.get('email'))
		subsci.save()
		return HttpResponseRedirect('/hear1/index/')
