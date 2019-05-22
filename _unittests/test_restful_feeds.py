import _unittests.restful_feeds as rf
from assertpy import assert_that

# --------------------------------------------------------

#
# def test_add_feed_1():
#     resp = rf.add_specific_feed(0)
#     assert_that(resp.ok, 'HTTP Request OK').is_true()
#
#
# def test_add_feed_2():
#     resp = rf.add_specific_feed(1)
#     assert_that(resp.ok, 'HTTP Request OK').is_true()
#
#
# def test_add_feed_3():
#     resp = rf.add_specific_feed(2)
#     assert_that(resp.ok, 'HTTP Request OK').is_true()
#
#
# def test_add_feed_4():
#     resp = rf.add_specific_feed(3)
#     assert_that(resp.ok, 'HTTP Request OK').is_true()


# --------------------------------------------------------


# def test_removefeed_1():
#     resp = rf.remove_feed(1)
#     assert_that(resp.ok, 'HTTP Request OK').is_true()
#
#
# def test_removefeed_2():
#     resp = rf.remove_feed(2)
#     assert_that(resp.ok, 'HTTP Request OK').is_true()
#
#
# def test_removefeed_3():
#     resp = rf.remove_feed(3)
#     assert_that(resp.ok, 'HTTP Request OK').is_true()
#
#
# def test_removefeed_4():
#     resp = rf.remove_feed(4)
#     assert_that(resp.ok, 'HTTP Request OK').is_true()


# --------------------------------------------------------

def test_updatefeed_1():
    resp = rf.update_feed(1, title='Realitatea', description='Stiri online',
                          url='http://rss.realitatea.net/stiri.xml', category='News')
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_updatefeed_2():
    resp = rf.update_feed(2, title='Realitatea', description='Stiri online',
                          url='http://rss.realitatea.net/stiri.xml', category='News')
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_updatefeed_3():
    resp = rf.update_feed(3, title='Realitatea', description='Stiri online',
                          url='http://rss.realitatea.net/stiri.xml', category='News')
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_updatefeed_4():
    resp = rf.update_feed(4, title='Realitatea', description='Stiri online',
                          url='http://rss.realitatea.net/stiri.xml', category='News')
    assert_that(resp.ok, 'HTTP Request OK').is_true()


