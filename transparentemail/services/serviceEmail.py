from transparentemail.services.Emails.email import Email
from abc import ABC, abstractmethod


class ServiceEmail(ABC):
    @abstractmethod
    def get_primary_email(self, email: Email) -> Email:
        pass

    @abstractmethod
    def is_supported(self, email: Email) -> bool:
        pass
