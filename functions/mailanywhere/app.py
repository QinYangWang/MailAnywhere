import logging

from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

# process_before_response must be True when running on FaaS
app = App(process_before_response=True)


@app.event("app_mention")
def handle_app_mentions(body, say, logger):
    logger.info(body)
    say("What's up?")


@app.command("/SendEmail")
def respond_to_slack_within_3_seconds(ack):
    ack("Thanks!")

SlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)

def handler(event, context):
    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)