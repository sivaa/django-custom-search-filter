django-custom-search-filter
===========================

Customized django search and extended filters

Search Customization
--------------------
- If any child table fields has the word being search, it will display the associated main record(app/admin.py).

 Filter Customization
 --------------------
 - By default, django admin filter and search are customized. But search and filter are not.
 - So the search query string in appended when filter URL is constructed(admin/filter.html).