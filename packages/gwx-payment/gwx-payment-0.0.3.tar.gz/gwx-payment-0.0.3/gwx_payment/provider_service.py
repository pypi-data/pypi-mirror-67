from typing import Any

from gwx_payment import config
from gwx_payment.abstract_payment_service import AbstractPaymentService
from gwx_payment.lib.service_locator_service import ServiceLocatorService
from gwx_core.services.config_parser_service import ConfigParserService


class ProviderService:
    """The Provider Service will resolve the service (Payment Provider Service) using the service locator,
    and inject the parsed configuration dependencies to the service, so this will only happen on boot and will
    act as a singleton behaviour for all the implementations that will have dependencies on this service.

    todo: I would recommend using a caching mechanism to store the instance of the resolved provider version (0.0.1)
    """

    # The placeholder for the resolved `Payment Provider Service`
    provider: AbstractPaymentService = None

    # Instance of the config_parser parser service
    config_parser: ConfigParserService = None

    # Resolved instance of the service locator service LOL redundant name
    provider_service_locator: ServiceLocatorService = None

    # Un-resolved instance of the Payment Provider Service
    provider_service: Any = None

    def __init__(self, config_path: str, config_file: str):
        """The instance of the provider service.

        :param config_path: string value of the config_parser's dir
        :param config_file: string value of the config_parser's file name.
        """

        self.config_parser = ConfigParserService(config_path, config_file, config['package_name'])
        self.provider_service_locator = ServiceLocatorService(self.config_parser.get_provider_name())
        self.provider_service = self.provider_service_locator.get_provider()

        try:
            self.provider = self.provider_service(self.config_parser.get_config())
        except RuntimeError:
            raise RuntimeError(self.provider)

    def get_payment_service(self) -> AbstractPaymentService:
        """Return the resolved instance of the AbstractPaymentService,
        @note: right now we only have StripeService.

        :return: AbstractPaymentService
        """
        return self.provider
