import keyring

service_id = "serpapi"
username = "bulle"

# store username & password
# keyring.set_password(service_id, "username", username)
# keyring.set_password(service_id, username, "thekey")

# retrieve username & password
username = keyring.get_password(service_id, "username")
password = keyring.get_password(service_id, username)
print(password, username)

# keyring.set_password("example_service", "example_username", "example_password")
credentials = keyring.get_credential(service_id, None)
if credentials is not None:
    username = credentials.username  # example_username
    password = credentials.password  # example_password

print(password, username)