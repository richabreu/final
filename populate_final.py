import os

def populate():
	boxing_sourcetag = add_sourcetag("Boxing")
	golf_sourcetag = add_sourcetag("Golf")
	mlb_sourcetag = add_sourcetag("MLB")
	mma_sourcetag = add_sourcetag("MMA")
	motorsports_sourcetag = add_sourcetag("Motorsports")
	nba_sourcetag = add_sourcetag("NBA")
	nfl_sourcetag = add_sourcetag("NFL")
	nhl_sourcetag = add_sourcetag("NHL")
	soccer_sourcetag = add_sourcetag("Soccer")
	tennis_sourcetag = add_sourcetag("Tennis")
	
	rich_user = add_user("Rich", ())
	kristin_user = add_user("Kristin", ())
	roman_user = add_user("Roman", ())
	
	"""add_userprofile(user=rich_user, tag=boxing_sourcetag)
	add_userprofile(user=rich_user, tag=golf_sourcetag)
	add_userprofile(user=rich_user, tag=mlb_sourcetag)
	add_userprofile(user=rich_user, tag=mma_sourcetag)
	add_userprofile(user=rich_user, tag=motorsports_sourcetag)
	add_userprofile(user=rich_user, tag=nba_sourcetag)
	add_userprofile(user=rich_user, tag=nfl_sourcetag)
	add_userprofile(user=rich_user, tag=nhl_sourcetag)
	add_userprofile(user=rich_user, tag=soccer_sourcetag)
	add_userprofile(user=rich_user, tag=tennis_sourcetag)
	
	add_userprofile(user=roman_user, tag=soccer_sourcetag)"""
	    
	add_sourceurl(tag=golf_sourcetag, 
					name="FOX Sports", 
					url="http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU&tag=golf")
					
	add_sourceurl(tag=mlb_sourcetag, 
					name="FOX Sports", 
					url="http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU&tag=mlb")
					
	add_sourceurl(tag=motorsports_sourcetag, 
					name="FOX Sports", 
					url="http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU&tag=nascar")
					
	add_sourceurl(tag=nba_sourcetag, 
					name="FOX Sports", 
					url="http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU&tag=nba")
					
	add_sourceurl(tag=nfl_sourcetag, 
					name="FOX Sports", 
					url="http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU&tag=nfl")
					
	add_sourceurl(tag=nhl_sourcetag, 
					name="FOX Sports", 
					url="http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU&tag=nhl")
					
	add_sourceurl(tag=soccer_sourcetag, 
					name="FOX Sports", 
					url="http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU&tag=soccer")
					
	add_sourceurl(tag=mma_sourcetag, 
					name="FOX Sports", 
					url="http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU&tag=ufc")
					
	add_sourceurl(tag=soccer_sourcetag, 
					name="Soccer News", 
					url="http://feeds.feedburner.com/soccernewsfeed?format=xml")
					
	add_sourceurl(tag=mlb_sourcetag, 
					name="MLB.com", 
					url="http://mlb.mlb.com/partnerxml/gen/news/rss/mlb.xml")
					
	add_sourceurl(tag=soccer_sourcetag, 
					name="ESPN", 
					url="http://soccernet.espn.com/rss/news")
					
	add_sourceurl(tag=mlb_sourcetag, 
					name="ESPN", 
					url="http://www.espn.com/espn/rss/mlb/news")
					
	add_sourceurl(tag=nba_sourcetag, 
					name="ESPN", 
					url="http://www.espn.com/espn/rss/nba/news")
					
	add_sourceurl(tag=nfl_sourcetag, 
					name="ESPN", 
					url="http://www.espn.com/espn/rss/nfl/news")
					
	add_sourceurl(tag=nhl_sourcetag, 
					name="ESPN", 
					url="http://www.espn.com/espn/rss/nhl/news")
					
	add_sourceurl(tag=motorsports_sourcetag, 
					name="ESPN", 
					url="http://www.espn.com/espn/rss/rpm/news")
					
	add_sourceurl(tag=soccer_sourcetag, 
					name="FIFA", 
					url="http://www.fifa.com/rss/index.xml")
					
	add_sourceurl(tag=nba_sourcetag, 
					name="NBA.com", 
					url="http://www.nba.com/rss/nba_rss.xml")
					
	add_sourceurl(tag=nfl_sourcetag, 
					name="NFL.com", 
					url="http://www.nfl.com/rss/rsslanding?searchString=home")
					
	add_sourceurl(tag=nhl_sourcetag, 
					name="NHL.com", 
					url="http://www.nhl.com/rss/news.xml")
					
	add_sourceurl(tag=nhl_sourcetag, 
					name="Sports Illustrated", 
					url="http://www.si.com/rss/si_hockey.rss")
					
	add_sourceurl(tag=mlb_sourcetag, 
					name="Sports Illustrated", 
					url="http://www.si.com/rss/si_mlb.rss")
					
	add_sourceurl(tag=mma_sourcetag, 
					name="Sports Illustrated", 
					url="http://www.si.com/rss/si_mma.rss")
					
	add_sourceurl(tag=motorsports_sourcetag, 
					name="Sports Illustrated", 
					url="http://www.si.com/rss/si_motorsports.rss")
					
	add_sourceurl(tag=nba_sourcetag, 
					name="Sports Illustrated", 
					url="http://www.si.com/rss/si_nba.rss")
					
	add_sourceurl(tag=nfl_sourcetag, 
					name="Sports Illustrated", 
					url="http://www.si.com/rss/si_nfl.rss")
					
	add_sourceurl(tag=soccer_sourcetag, 
					name="Sports Illustrated", 
					url="http://www.si.com/rss/si_soccer.rss")
					
	add_sourceurl(tag=tennis_sourcetag, 
					name="Sports Illustrated", 
					url="http://www.si.com/rss/si_tennis.rss")
					
	add_sourceurl(tag=boxing_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/box/rss.xml")
					
	add_sourceurl(tag=golf_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/golf/rss.xml")
					
	add_sourceurl(tag=mlb_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/mlb/rss.xml")
					
	add_sourceurl(tag=mma_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/mma/rss.xml")
					
	add_sourceurl(tag=motorsports_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/nascar/rss.xml")
					
	add_sourceurl(tag=nba_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/nba/rss.xml")
					
	add_sourceurl(tag=nfl_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/nfl/rss.xml")
					
	add_sourceurl(tag=nhl_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/nhl/rss.xml")
					
	add_sourceurl(tag=soccer_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/sow/rss.xml")
					
	add_sourceurl(tag=tennis_sourcetag, 
					name="Yahoo Sports", 
					url="https://sports.yahoo.com/ten/rss.xml")

def add_user(name, tags):
	u = User.objects.get_or_create(name=name)[0]
	u.tags.add(*SourceTag.objects.filter(name__in=[tags]))
	return u

def add_sourcetag(name):
    t = SourceTag.objects.get_or_create(name=name)[0]
    return t

def add_sourceurl(tag, name, url):
    u = SourceUrl.objects.get_or_create(tag=tag, name=name, url=url)[0]
    return u

"""def add_userprofile(user, tag):
    p = UserProfile.objects.get_or_create(user=user, tag=tag)[0]
    return p"""

# Start execution here!
if __name__ == '__main__':
    print ("Starting final population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')
    import django
    django.setup()
    from final.models import User, SourceTag, SourceUrl
    populate()
