software_version = input().split(".")
software_version = "".join(software_version)
software_version = int(software_version) + 1
software_version = ".".join(x for x in str(software_version))
print(software_version)

