from transparentemail.services.Emails.editableEmail import EditableEmail
from transparentemail.services.Emails.email import Email

from transparentemail.services.serviceEmail import ServiceEmail


class OutlookCom(ServiceEmail):
    def get_primary_email(self, email: Email) -> Email:
        return (
            EditableEmail(email)
            .remove_suffix_alias("+")
            .lower_case_local_part(True)
            .get_email()
        )

    def is_supported(self, email: Email) -> bool:
        return email.domain in ["outlook.com", "hotmail.com"]
