from Products.CMFCore.utils import getToolByName
from sll.portlet.tests.base import IntegrationTestCase


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

    def test_cssregistry(self):
        portal_css = getToolByName(self.portal, 'portal_css')
        self.assertTrue(
            '++resource++sll.portlet.stylesheets/portlet.css' in portal_css.getResourceIds()
        )

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

    def test_uninstall__cssregistry(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.portlet'])
        portal_css = getToolByName(self.portal, 'portal_css')
        self.assertFalse(
            '++resource++sll.portlet.stylesheets/portlet.css' in portal_css.getResourceIds()
        )
