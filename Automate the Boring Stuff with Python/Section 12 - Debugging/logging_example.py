# Great for step by step debugging through logging rather than relying on print
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
# Can add basicConfig(filename="...txt", to save log
# logging.disable(logging.CRITICAL)  # This disables logging

logging.debug("Start of program")


def factorial(n):
    logging.debug(f"Start of factorial({n})")
    total = 1
    for i in range(n + 1):  # Should be range(1, n + 1) as it starts at 0
        total *= i
        logging.debug("i is %s, total is %s" % (i, total))

    logging.debug("Return value is %s" % total)
    return total


print(factorial(5))

logging.debug("End of program")

# Logging has 5 different levels: debug, info, warning, error, critical
