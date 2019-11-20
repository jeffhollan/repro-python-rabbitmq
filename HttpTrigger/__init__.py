import logging

import azure.functions as func


def main(req: func.HttpRequest, outputQueueItem: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    outputQueueItem.set("hello")

    return func.HttpResponse(f"Sent")
