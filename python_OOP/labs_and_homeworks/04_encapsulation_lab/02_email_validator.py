import re


class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name: str):
        return self.min_length <= len(name)

    def __validate_mail(self, mail: str):
        return mail in self.mails

    def __validate_domain(self, domain: str):
        return domain in self.domains

    def validate(self, email):
        pattern = r"[@.]"
        email_name, mail, domain = re.split(pattern, email)
        return self.__validate_name(email_name) and self.__validate_mail(mail) and self.__validate_domain(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
