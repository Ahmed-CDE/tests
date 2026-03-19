import termcolor
import random
import pyfiglet
x_o=[["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
x_o_massage_str=(f"""

{" | ".join(x_o[0])}
{" | ".join(x_o[1])}
{" | ".join(x_o[2])}

""")
x_o_massage=((pyfiglet.figlet_format(x_o_massage_str)).strip())
x=(termcolor.colored(pyfiglet.figlet_format("x"), color="red")).strip()
o=(termcolor.colored(pyfiglet.figlet_format("o"), color="blue")).strip()
print(f"{o} {x} ",end="")
