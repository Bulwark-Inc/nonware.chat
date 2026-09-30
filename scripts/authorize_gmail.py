from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = [
    "https://www.googleapis.com/auth/gmail.send"
]


def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        "scripts/credentials.json",
        SCOPES,
    )

    credentials = flow.run_local_server(
        port=8080,
        access_type="offline",
        prompt="consent",
    )

    print("\nAuthorization successful!")
    print("\nRefresh token:")
    print(credentials.refresh_token)


if __name__ == "__main__":
    main()