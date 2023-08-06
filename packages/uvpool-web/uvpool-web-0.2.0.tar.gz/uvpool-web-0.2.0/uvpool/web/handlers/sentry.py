import logging

from sanic.log import error_logger, logger

from .exception import ExceptionHandler

try:
    import sentry_sdk
    from sentry_sdk.integrations.aiohttp import AioHttpIntegration
    from sentry_sdk.integrations.logging import EventHandler

    sentry_installed = True
except ImportError:
    sentry_installed = False


class ExceptionHandlerWithSentry(ExceptionHandler):
    def __init__(self, app):
        super().__init__(app)

        self.use_sentry = False
        sentry_dsn = app.config.get('SENTRY_DSN', None)
        if sentry_installed and sentry_dsn:
            app.config['SENTRY_PARAMS'] = {
                "release": app.config.get('VERSION'),
                "environment": app.config.get('ENVIRONMENT'),
            }

            sentry_sdk.init(
                dsn=app.config.get('SENTRY_DSN', None),
                integrations=[AioHttpIntegration()],
                **app.config.get('SENTRY_PARAMS', {})
            )

            self.handler = EventHandler(
                level=app.config.get('SENTRY_LEVEL', logging.WARNING),
            )
            logger.addHandler(self.handler)
            error_logger.addHandler(self.handler)

            self.use_sentry = True

    def external_report(self, request, exception: Exception):
        if not self.use_sentry:
            return

        if getattr(exception, 'status_code', 500) >= 500:
            report_id = sentry_sdk.capture_exception(exception)
            if report_id:
                logger.info('Exception reported to Sentry as event %s', report_id)
