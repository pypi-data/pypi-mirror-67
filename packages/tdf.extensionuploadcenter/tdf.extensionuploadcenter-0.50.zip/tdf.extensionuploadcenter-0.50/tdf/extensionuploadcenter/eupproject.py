# -*- coding: utf-8 -*-
import re

from Products.CMFPlone.utils import safe_unicode
from tdf.extensionuploadcenter import _, quote_chars

from collective import dexteritytextindexer
from plone import api
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.browser.view import DefaultView
from plone.namedfile.field import NamedBlobFile, NamedBlobImage
from plone.supermodel import model
from plone.supermodel.directives import primary
from plone.uuid.interfaces import IUUID
from z3c.form import validator
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema
from zope.interface import Invalid, directlyProvides, invariant, provider
from zope.schema.interfaces import (IContextAwareDefaultFactory,
                                    IContextSourceBinder)
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


def vocabCategories(context):
    # For add forms

    # For other forms edited or displayed
    from tdf.extensionuploadcenter.eupcenter import IEUpCenter
    while context is not None and not IEUpCenter.providedBy(context):
        # context = aq_parent(aq_inner(context))
        context = context.__parent__

    category_list = []
    if context is not None and context.available_category:
        category_list = context.available_category

    terms = []
    for value in category_list:
        terms.append(SimpleTerm(value, token=value.encode('unicode_escape'),
                                title=value))

    return SimpleVocabulary(terms)


directlyProvides(vocabCategories, IContextSourceBinder)


def isNotEmptyCategory(value):
    if not value:
        raise Invalid(safe_unicode(
            'You have to choose at least one category for your '
            'project.'))
    return True


checkEmail = re.compile(
    r"[a-zA-Z0-9._%-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}").match


def validateEmail(value):
    if not checkEmail(value):
        raise Invalid(_(safe_unicode("Invalid email address")))
    return True


@provider(IContextAwareDefaultFactory)
def allowedeupimagefileextensions(context):
    return context.allowed_eupimagefileextension.replace("|", ", ")


def validateimagefileextension(value):
    catalog = api.portal.get_tool(name='portal_catalog')
    result = catalog.uniqueValuesFor('allowedeupimagefileextensions')
    pattern = r'^.*\.({0})'.format(result[0])
    matches = re.compile(pattern, re.IGNORECASE).match
    if not matches(value.filename):
        raise Invalid(safe_unicode(
            'You could only upload files with an allowed file extension. '
            'Please try again to upload a file with the correct file'
            'extension.'))
    return True


@provider(IContextAwareDefaultFactory)
def allowedeupdocfileextensions(context):
    return context.allowed_docfileextension.replace("|", ", ")


def validatedocfileextension(value):
    catalog = api.portal.get_tool(name='portal_catalog')
    result = catalog.uniqueValuesFor('allowedeupdocfileextensions')
    pattern = r'^.*\.({0})'.format(result[0])
    matches = re.compile(pattern, re.IGNORECASE).match
    if not matches(value.filename):
        raise Invalid(safe_unicode(
            'You could only upload documentation files with an allowed '
            'file extension. Please try again to upload a file with the '
            'correct file extension.'))
    return True


class ProvideScreenshotLogo(Invalid):
    __doc__ = _(safe_unicode(
        "Please add a screenshot or a logo to your project. You find "
        "the appropriate fields below on this page."))


class MissingCategory(Invalid):
    __doc__ = _(safe_unicode(
        "You have not chosen a category for the project."))


