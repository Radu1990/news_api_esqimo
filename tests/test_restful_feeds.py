import tests.restful_feeds as rf
from assertpy import assert_that


# Test add feed
# --------------------------------------------------------
def test_add_feed_1():
    resp = rf.add_specific_feed(0)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_add_feed_2():
    resp = rf.add_specific_feed(1)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_add_feed_3():
    resp = rf.add_specific_feed(2)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_add_feed_4():
    resp = rf.add_specific_feed(3)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


# Test get feed
# --------------------------------------------------------
def test_get_feed_1():
    resp = rf.get_feed(1)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_get_feed_2():
    resp = rf.get_feed(2)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_get_feed_3():
    resp = rf.get_feed(3)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_get_feed_4():
    resp = rf.get_feed(4)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


# Test get all feeds
# --------------------------------------------------------
def test_get_all_feeds():
    resp = rf.get_all_feeds()
    assert_that(resp.ok, 'HTTP Request OK').is_true()


# Test remove feed
# --------------------------------------------------------
def test_remove_feed_1():
    # test remove feed from db
    resp = rf.remove_feed(1)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_remove_feed_2():
    # test remove feed from db
    resp = rf.remove_feed(2)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_remove_feed_3():
    # test remove feed from db
    resp = rf.remove_feed(3)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_remove_feed_4():
    # test remove feed from db
    resp = rf.remove_feed(4)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


# Test edit feed
# --------------------------------------------------------
def test_update_feed_1():
    # test if changing feed works
    resp = rf.update_feed(1, title='Realitatea', description='Stiri online',
                          url='http://rss.realitatea.net/stiri.xml', category='News')
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_update_feed_2_same_input_again():
    # here we test if unique url relation
    # holds
    resp = rf.update_feed(2, title='Realitatea', description='Stiri online',
                          url='http://rss.realitatea.net/stiri.xml', category='News')
    assert_that(resp.ok, 'HTTP Request OK').is_false()

