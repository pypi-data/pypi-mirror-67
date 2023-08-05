import requests
from concurrent.futures import ThreadPoolExecutor

from ..order.orderpackage import BaseOrderPackage, OrderPackageType

MAX_WORKERS = 32


class BaseExecution:

    EXCHANGE = None

    def __init__(self, flumine, max_workers=MAX_WORKERS):
        self.flumine = flumine
        self._thread_pool = ThreadPoolExecutor(max_workers=max_workers)

    def handler(self, order_package: BaseOrderPackage):
        """ Handles order_package, capable of place, cancel,
        replace and update.
        """
        http_session = requests.Session()  # todo keep
        if order_package.package_type == OrderPackageType.PLACE:
            func = self.execute_place
        elif order_package.package_type == OrderPackageType.CANCEL:
            func = self.execute_cancel
        elif order_package.package_type == OrderPackageType.REPLACE:
            func = self.execute_replace
        elif order_package.package_type == OrderPackageType.UPDATE:
            func = self.execute_update
        else:
            raise NotImplementedError()

        self._thread_pool.submit(func, order_package, http_session)

    def execute_place(
        self, order_package: BaseOrderPackage, http_session: requests.Session
    ) -> None:
        raise NotImplementedError

    def execute_cancel(
        self, order_package: BaseOrderPackage, http_session: requests.Session
    ) -> None:
        raise NotImplementedError

    def execute_update(
        self, order_package: BaseOrderPackage, http_session: requests.Session
    ) -> None:
        raise NotImplementedError

    def execute_replace(
        self, order_package: BaseOrderPackage, http_session: requests.Session
    ) -> None:
        raise NotImplementedError

    @property
    def handler_queue(self):
        return self.flumine.handler_queue

    @property
    def markets(self):
        return self.flumine.markets
