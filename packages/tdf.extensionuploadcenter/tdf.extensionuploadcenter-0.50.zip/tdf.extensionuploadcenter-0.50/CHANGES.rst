Changelog
=========

0.50 (2020-04-29)
-----------------

- Move strings of tupsmallproject module from unicode to
  save_unicode [Andreas Mantke]
- Update localization files [Andreas Mantke]
- Pep8 fixes [Andreas Mantke]


0.49 (2020-03-30)
-----------------

- Add a missing defaultFactory to mailextprojectowner.py [Andreas Mantke]


0.48 (2020-03-30)
-----------------

- Pep8 fixes
- Add a new module for a mail form to get in contact with project owner and
  link it from project pages. Link the mail to project author form from the
  extension center view [Andreas Mantke]
- Update localization files and localization into German [Andreas Mantke]


0.47 (2020-02-08)
-----------------

- Add the latest version of LibreOffice to the eupcenter
  module [Andreas Mantke]
- Add information about messaging for small extension
  projects and update the HTML and PDF versions of the user
  documentation [Andreas Mantke]
- Update localization files [Andreas Mantke]
- Change to @implementer in the releasecustomurl module for Python-3
  compatibility [Andreas Mantke]
- Change the messagefactory entry for compatiblity to current Plone
  versions [Andreas Mantke]
- Update the mailtoauthor module for compatibility with current Plone
  versions and Python-3


0.46 (2020-01-13)
-----------------

- Smaller text fixes in the user documentation and update the
  documentation in HTML and PDF file format [Andreas Mantke]
- Update localization files and German localization [Andreas Mantke]


0.45 (2020-01-01)
-----------------

- Changed bullet list style in the readme [Andreas Mantke]
- Fix typo in installation.rst [Andreas Mantke]
- Update user documentation in HTML and PDF file format [Andreas Mantke]


0.44 (2019-12-30)
-----------------

- Changed list bullets in the readme [Andreas Mantke]


0.43 (2019-12-30)
-----------------

- Bind project publication workflow to small extension
  projects too [Andreas Mantke]
- Move CHANGES.txt, README and LICENSE to the main directory [Andreas Mantke]
- Change CHANGES.txt to rst file type [Andreas Mantke]
- Add interface module with new interface and browserlayer.xml for
  install and unistall and use it in configure.zcml [Andreas Mantke]
- Reorder the edit form of the extension center module with further
  register [Andreas Mantke]
- Add user documentation and create a HTML and a PDF version
  of it [Andreas Mantke]
- Adapt the MANIFEST.in to the current structure of the add-on [Andreas Mantke]



0.42 (2019-09-21)
-----------------

- Pep8 fixes [Andreas Mantke]
- Update localization files [Andreas Mantke]


0.41 (2019-09-15)
-----------------

- Fix a typo in the notifications module [Andreas Mantke]
- Pep8 fixes [Andreas Mantke]
- Update localization files and German localization. [Andreas Mantke]


0.40 (2019-09-07)
-----------------

- Fix the name of the searched portal_catalog index in the
  notifications module [Andreas Mantke]


0.39 (2019-09-05)
-----------------

- Improve the message to the sender of the contact to author
  form. [Andreas Mantke]
- Send notifications about a new product version not to all users of
  the site, but only to the project contact addresses. [Andreas Mantke]
- Update localization files and German localization. [Andreas Mantke]


0.38 (2019-08-22)
-----------------

- Add a further table class from the Barceloneta theme for
  listing tables to the project view. [Andreas Mantke]
- Move 'contact the author' to the sidebar [Andreas Mantke]
- Fix description and title strings in the center module [Andreas Mantke]
- Update localization for string changes [Andreas Mantke]



0.37 (2019-08-17)
-----------------

- Fix css classes in project view [Andreas Mantke]
- Fix regular expressions for validation of file extensions [Andreas Mantke]



0.36 (2019-08-01)
-----------------

