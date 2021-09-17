from exchangelib import Credentials, Account, DELEGATE, Configuration, Message, Mailbox, FileAttachment, HTMLBody, Body

def sendEmailMessage(userName, passWord, primary_SMTP_Address, subjectTitle, subjectBody, receiverMail):
    try:
        creds = Credentials(
                    username=userName, 
                    password=passWord
                )
        config = Configuration(server='outlook.office365.com', credentials=creds)
        account = Account(
                    primary_smtp_address=primary_SMTP_Address,
                    autodiscover=False, 
                    config=config,
                    access_type=DELEGATE)

        m = Message(
                account=account,
                subject=subjectTitle,
                body= Body(subjectBody), 
                to_recipients=[
                    Mailbox(email_address=receiverMail),
                ])
        m.send()
        return "successlly sent mail"
    except Exception as ex:
        return ex