from dataclasses import dataclass, field
from typing import List

from transparentemail.services import *
from transparentemail.services.Emails.email import Email


@dataclass
class TransparentEmail:
    services: List = field(init=False)

    def __post_init__(self):
        self.services = [GmailCom, YahooCom, OutlookCom, Www33MailCom]

    def get_primary_email(self, email: str) -> str:

        email = Email(email)

        for service_class in self.services:
            if service_class().is_supported(email):
                return service_class().get_primary_email(email).get_email()

        return email.get_email()


get_primary_email = TransparentEmail().get_primary_email
