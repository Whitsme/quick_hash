from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static, Button, Input, TextLog
from textual import events
from rich.table import Table
import csv
import io

table_rows = ["resource", "sha256", "category", "sandbox_used", "classification"]

class CombiningLayoutsExample(App):
    CSS_PATH = "tui.css"

    def compose(self) -> ComposeResult:
        yield Container(id="header")
        with Container(id="input_grid"):
            yield Input(placeholder="input", id="input")
            yield Button("go", id="button")
        with Container(id="return_grid"):
            with Vertical(id="left_pane"):
                for number in range(15):
                    yield Static(f"Vertical layout, child {number}")
            with Horizontal(id="top_right"):
                yield TextLog(highlight=True, markup=True)
        yield Container(id="footer")
        
    def on_ready(self) -> None:
        """Called  when the DOM is ready."""
        text_log = self.query_one(TextLog)

        table = Table(table_rows[0], table_rows[1], table_rows[2], table_rows[3], table_rows[4])

        text_log.write(table)

    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""
        text_log = self.query_one(TextLog)
        text_log.write(event)


if __name__ == "__main__":
    app = CombiningLayoutsExample()
    app.run()
