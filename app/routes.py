from flask import Blueprint
from twilio.twiml.messaging_response import MessagingResponse
from app.controllers import process_message

whatsapp_bp = Blueprint("whatsapp", __name__)

@whatsapp_bp.route("/whatsapp", methods=["POST"])
def whatsapp():
    resp = MessagingResponse()
    resp.message(process_message())
    return str(resp)

@whatsapp_bp.route("/status", methods=["GET"])
def status():
    return "🤖 Bot !"
