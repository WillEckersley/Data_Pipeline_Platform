from logger_config import Log

class SendLogger:

    @staticmethod
    def callback(error, message):
        """
        Kafka delivery callback
        """
        if error:
            Log.get_logger.error("Delivery failed: %s", error)
        else:
            Log.get_logger.info(
                "Delivered to %s [%s] @ offset %s",
                message.topic(),
                message.partition(),
                message.offset(),
            )