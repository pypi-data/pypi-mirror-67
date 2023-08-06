from contextlib import contextmanager
from copy import deepcopy
from functools import reduce
import operator
import os
import threading
import time
from unittest.mock import patch

import pytest


class MyDummyComponent:
    def __init__(self, arg1, arg2='blargh', subcomponent=None):
        self.arg1 = arg1
        self.arg2 = arg2
        self.subcomponent = subcomponent
        self.initialize_component_arg = None

    def initialize_component(self, config):
        self.initialize_component_arg = config

    def __eq__(self, other):
        return all([
            self.arg1 == other.arg1,
            self.arg2 == other.arg2,
            self.subcomponent == other.subcomponent,
            self.initialize_component_arg == other.initialize_component_arg,
            ])


class BlockingDummy:
    def __init__(self):
        time.sleep(0.1)


class BadDummy:
    def __init__(self):
        from palladium.config import get_config
        self.cfg = get_config().copy()


@contextmanager
def cwd(path):
    before = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(before)


def test_config_class_keyerror():
    from palladium.config import Config
    with pytest.raises(KeyError) as e:
        Config({})['invalid']
    assert "Maybe you forgot to set" in str(e.value)


class TestInitializeConfig:
    @pytest.fixture
    def initialize_config(self):
        from palladium.config import initialize_config
        return initialize_config

    def test_extra(self, config, initialize_config):
        config.clear()
        initialize_config(two='three')
        assert config['two'] == 'three'

    def test_already_initialized(self, config, initialize_config):
        config.clear()
        config.initialized = True
        with pytest.raises(RuntimeError):
            initialize_config(two='three')