- Add a title to fields description and product_description of the
  eupcenter and remove their description entry [Andreas Mantke]
- Add fields to submit allowed image, documentation and extension
  file extensions instead of formerly hard coded file extensions
  for them to give more flexibility to the site administrator
  [Andreas Mantke]
- Add new indexes to the portal_catalog to hold the values of
  allowed image, documentation and extension file extensions
  [Andreas Mantke]
- Create new validators for image and documentation file extensions
  inside the eupproject and the eupsmallproject modules and move
  the validation to this validators [Andreas Mantke]
- Create new validators for extension file extensions inside the
  euprelease, the tuplinkedrelease module and the eupsmallproject
  module. Move the validation to this validators [Andreas Mantke]
- Add new fields to display the currently allowed image, documentation
  and extension file extensions to the eupproject, the eupsmallproject,
  the euprelease and the euplinkedrelease [Andreas Mantke]
- Remove old and unnecessary functions for the validation of
  image, documentation and template file extensions [Andreas Mantke]
- Update localization template, Spanish localization file and
  German translation file [Andreas Mantke]
- Add fields and a fieldset for documentation to the
  smallextensionsproject module [Andreas Mantke]
- Fix translation tags in project view [Andreas Mantke]



0.35 (2019-07-17)
-----------------

- Fix an import in the mailtoauthor module [Andreas Mantke]
- Improve portal_catalog search for projects, if the text search
  field stays empty [Andreas Mantke]


0.34 (2019-06-12)
-----------------

- Project view for stable releases changed thus a release date is only
  shown, if there is a publishing date for a release within a
  project available. {Andreas Mantke]
- Update localization template and German translation and Spanish
  localization file [Andreas Mantke]


0.33 (2019-05-30)
-----------------

- Change fallback email sender and recipient from hard coded to the variable
  site email address [Andreas Mantke]
- Remove redundant source code [Andreas Mantke]
- Update localization template and German translation and Spanish
  localization file [Andreas Mantke]


0.32 (2019-05-12)
-----------------

- Add a new email form to send feedback to a project author with recaptcha
  protection and link it from the project and the smallproject
  view [Andreas Mantke]
- Pep8 fixes [Andreas Mantke]
- Update localization template, Spanish localization file and German
  localization [Andreas Mantke]



0.30 (2019-04-11)
-----------------

- Add a missing entry for small extension projects in the search for newest
  projects [Andreas Mantke]
- CSS fix [Andreas Mantke]
- Structure the eupproject edit mode with register [Andreas Mantke]
- Update German localization [Andreas Mantke]
- Improve the edit dialog and split it into more register for the release and
  the linked release module. [Andreas Mantke]



0.29 (2019-03-28)
-----------------

- Improve the view and the search features of the eupcenter and include the new
  module for smalll projects in the search and listing [Andreas Mantke]
- Add the install instructions to the ressources of the new module for small
  projects view [Andreas Mantke]


0.28 (2019-03-24)
-----------------

- Add a new module for small extension projects [Andreas Mantke]
- New function to search and display categories for extension
  projects and small extension projects [Andreas Mantke]
- Update German localization [Andreas Mantke]


0.27 (2018-12-09)
-----------------

- CSS fix [Andreas Mantke]
- PEP8 fixes [Andreas Mantke]
- Change over to supermodel.directives for primary fields and fieldsets [Andreas Mantke]
- Change from plone.directives form.mode to plone.autoform directives.mode [Andreas Mantke]


0.26 (2018-11-18)
-----------------

- Move the messaging about the creation of new projects to
  the eupprojects module [Andreas Mantke]
- Changed the email address for notifications about projects and (linked) releases
  from hard coded to variable and added a validation for the email address [Andreas Mantke]
- Improve the extension project workflow [Andreas Mantke]
- Update German localization [Andreas Mantke]


0.25 (2018-10-24)
-----------------

