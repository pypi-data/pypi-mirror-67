..
    This file is part of jsonresolver
    Copyright (C) 2015, 2016 CERN.

    jsonresolver is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License; see LICENSE file for
    more details.

Changes
=======

Version 0.3.1 (released 2020-05-06)
-----------------------------------

- Deprecated Python versions lower than 3.6.0. Now supporting 3.6.0 and 3.7.0.


Version 0.3.0 (released 2020-03-12)
-----------------------------------

- Drops support for Python 2.7
- Updates testing method
- Updates python dependencies


Version 0.2.1 (released 2016-04-15)
-----------------------------------

Bug fixes
~~~~~~~~~

- Fixes issue with exceptions raised during e.g. resolver plugin
  loading being caught and not propagated.

Version 0.2.0 (released 2016-04-06)
-----------------------------------

Incompatible changes
~~~~~~~~~~~~~~~~~~~~

- Changes resolving to be based on hostname without 'http://' prefix.

Bug fixes
~~~~~~~~~

- Fixes issues with the hostname not being matched resulting in the
  same route on two hosts not to work.

Version 0.1.1 (released 2015-12-11)
-----------------------------------

Improved features
~~~~~~~~~~~~~~~~~

- Delays the url_map building until first resolve request.

Version 0.1.0 (released 2015-11-18)
-----------------------------------

- Initial public release.
