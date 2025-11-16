# Resend Email Sender

A simple Python application that sends emails using the Resend email service API.

## Features

- **Email Sending**: Send emails with custom subjects and HTML content
- **User-Friendly Input**: Interactive command-line interface for entering recipient, subject, and message
- **API Integration**: Uses Resend API for reliable email delivery
- **Error Handling**: Catches and displays errors if email sending fails
- **Email ID Confirmation**: Returns the email ID upon successful delivery

## Project Structure

- **`main.py`**: Entry point of the application that handles email sending
- **`api.py`**: Contains the Resend API key configuration

## How It Works

1. API key is loaded from `api.py`
2. User inputs are collected via command-line prompts:
   - Recipient email address
   - Email subject line
   - Email message (supports HTML formatting)
3. Email parameters are prepared with the sender address and recipient details
4. The Resend API sends the email
5. Success or error message is displayed with the email ID (if successful)

## How to Run

```bash
python main.py
```

Follow the prompts to enter:
- Recipient email address
- Email subject
- Message content (HTML supported)

## Example Output

```
--- Resend Email Sender ---
Enter recipient email: user@example.com
Enter email subject: Hello!
Enter message (HTML is okay): <h1>Welcome!</h1><p>This is a test email.</p>

Sending to user@example.com...
Success! Email sent with ID: 12345-67890-abcde
```

## Requirements

- Python 3.x
- Resend API key (set in `api.py`)
- Valid verified sender email