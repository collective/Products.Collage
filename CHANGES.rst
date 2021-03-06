Changelog
=========

1.4.1 (unreleased)
------------------

- Nothing changed yet.


1.4.0 (2015-12-11)
------------------

- Improvement: translated aliases w/o an explicit target set are falling back
  canonicals target now.
  [jensens]

- Improvement: migrate tests to plone.app.testing
  [jensens]

- Fix: Site Administrator can add a Collage.
  [jensens]

- Improvement: Use plone.api and cleanup utilities.
  [jensens]

- Code-Style: more pep8, make code-analysis happy, sorted imports.
  [jensens]

- Fix test: return value of LinguaPlone was in output and not checked.
  [jensens]

- Change CSS rendering mode to link, so it can be merged with other
  link-rendered resources.
  [thet]


1.3.11 (2014-10-08)
-------------------

- jQuery related fixes.
  [thet]

- Add uninstall profile.
  [thet]

- Fix reordering.
  [cippino, erral]

- Arrow images are now PNG files instead of GIFs.
  [erral]

- Added initial support for p.a.multilingual.
  [sneridagh]


1.3.10 (2013-10-22)
-------------------

- Added support for ``plone.app.contenttypes``.
  [benniboy, jensens]


1.3.9 (2013-07-01)
------------------

- Fixed html error
  [Andrew Pasquale]

- Removed relatedItems macro. This macro was from the
  plone_deprecated skin folder which is deactivated on plone 4.3 by
  default. relatedItems are now implemented as a viewlet.
  [Victor Fernandez de Alba]

- Conditional zcml configuration update.
  IContainer interface has been moved. The zcml declaration supports
  both locations now.
  [Rodrigo]


1.3.8 (2012-10-31)
------------------

* Moved to github.
  [maurits]

* Added views for plone.app.collection: standard and summary for now.
  [jensens]

* Added try-except block around getting helper
  when reindexing. This is not strictly our issue
  but I still consider it a stability improvement.
  [tmog]

* Remove deprecation warning on Zope 2.13:
  Products.ATReferenceBrowserWidget moved to archetypes.referencebrowserwidget
  DTMLFile is deprecated. import from App.special_dtml instead
  [toutpt]

* Don't add SearchableText to catalog query, if there is none. There has
  been issues with solr integration
  [tom_gross]

* Fall back to Id, if object has no Title in referencebrowser
  [tom_gross]

1.3.7 (2011-11-16)
------------------

* Added conditional include of CMFCore permisssions.zcml for Plone 4.1 support.
  [thet, tom_gross]

* Added addional renderer, which respects effective and expiry-date.
  [tom_gross]

* Restored Topic summary-view for Plone 3
  [tom_gross]

1.3.6 (2011-07-05)
------------------

* Updated set of catch exceptions; location error exception is 2.10+
  only. We fall back to attribute error. Also, narrow list to the
  exceptions likely to be raised because of environment errors.
  [malthe]

1.3.5 (2011-07-04)
------------------

* Catch name, type, value and location errors raised while rendering
  content inside a composition, but display a warning (status
  message).

  This allows a user to change to an alternative layout in the case
  that the system is broken.
  [malthe]

* Changed alised topic views such that only the initial batch is shown
  (without pagination). In addition, the headings in these views are
  now clickable and lead to the referenced topic.

  This makes topic views less busy in the general case where an
  already existing topic is shown.

  Note that topics created inside the composition retain their
  existing behavior.
  [malthe]

1.3.4 (2011-07-01)
------------------

* Fixed topic templates so that H2-headings are not marked with
  'documentFirstHeading'.
  [malthe]

1.3.3 (2011-07-01)
------------------

* Fixed topic templates so that headings used are ``H2``, not ``H1``.
  [malthe]

1.3.2 (2011-07-01)
------------------

* Fixed a broken expression in the ``topic_album`` template.
  [malthe]

1.3.1 (2011-06-08)
------------------

* Fixed ``folder_summary_view`` in Collage for Collections in Plone 4 - the
  macro does not exist anymore. Now the code is copied over here: suboptimal,
  but no better idea here (w/o touching Plone itself).
  [jensens]

* Make *existing items* view compatible with LinguaPlone. Use the
  navigation root as the default query path, and also supply the
  parameter ``Language``, set to ``"all"``, such that we get any
  object appearing under the current navigation root, regardless of
  session language.
  [malthe]

* Fixed imports that were changed in Plone 4.1.
  [malthe]

* Changed interface registration for Image and File views for Plone 3 to allow
  for p.a.blob image and file replacement types.
  [dunlapm]

