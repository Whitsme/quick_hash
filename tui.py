import csv
import io
import main

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
    to_this = main.view_table
    results = main.boxed

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app",),
        Binding(key="->", action="none", description="Whitsme 2023", key_display=""),
    ]

    def what_table(self):
        if self.to_this[0] == 'analysis':
            table_name = self.analysis
        elif self.to_this[0] == 'file_sandbox':
            table_name = self.file_sandbox
        elif self.to_this[0] == 'crx_report':
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
        text_log = self.query_one(TextLog)
        table_data = self.what_table()
        rows = iter(csv.reader(io.StringIO(table_data)))
        table = Table(*next(rows))
        for row in rows:
            table.add_row(*row)

        text_log.write(table, expand=True)

if __name__ == "__main__":
    app = quick_hash()
    app.run()

    
