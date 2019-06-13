from . import WikiBaseTestCase


class WebContentTestCase(WikiBaseTestCase):
    """
        Various test cases around web content.
    """

    def test_index_missing(self):
        """
            Assert the wiki will correctly play the content missing
            index page, if no index page exists.
        """
        rsp = self.app.get('/')
        assert b"You did not create any content yet." in rsp.data
        assert rsp.status_code == 200

    def test_page_index(self):
        """
            Assert /index/ will take you to the page index.
        """
        rsp = self.app.get('/index/')
        assert b'Page Index' in rsp.data
        assert rsp.status_code == 200
