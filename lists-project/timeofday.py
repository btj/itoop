def test_TimeOfDay_class(TimeOfDay):
    t = TimeOfDay()
    assert t.get_hours() == 0
    assert t.get_minutes() == 0

    t.set_hours(10)
    assert t.get_hours() == 10
    assert t.get_minutes() == 0

    t.set_minutes(30)
    assert t.get_hours() == 10
    assert t.get_minutes() == 30

    t = TimeOfDay(11, 45)
    assert t.get_hours() == 11
    assert t.get_minutes() == 45

    t.set_hours(10)
    assert t.get_hours() == 10
    assert t.get_minutes() == 45

    t.set_minutes(30)
    assert t.get_hours() == 10
    assert t.get_minutes() == 30

class TimeOfDay:
    def __init__(self, hours = 0, minutes = 0):
        assert 0 <= hours <= 23
        assert 0 <= minutes <= 59
        self._hours = hours
        self._minutes = minutes

    def get_hours(self):
        return self._hours

    def get_minutes(self):
        return self._minutes

    def set_hours(self, hours):
        assert 0 <= hours <= 23
        self._hours = hours

    def set_minutes(self, minutes):
        assert 0 <= minutes <= 59
        self._minutes = minutes

test_TimeOfDay_class(TimeOfDay)

class TimeOfDay:
    def __init__(self, hours = 0, minutes = 0):
        assert 0 <= hours <= 23
        assert 0 <= minutes <= 59
        self._msm = hours * 60 + minutes

    def get_hours(self):
        return self._msm // 60

    def get_minutes(self):
        return self._msm % 60

    def set_hours(self, hours):
        assert 0 <= hours <= 23
        self._msm = hours * 60 + self._msm % 60

    def set_minutes(self, minutes):
        assert 0 <= minutes <= 59
        self._msm = self._msm // 60 * 60 + minutes

test_TimeOfDay_class(TimeOfDay)