class IEUpProject(model.Schema):
    directives.mode(information="display")
    information = schema.Text(
        title=_(safe_unicode("Information")),
        description=_(safe_unicode(
            "The Dialog to create a new project consists of "
            "different register. Please go through this register "
            "and fill in the appropriate data for your project. "
            "The register 'Documentation' and its fields are "
            "optional."))
    )

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(safe_unicode("Title")),
        description=_(safe_unicode(
            "Project Title - minimum 5 and maximum 50 characters")),
        min_length=5,
        max_length=50
    )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
        title=_(safe_unicode("Project Summary")),
    )

    dexteritytextindexer.searchable('details')
    primary('details')
    details = RichText(
        title=_(safe_unicode("Full Project Description")),
        required=False
    )

    model.fieldset('Categories',
                   label='Category / Categories',
                   fields=['category_choice']
                   )

    model.fieldset('logo_screenshot',
                   label='Logo / Screenshot',
                   fields=['eupimageextension', 'project_logo',
                           'eupimageextension1', 'screenshot']
                   )

    model.fieldset('documentation',
                   label='Documentation',
                   fields=['documentation_link', 'eupdocextension',
                           'documentation_file']
                   )

    dexteritytextindexer.searchable('category_choice')
    directives.widget(category_choice=CheckBoxFieldWidget)
    category_choice = schema.List(
        title=_(safe_unicode("Choose your categories")),
        description=_(safe_unicode(
            "Please select the appropriate categories (one or "
            "more) for your project.")),
        value_type=schema.Choice(source=vocabCategories),
        constraint=isNotEmptyCategory,
        required=True
    )

    contactAddress = schema.TextLine(
        title=_(safe_unicode("Contact email-address")),
        description=_(safe_unicode(
            "Contact email-address for the project.")),
        constraint=validateEmail
    )

    homepage = schema.URI(
        title=_(safe_unicode("Homepage")),
        description=_(safe_unicode(
            "If the project has an external home page, enter its "
            "URL (example: 'http://www.mysite.org').")),
        required=False
    )

    documentation_link = schema.URI(
        title=_(safe_unicode("URL of documentation repository ")),
        description=_(safe_unicode(
            "If the project has externally hosted "
            "documentation, enter its URL "
            "(example: 'http://www.mysite.org').")),
        required=False
    )

    directives.mode(eupdocextension='display')
    eupdocextension = schema.TextLine(
        title=_(safe_unicode(
            'The following file extensions are allowed for documentation '
            'files (upper case and lower case and mix of both):')),
        defaultFactory=allowedeupdocfileextensions,
    )

    documentation_file = NamedBlobFile(
        title=_(safe_unicode("Dokumentation File")),
        description=_(safe_unicode(
            "If you have a Documentation in the file format 'PDF' "
            "or 'ODT' you could add it here.")),
        required=False,
        constraint=validatedocfileextension
    )

    directives.mode(eupimageextension='display')
    eupimageextension = schema.TextLine(
        title=_(safe_unicode(
            'The following file extensions are allowed for project logo '
            'files (upper case and lower case and mix of both):')),
        defaultFactory=allowedeupimagefileextensions,
    )

    project_logo = NamedBlobImage(
        title=_(safe_unicode("Logo")),
        description=_(safe_unicode(
            "Add a logo for the project (or organization/company) "
            "by clicking the 'Browse' button. You could provide "
            "an image of the file format 'png', 'gif' or 'jpg'.")),
        required=False,
        constraint=validateimagefileextension
    )

    directives.mode(eupimageextension1='display')
    eupimageextension1 = schema.TextLine(
        title=_(safe_unicode(
            'The following file extensions are allowed for screenshot '
            'files (upper case and lower case and mix of both):')),
        defaultFactory=allowedeupimagefileextensions,
    )

    screenshot = NamedBlobImage(
        title=_(safe_unicode("Screenshot of the Extension")),
        description=_(safe_unicode(
            "Add a screenshot by clicking the 'Browse' button. You "
            "could provide an image of the file format 'png', "
            "'gif' or 'jpg'.")),
        required=False,
        constraint=validateimagefileextension
    )

    @invariant
    def missingScreenshotOrLogo(data):
        if not data.screenshot and not data.project_logo:
            raise ProvideScreenshotLogo(
                _(safe_unicode(
                    'Please add a screenshot or a logo '
                    'to your project page. You will '
                    'find the appropriate fields below '
                    'on this page.')))


def notifyProjectManager(self, event):
    state = api.content.get_state(self)
    if self.__parent__.contactForCenter is not None:
        mailsender = str(self.__parent__.contactForCenter)
    else:
        mailsender = api.portal.get_registry_record('plone.email_from_address')
    api.portal.send_email(
        recipient="{}".format(self.contactAddress),
        sender=safe_unicode(
            "{} <{}>").format('Admin of the Website', mailsender),
        subject=safe_unicode("Your Project {}").format(self.title),
        body=(safe_unicode(
            "The status of your LibreOffice extension project changed. "
            "The new status is {}")).format(state)
    )


def notifyProjectManagerReleaseAdd(self, event):
    if self.__parent__.contactForCenter is not None:
        mailrecipient = str(self.__parent__.contactForCenter)
    else:
        mailrecipient = api.portal.get_registry_record(
            'plone.email_from_address')
    api.portal.send_email(
        recipient="{}".format(self.contactAddress),
        sender=safe_unicode(
            "{} <{}>").format('Admin of the Website', mailrecipient),
        subject=safe_unicode(
            "Your Project [{}: new Release added").format(self.title),
        body=(safe_unicode(
            "A new release was added to your project: "
            "'{}'")).format(self.title),
    )


def notifyProjectManagerReleaseLinkedAdd(self, event):
    if self.__parent__.contactForCenter is not None:
        mailrecipient = str(self.__parent__.contactForCenter)
    else:
        mailrecipient = api.portal.get_registry_record(
            'plone.email_from_address')
    api.portal.send_email(
        recipient="{}".format(self.contactAddress),
        sender=safe_unicode(
            "{} <{}>").format('Admin of the Website', mailrecipient),
        subject=(safe_unicode(
            "Your Project {}: new linked Release "
            "added")).format(self.title),
        body=(safe_unicode(
            "A new linked release was added to your "
            "project: '{}'")).format(self.title),
    )


