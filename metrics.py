
def create_metrics():
    """returns metrics

    This function creates a blank dictionary called metrics.

    :return: metrics
    :rtype: dictionary
    """
    import logging
    from logging import config

    logging.config.fileConfig('logger_config.ini', disable_existing_loggers=False)

    metrics = {}
    logging.info(metrics)

    return metrics
