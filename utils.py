from rich.console import Console

console = Console()

def banner():
    console.print("""
[bold cyan]
 _   _      _   _____                       
| \ | |    | | |  __ \                      
|  \| | ___| |_| |__) |__  __ ___   _____  
| . ` |/ _ \ __|  ___/ _ \/ _` \ \ / / _ \ 
| |\  |  __/ |_| |  |  __/ (_| |\ V /  __/ 
\_| \_/\___|\__\_|   \___|\__,_| \_/ \___| 
[/bold cyan]
""")
