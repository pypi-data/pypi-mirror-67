from timeboard.calendars.calendarbase import (
    CalendarBase,
    nth_weekday_of_month, extend_weekends, from_easter)
from timeboard.calendars.weekly_template import read_config, WeeklyTemplate
from timeboard.exceptions import OutOfBoundsError
from timeboard.core import get_period, get_timestamp
from pandas import Timedelta
import os
import pytest


class TestCalendarUtils(object):

    def test_nth_weekday_positive(self):
        date_tuples_2017={
            (12, 5, 1): get_timestamp('01 Dec 2017'),
            (12, 7, 1): get_timestamp('03 Dec 2017'),
            (12, 3, 1): get_timestamp('06 Dec 2017'),
            (12, 3, 4): get_timestamp('27 Dec 2017'),
            (12, 3, 5): None,
            (12, 5, 5): get_timestamp('29 Dec 2017'),
            (12, 7, 5): get_timestamp('31 Dec 2017'),
            (5, 1, 1):  get_timestamp('01 May 2017'),
            (5, 1, 5):  get_timestamp('29 May 2017'),
        }
        result = nth_weekday_of_month(2017, date_tuples_2017.keys(), label=5)
        valid_dates = [x for x in  date_tuples_2017.values() if x is not None]
        assert sorted(result.keys()) == sorted(valid_dates)
        assert list(result.values()).count(5) == len(result)

    def test_nth_weekday_negative(self):

        date_tuples_2017 = {
            (12, 3, -1): get_timestamp('27 Dec 2017'),
            (12, 3, -4): get_timestamp('06 Dec 2017'),
            (12, 3, -5): None,
            (12, 5, -1): get_timestamp('29 Dec 2017'),
            (12, 7, -1): get_timestamp('31 Dec 2017'),
            (5, 1, -1):  get_timestamp('29 May 2017'),
            (5, 1, -5):  get_timestamp('01 May 2017'),
        }
        result = nth_weekday_of_month(2017, date_tuples_2017.keys(), label=5)
        valid_dates = [x for x in  date_tuples_2017.values() if x is not None]
        assert sorted(result.keys()) == sorted(valid_dates)
        assert list(result.values()).count(5) == len(result)

    def test_nth_weekday_shift(self):
        date_tuples_2017={
            (12, 5, 1, 0): get_timestamp('01 Dec 2017'),
            (12, 5, 1, 2): get_timestamp('03 Dec 2017'),
            (12, 5, 1, -2): get_timestamp('29 Nov 2017')
        }
        result = nth_weekday_of_month(2017, date_tuples_2017.keys())
        valid_dates = [x for x in  date_tuples_2017.values() if x is not None]
        assert sorted(result.keys()) == sorted(valid_dates)
        assert list(result.values()).count(0) == len(result)

    def test_nth_weekday_bad_n(self):
        with pytest.raises(OutOfBoundsError):
            nth_weekday_of_month(2017, [(12, 3, 5)], errors='raise')
        with pytest.raises(OutOfBoundsError):
            nth_weekday_of_month(2017, [(12, 3, -5)], errors='raise')
        with pytest.raises(AssertionError):
            nth_weekday_of_month(2017, [(5, 1, -6)])
        with pytest.raises(AssertionError):
            nth_weekday_of_month(2017, [(5, 1, 6)])
        with pytest.raises(AssertionError):
            nth_weekday_of_month(2017, [(5, 1, 0)])

    def test_extend_weekend_saturday(self):
        amds = {'16 Dec 2017': 5}
        result = extend_weekends(amds, how='nearest')
        assert result == {get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('15 Dec 2017'): 5}
        result = extend_weekends(amds, how='previous')
        assert result == {get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('15 Dec 2017'): 5}
        result = extend_weekends(amds, how='next')
        assert result == {get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 5}

    def test_extend_weekend_sunday(self):
        amds = {'17 Dec 2017': 5}
        result = extend_weekends(amds, how='nearest')
        assert result == {get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 5}
        result = extend_weekends(amds, how='previous')
        assert result == {get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('15 Dec 2017'): 5}
        result = extend_weekends(amds, how='next')
        assert result == {get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 5}

    def test_extend_weekend_new_label(self):
        amds = {'17 Dec 2017': 5}
        result = extend_weekends(amds, how='nearest', label='a')
        assert result == {get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 'a'}

    def test_extend_weekend_weekday(self):
        amds = {'15 Dec 2017': 5}
        result = extend_weekends(amds, how='nearest')
        assert result == {get_timestamp('15 Dec 2017'): 5}

    def test_extend_weekend_weekday_already_off1(self):
        amds = {'17 Dec 2017': 5, '18 Dec 2017': 5}
        result = extend_weekends(amds, how='next')
        assert result == {get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 5,
                          get_timestamp('19 Dec 2017'): 5
                          }

    def test_extend_weekend_weekday_already_off2(self):
        amds = {'17 Dec 2017': 5, '15 Dec 2017': 5}
        result = extend_weekends(amds, how='previous')
        assert result == {get_timestamp('14 Dec 2017'): 5,
                          get_timestamp('15 Dec 2017'): 5,
                          get_timestamp('17 Dec 2017'): 5
                          }

    def test_extend_weekend_two_holidays_same_labels(self):
        amds = {'16 Dec 2017': 5, '17 Dec 2017': 5}
        result = extend_weekends(amds, how='nearest')
        assert result == {get_timestamp('15 Dec 2017'): 5,
                          get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 5
                          }
        result = extend_weekends(amds, how='previous')
        assert result == {get_timestamp('14 Dec 2017'): 5,
                          get_timestamp('15 Dec 2017'): 5,
                          get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('17 Dec 2017'): 5,
                          }
        result = extend_weekends(amds, how='next')
        assert result == {get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 5,
                          get_timestamp('19 Dec 2017'): 5
                          }

    def test_extend_weekend_two_holidays_new_label(self):
        amds = {'16 Dec 2017': 5, '17 Dec 2017': 5}
        result = extend_weekends(amds, how='nearest', label=0)
        assert result == {get_timestamp('15 Dec 2017'): 0,
                          get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 0}
        result = extend_weekends(amds, how='previous', label=0)
        assert result == {get_timestamp('14 Dec 2017'): 0,
                          get_timestamp('15 Dec 2017'): 0,
                          get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('17 Dec 2017'): 5,
                          }
        result = extend_weekends(amds, how='next', label=0)
        assert result == {get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 0,
                          get_timestamp('19 Dec 2017'): 0}

    def test_extend_weekend_two_holidays_diff_labels(self):
        amds = {'16 Dec 2017': 3, '17 Dec 2017': 5}
        result = extend_weekends(amds, how='nearest')
        assert result == {get_timestamp('15 Dec 2017'): 3,
                          get_timestamp('16 Dec 2017'): 3,
                          get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 5}
        result = extend_weekends(amds, how='previous')
        assert result == {get_timestamp('14 Dec 2017'): 5,
                          get_timestamp('15 Dec 2017'): 3,
                          get_timestamp('16 Dec 2017'): 3,
                          get_timestamp('17 Dec 2017'): 5,
                          }
        result = extend_weekends(amds, how='next')
        assert result == {get_timestamp('16 Dec 2017'): 3,
                          get_timestamp('17 Dec 2017'): 5,
                          get_timestamp('18 Dec 2017'): 3,
                          get_timestamp('19 Dec 2017'): 5}

    def test_extend_weekend_strange_weekend(self):
        amds = {'16 Dec 2017': 5}
        result = extend_weekends(amds, how='nearest', weekend=[5])
        # if there is a tie, 'nearest' == 'next'
        assert result == {get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('17 Dec 2017'): 5}
        result = extend_weekends(amds, how='next', weekend=[5, 6, 0])
        assert result == {get_timestamp('16 Dec 2017'): 5,
                          get_timestamp('19 Dec 2017'): 5}
        result = extend_weekends(amds, how='previous', weekend=[3, 4, 5])
        assert result == {get_timestamp('13 Dec 2017'): 5,
                          get_timestamp('16 Dec 2017'): 5}
        result = extend_weekends(amds, weekend=[])
        assert result == {get_timestamp('16 Dec 2017'): 5}

    def test_from_easter(self):
        assert from_easter(2017, [0, 1, -2]) == {
                                            get_timestamp('16 Apr 2017'): 0,
                                            get_timestamp('17 Apr 2017'): 0,
                                            get_timestamp('14 Apr 2017'): 0}

        assert from_easter(2017, [1], easter_type='orthodox', label=5) == {
            get_timestamp('17 Apr 2017'): 5}
        assert from_easter(2000, [0]) == {get_timestamp('23 Apr 2000'): 0}
        assert from_easter(2000, [0],
                   easter_type='orthodox') == {get_timestamp('30 Apr 2000'): 0}
        assert from_easter(2000, []) == {}


