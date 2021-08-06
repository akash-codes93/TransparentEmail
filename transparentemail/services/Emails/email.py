import re

from dataclasses import dataclass, field
from transparentemail.services.Emails.emailException import InvalidEmailException

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


@dataclass
class Email:
    email: str

    local_part: str = field(init=False)
    domain: str = field(init=False)

    def __post_init__(self):
        if not re.match(regex, self.email):
            raise InvalidEmailException("Not a valid email address")

        self.local_part, self.domain = self.email.split("@")

    def get_email(self):
        return self.local_part + "@" + self.domain
