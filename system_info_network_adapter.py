import os
import platform
import socket
import subprocess
import pwd
from rich.console import Console
from rich.table import Table

# Check if rich module is installed, if not, install it
try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    print("rich module is not installed. Installing now...")
    subprocess.run(["pip", "install", "rich"])
    from rich.console import Console
    from rich.table import Table

# Check if psutil module is installed, if not, install it
try:
    import psutil
except ImportError:
    print("psutil module is not installed. Installing now...")
    subprocess.run(["pip", "install", "psutil"])
    import psutil

def get_user_names():
    return [user.pw_name for user in pwd.getpwall()]

def get_private_ip():
    private_ip = socket.gethostbyname(socket.gethostname())
    return private_ip

def get_public_ip():
    public_ip = subprocess.check_output(['curl', 'ifconfig.me']).decode().strip()
    return public_ip

def get_os_version():
    return platform.platform()

def get_ssh_version():
    ssh_version = subprocess.check_output(['ssh', '-V']).decode().strip()
    return ssh_version

def get_network_adapters():
    adapters = psutil.net_if_addrs()
    return adapters

def main():
    console = Console()

    # Create a table for displaying information
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Category", style="dim", width=20)
    table.add_column("Information")

    # Add data to the table
    table.add_row("User Names", ", ".join(get_user_names()))
    table.add_row("Private IP", get_private_ip())
    table.add_row("Public IP", get_public_ip())
    table.add_row("OS Version", get_os_version())
    table.add_row("SSH Version", get_ssh_version())

    # Display the table
    console.print("\n[bold cyan]System Information[/bold cyan]")
    console.print(table)

    # Display network adapter information
    console.print("\n[bold cyan]Network Adapter List[/bold cyan]")
    adapters = get_network_adapters()
    for adapter, addrs in adapters.items():
        adapter_table = Table(show_header=True, header_style="bold green")
        adapter_table.add_column("Family")
        adapter_table.add_column("Address")
        for addr in addrs:
            adapter_table.add_row(addr.family.name, addr.address)
        console.print(f"[bold]Adapter: {adapter}[/bold]")
        console.print(adapter_table)

if __name__ == "__main__":
    main()
