# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.Collage.interfaces import ICollageAlias
from Products.Collage.interfaces import IDynamicViewManager
from Products.Collage.viewmanager import mark_request
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from zope.interface import Interface, directlyProvides


class IKSSHelper(Interface):

    def getUniqueIdentifier():
        pass

    def getKssView():
        pass

    def getKssClasses(field_name):
        pass


class KSSHelper(BrowserView):
    """To better support various Plone environments we implement
    this view to help generate the right inline-editing bindings."""

    def getUniqueIdentifier(self):
        return self.context.UID()

    def getKssView(self):
        return self.context.restrictedTraverse('@@kss_field_decorator_view')

    def getKssClasses(self, field_name):
        kss = self.getKssView()

        # choose appropriate kss class generator depending on rendering mode
        if self.request.get('URL').endswith('/replaceField'):
            get_classes = kss.getKssClasses
        else:
            get_classes = kss.getKssClassesInlineEditable

        editing_classes = get_classes(
            field_name,
            templateId='kss_collage_macro_proxy',
            macro=field_name,
            target="%s-%s" % (field_name, self.getUniqueIdentifier())
        )
        uid_class = kss.getKssUIDClass()
        return " ".join((editing_classes, uid_class))


class CollageMacrosView(BrowserView):
    """This helper view looks up the current view for the context-object
    and returns it without rendering it."""

    @property
    def __call__(self):
        context = aq_inner(self.context)

        manager = IDynamicViewManager(context)
        layout = manager.getLayout()

        if not layout:
            layout, title = manager.getDefaultLayout()

        if ICollageAlias.providedBy(context):
            context = context.get_target()

            # if not set, revert to self.context
            if not context:
                context = self.context

        # transmute request interfaces
        ifaces = mark_request(self.context, self.request)

        view = getMultiAdapter((context, self.request), name=layout)

        # restore interfaces
        directlyProvides(self.request, ifaces)

        return view.index


class DummyFieldsView(BrowserView):

    def getKssUIDClass(self):
        return ''

    def getKssClassesInlineEditable(self, *args, **kwargs):
        return ''

    def getKssClasses(self, *args, **kwargs):
        return ''
