from click import echo, style
import os


def setup_env():
    """
    Sets up the environment by importing the environment variables found in .env file it it exists
    """
    if os.path.exists(".env"):
        echo(style(text="Importing environment variables", fg="green", bold=True))
        for line in open(".env"):
            var = line.strip().split("=")
            if len(var) == 2:
                os.environ[var[0]] = var[1]


if __name__ == "__main__":
    setup_env()
