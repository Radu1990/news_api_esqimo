import _unittests.restful_feeds as rf
from assertpy import assert_that


def test_feeds_for_other():
    resp = rf.get_feeds('Mark')
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    for feed in resp.json():
        assert_that(resp.ok, 'HTTP Request OK').is_true()
        resp2 = rf.describe_feed(feed['feed_id'])
        assert_that(resp2.json()["title"], 'title').contains('other')


def test_addfeed():
    resp = rf.add_random_feed()
    print(resp.json())
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_updatefeed():
    new_feed = rf.add_random_feed().json()['feed_id']
    resp = rf.update_feed(new_feed)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_removefeed():
    new_feed = rf.add_random_feed().json()['feed_id']
    resp = rf.remove_feed(new_feed)
    assert_that(resp.ok, 'HTTP Request OK').is_true()
