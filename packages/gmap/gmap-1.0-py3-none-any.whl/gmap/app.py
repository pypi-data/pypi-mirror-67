import clipboard
import chalk
import webbrowser
from simple_term_menu import TerminalMenu
from decimal import Decimal


def take_input(placeholder):
    value = None
    while value is None:
        inp = input(chalk.bold(f'{placeholder}: '))
        try:
            value = Decimal(inp)
        except:
            print(chalk.red(f'{placeholder} needs to be a valid number'))
    return value


lat = take_input("latitude")
lon = take_input('longitude')

link = f'https://www.google.com/maps/search/?api=1&query={lat},{lon}'


term_menu = TerminalMenu(
    ["Open in browser", "Copy to clipboard"], chalk.green("Select Action:"), )
action = term_menu.show()

if action == 0:
    webbrowser.open(link)
elif action == 1:
    clipboard.copy(link)
    print(chalk.cyan('🌎 Google map link had been copioed to you clipboard 🔖'))
else:
    pass

print('Thanks for using gmap 👋')
