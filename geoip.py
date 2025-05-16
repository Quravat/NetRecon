import requests
from rich.console import Console

console = Console()

def geoip_lookup(ip):
    url = f"https://ipapi.co/{ip}/json/"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if 'error' in data:
            console.print(f"[red]Error: {data.get('reason', 'Unknown error')}[/red]")
            return

        country = data.get('country_name', 'Unknown')
        region = data.get('region', 'Unknown')
        city = data.get('city', 'Unknown')
        isp = data.get('org', 'Unknown')

        console.print(f"[bold cyan]GeoIP info for {ip}[/bold cyan]")
        console.print(f"Country: {country}")
        console.print(f"Region: {region}")
        console.print(f"City: {city}")
        console.print(f"ISP: {isp}")

    except Exception as e:
        console.print(f"[red]Failed to get GeoIP info: {e}[/red]")