class TestReadClndConfig(object):

    def test_read_clnd_config_empty(self, tmpdir):
        fh = tmpdir.join("test_calendar.yml")
        fh.write("")
        filename = os.path.join(fh.dirname, fh.basename)
        config = read_config(filename)
        assert isinstance(config, dict)
        assert len(config) == 0
        fh.write("\n")
        config = read_config(filename)
        assert isinstance(config, dict)
        assert len(config) == 0

    def test_read_clnd_config(self, tmpdir):
        fh = tmpdir.join("test_calendar.yml")
        fh.write("""
        weekday_labels: [8, 8, 8, 8, 8, 0, 0]
        start: "01 Jan 2000"
        long_weekends: next

        scopes:
          country: [england, northern_ireland, scotland]

        amend:

          - name: new_year
            label: 0
            scopes:
                country: [england, northern_ireland]            
            observance: day_of_month
            when: 
              month: -1
              day: 1
              
          - name: royal
            label: 1
            scopes:
                undefined_key: some_stuff
            observance: date
            when:
              date: ["29 Apr 2011", "04 Jun 2012", "05 Jun 2012"]

        """)
        filename = os.path.join(fh.dirname, fh.basename)
        config = read_config(filename)
        assert isinstance(config, dict)
        keys = {'weekday_labels', 'start',
                'long_weekends', 'scopes', 'amend'}
        assert set(config.keys()) == keys
        assert config['weekday_labels'] == [8, 8, 8, 8, 8, 0, 0]
        assert config['start'] == '01 Jan 2000'
        assert config['long_weekends'] == 'next'
        assert isinstance(config['scopes'], dict)
        assert set(config['scopes'].keys()) == {'country'}
        assert config['scopes']['country'] == ['england', 'northern_ireland',
                                               'scotland']
        assert isinstance(config['amend'], list)
        assert len(config['amend']) == 2
        for i in range(2):
            assert isinstance(config['amend'][i], dict)
            assert set(config['amend'][i].keys()) == {'name', 'label', 'scopes',
                                                      'observance', 'when'}
            assert isinstance(config['amend'][i]['when'], dict)
            assert isinstance(config['amend'][i]['scopes'], dict)
        assert config['amend'][0]['label'] == 0
        assert config['amend'][0]['scopes']['country'] == [
            'england', 'northern_ireland']
        assert config['amend'][0]['when']['month'] == -1
        assert config['amend'][1]['name'] == 'royal'
        assert config['amend'][1]['label'] == 1
        assert config['amend'][1]['when']['date'] == [
            "29 Apr 2011", "04 Jun 2012", "05 Jun 2012"]


