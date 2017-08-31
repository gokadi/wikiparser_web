# wikiparser_web
Django app to parse wikipedia by article_name
Web version for wikipedia parser. Django app. Install requirements, then use pip install git+https://github.com/lucasdnd/Wikipedia.git

ALSO go to wikipedia.py in wikipedia package and replace def section by following:
```python
    def section(self, section_title):
        '''
    Get the plain text content of a section from `self.sections`.
    Returns None if `section_title` isn't found, otherwise returns a whitespace stripped string.

    This is a convenience method that wraps self.content.

    .. warning:: Calling `section` on a section that has subheadings will NOT return
           the full text of all of the subsections. It only gets the text between
           `section_title` and the next subheading, which is often empty.
    '''

        section = u"== {} ==".format(section_title)
        try:
            index = self.content.index(section) + len(section)
        except ValueError:
            return None

        try:
            if self.content[index + 1] != '=':
                next_index = self.content.index("==", index)
            else:
                next_index = self.content.index("==", index + 1)
        except (ValueError, IndexError):
            next_index = len(self.content)

        return self.content[index:next_index].lstrip("=").strip()
