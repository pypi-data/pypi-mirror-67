=======
History
=======

1.0.4 (2020-03-20)
------------------

* Remove migration for user attribute mapping which was still there accidentally and breaking all tests.

1.0.3 (2020-03-13)
------------------

* Remove user attribute mapping. This feature was buggy and the same can be achieved using hooks.

1.0.2 (2020-03-13)
------------------

* Fix get_hook() to work with database configuration.

1.0.1 (2020-03-13)
------------------

* Fixes bug when reading user attribute mappings.

1.0.0 (2020-03-13)
------------------

* Fixes bug with Site note existing
* Add feature to sync user attributes from Azure AD.

0.2.11 (2020-01-13)
-------------------

* Fixes bug where the max_length on a CharField wasn't long enough for all choices to be stored.

0.2.10 (2019-09-24)
-------------------

* Fixes bug in 0.2.9 where cache key was failing.

0.2.9 (2019-09-24)
------------------

* Update cache to work on a per-site basis.

0.2.8 (2019-09-23)
------------------

* Fix bug where migrations were relying on undefined ordering.

0.2.7 (2019-09-23)
------------------

* Fix tests to work with new default for login_enabled.

0.2.6 (2019-09-23)
------------------

* Make sure migrations for sites_microsoft_auth run after migrations for sites framework.

0.2.5 (2019-09-23)
------------------

* Add SiteConfiguration object for all sites during initial migrate.
* Change default for login_enabled to False

0.2.4 (2019-09-23)
------------------

* Fix bug where 'MicrosoftAuthenticationBackend` is not respecting `site` on the MicrosoftAccount model.

0.2.3 (2019-09-23)
------------------

* Fixed bug with `MicrosoftAuthenticationBackend` not restricting users to their respective sites.

0.2.2 (2019-09-23)
------------------

* Updated package name to `sites_microsoft_auth` from `microsoft_auth`

0.2.1 (2019-09-23)
------------------

* Updated documentation.

0.2.0 (2019-09-23)
------------------

* First working release on PyPi
