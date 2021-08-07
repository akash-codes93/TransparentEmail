import sys
import unittest

sys.path.append("..")

from transparentemail import __version__
from transparentemail.src import get_primary_email
from transparentemail.services.Emails import emailException


class TestTransparentEmail(unittest.TestCase):
    def test_gmail(self):
        email = "akash.gupta1+1@gmail.com"
        _email = get_primary_email(email)
        self.assertEqual(_email, "akashgupta1@gmail.com")

    def test_googlemail(self):
        email = "akash.gupta1+1@googlemail.com"
        _email = get_primary_email(email)
        self.assertEqual(_email, "akashgupta1@gmail.com")

    def test_outlook(self):
        email = "akash.gupta1+1@outlook.com"
        email1 = "akash.gupta1+1@hotmail.com"
        _email = get_primary_email(email)
        _email1 = get_primary_email(email1)
        self.assertEqual(_email, "akash.gupta1@outlook.com")
        self.assertEqual(_email1, "akash.gupta1@hotmail.com")

    def test_yahoo(self):
        email = "akash.gupta1-1@yahoo.com"
        _email = get_primary_email(email)
        self.assertEqual(_email, "akash.gupta1@yahoo.com")

    def test_33mail(self):
        email = "qwerty@name.33mail.com"
        _email = get_primary_email(email)
        self.assertEqual(_email, "name@name.33mail.com")

    def test_invalid(self):
        email = "akash.gupta1 1@yahoo.com"
        self.assertRaises(
            emailException.InvalidEmailException, get_primary_email, email
        )

    def test_version(self):
        assert __version__ == "0.1.0"


if __name__ == "__main__":
    unittest.main()
