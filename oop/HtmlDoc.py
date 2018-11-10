# Tag superclass
class Tag(object):
    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return '{0.start_tag}{0.contents}{0.end_tag}'.format(self)

    def display(self, file=None):
        print(self, file=file)


# Doc type class
class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DocType does not have an end tag


# Header tag
class Head(Tag):

    def __init__(self):
        super().__init__('head', '')


# Body tag
class Body(Tag):

    def __init__(self):
        super().__init__('body', '')  # body contents will be built uo separately
        self._body_content = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_content.append(new_tag)

    def display(self, file=None):
        for tag in self._body_content:
            self.contents += str(tag)

        super().display(file=file)


# Document class
class HtmlDoc(object):

    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_tag('h1', 'Main Heading')
    my_page.add_tag('h2', 'Sub-heading')
    my_page.add_tag('p', 'This is the content of this page')

    with open('./data/test.html', 'w') as test_doc:
        my_page.display(file=test_doc)
