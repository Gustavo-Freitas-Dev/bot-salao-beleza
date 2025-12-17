from flask import request
from app.messages import ask_service, menu, services_and_prices, business_hours, salon_address, contact_attendant

def process_message():
    msg = request.form.get("Body", "").strip()

    print(f"Mensagem recebida: '{msg}'")

    if msg.startswith("1"):
        return ask_service()

    elif msg.startswith("2"):
        return services_and_prices()

    elif msg.startswith("3"):
        return business_hours()

    elif msg.startswith("4"):
        return salon_address()
    
    elif msg.startswith("5"):
        return contact_attendant()

    else:
        return menu()
