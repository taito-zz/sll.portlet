from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from string import Template
from zope.component import getMultiAdapter
from zope.i18nmessageid import MessageFactory
from zope.interface import implements


PLMF = MessageFactory('plonelocales')


class ISLLMapPortlet(IPortletDataProvider):
    """A portlet displaying a SLL map.
    """


class Assignment(base.Assignment):
    implements(ISLLMapPortlet)

    title = _(u'SLL Map')


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('sllmap.pt')

    areas = (
        {
            'area': "uusimaa",
            'coords': "49,189, 61,185, 63,186, 82,179, 82,186, 75,170, 63,176, 59,175, 57,180, 50,185, 49,189",
        },
        {
            'area': "kymenlaakso",
            'coords': "84,178, 88,177, 90,178, 94,175, 84,165, 82,165, 79,167, 78,170, 79,172, 83,177",
        },
        {
            'area': "etela-karjala",
            'coords': "96,173, 111,155, 109,155, 106,158, 104,159, 98,161, 96,163, 87,162, 89,164, 89,166, 88,166, 88,168, 90,171, 94,173",
        },
        {
            'area': "etela-savo",
            'coords': "87,165, 88,165, 88,164, 86,163, 86,161, 96,161, 99,159, 102,159, 108,155, 105,146, 100,141, 99,141, 98,142, 98,148, 93,147, 89,143, 85,143, 81,148, 83,157, 81,159, 81,161",
        },
        {
            'area': "pohjois-karjala",
            'coords': "109,153, 112,153, 120,141, 122,135, 122,133, 119,129, 110,121, 106,119, 98,119, 98,120, 100,123, 100,129, 103,133, 103,136, 100,139, 104,142, 107,146",
        },
        {
            'area': "pohjois-savo",
            'coords': "83,142, 90,142, 95,146, 97,146, 96,145, 96,142, 99,139, 99,137, 102,134, 99,130, 98,123, 90,117, 84,116, 81,119, 81,125, 80,125, 80,136, 83,138",
        },
        {
            'area': "keski-suomi",
            'coords': "69,127, 72,124, 74,124, 78,127, 78,130, 79,131, 79,138, 81,138, 81,142, 82,143, 82,145, 79,148, 79,151, 80,152, 80,156, 79,156, 78,155, 75,155, 72,157, 72,159, 70,159, 70,153, 68,153, 67,152, 67,146, 63,146, 63,144, 64,144, 67,141, 66,139, 66,132, 69,130",
        },
        {
            'area': "etela-hame",
            'coords': "64,175, 74,170, 77,169, 78,166, 80,165, 80,162, 79,161, 79,158, 77,156, 74,158, 72,161, 69,161, 68,163, 64,164, 61,167, 58,167, 55,165, 54,168, 54,175, 56,176, 60,174",
        },
        {
            'area': "varsinais-suomi",
            'coords': "39,167, 38,169, 38,173, 50,183, 56,182, 56,178, 52,175, 52,168, 43,170, 39,166",
        },
        {
            'area': "satakunta",
            'coords': "40,150, 40,163, 38,165, 41,165, 44,168, 49,167, 53,166, 53,165, 49,164, 47,162, 48,159, 49,155, 50,152, 47,149, 43,151, 40,150",
        },
        {
            'area': "pirkanmaa",
            'coords': "49,161, 49,162, 50,163, 54,163, 58,166, 63,164, 65,162, 67,162, 67,157, 68,156, 68,155, 66,154, 65,151, 66,150, 66,149, 63,147, 60,143, 56,144, 54,146, 50,146, 49,147, 49,149, 52,152, 51,154, 50,155, 50,160",
        },
        {
            'area': "pohjanmaa",
            'coords': "40,148, 44,149, 50,144, 54,144, 56,142, 65,142, 64,139, 64,131, 67,129, 68,126, 68,124, 60,112, 56,117, 51,118, 49,124, 49,127, 42,127, 41,133, 38,136, 39,149",
        },
        {
            'area': "pohjois-pohjanmaa",
            'coords': "73,87, 79,85, 87,85, 89,81, 92,84, 96,84, 98,82, 98,73, 104,73, 107,78, 108,84, 106,86, 106,88, 101,88, 92,95, 88,96, 88,99, 80,107, 83,112, 83,115, 79,119, 79,124, 75,123, 74,122, 69,122, 61,111, 69,101, 74,98",
        },
        {
            'area': "kainuu",
            'coords': "82,107, 90,100, 90,97, 102,90, 106,90, 106,101, 109,103, 109,107, 113,112, 113,114, 111,119, 108,119, 108,118, 104,117, 98,117, 96,119, 93,117, 88,115, 85,115, 85,111, 83,109",
        },
        {
            'area': "lappi",
            'coords': "69,85, 65,81, 63,76, 63,44, 47,27, 45,24, 50,20, 52,21, 57,31, 64,31, 66,29, 73,33, 77,27, 78,15, 82,10, 92,7, 100,15, 100,19, 98,23, 96,39, 101,43, 107,51, 100,64, 103,71, 98,71, 96,73, 97,76, 97,87, 96,82, 92,82, 90,80, 88,81, 86,84, 81,84, 80,83, 78,83, 77,84, 74,84, 72,86",
        },
    )

    @property
    def available(self):
        items = [area['area'] for area in self.areas]
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        portal = portal_state.portal()
        for item in items:
            if portal.get(item) is None:
                return False
        return True

    def script(self):
        template = """<script language="javascript" type="text/javascript">
    jQuery.noConflict();
    jQuery(document).ready(
        function(jq) {
            var map_overlay = jq("#map_overlay");
            map_overlay.hide();
            map_overlay.addClass("loading");
            map_overlay.fadeIn();

            var bgmap = {};
            jq("#map_imagemap > area").each(
                function() {
                    var id = jq(this).attr("id");
                    var offset = parseInt(jq(this).attr("id").split("_")[2], 10);
                    offset = (15-offset)*141;
                    var bgpos = String(offset) +"px 0px";
                    bgmap[id] = bgpos;
                }
            );

            var map_kartta_image = jq("#map_kartta_image");
            var map_hilight_image = jq("#map_hilight_image");

            var preload = new Array('$spinner_gif', '$transparent_gif', '$kartta_gif');
            var img = document.createElement('img');
            jq(img).bind(
                'load', function() {
                    if(preload[0]) {
                        this.src = preload.shift();
                    }  else {
                    /* all images have been loaded */
                        jq("#map_imagemap area").each(function() {
                            this.onmouseover = function() {
                                map_hilight_image.css("background-position", bgmap[jq(this).attr("id")]);
                                map_hilight_image.fadeIn("fast");
                            }
                        this.onmouseout = function() {
                            map_hilight_image.hide();
                        }
                    }
                );
                map_kartta_image.show();
                map_overlay.fadeOut(
                    "fast", function() {
                        jq(this).removeClass("loading");
                        jq("#map_background_image").fadeIn("fast");
                    }
                );
                jq("#map_background_image").css("background-image", "url($kartta_gif)");
                map_hilight_image.css("background-image", "url($kartta_gif)");
            }
        }
    ).trigger('load');
}
);
</script>"""
        s = Template(template)
        items = {
            'kartta_gif': '{0}/++resource++sll.portlet.images/kartta.gif'.format(self.portal_url),
            'spinner_gif': '{0}/spinner.gif'.format(self.portal_url),
            'transparent_gif': self.transparent_gif,
        }
        return s.substitute(items)

    @property
    def portal(self):
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        return portal_state.portal()

    @property
    def portal_url(self):
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        return portal_state.portal_url()

    def area_items(self):
        return [
            {
                'id': 'map_area_{0}'.format(self.areas.index(item)),
                'coords': item['coords'],
                'url': '{0}/{1}'.format(self.portal_url, item['area']),
            } for item in self.areas
        ]

    @property
    def transparent_gif(self):
        return '{0}/++resource++sll.portlet.images/transparent.gif'.format(self.portal_url)


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
