import requests
import argparse
from rich.console import Console
from rich.table import Table
import pyfiglet

console = Console()

# Important Security Headers
SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps prevent XSS by defining content sources.",
    "Strict-Transport-Security": "Enforces HTTPS to prevent SSL stripping.",
    "X-Frame-Options": "Prevents clickjacking attacks.",
    "X-Content-Type-Options": "Stops MIME-sniffing vulnerabilities.",
    "Referrer-Policy": "Controls how much referrer info is shared.",
    "Permissions-Policy": "Restricts browser features (camera, mic, etc.)."
}

def banner():
    ascii_banner = pyfiglet.figlet_format("HeadHunt")
    console.print(f"[bold cyan]{ascii_banner}[/bold cyan]")
    console.print("[yellow]🔍 Security Headers Finder Tool[/yellow]")
    console.print("[green]By Draxel01[/green]\n")

def scan_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        table = Table(title=f"🔍 Security Headers Scan for {url}")
        table.add_column("Header", style="cyan", no_wrap=True)
        table.add_column("Status", style="magenta")
        table.add_column("Details / Risk", style="yellow")

        for header, description in SECURITY_HEADERS.items():
            if header in headers:
                table.add_row(header, "[green]✅ Present", f"[white]{headers[header]}")
            else:
                table.add_row(header, "[red]❌ Missing", f"[red]{description}")

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(description="HeadHunt - Security Headers Finder Tool")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g., https://example.com)")
    args = parser.parse_args()
    scan_headers(args.url)

