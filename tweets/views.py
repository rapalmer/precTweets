from django.shortcuts import render
from django.http import HttpResponse
from twython import Twython
from django.conf import settings

twitter = Twython(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, settings.TWITTER_OAUTH_TOKEN, settings.TWITTER_OAUTH_TOKEN_SECRET)
timeline = twitter.get_user_timeline(screen_name='realDonaldTrump')
latest_tweet1 = timeline[0]
latest_tweet2 = timeline[1]
latest_tweet3 = timeline[2]
latest_tweet4 = timeline[3] 
latest_tweet5 = timeline[4]
latest_tweet6 = timeline[5]
latest_tweet7 = timeline[6]
latest_tweet8 = timeline[7]
latest_tweet9 = timeline[8]
latest_tweet10 = timeline[9]
html = '<p style="color:grey;\
				  font-size:20;\
				  line-height: 1.8;\
				">\
		"%s" <br> \
		"%s" <br> \
		"%s" <br> \
		"%s" <br> \
		"%s" <br> \
		"%s" <br> \
		"%s" <br> \
		"%s" <br> \
		"%s" <br> \
		"%s" </p>' \
		% (latest_tweet1['text'], latest_tweet2['text'], latest_tweet3['text'],latest_tweet4['text'],latest_tweet5['text'],latest_tweet6['text'],latest_tweet7['text'],latest_tweet8['text'],latest_tweet9['text'],latest_tweet10['text'])


# Create your views here.
def index(request):
	print(html)
	return HttpResponse(html)