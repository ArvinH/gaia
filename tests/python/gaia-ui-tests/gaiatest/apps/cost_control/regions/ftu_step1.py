# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from marionette.by import By
from gaiatest.apps.base import Base
from gaiatest.apps.cost_control.regions.ftu_step2 import FTUStep2


class FTUStep1(Base):

    _welcome_title_locator = (By.CSS_SELECTOR, 'h1[data-l10n-id="fte-welcome-title"]')
    _next_button_locator = (By.CSS_SELECTOR, '#step-1 button[data-l10n-id="next"]')

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        self.wait_for_condition(lambda m: m.find_element(*self._welcome_title_locator).location['x'] == 0)

    def tap_next(self):
        # TODO Remove the sleep when Bug 1013249 is fixed
        time.sleep(2)

        self.wait_for_element_displayed(*self._next_button_locator)
        self.marionette.find_element(*self._next_button_locator).tap()
        return FTUStep2(self.marionette)
