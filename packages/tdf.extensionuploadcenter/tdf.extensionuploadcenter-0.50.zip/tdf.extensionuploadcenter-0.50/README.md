# tdf.extensionuploadcenter

A Plone add-on for the LibreOffice extension uploadcenter that will make the publishing of extensions for LibreOffice much easier.

## Features


- The add-on creates four content objects: Extension Upload Center, Extension Project, Extension Release, Extension Linked Release
- The Center is used for the configuration:
   + Name of the Extensions Center
   + Description of the center
   + Product description
   + Product title
   + (Product) Categories
   + (Product) Lizenses
   + (Product) Versions
   + Platforms
   + (Product) Install instructions
   + Instructions for bug reports
   + Legal Disclaimer for contributions and downloads
   + Email-Address for the optional messaging of new releases to a

- The Project contains all the necessary information about the contributor and the project:
   + Project description and details
   + Links to external homepage and documentation of the project
   + Project contact email address
   + Project screenshot and logo

- The Release and the linked Release provide fields for the necessary information for downloadable and linked extensions files:
   + Release title, created from project title and release number
   + Description and details of the release
   + Changelog
   + Release license
   + Release compatibility
   + Legal declaration for contributors
   + Optional link to the source code
   + Form fields for file upload or the links to the files
   + Release platform compatibility

- Messaging:
   + to all project owner once a new product version is added
   + to a project owner if the status of his project changed
   + to a project owner if a release was added (to his project)
   + to the administrator email if a new project was added
   + to a hub email address if a new release was published in final state


## Examples

This add-on can be seen in action at the following sites:
- https://extensions.libreoffice.org/extensions


## Documentation

The documentation will be in the docs folder of this add-on.


## Translations

This product has been translated into

- (currently no translations)


## Installation

Install tdf.extensionuploadcenter by adding it to your buildout:

```

    [buildout]

    ...

    eggs =
        tdf.extensionuploadcenter


```


## Contribute


- Issue Tracker: https://github.com/tdf/tdf.extensionuploadcenter/issues
- Source Code: https://github.com/tdf/tdf.extensionuploadcenter
- Documentation: inside the docs folder of the add-on


## Support

If you are having issues, please let us know.



## License

The project is licensed under the GPLv2.





