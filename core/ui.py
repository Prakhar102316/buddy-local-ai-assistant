from rich.console import Console
from rich.panel import Panel
from rich.align import Align

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
    def buddy(message):

        console.print(
            f"[bold cyan]Buddy :[/bold cyan] {message}"
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