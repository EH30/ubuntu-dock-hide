import CommandRun

hide_docker_commands = [
    "gsettings set org.gnome.shell.extensions.dash-to-dock autohide true",
    "gsettings set org.gnome.shell.extensions.dash-to-dock intellihide false",
    "gsettings set org.gnome.shell.extensions.dash-to-dock pressure-threshold 100000"
]

reset_docker_commands = [
    "gsettings reset org.gnome.shell.extensions.dash-to-dock autohide",
    "gsettings reset org.gnome.shell.extensions.dash-to-dock intellihide",
    "gsettings reset org.gnome.shell.extensions.dash-to-dock pressure-threshold",
    "gsettings reset org.gnome.shell.extensions.dash-to-dock hide-delay",
    "gsettings reset org.gnome.shell.extensions.dash-to-dock dock-fixed"
]


if __name__ == "__main__":
    shell = CommandRun.CommandRun()
    user_input = int(input("Press 1 to hide dock and press 0 to reset the dock: "))
    if (user_input == 1):
        for command in hide_docker_commands:
            shell.runCommand(command)
    else:
        for command in reset_docker_commands:
            shell.runCommand(command)
