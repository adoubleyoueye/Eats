from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.urls import path

from slack_bolt.adapter.django import SlackRequestHandler
from bot.slack_listeners import app

handler = SlackRequestHandler(app=app)


@csrf_exempt
def slack_events_handler(request: HttpRequest):
    return handler.handle(request)


urlpatterns = [
    path("slack/events", slack_events_handler, name="slack_events"),
]
