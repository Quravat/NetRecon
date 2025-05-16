import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.spinner import Spinner
from services import common_ports

console = Console()

def check_port(ip, port, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            result = s.connect_ex((ip, port))
            if result == 0:
                return port, True
        except Exception:
            pass
    return port, False

def tcp_port_scan(ip, start_port=1, end_port=1024, max_workers=100):
    open_ports = []

    with console.status("[bold cyan]Scanning ports...[/bold cyan]", spinner="dots") as status:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(check_port, ip, port): port for port in range(start_port, end_port + 1)}
            for future in as_completed(futures):
                port, is_open = future.result()
                if is_open:
                    service = common_ports.get(port, "Unknown service")
                    console.print(f"[green]✅ Port {port} is open → {service}[/green]")
                    open_ports.append((port, service))

    if not open_ports:
        console.print("\n[yellow]❌ No open ports found.[/yellow]")
    else:
        console.print("\n[bold green]✔ Scan complete. Open ports:[/bold green]")
        for port, service in open_ports:
            console.print(f"  • [bold]{port}[/bold]: {service}")

    console.print(f"\n📦 Scan finished for {ip} ✅")
