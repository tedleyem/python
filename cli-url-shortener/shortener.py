import hashlib
import argparse
import sys

# Simple in-memory "database" to store shortened URLs
url_database = {}

# Base URL for the shortener (you can replace this with your domain)
BASE_URL = "http://short.ly/"

def generate_shortened_url(long_url):
    """Generate a unique shortened URL using hashlib."""
    # Create a hash of the long URL
    url_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]  # First 6 chars of the MD5 hash
    short_url = BASE_URL + url_hash
    return short_url

def save_url(long_url, short_url):
    """Save the URL mapping to the "database"."""
    url_database[short_url] = long_url

def get_long_url(short_url):
    """Retrieve the original long URL from the shortened URL."""
    return url_database.get(short_url, "URL not found")

def create_short_url(long_url):
    """Generate and save the shortened URL."""
    short_url = generate_shortened_url(long_url)
    save_url(long_url, short_url)
    return short_url

def main():
    parser = argparse.ArgumentParser(description="A simple URL shortener.")
    
    # Add subcommands for shortening a URL or expanding it
    subparsers = parser.add_subparsers(dest="command")

    # Subcommand for shortening a URL
    shorten_parser = subparsers.add_parser("shorten", help="Shorten a URL")
    shorten_parser.add_argument("long_url", help="The long URL to shorten")
    
    # Subcommand for expanding a shortened URL
    expand_parser = subparsers.add_parser("expand", help="Expand a shortened URL")
    expand_parser.add_argument("short_url", help="The shortened URL to expand")
    
    args = parser.parse_args()

    if args.command == "shorten":
        # Shorten the provided long URL
        short_url = create_short_url(args.long_url)
        print(f"Shortened URL: {short_url}")
    
    elif args.command == "expand":
        # Expand the provided shortened URL
        long_url = get_long_url(args.short_url)
        if long_url == "URL not found":
            print(f"Error: {long_url}")
        else:
            print(f"Original URL: {long_url}")
    
    else:
        print("Invalid command. Use 'shorten' or 'expand'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