- Moved changelog to CHANGES.txt [Andreas Mantke]
- Move CSS styles for tables on eupproject view from inline
  style to the stylesheet file and improve the styles
  [Andreas Mantke]
- Added a new notify subscriber for modifications of
  projects to get an information about the content of
  the text fields. The content of the text fields will
  be forwarded by email. [Andreas Mantke]
- Add specific workflow permissions for private project
  objects.[Andreas Mantke]
- Update buildout.cfg and plone.cfg to Plone 5.1 [Andreas Mantke]


0.24 (2018-08-28)
-----------------

- Add a function for search and display the compatibility from the indexes of
  the portal_catalog [Andreas Mantke]
- Add an optional field to give users an information how to search for older
  versions, if they are removed from the compatibility list in the eupcenter.py
  [Andreas Mantke]
- Update of the internationalization template and the po-files for the
  German and Spanish language [Andreas Mantke]


0.23 (2018-08-11)
-----------------

- Marked some message strings as utf-8. [Andreas Mantke]


0.22 (2018-08-08)
-----------------

- A type_id issue fixed in the project workflow [Andreas Mantke]
- Fixed some strings in the modules eupcenter, eupproject, euprelease
  and eupreleaselink [Andreas Mantke]
- Update of localization to German after string changes [Andreas Mantke]


0.21 (2018-08-01)
-----------------

- Added a workflow for extension projects [Andreas Mantke]
- Update of the localization to German. [Andreas Mantke]


0.20 (2018-07-21)
-----------------

- Removed a redundant link from the linked release view [Andreas Mantke]
- Added download links for unstable release files to the project view, which
  are displayed, if there is no stable release [Andreas Mantke]
- Add an information about the current status to the message for the
  project manager, send for changing the workflow state. [Andreas Mantke]


0.19 (2018-06-24)
-----------------

- Adding a function to collect the latest unstable release and a slot in
  the project view to present such releases to the user [Andreas Mantke]
- Fixed link to the documentation file in the project view [Andreas Mantke]
- Updated string format handling to modern method in eupcenter.py, eupproject.py,
  euprelease.py, eupreleaselink.py and bootstrap.py [Andreas Mantke]
- Add a function for search and display the license from the indexes of
  the portal_catalog [Andreas Mantke]
- Update of the localization to German [Andreas Mantke]




0.18 (2018-01-30)
-----------------

- Heading for release details and changelog will be hidden in the
  eupreleases and eupreleaseslink view, if there is no content for
  this topics [Andreas Mantke]
- Update versions of LibreOffice [Andreas Mantke]
- Add a further explanation for publishing a release and linked release
  and a link to the advanced state change. [Andreas Mantke]
- Update of the internationalization template and the po-files for the
  German and Spanish language [Andreas Mantke]



0.17 (2018-01-07)
-----------------

- Fixed Tal-expression in views of release and linked release [Andreas Mantke]


0.16a0 (2017-09-18)
-------------------

-

0.16 (2017-09-18)
-----------------

- Notification about a new entry in the review list added to help the reviewer. [Andreas Mantke].


0.15 (2017-04-11)
-----------------

- Fixed a condition for linked releases on project view [Andreas Mantke]
- Project screenshot will be displayed in large scale with a mouse click [Andreas Mantke]
- Improve the messaging for new projects according to the review status. [Andreas Mantke]
- Remove two not necessary i18n-domain declarations [Andreas Mantke]
- Fixed typo in the add on extension command in own_project.pt [Andreas Mantke]
- Fixed issue in command for listing of projects of current user [Andresa Mantke]
- Fixed listing of eupreleases and linked eupreleases and the display of the latest
  final (linked) release on the project page [Andreas Mantke]
- Update localisation template and localisation into German [Andreas Mantke]


0.14 (2017-03-02)
-----------------