class TestGetConfig:
    @pytest.fixture
    def get_config(self):
        from palladium.config import get_config
        return get_config

    @pytest.fixture
    def config1_fname(self, tmpdir):
        path = tmpdir.join('palladium-config.py')
        path.write("""{
            'env': environ['ENV1'],
            'here': here,
            'blocking': {
                '!': 'palladium.tests.test_config.BlockingDummy',
            }
        }""")
        return str(path)

    @pytest.fixture
    def config2_fname(self, tmpdir):
        path = tmpdir.join('config2.py')
        path.write("{'env': environ['ENV2']}")
        return str(path)

    @pytest.fixture
    def config3_fname(self, tmpdir):
        path = tmpdir.join('config3.py')
        path.write("""{
            'bad': {
                '!': 'palladium.tests.test_config.BadDummy'
             }
        }""")
        return str(path)

    def test_extras(self, get_config):
        assert get_config(foo='bar')['foo'] == 'bar'

    def test_default_config(self, get_config, config1_fname, monkeypatch):
        here = os.path.dirname(config1_fname)
        monkeypatch.setitem(os.environ, 'ENV1', 'one')
        with cwd(here):
            config = get_config()
        assert config['here'] == here

    def test_variables(self, get_config, config1_fname, monkeypatch):
        monkeypatch.setitem(os.environ, 'PALLADIUM_CONFIG', config1_fname)
        monkeypatch.setitem(os.environ, 'ENV1', 'one')
        config = get_config()
        assert config['env'] == 'one'
        assert config['here'] == os.path.dirname(config1_fname)

    def test_multiple_files(self, get_config, config1_fname, config2_fname,
                            monkeypatch):
        monkeypatch.setitem(os.environ, 'PALLADIUM_CONFIG',
                            ','.join([config1_fname, config2_fname]))
        monkeypatch.setitem(os.environ, 'ENV1', 'one')
        monkeypatch.setitem(os.environ, 'ENV2', 'two')
        config = get_config()
        assert config['env'] == 'two'
        assert config['here'] == os.path.dirname(config1_fname)

    def test_multithreaded(self, get_config, config1_fname, monkeypatch):
        monkeypatch.setitem(os.environ, 'PALLADIUM_CONFIG', config1_fname)
        monkeypatch.setitem(os.environ, 'ENV1', 'one')

        cfg = {}

        def get_me_config():
            cfg[threading.get_ident()] = get_config().copy()

        threads = [threading.Thread(target=get_me_config) for i in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        assert reduce(operator.eq, cfg.values())

    def test_pld_config_key(self, get_config, config1_fname, monkeypatch):
        monkeypatch.setitem(os.environ, 'PALLADIUM_CONFIG', config1_fname)
        monkeypatch.setitem(os.environ, 'ENV1', 'one')
        config = get_config()
        assert config['blocking'].__pld_config_key__ == 'blocking'


class TestProcessConfig:
    @pytest.fixture
    def process_config(self):
        from palladium.config import process_config
        return process_config

    @pytest.fixture
    def config1(self):
        dummy = 'palladium.tests.test_config.MyDummyComponent'
        return {
            'mycomponent': {
                '!': dummy,
                'arg1': 3,
                'arg2': {'no': 'factory'},
                'subcomponent': {
                    '!': dummy,
                    'arg1': {
                        'subsubcomponent': {
                            '!':
                            dummy,
                            'arg1': 'wobwob',
                            'arg2': 9,
                            },
                        },
                    'arg2': 6,
                    },
                },
            'mylistofcomponents': [{
                '!': dummy,
                'arg1': 'wobwob',
                },
                'somethingelse',
                ],
            'mynestedlistofcomponents': [[{
                '!': dummy,
                'arg1': 'feep',
                'arg2': {
                    '__factory__': dummy,  # alternative to '!'
                    'arg1': 6,
                },
            }]],
            'myconstant': 42,

            'mycopiedconstant': {
                '__copy__': 'mycomponent.arg1',
                },

            'mydict': {
                'arg1': 1,
                'mycopiedcomponent': {
                    '__copy__': 'mycomponent',
                    'arg2': None,
                    },
                },

            '__python__': """
C['mynestedlistofcomponents'][0][0]['arg2']['!'] = 'builtins:dict'
C['myotherconstant'] = 13
""",
            }

    @pytest.fixture
    def config2(self):
        return {
            'mydict': {
                '__copy__': 'mydict',
                'arg1': 3,
                'arg2': None,
                },
            'mynewdict': {
                '__copy__': 'mydict',
                'arg2': 2,
                },
            'mysupernewdict': {
                '__copy__': 'mynewdict',
                },
            'mycopiedconstant': {
                '__copy__': 'mycopiedconstant',
                '__default__': 42,
                },
            'mycopywithdefault': {
                '__copy__': 'nonexistant',
                '__default__': 42,
                },
            }

    def test_config1(self, process_config, config1):
        config = process_config(config1)

        assert config['myconstant'] == 42

        mycomponent = config['mycomponent']
        assert isinstance(mycomponent, MyDummyComponent)
        assert mycomponent.arg1 == 3
        assert mycomponent.arg2 == {'no': 'factory'}
        assert mycomponent.initialize_component_arg is config

        subcomponent = mycomponent.subcomponent
        assert isinstance(subcomponent, MyDummyComponent)
        assert subcomponent.arg2 == 6
        assert subcomponent.initialize_component_arg is config

        subsubcomponent = subcomponent.arg1['subsubcomponent']
        assert isinstance(subsubcomponent, MyDummyComponent)
        assert subsubcomponent.arg1 == 'wobwob'
        assert subsubcomponent.arg2 == 9
        assert subsubcomponent.initialize_component_arg is config

        mylistofcomponents = config['mylistofcomponents']
        assert len(mylistofcomponents) == 2
        assert isinstance(mylistofcomponents[0], MyDummyComponent)
        assert mylistofcomponents[0].arg1 == 'wobwob'
        assert mylistofcomponents[1] == 'somethingelse'

        mnl = config['mynestedlistofcomponents']
        assert isinstance(mnl[0][0], MyDummyComponent)
        assert mnl[0][0].arg1 == 'feep'

        assert config['mycopiedconstant'] == 3

        mcc = config['mydict']['mycopiedcomponent']
        assert mcc.arg2 is None
        assert mcc.arg1 == mycomponent.arg1
        assert mcc.subcomponent == mycomponent.subcomponent
        assert mcc.subcomponent is not mycomponent.subcomponent

        assert isinstance(mnl[0][0].arg2, dict)
        assert config['myotherconstant'] == 13

    def test_config1_and_2(self, process_config, config1, config2):
        config = process_config(config1, config2)

        assert config['mydict']['arg1'] == 3

        mycomponent = config['mycomponent']
        mcc = config['mydict']['mycopiedcomponent']
        assert mcc.arg2 is None
        assert mcc.arg1 == mycomponent.arg1
        assert mcc.subcomponent == mycomponent.subcomponent
        assert mcc.subcomponent is not mycomponent.subcomponent

        assert config['mynewdict']['arg1'] == config['mydict']['arg1']
        assert config['mynewdict']['arg2'] == 2
        assert isinstance(
            config['mynewdict']['mycopiedcomponent'], MyDummyComponent)
        assert isinstance(
            config['mysupernewdict']['mycopiedcomponent'], MyDummyComponent)

        assert config['mycopiedconstant'] == 3
        assert config['mycopywithdefault'] == 42

    @pytest.fixture
    def config3(self):
        return {
            'first': 5,
            'second': {
                '__copy__': 'first',
                '__default__': 6,
                },
            }

    def test_copy_source_exists_with_default(self, process_config, config3):
        expected = deepcopy(config3)
        expected['second'] = expected['first']
        got = process_config(config3)
        assert got == expected

    def test_copy_source_exists_no_default(self, process_config, config3):
        expected = deepcopy(config3)
        expected['second'] = expected['first']
        del config3['second']['__default__']
        got = process_config(config3)
        assert got == expected

    def test_copy_source_missing_with_default(self, process_config, config3):
        expected = deepcopy(config3)
        expected['second'] = expected['second']['__default__']
        del expected['first']
        del config3['first']
        got = process_config(config3)
        assert got == expected

    def test_copy_source_missing_no_default(self, process_config, config3):
        del config3['first']
        del config3['second']['__default__']
        with pytest.raises(KeyError):
            process_config(config3)

    def test_initialize_config_logging(self, process_config):
        with patch('palladium.config.dictConfig') as dictConfig:
            process_config({'logging': 'yes, please'})
            dictConfig.assert_called_with('yes, please')