* Updated Insert Current/New item menus to use Plone 4 methods for getting type
  icons when available.
  [dunlapm]


1.3.0-final (2010-10-22)
------------------------

* Add missing Products.Archetypes to setup dependencies.
  [thet]

* Show folderContents action in actions-viewlet for ColageColumns. This allows
  to browse and edit individual objects created in a collage column.
  [thet]

* Included new properties following 'rnix' and 'khink' new features in default
  setup profile and last upgrade step.
  [glenfant]

* Plone 3 support is back. No change for Plone 4
  [glenfant]

* Fix #85 - Add a new event break collage view [yboussard]

* Image and File layouts work with blob objects.
  [thomasdesvenain]

* Fixed many internationalizations.
  [thomasdesvenain]

* Updated french translations.
  [thomasdesvenain]

* Synched ``i18n/collage-xx.po`` files.
  [thomasdesvenain]

* Number of columns per batch is configurable via @@collage-controlpanel.
  Added support for 4- and 5-column layout (CSS and templates).
  [khink]

1.3.0-b4 (2010-04-06)
---------------------

* Fixed issue where layout viewlets would not be shown on Plone 4 due
  to an incorrect type assertion.

* The content type icon for Aliased content now appears with a border
  instead of the "alias" label.

* Fixed UI styling on Plone 4.

* Compatibility fix for Chameleon.

1.3.0-b3 (2010-02-04)
---------------------

* Plone 4 compatibility.
  [malthe]

* New icons.
  [malthe]

1.3.0-b2 (2010-01-17)
---------------------

* Added topic view which inherits the view setting from the topic
  content object (using a mapping to collage view names).
  [malthe]

* Added topic views for tabular and summary displays.
  [malthe]

* Fixed issue where you could not choose the standard layout if a
  missing layout was already selected (this might occur if an add-on
  product had been removed).
  [malthe]

* Synched ``i18n/collage-xx.po`` files (10 messages added, 5 removed)
  [glenfant]

* Added a GS upgrade step to 1.3.0
  [glenfant]

1.3.0-b1 (2010-01-09)
---------------------

* Adjusted the row renderer's use of template arguments for compatibility
  with Zope 2.12.
  [davisagli]

* Aliases are now inserted using an ajax-driven reference browser
  (custom implementation) which operates similarly to the standard
  Plone reference browser widget.
  [malthe]

* Fail gracefully (and informatively) when a layout cannot render.
  [malthe]

* Move the "split column" action to the row.
  [malthe]

* Cleaned up layout stylesheet.
  [malthe]

* Fixed issue that prevented inline-editing from working properly.
  [malthe]

* Changes to user interface appearance.
  [malthe]

* Added form protection.
  [malthe]

* Rewired compose view to simplify templates and avoid needless
  indirection.
  [malthe]

* Rename 'Manage page' to 'Compose'.
  [malthe]

* Move settings fields to the settings schemata. Added field descriptions.
  [malthe]

1.2.3 (2009-11-02)
------------------

* Fixed search bug mentioned in #57 when adding alias.
  [glenfant]

* Worked around IE CSS bugs mentioned in issue #60. Thanks to Kevin Deldycke.
  [glenfant]

* Synched all .po with the latest labels and updated the ``*-fr.po``
  files. Collage translators, new .po files are wawiting for your inputs.
  [glenfant]

* Following jensens change on types whitelist, change the test accordingly.
  [glenfant]

* On alias target removal, the alias layout is reset to "standard". This gives a
  chance to content authors to delete the alias, rather tha saying "Error:
  Layout not found". This fixes #63
  [glenfant]

* Update JavaScript to no longer use reserved function postMessage. This fixes
  #54.
  [dunlapm]

* Update french translation (tiny semantic improvement).
  [kdeldycke]

* Avoid BadRequest error while adding alias_whitelist property in
  upgrade step if this property already exists.  You should usually be
  able to run an upgrade step a second time without fail.
  [maurits]

* Added a useful very reduced 'minimal' view for files.
  [jensens]

* Removed type 'Folder' from Collage properties -> types whitelist. It does not
  make much sense (and will confuse users) to add a folder direct inside a
  Collage. if someone really needs it, it can be enabled with minor effort.
  [jensens]

* Made Collage fields: show_title, show_description and index_subobjects
  languageIndependent.
  [jensens]

* Fixed deprecated URL for add on packages (third party content types)
  in the doc.
  [glenfant]

1.2.2 (2009-06-07)
------------------

