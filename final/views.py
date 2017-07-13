from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from final.models import User, SourceTag, SourceUrl
from final.forms import UserForm
from datetime import datetime

import feedparser

# Create your views here.

from django.http import HttpResponse
def feeds(request):
	context = RequestContext(request)
	
	user = 0
	i = 0
	
	users = User.objects.all()
	context_dict = {'users': users}
	
	if request.method == 'POST':
		user = request.POST['user'].strip()
		
		if user:
			selected_user = User.objects.get(id=user)
			context_dict['selected_user'] = selected_user
	
	feeds = SourceUrl.objects.filter(tag__user__id=user)
	selected_tags = SourceTag.objects.filter(user__id=user)
	
	context_dict['sources'] = feeds
	context_dict['selected_tags'] = selected_tags
	
	entries = []
	for feed in feeds:
		posts = feedparser.parse(feed.url).entries
		for post in posts:
			i=i+1;
			entries.append( {"published_parsed":post["published_parsed"], 
							 "tag":feed.tag.name, 
							 "name":feed.name, 
							 "published":post["published"], 
							 "link":post["link"], 
							 "id":i,
							 "title":post["title"]} )
							 
	entries.sort(key = lambda x: (x["tag"], x["published_parsed"]))
	
	context_dict['entries'] = entries
	
	return render(request, 'final/feeds.html', context_dict, context)

def tags(request, user_id):
	context = RequestContext(request)
	
	selected_user = User.objects.get(id=user_id)
	selected_tags = SourceTag.objects.filter(user__id=user_id)
	
	context_dict = {'selected_user': selected_user}
	context_dict['user_id'] = user_id
	context_dict['selected_tags'] = selected_tags
	
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=selected_user)
		if user_form.is_valid():
			user_form.save(commit=True)
			#user_form.save()
	else:
		user_form = UserForm(instance=selected_user)
		
	context_dict['user_form'] = user_form
	
	return render(request, 'final/tags.html', context_dict, context)