from loguru import logger


def genkan(event, context):
    test_num = 8
    changes = "Code Sync..."
    print(f"Input params: {event['key1']}")
    print(f"Kon'nichiwa. Test {test_num} for changes: {changes}")
    logger.info("Logger printing it's message...")
    return True
