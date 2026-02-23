from service import email_service
from fastapi import APIRouter, HTTPException
from models.notification import EmailSentRequest
router = APIRouter()

@router.post("/send", summary="Send email", description="Send an email to the specified recipient")
def send_email(emailSendRequest: EmailSentRequest):
    print(f"Received email send request: {emailSendRequest}")
    try:
        email_service.send_email(emailSendRequest.to, emailSendRequest.subject, emailSendRequest.message)
        return {"message": "Email sent successfully"}
    except Exception as e:
        print(f"Error sending email: {e}")
        raise HTTPException(status_code=500, detail="Error sending email")