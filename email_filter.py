import argparse
import re
from collections import defaultdict

HEADER = r"""
 _______ _______ _______ _____             _______ _____        _______ _______  ______
 |______ |  |  | |_____|   |   |           |______   |   |         |    |______ |_____/
 |______ |  |  | |     | __|__ |_____      |       __|__ |_____    |    |______ |    \_
                                                                                       
GitHub - https://github.com/yogsec
Donate - https://buymeacoffee.com/yogsec
"""

def is_useful_email(email):
    """Check if email is useful."""
    lower_email = email.lower()
    if lower_email.endswith('.gov') or lower_email.endswith('.mil'):
        return False
    if "address not found" in lower_email:
        return False
    return True

def get_domain(email):
    """Extract domain from email."""
    return email.split('@')[1].lower()

def score_email(email):
    """Score email to choose the best one from the same domain."""
    # Prioritize shorter usernames (likely to be generic contact emails)
    username = email.split('@')[0]
    return len(username)

def process_single_email(email):
    print(HEADER)

    if not is_useful_email(email):
        print(f"❌ Not a useful email: {email}")
        return

    print(f"✅ Useful Email: {email}")

def process_email_list(input_file, save_file=None):
    print(HEADER)

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            emails = []
            for line in file.readlines():
                line = line.strip()
                # Extract first valid email from noisy line
                match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', line)
                if match:
                    emails.append(match.group())

        # Step 1: Filter only useful emails
        useful_emails = [email for email in emails if is_useful_email(email)]

        # Step 2: Remove duplicates
        useful_emails = list(set(useful_emails))

        # Step 3: Keep only the best email per domain
        domain_map = defaultdict(list)
        for email in useful_emails:
            domain = get_domain(email)
            domain_map[domain].append(email)

        best_emails = []
        for domain, domain_emails in domain_map.items():
            best_email = min(domain_emails, key=score_email)
            best_emails.append(best_email)

        # Final counts
        print(f"Total Emails in File: {len(emails)}")
        print(f"Useful Emails (After Filtering): {len(useful_emails)}")
        print(f"Unique Domains: {len(best_emails)}")

        if save_file:
            with open(save_file, 'w', encoding='utf-8') as file:
                file.write('\n'.join(best_emails))
            print(f"✅ Saved to: {save_file}")
        else:
            print("\nBest Emails Per Domain:")
            print("\n".join(best_emails))

    except FileNotFoundError:
        print(f"❌ File Not Found: {input_file}")

def show_help():
    print(HEADER)
    print("Usage:")
    print("  python email_filter.py -e EMAIL             Check single email")
    print("  python email_filter.py -l FILE               Check email list from file")
    print("  python email_filter.py -l FILE -s OUTPUT     Check list and save result to file")
    print("  python email_filter.py -h                     Show help")

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-e', '--email', type=str, help="Check a single email")
    parser.add_argument('-l', '--list', type=str, help="Check a list of emails from file")
    parser.add_argument('-s', '--save', type=str, help="Save filtered result to file")
    parser.add_argument('-h', '--help', action='store_true', help="Show help menu")

    args = parser.parse_args()

    if args.help:
        show_help()
        return

    if args.email:
        process_single_email(args.email)
    elif args.list:
        process_email_list(args.list, args.save)
    else:
        show_help()

if __name__ == "__main__":
    main()
