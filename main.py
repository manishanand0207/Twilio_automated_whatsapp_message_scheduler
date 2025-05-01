from twilio.rest import Client
from datetime import datetime, timedelta
import time

account_sid = "ACee5ed569f7d67a92558ae68732d276bb"
auth_token = "96def0b8bc4d7a87be08423a52d87274"

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message=client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message send successfully! Message SID {message.sid}")
    except Exception as e:
        print("An error occurred")

name = input("Enter the Recipient number =")
recipient_number = input("Enter the Recipient number with country code =")
message_body = input(f"Enter the message you want to send {name}: ")

date_str = input("Enter the date when you want to send the message(YYYY-MM-DD)")
time_str = input("Enter the time when you want to send the message(HH:MM)")

schedule_datetime = datetime.strptime(f"{date_str} {time_str}" , "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("This specified time is in the past, please enter a future date and time")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}")


time.sleep(delay_seconds)

send_whatsapp_message(recipient_number, message_body)








