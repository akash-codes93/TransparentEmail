from transparentemail.services.Emails.email import Email
from transparentemail.services.Emails.editableEmail import EditableEmail
from transparentemail.services.serviceEmail import ServiceEmail


class GmailCom(ServiceEmail):
    def get_primary_email(self, email: Email) -> Email:
        return (
            EditableEmail(email)
            .remove_from_local_part(".")
            .remove_suffix_alias("+")
            .lower_case_local_part(True)
            .set_domain(self.get_domain(email.domain))
            .get_email()
        )

    def is_supported(self, email: Email) -> bool:
        return email.domain in ["googlemail.com", "gmail.com"]

    @staticmethod
    def get_domain(domain) -> str:
        return {
            "googlemail.com": "gmail.com",
        }.get(domain, "gmail.com")