def notifyAboutNewReviewlistentry(self, event):
    state = api.content.get_state(self)
    if self.__parent__.contactForCenter is not None:
        mailrecipient = str(self.__parent__.contactForCenter)
    else:
        mailrecipient = api.portal.get_registry_record(
            'plone.email_from_address')

    if state == "pending":
        api.portal.send_email(
            recipient=mailrecipient,
            subject=(safe_unicode(
                "A Project with the title {} was added to the review "
                "list")).format(self.title),
            body="Please have a look at the review list and check if the "
                 "project is ready for publication. \n"
                 "\n"
                 "Kind regards,\n"
                 "The Admin of the Website"
        )


def textmodified_project(self, event):
    state = api.content.get_state(self)
    if self.__parent__.contactForCenter is not None:
        mailrecipient = str(self.__parent__.contactForCenter)
    else:
        mailrecipient = api.portal.get_registry_record(
            'plone.email_from_address')
    if state == "published":
        if self.details is not None:
            detailed_description = self.details.output
        else:
            detailed_description = None

        api.portal.send_email(
            recipient=mailrecipient,
            sender=safe_unicode(
                "{} <{}>").format('Admin of the Website', mailrecipient),
            subject=(safe_unicode(
                "The content of the project {} has "
                "changed")).format(self.title),
            body=(safe_unicode(
                "The content of the project {} has changed. Here you get "
                "the text of the description field of the "
                "project: \n'{}\n\nand this is the text of the "
                "details field:\n{}'")).format(self.title,
                                               self.description,
                                               detailed_description),
        )


def notifyAboutNewProject(self, event):
    if self.__parent__.contactForCenter is not None:
        mailrecipient = str(self.__parent__.contactForCenter),
    else:
        mailrecipient = api.portal.get_registry_record(
            'plone.email_from_address')
    api.portal.send_email(
        recipient=mailrecipient,
        subject=safe_unicode(
            "A Project with the title {} was added").format(self.title),
        body="A member added a new project"
    )


class ValidateEUpProjectUniqueness(validator.SimpleFieldValidator):
    # Validate site-wide uniqueness of project titles.

    def validate(self, value):
        # Perform the standard validation first
        from tdf.extensionuploadcenter.eupsmallproject import IEUpSmallProject

        super(ValidateEUpProjectUniqueness, self).validate(value)
        if value is not None:
            catalog = api.portal.get_tool(name='portal_catalog')
            results1 = catalog({'Title': quote_chars(value),
                                'object_provides':
                                    IEUpProject.__identifier__, })
            results2 = catalog({'Title': quote_chars(value),
                                'object_provides':
                                    IEUpSmallProject.__identifier__, })
            results = results1 + results2

            contextUUID = IUUID(self.context, None)
            for result in results:
                if result.UID != contextUUID:
                    raise Invalid(_(safe_unicode(
                        "The project title is already in use.")))


validator.WidgetValidatorDiscriminators(
    ValidateEUpProjectUniqueness,
    field=IEUpProject['title'],
)


class EUpProjectView(DefaultView):

    def all_releases(self):
        """Get a list of all releases, ordered by version, starting with
           the latest.
        """

        catalog = api.portal.get_tool(name='portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        res = catalog.searchResults(
            portal_type=('tdf.extensionuploadcenter.euprelease',
                         'tdf.extensionuploadcenter.eupreleaselink'),
            path=current_path,
            sort_on='Date',
            sort_order='reverse')
        return [r.getObject() for r in res]

    def latest_release(self):
        """Get the most recent final release or None if none can be found.
        """

        context = self.context
        res = None
        catalog = api.portal.get_tool('portal_catalog')

        res = catalog.searchResults(
            portal_type=('tdf.extensionuploadcenter.euprelease',
                         'tdf.extensionuploadcenter.eupreleaselink'),
            path='/'.join(context.getPhysicalPath()),
            review_state='final',
            sort_on='effective',
            sort_order='reverse')

        if not res:
            return None
        else:
            return res[0].getObject()

    def latest_release_date(self):
        """Get the date of the latest release
        """

        latest_release = self.latest_release()
        if latest_release:
            return self.context.toLocalizedTime(latest_release.effective())
        else:
            return None

    def latest_unstable_release(self):

        context = self.context
        res = None
        catalog = api.portal.get_tool('portal_catalog')

        res = catalog.searchResults(
            portal_type=('tdf.extensionuploadcenter.euprelease',
                         'tdf.extensionuploadcenter.eupreleaselink'),
            path='/'.join(context.getPhysicalPath()),
            review_state=('alpha', 'beta', 'release-candidate'),
            sort_on='effective',
            sort_order='reverse')

        if not res:
            return None
        else:
            return res[0].getObject()

    def projectCategory(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        path = "/".join(self.context.getPhysicalPath())
        idx_data = catalog.getIndexDataForUID(path)
        category = idx_data.get('getCategories')
        return (r for r in category)
