import _unittests.restful_feeds as rf
from assertpy import assert_that


def test_feeds_for_somethingelse():
    resp = rf.get_feeds('Mark')
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    for feed in resp.json():
        assert_that(resp.ok, 'HTTP Request OK').is_true()
        resp2 = rf.get_feed(feed['feed_id'])
        assert_that(resp2.json()["title"], 'title').contains('somethingelse')


def test_addbooking():
    resp = rf.add_feed()
    print(resp.json())
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    # TODO construct a booking to create and assert created booking against it


def test_updatebooking():
    auth_token = restfullbooker.get_authtoken()
    new_booking = restfullbooker.add_random_booking().json()['bookingid']
    resp = restfullbooker.update_booking(new_booking, auth_token)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_removebooking():
    auth_token = restfullbooker.get_authtoken()
    new_booking = restfullbooker.add_random_booking().json()['bookingid']
    resp = restfullbooker.remove_booking(new_booking, auth_token)
    assert_that(resp.ok, 'HTTP Request OK').is_true()