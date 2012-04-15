from sll.portlet.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_sll_portlet_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.portlet'))

    def test_browserlayer(self):
        from sll.portlet.browser.interfaces import ISllPortletLayer
        from plone.browserlayer import utils
        self.failUnless(ISllPortletLayer in utils.registered_layers())

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.portlet'])
        self.failIf(installer.isProductInstalled('sll.portlet'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.portlet'])
        from sll.portlet.browser.interfaces import ISllPortletLayer
        from plone.browserlayer import utils
        self.failIf(ISllPortletLayer in utils.registered_layers())