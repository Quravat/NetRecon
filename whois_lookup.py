import socket
from rich.console import Console
import re

console = Console()

def query_whois_server(server, query, timeout=7):
    try:
        with socket.create_connection((server, 43), timeout=timeout) as s:
            s.sendall((query + "\r\n").encode())
            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
        return response.decode(errors="ignore")
    except Exception as e:
        console.print(f"[red]Whois query failed on {server}: {e}[/red]")
        return None

def clean_whois_response(response):
    ignore_patterns = [
        r"For more information on Whois status codes",
        r"IMPORTANT INFORMATION ABOUT THE DEPLOYMENT",
        r"The registration data available in this service is limited",
        r"By using this service you are agreeing",
        r"Access to the Whois and RDAP services is rate limited",
        r"All data is \(c\)",
        r"Abuse of this service is monitored",
        r"Whois and RDAP services",
        r"Internet domain names registered by",
        r"information presented here",
        r"not to use any",
        r"actions in contravention",
        r"permanently blacklisted",
        r"https?://\S+",
        r"%% This is the AFNIC Whois server.",
        r"%% complete date format: YYYY-MM-DDThh:mm:ssZ",
        r"%% Rights restricted by copyright."
    ]

    lines = response.splitlines()
    cleaned_lines = []
    for line in lines:
        if any(re.search(pattern, line, re.IGNORECASE) for pattern in ignore_patterns):
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

def whois_query(domain):
    console.print(f"[bold cyan]Querying IANA WHOIS server for {domain}[/bold cyan]")
    response = query_whois_server("whois.iana.org", domain)
    if not response:
        return

    refer_match = re.search(r"refer:\s*(\S+)", response, re.IGNORECASE)
    if not refer_match:
        console.print("[red]No referral server found from IANA WHOIS response.[/red]")
        console.print(response)
        return

    refer_server = refer_match.group(1).strip()
    console.print(f"[yellow]Referral found: {refer_server}[/yellow]")
    console.print(f"[bold cyan]Querying referral WHOIS server {refer_server} for {domain}[/bold cyan]")

    final_response = query_whois_server(refer_server, domain)
    if final_response:
        cleaned = clean_whois_response(final_response)
        console.print(f"[bold green]Whois result for {domain} from {refer_server}:[/bold green]\n")
        console.print(cleaned)
    else:
        console.print(f"[red]Failed to query referral server {refer_server}[/red]")
