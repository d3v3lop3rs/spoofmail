##Python3
import base64
import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
import urllib.request as urllib
message = Mail(
    from_email='',#enter senders mail
    to_emails='',#enter recievers mail
    subject='',#enter subject of the mail
    html_content=''###enter content of mail in the following way <font>matter</font>
    )

file_path = ''#file path incase you want to send some files
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('application/pdf')#file type here i used application/pdf
attachment.file_name = FileName('File_notice.pdf')#file name to be displayed
attachment.disposition = Disposition('attachment')#disposition notification service was choosen
attachment.content_id = ContentId('Example Content ID')#content id
message.attachment = attachment
try:
    sendgrid_client = SendGridAPIClient('')#here it is the main part ****you should get your sendgrid api key***
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
