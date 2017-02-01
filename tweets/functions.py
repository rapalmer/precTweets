from django.conf import settings
from django.core.cache import cache
from twython import Twython, TwythonError

def latest_tweet(request):
	latest_tweet = cache.get('latest_tweet')

	if not latest_tweet:
		twitter = Twython(settings.TWITTER_CONSUMER_KEY,
						settings.TWITTER_CONSUMER_SECRET,
						settings.TWITTER_OAUTH_TOKEN,
						settings.TWITTER_OAUTH_TOKEN_SECRET)
		try:
			user_timeline = twitter.get_user_timeline(screen_name='realDonaldTrump')
		except TwythonError as e:
			return {"latest_tweet": e}

		latest_tweet = user_timeline[0]
		cache.set('latest_tweet', latest_tweet, settings.TWITTER_TIMEOUT)
	return {'latest_tweet': latest_tweet}