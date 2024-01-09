from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern_name = r"[\w+\.]+"
pattern_domain = r"\.[a-z]+"
valid_domains = [".com", ".bg", ".org", ".net"]

email = input()

while email != "End":

    if len(findall(pattern_name, email.split("@")[0])[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if findall(pattern_domain, email.split("@")[1])[0] not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    print("Email is valid")

    email = input()




    
