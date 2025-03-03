# Email Filter

**Email Filter** is a command-line tool designed to clean and filter email lists by removing unwanted or invalid emails, removing duplicates, and keeping only the most useful email for each domain (such as `contact@` or `info@`). It also handles noisy lines and extracts only valid emails from messy inputs.

![https://github.com/yogsec/Email-Filter/blob/main/Screenshot%20from%202025-03-04%2003-09-22.png?raw=true](https://github.com/yogsec/Email-Filter/blob/main/Screenshot%20from%202025-03-04%2003-09-22.png?raw=true)

---

## Features

✅ Remove government, educational, and other unwanted emails  
✅ Automatically clean noisy lines (like `contact@site.comJoin`)  
✅ Remove duplicates  
✅ For each domain, keeps **only the best email** (e.g., prefers `contact@` over generic ones)  
✅ Supports both **single email check** and **bulk processing from file**  
✅ Option to save filtered output to a file

---

## Installation

Install required library:

```bash
pip install argparse
```

---

## Usage

### Check a single email
```bash
python email_filter.py -e <email>
```

### Process a list of emails from file
```bash
python email_filter.py -l <path_to_file>
```

### Process and save filtered output to a file
```bash
python email_filter.py -l <path_to_file> -s <output_file>
```

### Show help menu
```bash
python email_filter.py -h
```

---

## Example

```bash
python email_filter.py -l emails.txt -s cleaned_emails.txt
```

This reads `emails.txt`, filters out noisy or unwanted emails, keeps only the best contact per domain, and saves the result in `cleaned_emails.txt`.

---

## Why Use This Tool?

✔️ Clean email lists for outreach campaigns  
✔️ Avoid wasting time on invalid/government addresses  
✔️ Ensure you’re reaching out to the **most relevant contact** for each organization  
✔️ Save time and improve targeting accuracy

---

## 🌟 Let's Connect!

Hello, Hacker! 👋 We'd love to stay connected with you. Reach out to us on any of these platforms and let's build something amazing together:

🌐 **Website:** [https://yogsec.github.io/yogsec/](https://yogsec.github.io/yogsec/)  
📜 **Linktree:** [https://linktr.ee/yogsec](https://linktr.ee/yogsec)  
🔗 **GitHub:** [https://github.com/yogsec](https://github.com/yogsec)  
💼 **LinkedIn (Company):** [https://www.linkedin.com/company/yogsec/](https://www.linkedin.com/company/yogsec/)  
📷 **Instagram:** [https://www.instagram.com/yogsec.io/](https://www.instagram.com/yogsec.io/)  
🐦 **Twitter (X):** [https://x.com/yogsec](https://x.com/yogsec)  
👨‍💼 **Personal LinkedIn:** [https://www.linkedin.com/in/cybersecurity-pentester/](https://www.linkedin.com/in/cybersecurity-pentester/)  
📧 **Email:** abhinavsingwal@gmail.com

---

## ☕ Buy Me a Coffee

If you find our work helpful and would like to support us, consider buying us a coffee. Your support keeps us motivated and helps us create more awesome content. ❤️

☕ **Support Us Here:** [https://buymeacoffee.com/yogsec](https://buymeacoffee.com/yogsec)
