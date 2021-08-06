import re

from transparentemail.services.Emails.email import Email
from transparentemail.services.Emails.editableEmail import EditableEmail
from transparentemail.services.serviceEmail import ServiceEmail


class Www33MailCom(ServiceEmail):
    def get_primary_email(self, email: Email) -> Email:
        return (
            EditableEmail(email)
            .set_local_part(re.sub(".33mail.com", "", email.domain))
            .get_email()
        )

    def is_supported(self, email: Email) -> bool:
        # return bool(re.match(r'.33mail.com', email.domain))
        return bool(".33mail.com" in email.domain)
