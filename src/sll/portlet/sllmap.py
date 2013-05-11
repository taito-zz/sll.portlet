from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from sll.portlet import _
from sll.portlet.config import AREAS
from string import Template
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from zope.schema import TextLine


class ISLLMapPortlet(IPortletDataProvider):
    """A portlet displaying a SLL map.
    """

    name = TextLine(
        title=_(u"Name of Portlet"),
        default=u"",
        required=False)


class Assignment(base.Assignment):
    implements(ISLLMapPortlet)

    name = u""

    def __init__(self, name=u""):
        self.name = name

    def title(self):
        return self.name or _(u'SLL Map')


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('sllmap.pt')

    areas = AREAS

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
        template = """<script type="text/javascript">
    jq(function() {
        var map_overlay = jq("#map_overlay");
        map_overlay.hide();
        map_overlay.addClass("loading");
        map_overlay.fadeIn();
        var bgmap = {};

        jq("#map_imagemap > area").each(function() {
            var id = jq(this).attr("id");
            var offset = parseInt(jq(this).attr("id").split("_")[2], 10);
            offset = (15-offset)*141;
            var bgpos = String(offset) +"px 0px";
            bgmap[id] = bgpos;
        });

        var map_kartta_image = jq("#map_kartta_image");
        var map_hilight_image = jq("#map_hilight_image");
        var preload = new Array('$spinner_gif', '$transparent_gif', '$kartta_img');
        var img = document.createElement('img');

        jq(img).bind('load', function() {
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
                });
                map_kartta_image.show();
                map_overlay.fadeOut("fast", function() {
                    jq(this).removeClass("loading");
                    jq("#map_background_image").fadeIn("fast");
                });
                jq("#map_background_image").css("background-image", "url($kartta_img)");
                map_hilight_image.css("background-image", "url($kartta_img)");
            }
        }).trigger('load');
    });
</script>"""
        s = Template(template)
        items = {
            'kartta_img': '{0}/++resource++sll.portlet.images/kartta.png'.format(self.portal_url),
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
                'title': self.portal[item['area']].Title(),
            } for item in self.areas
        ]

    @property
    def transparent_gif(self):
        return '{}/++resource++sll.portlet.images/transparent.png'.format(self.portal_url)

    def title(self):
        return self.data.name or self.data.title()

    def is_ie(self):
        if 'MSIE' in self.request.get('HTTP_USER_AGENT', ''):
            return True


class AddForm(base.AddForm):

    form_fields = form.Fields(ISLLMapPortlet)
    label = _(u"Add SLL Map Portlet")
    description = _(u"This portlet display a SLL map.")

    def create(self, data):
        return Assignment(name=data.get('name', u""))


class EditForm(base.EditForm):
    form_fields = form.Fields(ISLLMapPortlet)
    label = _(u"Edit SLL Map Portlet")
    description = _(u"This portlet display a SLL map.")
