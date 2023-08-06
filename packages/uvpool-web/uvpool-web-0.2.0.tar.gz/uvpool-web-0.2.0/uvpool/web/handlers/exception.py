from sanic.exceptions import SanicException
from sanic.log import error_logger
from sanic.response import json


class ExceptionHandler:
    def __init__(self, app):
        self.app = app

    def __call__(self, request, exception: Exception):
        message = 'Internal server error'
        extra = {}

        if isinstance(exception, SanicException):
            # keep the message when it comes from the app
            message = exception.args[0]
            # Get injected errors info
            if hasattr(exception, 'errors'):
                extra['errors'] = exception.errors

        # The assumption is that if this isn't a SanicException, then it is an internal server error
        status_code = getattr(exception, 'status_code', 500)

        if status_code >= 500:
            error_logger.exception(
                'Exception in app: %s(%s)',
                exception.__class__.__name__, ','.join(f"'{a}'" for a in exception.args),
            )

        self.external_report(request, exception)

        return json({
            'status': 'ERROR',
            'message': message,
            **extra,
        }, status=status_code)

    def external_report(self, request, exception: Exception):
        pass
