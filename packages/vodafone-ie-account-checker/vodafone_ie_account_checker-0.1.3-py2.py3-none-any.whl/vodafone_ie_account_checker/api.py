"""Main module."""

import logging
import requests

from lxml import html
from collections import namedtuple

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Account:
    """
    Represents a VF Account.
    """

    def __init__(self, username, password, token1, token2):
        """
        Defines an vf account.

        :param username: VF Broadband username (email)
        :param password: VF Broadband password
        :param token1: Token 1
        :param token2: Token 2
        """
        log.debug("Initialising new VF Account")

        if "@" not in username:
            log.warning("Vodafone Broadband username "
                        "should be an email address.")
        self.logged_in = False

        self._session = requests.Session()
        self.username = username
        self.password = password

        self.verification_token1 = token1
        self.verification_token2 = token2

        self.get_account_overview_request()

    def get_account_overview_request(self):
        """ Do the account overview request and return account tuple """

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': 'https://broadband.vodafone.ie',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; '
                          'Intel Mac OS X 10_15_4) '
                          'AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml'
                      ',application/xml;q=0.9,image/webp,'
                      'image/apng,*/*;q=0.8,application/'
                      'signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://broadband.vodafone.ie'
                       '/myaccount/session/login?t=1',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        params = (
            ('t', '1'),
        )

        # log.debug(f"self.verification_token1 {self.verification_token1}")
        # log.debug(f"self.verification_token2 {self.verification_token2}")

        cookies = {
            '__RequestVerificationToken': self.verification_token1,
        }

        data = {
            '__RequestVerificationToken': self.verification_token2,
            'emailAddress': self.username,
            'password': self.password
        }
        response = self._session.post('https://broadband.'
                                      'vodafone.ie/myaccount/session/login',
                                      headers=headers,
                                      cookies=cookies,
                                      params=params,
                                      data=data
                                      )

        self.log_session_info()
        tree = html.fromstring(response.content)

        # usage since date
        # e.g. ['Since 15 Apr 2020']
        usage_since = tree.xpath(
            '//*[@id="main"]/div/section/div[2]/section[1]/div/h2/text()')

        # data usage. e.g. ['397.35 GB']
        usage_value = tree.xpath(
            '//*[@id="main"]/div/section/div[2]/section[1]/div/div/div/'
            'strong/text()')

        if len(usage_since) == 0 or len(usage_value) == 0:
            log.warning("Unable to get usage data.")
            log.warning(response.content)
        else:
            AccountDetails = namedtuple("AccountDetails",
                                        ["usage_since", "usage_value"])
            accountDetails = AccountDetails(usage_since[0], usage_value[0])
            log.debug(accountDetails)
            self.logged_in = True
            return accountDetails

        return None

    def is_logged_in(self):
        """Returns true if a successful login has happened"""
        return self.logged_in

    def log_session_info(self):
        """ Log session cookies etc. """

        # log.debug("Session Cookies: " +
        #             str(self._session.cookies.get_dict()))
