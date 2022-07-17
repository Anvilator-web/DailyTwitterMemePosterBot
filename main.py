import os
import rich
from dotenv import load_dotenv
from functions.sleep import *

version = 0.1
load_dotenv()

rich.print("Daily[bold cyan]Twitter[/bold cyan]MemePosterBot")
rich.print("[red]version[/red]", version)
