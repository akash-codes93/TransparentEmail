from dataclasses import dataclass, field

from transparentemail.services.Emails.email import Email


@dataclass
class EditableEmail:
    email: Email

    local_part: str = field(init=False)
    domain: str = field(init=False)

    def __post_init__(self):
        self.local_part = self.email.local_part
        self.domain = self.email.domain

    def remove_from_local_part(self, to_remove: str) -> "EditableEmail":
        self.local_part = self.local_part.replace(to_remove, "")
        return self

    def remove_suffix_alias(self, delimiter: str) -> "EditableEmail":
        self.local_part = self.local_part.split(delimiter)[0]
        return self

    def lower_case_local_part(self, condition: bool) -> "EditableEmail":
        if condition:
            self.local_part = self.local_part.lower()
        return self

    def set_domain(self, domain: str) -> "EditableEmail":
        self.domain = domain
        return self

    def get_email(self) -> Email:
        return Email(self.local_part + "@" + self.domain)

    def set_local_part(self, local_part: str) -> "EditableEmail":
        self.local_part = local_part
        return self
