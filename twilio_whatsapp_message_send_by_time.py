from twilio.rest import Client
import pandas as pd

from datetime import datetime, timedelta
# Twilio credentials
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

twilio_phone_number = ""

# Read Excel file
excel_file_path = "Book2.xlsx"
df = pd.read_excel(excel_file_path)

# Iterate through rows
for index, row in df.iterrows():
    phone_number = str(row['Phone'])  # Adjust column name
    date_format = "%Y-%m-%d %H:%M:%S"
    current_timee=datetime.strptime(str(row['classtime']), date_format)
    #current_timee=str(row['classtime'])
    five_minutes_ago = current_timee - timedelta(minutes=2)
    message = "*Remainder:* please reach the class @ "+ str(five_minutes_ago.strftime("%Y-%m-%d %H:%M:%S"))  # Adjust column name
    #send_time = datetime.strptime(str(row['sendtime']), "%H:%M")  # Adjust column name
    send_timee=five_minutes_ago.strftime("%Y-%m-%d %H:%M:%S")
    send_time=datetime.strptime(str(send_timee), date_format)
    
    print(send_time.time())
    # Check if the current time is before the specified time
    current_time = datetime.now().time()
    print(current_time)
    if current_time < send_time.time():
        # Send WhatsApp message
        message = client.api.account.messages.create(
            body=message,
            from_='whatsapp:' + twilio_phone_number,
            to='whatsapp:' +'+91'+phone_number
        )
        print(f"Message sent to {phone_number} with SID: {message.sid}")
    else:
        print(f"Skipped sending to {phone_number} as it's past the specified time.")
