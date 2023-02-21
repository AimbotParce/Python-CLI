import importlib as imp
import inspect
import os

import lib.console as console

console.logger.formatter.setFormat(fmt="%(filename)s @ [%(levelname)s] %(message)s")
console.setLevel(console.DEBUG)

console.setLevelName(console.DEBUG, "\033[1;30m%s\033[0m" % console.getLevelName(console.DEBUG))
console.setLevelName(console.INFO, "\033[1;32m%s\033[0m" % console.getLevelName(console.INFO))
console.setLevelName(console.WARNING, "\033[1;33m%s\033[0m" % console.getLevelName(console.WARNING))
console.setLevelName(console.ERROR, "\033[1;31m%s\033[0m" % console.getLevelName(console.ERROR))
console.setLevelName(console.CRITICAL, "\033[1;31m%s\033[0m" % console.getLevelName(console.CRITICAL))
console.setLevelName(console.INPUT, "\033[1;34m%s\033[0m" % console.getLevelName(console.INPUT))


def printUsage(path: str):
    """
    Print usage of the command.
    """
    relative = os.path.relpath(path, os.path.join(os.path.dirname(__file__), "bin"))

    commands = []
    for f in os.listdir(path):
        if f.startswith("__"):
            continue
        if f.endswith(".py"):
            commands.append(f[:-3])
        elif os.path.isdir(os.path.join(path, f)):
            commands.append(f)

    console.info(
        "Usage: %s [%s] [arguments]",
        " ".join(os.path.split(relative)).strip(),
        "|".join(commands),
    )


def findCommands(commands: list[str]):
    """
    Find exact command on the bin folder.
    """
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "bin"))
    for command in commands:
        if os.path.isdir(os.path.join(path, command)):
            path = os.path.join(path, command)
            continue
        npath = os.path.join(path, command + ".py")
        if os.path.exists(npath):
            return npath, commands[commands.index(command) + 1 :]
        else:
            console.error("Command not found: %s" % " ".join(commands))
            printUsage(path)
            return None, None
    console.error("Incorrect ussage: %s" % " ".join(commands))
    printUsage(path)
    return None, None


console.info("Python-CLI starting:")

acceptedMainFunctions = ["main", "run", "execute"]  # + File name

try:
    while True:
        cmd = console.input("> ")

        if cmd.strip() == "exit":
            console.info("Exiting...")
            break

        commands = [c for c in cmd.strip().split(" ") if c != ""]
        if len(commands) == 0:
            continue

        path, arguments = findCommands(commands)
        if path is None:
            continue

        module = imp.machinery.SourceFileLoader("module", path).load_module()

        for funcName in acceptedMainFunctions + [os.path.basename(path)[:-3]]:
            if funcName in dir(module):
                func = getattr(module, funcName)
                if callable(func):
                    # Check if the function has arguments.
                    if len(inspect.signature(func).parameters) == 0:
                        func()
                    else:
                        func(arguments)
                    break
        else:
            # No main function. But this doesn't mean that the command is invalid. Maybe the
            # command doesn't need any arguments.
            pass


except KeyboardInterrupt:
    print()
    console.info("Exiting...")
    exit(0)
