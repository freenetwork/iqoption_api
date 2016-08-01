# -*- coding: utf-8 -*-
"""Module for IQ option buy websocket chanel."""

from iqoption_api.chanel import Chanel


class Buy(Chanel):
    # pylint: disable=too-few-public-methods
    """Class for IQ option buy websocket chanel."""

    name = "buy"

    def __call__(self, time, show_value, skey):
        """Method to send message to buy websocket chanel.

        :param msg: The websocket buy chanel message.
        """
        
        self.exp = None
        
        if (time%60) > 29:
            self.exp = time + (60-(time%60)) + 60
        else:
            self.exp = time + (60-(time%60))

        data = dict(price=10,
                    refund_value=0,
                    act=99,
                    exp=self.exp,
                    type="turbo",
                    direction="call",
                    value=show_value,
                    time=time)
                    skey=skey)

        self.send_wss_request(self.name, data)
