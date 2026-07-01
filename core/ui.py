from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table

console = Console()


class UI:

    @staticmethod
    def print_banner():

        banner = Align.center(
            "[bold cyan]🤖 Buddy AI[/bold cyan]\n\n"
            "[white]Your Personal Local AI Assistant[/white]\n\n"
            "[green]Version 0.5[/green]"
        )

        console.print(
            Panel.fit(
                banner,
                border_style="cyan"
            )
        )

        console.print(
            "[dim]Type [bold]/help[/bold] to see available commands.[/dim]\n"
        )

    @staticmethod
    def user():

        console.print(
            "\n[bold green]You :[/bold green] ",
            end=""
        )

    @staticmethod
    def buddy_prefix():

        console.print(
            "\n[bold cyan]🤖 Buddy :[/bold cyan] ",
            end=""
        )

    @staticmethod
    def success(message):

        console.print(
            f"[bold green]✓[/bold green] {message}"
        )

    @staticmethod
    def error(message):

        console.print(
            f"[bold red]✗[/bold red] {message}"
        )

    @staticmethod
    def info(message):

        console.print(
            f"[yellow]ℹ[/yellow] {message}"
        )

    @staticmethod
    def show_help():

        console.print()

        table = Table(
            title="📖 Buddy Commands",
            border_style="cyan",
            header_style="bold cyan",
            show_lines=False
        ) 

        table.add_column("Command", style="green", no_wrap=True)
        table.add_column("Description", style="white")

        table.add_row("/help", "Show all available commands")
        table.add_row("/clear", "Clear the current conversation")
        table.add_row("/model", "Show the current AI configuration")
        table.add_row("/about", "Information about Buddy AI")
        table.add_row("/version", "Show Buddy version")
        table.add_row("exit", "Exit Buddy")

        console.print(table)
        console.print()

    @staticmethod
    def show_model(model_name):

        console.print()

        console.print("[bold cyan]🤖 Current AI Configuration[/bold cyan]\n")

        console.print(f"[green]Model[/green]       : {model_name}")
        console.print("[green]Provider[/green]    : Ollama")
        console.print("[green]Mode[/green]        : Local AI")
        console.print("[green]Streaming[/green]   : Enabled")
        console.print("[green]Memory[/green]      : Enabled")

        console.print()

    @staticmethod
    def show_about(version):

        console.print()

        banner = Align.center(
            "[bold cyan]🤖 Buddy AI[/bold cyan]\n\n"
            "[white]Your Personal Local AI Assistant[/white]\n\n"
            f"[green]Version {version}[/green]\n\n"
            "[yellow]Runs completely offline using Ollama[/yellow]\n\n"
            "[bold]Developed by[/bold]\n"
            "Prakhar Pandey\n\n"
            "[magenta]Crafted with ❤️ by Prakhar Pandey[/magenta]\n\n"
            "[dim]© 2026 Buddy AI Project[/dim]"
        )

        console.print(
            Panel.fit(
                banner,
                border_style="cyan"
            )
        )

        console.print()
    @staticmethod
    def show_version(version):

        console.print()

        table = Table(
            title="📦 Buddy Version Information",
            border_style="cyan",
            header_style="bold cyan"
        )

        table.add_column("Property", style="green", no_wrap=True)
        table.add_column("Value", style="white")

        table.add_row("Application", "Buddy AI")
        table.add_row("Version", version)
        table.add_row("Developer", "Prakhar Pandey")
        table.add_row("Engine", "Ollama")
        table.add_row("Language", "Python")

        console.print(table)
        console.print()