class TestCheckClndConfig(object):

    def test_check_clnd_config_not_dict(self):
        config = "dummy"
        with pytest.raises(TypeError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_empty_dict(self):
        config = dict()
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_missing_req_params(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      description='abc')
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_minimum_params(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010')
        template = WeeklyTemplate(config)
        assert template.pattern == [1, 1, 1, 1, 1, 0, 0]
        assert template.start == get_timestamp('01 Jan 2001')
        assert template.end == get_timestamp('31 Dec 2010')
        assert len(template.scopes) == 0
        assert len(template.names) == 0
        assert template._config['long_weekends'] == 'none'
        assert len(template._config['amend']) == 0

    def test_check_clnd_config_invalid_labels(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010')
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010')
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

        config = dict(weekday_labels="1, 1, 1, 1, 1, 0, 0",
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010')
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_unknown_params(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      description='abc',
                      invalid_parameter=1)
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_invalid_scopes(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      scopes=[1, 2, 3])
        with pytest.raises(TypeError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_scopes(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      scopes={'a': 'x', 'b': 'y'})
        template = WeeklyTemplate(config)
        assert len(template.scopes) == 2
        assert template.scopes['a'] == 'x'
        assert template.scopes['b'] == 'y'

    def test_check_clnd_config_invalid_amend_type(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=1)
        with pytest.raises(TypeError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_minimal_amend(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '01 Jan 2005'}
                           }
                      ])
        template = WeeklyTemplate(config)
        assert len(template.names) == 0
        assert len(template._config['amend']) == 1
        assert template._config['amend'][0]['label'] == 0

    def test_check_clnd_config_minimal_names(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '01 Jan 2005'},
                           'name': 'a',
                           },
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '02 Jan 2005'},
                           'name': 'b',
                           }
                      ])
        template = WeeklyTemplate(config)
        assert len(template.names) == 2
        assert template.names == {'a', 'b'}
        assert len(template._config['amend']) == 2
        assert template._config['amend'][0]['name'] == 'a'
        assert template._config['amend'][1]['name'] == 'b'

    def test_check_clnd_config_amend_item_not_dict(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '01 Jan 2005'}
                           },
                          1
                      ])
        with pytest.raises(TypeError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_amend_item_empty_dict(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '01 Jan 2005'}
                           },
                          dict()
                      ])
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_amend_item_missing_req_params(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '01 Jan 2005'}
                           },
                          {'label': 0,
                           'observance': 'date',
                           },
                      ])
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_amend_item_unknown_param(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '01 Jan 2005'},
                           'name': 'n',
                           'unknown_parameter': 0
                           },
                      ])
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_amend_item_wrong_type_of_when(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': [1,2,3],
                           },
                      ])
        with pytest.raises(TypeError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_amend_item_empty_when(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': dict(),
                           },
                      ])
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_amend_item_wrong_type_of_scopes(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '01 Jan 2005'},
                           'scopes': [1,2,3]
                           },
                      ])
        with pytest.raises(TypeError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_amend_item_empty_scopes(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '01 Jan 2005'},
                           'scopes': dict(),
                           },
                      ])
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_long_weekends(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      long_weekends='next')
        template = WeeklyTemplate(config)
        assert template._config['long_weekends'] == 'next'

    def test_check_clnd_config_bad_long_weekends(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      long_weekends='invalid_value')
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)

    def test_check_clnd_config_amend_item_bad_long_weekends(self):
        config = dict(weekday_labels=[1, 1, 1, 1, 1, 0, 0],
                      holiday_label=0,
                      start='01 Jan 2001',
                      end='31 Dec 2010',
                      amend=[
                          {'label': 0,
                           'observance': 'date',
                           'when': {'dates': '01 Jan 2005'},
                           'long_weekends': 'invalid_value',
                           },
                      ])
        with pytest.raises(ValueError):
            template = WeeklyTemplate(config)


