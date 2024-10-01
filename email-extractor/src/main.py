from email_parser import extract_email_data
from utils import clean_email_text, validate_email_address

def main():
    email_text = """
    From: john.doe@example.com
    To: jane.doe@example.com
    Subject: Meeting reminder
    Date: 2024-09-30

    Hi Jane,
    
    This is just a reminder for the meeting tomorrow at 10 AM. Please let me know if you need anything.

    Best regards,
    John
    """

    cleaned_text = clean_email_text(email_text)
    
    
    extracted_data = extract_email_data(cleaned_text)

    print("Extracted Data: ", extracted_data)

if __name__ == "__main__":
    main()
