import os
from threading import Thread
from unittest.mock import MagicMock
from unittest.mock import patch

from pandas import DataFrame
import pytest
import sklearn

dummy_dataframe = DataFrame({
    'datacol1': [10, 11, 12, 13, 14],
    'datacol2': [20.0, 21.0, 22.0, 23.0, 24.0],
    'targetcol': [0, 1, 2, 3, 4],
    })


class TestCSV:
    @pytest.fixture
    def CSV(self):
        from palladium.dataset import CSV
        return CSV

    def test_it(self, CSV):
        with patch("palladium.dataset.CSV.pandas_read") as read_csv:
            read_csv.return_value = dummy_dataframe[3:5]  # simulate skiprows
            dataset = CSV('mypath', 'targetcol', some='keyword', skiprows=3)
            data, target = dataset()

        read_csv.assert_called_with('mypath', some='keyword', skiprows=3)
        assert len(data) == len(target) == 2
        assert data.tolist() == [[13, 23.0], [14, 24.0]]
        assert target.tolist() == [3, 4]

    def test_ndarray_false(self, CSV):
        with patch("palladium.dataset.CSV.pandas_read") as read_csv:
            read_csv.return_value = dummy_dataframe[3:5]
            dataset = CSV('mypath', 'targetcol', some='keyword',
                          skiprows=3, ndarray=False)  # simulate skiprows
            data, target = dataset()

        assert data['datacol1'].tolist() == [13, 14]
        assert data['datacol2'].tolist() == [23.0, 24.0]
        assert target.tolist() == [3, 4]

    def test_no_slice(self, CSV):
        with patch("palladium.dataset.CSV.pandas_read") as read_csv:
            read_csv.return_value = dummy_dataframe
            dataset = CSV('mypath', 'targetcol', some='keyword')
            data, target = dataset()

        read_csv.assert_called_with('mypath', some='keyword')
        assert len(data) == len(target) == len(dummy_dataframe)
        assert data.tolist() == [
            [10, 20.0], [11, 21.0], [12, 22.0], [13, 23.0], [14, 24.0],
            ]
        assert target.tolist() == [0, 1, 2, 3, 4]

    def test_no_target(self, CSV):
        with patch("palladium.dataset.CSV.pandas_read") as read_csv:
            read_csv.return_value = dummy_dataframe
            dataset = CSV('mypath', some='keyword')
            data, target = dataset()

        read_csv.assert_called_with('mypath', some='keyword')
        assert len(data) == len(dummy_dataframe)
        assert target is None


class TestSQL:
    @pytest.fixture
    def SQL(self):
        from palladium.dataset import SQL
        return SQL

    @pytest.fixture
    def sql(self, request, SQL):
        path = '/tmp/palladium.testing-{}.sqlite'.format(os.getpid())
        request.addfinalizer(lambda: os.remove(path))
        sql = SQL(
            url='sqlite:///{}'.format(path),
            sql='select age, weight, salary from employee',
            target_column='salary',
            )

        connection = sql.engine.connect()
        connection.execute("""
        CREATE TABLE EMPLOYEE (
           id INT PRIMARY KEY,
           name TEXT,
           age INT,
           weight REAL,
           salary REAL
           )
           """)
        for values in [
            "(1, 'James', 24, 60.0, 10000.0)",
            "(2, 'Guido', 33, 73.0, 20000.0)",
            "(3, 'Handsome Jack', 27, 67.5, 35000.0)",
            ]:
            connection.execute(
                "INSERT INTO EMPLOYEE VALUES {}".format(values))

        return sql

    def test_it(self, sql):
        X, y = sql()
        assert X.tolist() == [
            [24., 60.],
            [33., 73.],
            [27., 67.5],
            ]
        assert y.tolist() == [
            10000.0,
            20000.0,
            35000.0,
            ]

    def test_ndarray_false(self, sql):
        sql.ndarray = False
        X, y = sql()
        assert X.values.tolist() == [
            [24., 60.],
            [33., 73.],
            [27., 67.5],
            ]
        assert y.values.tolist() == [
            10000.0,
            20000.0,
            35000.0,
            ]

    def test_concurrency(self, sql):
        threads = [Thread(target=sql) for i in range(5)]
        [th.start() for th in threads]
        [th.join() for th in threads]


@pytest.mark.skipif(sklearn.__version__ < "0.20.1",
                    reason="scikit-learn version too old")
class TestOpenML:
    @pytest.fixture
    def OpenML(self):
        from palladium.dataset import OpenML
        return OpenML

    @pytest.mark.slow
    def test_wine_quality(self, OpenML):
        X, y = OpenML('wine-quality-red')()
        assert X.shape == (1599, 11)
        assert y.shape == (1599,)


def test_empty_dataset_loader():
    from palladium.dataset import EmptyDatasetLoader
    edl = EmptyDatasetLoader()
    X, y = edl()
    assert X is None
    assert y is None


class TestScheduledDatasetLoader:
    @pytest.fixture
    def ScheduledDatasetLoader(self, process_store):
        from palladium.dataset import ScheduledDatasetLoader
        return ScheduledDatasetLoader

    @pytest.fixture
    def loader(self, ScheduledDatasetLoader, config):
        loader = ScheduledDatasetLoader(
            MagicMock(),
            {
                'freq': 'DAILY',
                'dtstart': '2014-10-30T13:21:18',
                },
            )
        loader.initialize_component(config)
        return loader

    def test_call(self, process_store, loader):
        assert loader() is loader.impl.return_value

    def test_call_custom_value(self, process_store, loader):
        process_store['data'] = ('X', 'y')
        assert loader() == ('X', 'y')

    def test_update_cache(self, loader):
        loader.impl.return_value = ('bla', 'bla')
        assert loader.update_cache() == ('bla', 'bla')
        assert loader() == ('bla', 'bla')
        assert loader.impl.call_count == 2
