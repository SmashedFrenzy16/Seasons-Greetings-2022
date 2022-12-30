import time
import datetime
from rich import print

year = int(input("Enter current year: "))

newyear = datetime.datetime(year, 1, 1)

delta = datetime.timedelta(microseconds = -0.0000000000001)

close = datetime.timedelta(seconds = 60)

while True:

    timeleft = newyear - datetime.datetime.now()
    secondsleft = timeleft.total_seconds()
    hours, remainder = divmod(secondsleft, 3600)
    minutes, seconds = divmod(remainder, 60)

    if timeleft < close:

        if timeleft < delta:

            print("[bold red]Happy New Year!!!!! :partying_face:[/]")

            break

        else:

            print(f"[bold]{int(seconds)} seconds[/]")

    else:

        print(f"{int(hours)} hours : {int(minutes):02d} minutes : {int(seconds):02d} seconds")

    time.sleep(1)