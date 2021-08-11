import logging
import os

from slack_bolt import App
from eats.settings import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET
from bot.models import Order
logger = logging.getLogger(__name__)

# Initialise app with your bot token and signing secret
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET,
    # disable eagerly verifying the given SLACK_BOT_TOKEN value
    token_verification_enabled=False,
)


# The budget shortcut listens to a shortcut with the callback_id "open_modal"


@app.shortcut("create_order")
def open_modal(ack, shortcut, client):
    # Acknowledge the shortcut request
    ack()
    # Call the views_open method using the built-in WebClient
    client.views_open(
        trigger_id=shortcut["trigger_id"],
        # A simple view payload for a modal
        # view=SLACK_ORDER_BLOCK
        view={
            "type": "modal",
            "submit": {
                "type": "plain_text",
                "text": "Submit",
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel"
            },
            "title": {
                "type": "plain_text",
                "text": "Lunch order"
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": ":wave: Hey!\n\n What are you ordering today?"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Item(s)"
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Price"
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Restuarant"
                    }
                }
            ]
        }
    )

# TODO: santize data


@app.view("")
def handle_view_events(ack, body, logger):
    ack()
    response_data = body
    team_id = response_data['user']['team_id']
    user_id = response_data['user']['id']
    form_values = response_data['view']['state']['values']
    modal_fields = ['item', 'price', 'restaurant']
    modal_values = []
    for v in form_values.values():
        modal_values.append(v['plain_text_input-action']['value'])
    modal_data = zip(modal_fields, modal_values)
    logger.info(response_data)

    create_order(user_id, team_id,
                 modal_values[0], modal_values[1], modal_values[2])


def create_order(slack_user_id, slack_team_id, item, price, restaurant):
    try:
        price = round(float(price), 2)
    except Exception as e:
        logger.info(e)
        price = 0
    try:
        order = Order(user_id=slack_user_id, team_id=slack_team_id,
                      item=item, price=price, restaurant=restaurant)
        order.save()
    except Exception as e:
        logger.info(e)