class TestCalendarBase(object):
    def test_calendar_base(self):
        assert CalendarBase.amendments() == {}
        start = CalendarBase.parameters()['start']
        end = CalendarBase.parameters()['end']
        freq = CalendarBase.parameters()['base_unit_freq']
        clnd = CalendarBase()
        assert clnd.start_time == get_period(start, freq=freq).start_time
        assert clnd.end_time == get_period(end, freq=freq).end_time
        delta = end - start
        assert clnd.get_interval().count() == delta.components.days + 1

    def test_calendar_base_custom_limits(self):
        clnd = CalendarBase(custom_start='01 Jan 2017',
                            custom_end='31 Dec 2018')
        assert clnd.get_interval().count() == 365*2

    def test_calendar_base_custom_amds(self):
        clnd = CalendarBase(custom_start='01 Jan 2017',
                            custom_end='31 Dec 2018',
                            custom_amendments={
                                '01 Mar 2017': 0,
                                '01 Mar 2019': 0}
                            )
        assert clnd.get_interval().count() == 365 * 2 - 1

    def test_calendat_base_OOB(self):
        start = CalendarBase.parameters()['start']
        end = CalendarBase.parameters()['end']
        with pytest.raises(OutOfBoundsError):
            CalendarBase(start-Timedelta(days=1))
        with pytest.raises(OutOfBoundsError):
            CalendarBase(custom_end=end+Timedelta(days=1))
