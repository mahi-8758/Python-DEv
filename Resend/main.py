import resend
import api

# --- CONFIGURATION ---
# PASTE YOUR API KEY HERE DIRECTLY
resend.api_key = api.api_key
FROM_EMAIL = "supportfrommahi@sending.studio" # Or your verified sender
# ---------------------

print("--- Resend Email Sender ---")

# 1. Get inputs from the user
recipient_email = input("Enter recipient email: ")
email_subject = input("Enter email subject: ")
email_html = input("Enter message (HTML is okay): ")

params = {
    "from": FROM_EMAIL,
    "to": [recipient_email],
    "subject": email_subject,
    "html": email_html,
}

try:
    print(f"\nSending to {recipient_email}...")
    response = resend.Emails.send(params)
    print(f"Success! Email sent with ID: {response['id']}")
except Exception as e:
    print(f"\nError sending email: {e}")