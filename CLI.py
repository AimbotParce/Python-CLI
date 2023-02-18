import lib.console as console

console.logger.formatter.setFormat(fmt="%(filename)s @ [%(levelname)s] %(message)s")
console.setLevel(console.DEBUG)

console.setLevelName(console.DEBUG, "\033[1;30m%s\033[0m" % console.getLevelName(console.DEBUG))
console.setLevelName(console.INFO, "\033[1;32m%s\033[0m" % console.getLevelName(console.INFO))
console.setLevelName(console.WARNING, "\033[1;33m%s\033[0m" % console.getLevelName(console.WARNING))
console.setLevelName(console.ERROR, "\033[1;31m%s\033[0m" % console.getLevelName(console.ERROR))
console.setLevelName(console.CRITICAL, "\033[1;31m%s\033[0m" % console.getLevelName(console.CRITICAL))
console.setLevelName(console.INPUT, "\033[1;34m%s\033[0m" % console.getLevelName(console.INPUT))

console.debug("debug")
console.info("info")
console.warning("warning")
console.error("error")
console.critical("critical")
print(console.input("Give me input: "))