* A UID can start with numbers. The value of the id attribute cannot start
  with a number by naming convention. The views now use:
  string:title-${view/getUniqueIdentifier}, which always starts with a t
  [jladage]

* Don't render empty descriptions in standard document.
  [jensens]

* In Plone 3 the contributor is the one adding content. So default roles for
  "Add Collage content" is now Contributor, additional to Owner & Manager.

* Don't assume that a view is always available: added error view as fallback.
  It helps a lot in development and doesn't expose ugly tracebacks to users
  if site has a configuration problem. Also minor cleanup and fixed tests.
  [jensens]

* Added confirmation-popup for delete/remove action.
  [jensens]

* Make viewlets following all the same paradigm.
  Reorder them according to usability thought. Turn expandable content into
  overlayed box.
  [jensens]

* Turn add row into menu. Fix circular import problem instead ugly workaround.
  [jensens]

* Added upgrade step to 1.2.2 that adds the alias whitelist property, without
  which the control panel crashes.
  [glenfant]

* Synched all .po files following jensens's changes and added french
  missing labels.
  [glenfant]

* Make a difference between types to be added to Collage and types
  enabled for alias. This introduces a new whitelist in controlpanel.
  [jensens]

* Feature "automatic split of rows with more than 3 entries" was broken.
  Its fixed now. I also added an unbatched view for the row.
  [jensens]

* Almost completed German translation.
  [jensens]

* Added Dutch translation (nl).
  [reinout]

* Added portuguese (pt) translation.
  [igbun]

* Added additional CSS classes to Collage blocks to make it easier to
  apply styles only for particular positions, content types, or Collage
  view names.
  [davisagli]

* Typo in collage.css.dtml
  [glenfant]

* Fixed issue where layouts would not be looked up correctly for
  aliases.
  [malthe]

* Added support for theme-specific overrides of Collage views.  See
  DEVELOPERS.txt for details.
  [davisagli]

* Update and sync french and english translation.
  [kdeldycke]


Collage 1.2.1 (2008-12-10)
--------------------------

https://svn.plone.org/collective/Products.Collage/tags/1.2.1/

* Moved event handlers in events.py module
  [glenfant]

* Fixed bug on searching (spaces in type name or non ascii searchable
  text). Found items titles are colored according their workflow state as in
  folder_contents (...)
  [glenfant]

* Use `folder_summary_view` instead of `folder_listing` in topic
  views. This fixes issue #43.
  [malthe]

* Added Alias target search limit in config panel.
  [glenfant]

* Optimizations of existing items view including link to target.
  [glenfant]

* Removed code for old Plone (< 3.1) support since we can't be used in
  Plone 3.0 or older anymore
  [glenfant]

* Memoizing where possible to speed up views (not sure to be exhaustive)
  [glenfant]

* New translations due to the control panel, and added translations synch
  script.
  [glenfant]

* Fixed bug on @@collage_helper
  [glenfant]

* Added control panel for Collage inner content types whitelist.
  [glenfant]

* Collage is now LinguaPlone compatible and therefore Collage elements
  are now translatable.
  [erral]

* Renderer: if a layout is defined on a canonical object, but not
  on a translation, now the canonical version's layout setting
  is used for the translation rather than the default. (Language
  versions should look the same unless explicitly defined otherwise.)
  [thomasw]

* Added Basque (eu) and Spanish (es) translations.
  [erral]

* Added safety belt to GenericSetup upgrade scripts.
  [glenfant]

* Added translation entries for new boolean in Collage.
  [glenfant]

* Collage subcontents indexing is now an option, since a Collage
  object may be irrelevant in search results (i.e: a Collage with
  only File contents).
  [glenfant]

* Added utilities.getFSVersionTuple that may help Collage extension
  components (add skins, content type support, ...)
  [glenfant]

* version.txt is major.minor.bugfix-[beta] to get synch with
  metadata.xml/version (when upgrade step required) and complying
  getFSVersionTuple above
  [glenfant]

* Add missing event-related translation.
  [kdeldycke]

Collage 1.2.0 beta 3 (2008-08-15)
---------------------------------

https://svn.plone.org/collective/Products.Collage/tags/1.2b3

* Packaged as a python egg and released on pypi.
  [davisagli]

* Renamed builtin portlet skins and gave minimum CSS to them.
  [glenfant]

* Re-using ATContentTypes.content.schemata.ATContentTypesSchema and
  removing copied/pasted portions of code in our schema definitions.
  [glenfant]

* Removed CMF skins layer "Collage" and spreaded its stuffs in Zope 3
  style browser resources and pages (CSS). Added an upgrade step for
  this.
  [glenfant]

