import csv
import io

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Vertical
from textual.widgets import Static, Button, Input, TextLog, Header, Footer
from textual import events
from rich.table import Table

class quick_hash(App):
    CSS_PATH = "tui.css"
    file_sandbox = "category,sandbox_used,classification"
    analysis = "category, result, method, engine_name"
    crx_report = "permissions, total, last_update, name, permission_warnings, size, users, version"
    to_this = ""
    results = "\n"

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app",),
        Binding(key="->", action="none", description="Whitsme 2023", key_display=""),
    ]


    def what_table(self, to_this):
        if to_this == 'analysis':
            table_name = self.analysis
        elif to_this == 'file_sandbox':
            table_name = self.file_sandbox
        elif to_this == 'crx_report':
            table_name = self.crx_report
        else:
            table_name = "hello dave"

        table_data = "{}{}".format(table_name.upper(), self.results)

        return table_data
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with Container(id="input_grid"):
            yield Input(placeholder="input", id="input")
            yield Button("go", id="button")
        with Container(id="return_grid"):
            with Vertical(id="left_pane"):
                for number in range(15):
                    yield Static(f"Vertical layout, child {number}")
            with Container(id="top_right"):
                yield TextLog(wrap=True)
        
    def on_ready(self) -> None:
        """Called  when the DOM is ready."""
        text_log = self.query_one(TextLog)
        table_data = self.what_table(self.to_this)
        rows = iter(csv.reader(io.StringIO(table_data)))
        table = Table(*next(rows))
        for row in rows:
            table.add_row(*row)

        text_log.write(table, expand=True)

    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""
        text_log = self.query_one(TextLog)
        text_log.write(event)

if __name__ == "__main__":
    app = quick_hash()
    app.run()

    
