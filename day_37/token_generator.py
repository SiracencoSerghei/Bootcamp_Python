import secrets

def generate_token():
  """Generates a random token string that meets Pixe.la's requirements.

  Returns:
      str: A random token string between 8 and 128 characters long, containing characters
          from the printable ASCII range (including space).
  """

  token = secrets.token_urlsafe(32)  # urlsafe generates printable characters
  return token

# Example usage
token = generate_token()
print(f"Generated token: {token}")