* Using the MessageFactory for labels and descriptions in
  schemas. Code is more compact and i18ndude friendly.
  [glenfant]

* Added unit tests for utilities.
  [glenfant]


Collage 1.2.0 beta 2
--------------------

https://svn.plone.org/collective/Collage/tags/1.2.0beta2

* Added a GenericSetup upgrade step to 1.2.0.
  [glenfant]

* Removed useless Folder and Plone Site types setups.
  [glenfant]

Collage 1.2.0 beta 1
--------------------

https://svn.plone.org/collective/Collage/tags/1.2.0beta1

* Added a skin demo for portlets
  [glenfant]

* Code cleanup with pyflakes
  [glenfant]

* Registering skin with ZCML
  [glenfant]

* Version is now 3 digits (major.minor.bugfix) as most components.
  [glenfant]

* Extensions/* (Install script) is now useless. Removed
  [glenfant]

* Removed meta_type attr in GS profile when not creating
  objects. (potentially harmful according to MArtin Aspeli)
  [glenfant]

* Defining "view" variables in templates is harmful. Renamed to
  kssview (generally)
  [glenfant]

* For  reason I can't understand, templates macros for KSS editing
  only work when in a <span metal:define-macro ...> or a <div
  metal:define-macro ...>
  [glenfant]

* We must set each fied in its own macro in the xx_portlet.pt views
  otherwise KSS screams.
  [glenfant]

* Made portlets skinnable (reintroduced some of the zegor branch)
  [glenfant]

* Fixed unicode error in clipboard's title (reintroduced fix from
  zegor branch).
  [glenfant]

* I hate tabs for indenting (removed in every file I needed to change)
  [glenfant]

* Some easy code refactorings: the trunk does not support Plone 2.x
  and older versions any more.
  [glenfant]

* Added some markups for i18ndude in Python.
  [glenfant]

* Moved (and added) tests to "tests" directory.
  [glenfant]

* Making templates ready for i18ndude that found malformed stuffs when
  ZPT is more tolerant.
  [glenfant]

* Made split- and expand-icons transparent
  [malthe]

* Added clickable link view.

* Simplified view class names.
  [malthe]

* Removed annotations hack (we now expect content to be IAnnotatable).
  [malthe]

* Image standard display now shows the actual image rather than its
  preview.  This caused issues with large images in a Collage being
  upscaled when displayed.
  [rockdj]


Collage 1.1
-----------

https://svn.plone.org/collective/Collage/tags/1.1

* Various bug fixes
  [malthe]

* No longer ship with jQuery.
  [malthe]

* Show locking viewlet in content menu
  [malthe]

* Fixed a jQuery integration issue
  [malthe]


Collage 1.0
-----------

https://svn.plone.org/collective/Collage/tags/1.0-final

* Added a search text field in existing_items to find items in large sites.
  Thanks to Silvio Tomatis for the patch.
  This closes ticket http://plone.org/products/collage/issues/12.
  [zegor]

* Renamed manage_page to compose_page to avoid ZMI filtering access problem
  [zegor]

* Added borders on manage_page to distinct rows, columns and items
  [zegor]

* Added "portlets" views
  [zegor]

* Rows, Colums and Aliases not indexed in portal_catalog
  [zegor]

* Do not display Aliases with insufficient privileges
  [zegor]

* Made the Collection item size matter, and added a More... button [regebro]

* Added content views for ATLink, ATFile and ATNewsItem
  [zegor]

* Fixed some i18n problems
  Added English and French po files
  Resynchronized po files with pot
  [zegor]

* Do not display share and properties tabs with Plone 3.0
  [zegor]

* Added .metadata to cache icons
  [zegor]

* Added delete-object view method to avoid redirection to confirmation_form
  [zegor]

* Refactored codebase
    Moved code out of ./browser/browser.py into separate files.

    New directory structure:

    ./browser/viewlets     viewlet templates
    ./browser/views        content view templates
    ./browser/templates    collage ui templates

    Zope 3 configuration files:

    configuration.zcml     collage ui and functionality
    views.zcml             content views
    actions.zcml           ui actions (insert, split etc.)
    viewlets.zcml          ui configuration

    [malthe]

* Nested headings properly
    Lets have a 'safe' structure:
    <h1> title of the collage
    <h2> could be a row heading and / or object item
    http://www.w3.org/TR/1999/WAI-WEBCONTENT-19990505/#tech-logical-headings

    [pelle]


* Added HISTORY file
    Lets use this file again to log changes...

    [pelle]
