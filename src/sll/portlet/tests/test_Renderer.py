from sll.portlet.tests.base import IntegrationTestCase
from zope.publisher.browser import TestRequest

import mock


class TestRenderer(IntegrationTestCase):
    """TestCase for Renderer class."""

    def setUp(self):
        self.portal = self.layer['portal']

    def createInstance(self):
        from sll.portlet.sllmap import Renderer
        return Renderer(self.portal, TestRequest(), None, None, None)

    @mock.patch('sll.portlet.sllmap.getMultiAdapter')
    def test_renderer__available__False(self, getMultiAdapter):
        instance = self.createInstance()
        getMultiAdapter().portal.return_value = {}
        self.assertFalse(instance.available)

    @mock.patch('sll.portlet.sllmap.getMultiAdapter')
    def test_renderer_available__True(self, getMultiAdapter):
        instance = self.createInstance()
        getMultiAdapter().portal.return_value = {
            'uusimaa': mock.Mock(),
            'kymenlaakso': mock.Mock(),
            'etela-karjala': mock.Mock(),
            'etela-savo': mock.Mock(),
            'pohjois-karjala': mock.Mock(),
            'pohjois-savo': mock.Mock(),
            'keski-suomi': mock.Mock(),
            'etela-hame': mock.Mock(),
            'varsinais-suomi': mock.Mock(),
            'satakunta': mock.Mock(),
            'pirkanmaa': mock.Mock(),
            'pohjanmaa': mock.Mock(),
            'pohjois-pohjanmaa': mock.Mock(),
            'kainuu': mock.Mock(),
            'lappi': mock.Mock(),
        }
        self.assertTrue(instance.available)

    @mock.patch('sll.portlet.sllmap.getMultiAdapter')
    def test_script(self, getMultiAdapter):
        instance = self.createInstance()
        getMultiAdapter().portal_url.return_value = 'URL'
        self.assertEqual(
            instance.script().split('\n')[0],
            '<script type="text/javascript">'
        )

    @mock.patch('sll.portlet.sllmap.getMultiAdapter')
    def test_portal(self, getMultiAdapter):
        instance = self.createInstance()
        portal = mock.Mock()
        getMultiAdapter().portal.return_value = portal
        self.assertEqual(
            instance.portal,
            portal
        )

    @mock.patch('sll.portlet.sllmap.getMultiAdapter')
    def test_area_items(self, getMultiAdapter):
        instance = self.createInstance()
        title = mock.Mock()
        getMultiAdapter().portal.return_value = {
            'uusimaa': title,
            'kymenlaakso': title,
            'etela-karjala': title,
            'etela-savo': title,
            'pohjois-karjala': title,
            'pohjois-savo': title,
            'keski-suomi': title,
            'etela-hame': title,
            'varsinais-suomi': title,
            'satakunta': title,
            'pirkanmaa': title,
            'pohjanmaa': title,
            'pohjois-pohjanmaa': title,
            'kainuu': title,
            'lappi': title,
        }
        getMultiAdapter().portal_url.return_value = 'URL'
        self.assertEqual(
            len(instance.area_items()),
            15
        )
        self.assertEqual(
            instance.area_items()[0],
            {
                'coords': '49,189, 61,185, 63,186, 82,179, 82,186, 75,170, 63,176, 59,175, 57,180, 50,185, 49,189',
                'id': 'map_area_0',
                'title': title.Title(),
                'url': 'URL/uusimaa',
            }
        )
        self.assertEqual(
            instance.area_items()[14],
            {
                'coords': '69,85, 65,81, 63,76, 63,44, 47,27, 45,24, 50,20, 52,21, 57,31, 64,31, 66,29, 73,33, 77,27, 78,15, 82,10, 92,7, 100,15, 100,19, 98,23, 96,39, 101,43, 107,51, 100,64, 103,71, 98,71, 96,73, 97,76, 97,87, 96,82, 92,82, 90,80, 88,81, 86,84, 81,84, 80,83, 78,83, 77,84, 74,84, 72,86',
                'id': 'map_area_14',
                'title': title.Title(),
                'url': 'URL/lappi',
            }
        )

    def test_is_ie(self):
        instance = self.createInstance()
        instance.request = {'HTTP_USER_AGENT': ['MSIE']}
        self.assertTrue(instance.is_ie())
