import logging

logging.basicConfig(
    filename="appp.log",
    level=logging.INFO
)

try:
    a = 5
    b = 0
    c = a / b

except Exception as e:
    logging.error(e)