- Add a displayed title to the further file upload sections of a release [Andreas Mantke]
- Create a fieldset for every further linked file of a linked release and the associated fields [Andreas Mantke]
- Add an index for the project contact address to the portal catalog [Andreas Mantke]
- Add a field for uploaded project documentation and display it, add more translation tags
  to project view [Anddreas Mantke]
- Update localisation template and German localisation [Andreas Mantke]
- Improvement for the error messages and instructions on eupprojects [Andreas Mantke]
- Better error messages on eupreleases and linked eupreleases [Andreas Mantke]
- Fix catalog search to the Title index in case of special () characters [Victor Fernandez de Alba]
- Added a description to the install instructions field and removed the default value (text) [Andreas Mantke]
- Add guard in case that a malformed query was entered, return empty record [Victor Fernandez de Alba]
- Update localisation template file and German localisation [Andreas Mantke]


0.13 (2016-12-31)
-----------------

- Fix of the header of the German localization file [Andreas Mantke]
- Fix field releated issues [Victor Fernandez de Alba]
- Fix views and project_logo conditions [Victor Fernandez de Alba]
- Fix templates responsive classes and use the Bootstrap ones [Victor Fernandez de Alba]
- Fix optional fields for additional file fields marked as required [Victor Fernandez de Alba]
- Add categorization behavior to the custom contenttypes [Victor Fernandez de Alba]
- Unify the license list [Victor Fernandez de Alba]
- Fix search issues in templates [Victor Fernandez de Alba]
- Fixed a typo [Samuel Mehrbrodt]
- Add support for querying the release compatibility version of inner releases from projects [Victor Fernandez de Alba]
- Set the max length of a release name/numbering to twelf [Andreas Mantke]
- Display the specific file name for each downloadable file [Andreas Mantke]
- Add the file names next to the download arrow for the current release [Andreaas Mantke]
- Fix of fieldset and migrate it to model from plone.supermodel [Andreas Mantke]
- Spellcheck fix in own_project.pt [Andreas Mantke]
- Update of localization template file and of the translation into German [Andreas Mantke]

0.12 (2016-09-08)
-----------------

- Fix and add some more localization tags.
- Fix of ressource registry css URL [Victor Fernandez de Alba]


0.11 (2016-09-02)
-----------------

- Update localisation template and translation into German [Andreas Mantke]
- Fix and add some localization tags [Andreas Mantke]
- Spanish localisation [Adolfo Jayme Barrientos]


0.9 (2016-08-28)
----------------

- Adding German localisation [Andreas Mantke]
- Update of localisation template file (pot) [Andreas Mantke]
- Fixes for localisation tags [Andreas Mantke]


0.8 (2016-08-20)
----------------

- Adding file extension validation for linked extension releases [Andreas Mantke]
- Adding image extension validation to project module [Andreas Mantke]
- Adding file extension validation to release module [Andreas Mantke]


0.7 (2016-07-05)
----------------

- Shorten boolean testing expressions [Andreas Mantke]
- CSS list style optimisation and style fixes [Andreas Mantke]
- PEP-8-Fixes [Andreas Mantke]


0.6 (2016-05-28)
----------------

- Adding a MANIFEST.in file [Andreas Mantke]


0.5 (2016-05-25)
----------------

- Updated the translation template file [Andreas Mantke]
- Added a missing closing div to the project view [Andreas Mantke]
- Added a validator for the release and linked release name uniqueness and it's adapters [Andreas Mantke]
- Changed the compatibility list in the project view to a text line [Andreas Mantke]
- Removed an obsolet div from the project view [Andreas Mantke]

0.4 (2016-05-21)
----------------

- Reordering of the project view template [Andreas Mantke]
- Removing the navtree from project and releases view [Andreas Mantke]
- Update of strings in the internationalisation template file (pot) [Andreas Mantke]


0.3 (2016-03-10)
----------------

- Add of README.md [Andreas Mantke]
- Removed doubled directory of tdf.extensionuploadcenter.egg-info [Andreas Mantke]

0.1 (2016-03-07)
----------------

- Initial release
