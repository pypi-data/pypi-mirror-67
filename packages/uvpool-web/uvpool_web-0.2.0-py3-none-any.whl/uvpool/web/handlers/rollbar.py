import logging

from sanic.log import error_logger, logger

from .exception import ExceptionHandler

try:
    import rollbar
    from rollbar.logger import RollbarHandler

    rollbar_installed = True
except ImportError:
    rollbar_installed = False


class ExceptionHandlerWithRollbar(ExceptionHandler):
    def __init__(self, app):
        super().__init__(app)

        self.use_rollbar = False
        rollbar_access_token = app.config.get('ROLLBAR_ACCESS_TOKEN', None)
        if rollbar_installed:
            if not rollbar_access_token:
                logger.warning('Rollbar access token not provided, handlers will not be set')
                return

            kwargs = {
                'environment': app.config.get('ENVIRONMENT').lower(),
                'code_version': app.config.get('VERSION'),
            }

            rollbar.init(
                access_token=rollbar_access_token,
                suppress_reinit_warning=True,
                **kwargs,
            )

            # Do not pass the access_token here, rollbar was initialized before
            handler = RollbarHandler(
                level=logging.WARNING,
                **kwargs,
            )
            logger.addHandler(handler)
            error_logger.addHandler(handler)

            self.use_rollbar = True

    def external_report(self, request, exception: Exception):
        if not self.use_rollbar:
            return

        if getattr(exception, 'status_code', 500) >= 500:
            report_id = rollbar.report_exc_info()
            if report_id:
                logger.info('Exception reported to Rollbar as event %s', report_id)
