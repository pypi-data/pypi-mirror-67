# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_import_tables_from_csv_files 1'] = {
    'beam_file_paths': [
        {
            'beam_file_path_id': 1,
            'beam_id': 1070,
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20190304'
        },
        {
            'beam_file_path_id': 2,
            'beam_id': 1120,
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20190607'
        },
        {
            'beam_file_path_id': 3,
            'beam_id': 1130,
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20200123'
        },
        {
            'beam_file_path_id': 4,
            'beam_id': 1150,
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20200207'
        }
    ],
    'beams': [
        {
            'beam_id': 1010,
            'input_beam_id': '',
            'input_map_id': '',
            'name': '20180101'
        },
        {
            'beam_id': 1070,
            'input_beam_id': '',
            'input_map_id': '',
            'name': '20190304'
        },
        {
            'beam_id': 1120,
            'input_beam_id': '',
            'input_map_id': '',
            'name': '20190607'
        },
        {
            'beam_id': 1130,
            'input_beam_id': '',
            'input_map_id': 1012,
            'name': '20200123'
        },
        {
            'beam_id': 1150,
            'input_beam_id': 1130,
            'input_map_id': 1013,
            'name': '20200207'
        }
    ],
    'map_file_paths': [
        {
            'map_file_path_id': 1,
            'map_id': 1001,
            'note': '',
            'path': 'nersc:/go/to/my/maps'
        },
        {
            'map_file_path_id': 2,
            'map_id': 1012,
            'note': 'lat only',
            'path': 'nersc:/go/to/my/maps_v2'
        },
        {
            'map_file_path_id': 3,
            'map_id': 1012,
            'note': 'lat only',
            'path': 'abcde:/path/to/the/maps_v2'
        },
        {
            'map_file_path_id': 4,
            'map_id': 1013,
            'note': 'lat only',
            'path': 'nersc:/go/to/my/maps_v3'
        }
    ],
    'maps': [
        {
            'date_posted': GenericRepr('datetime.date(2019, 2, 13)'),
            'map_id': 1001,
            'mapper': 'pwg-pmn',
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam'''
        },
        {
            'date_posted': GenericRepr('datetime.date(2020, 1, 20)'),
            'map_id': 1012,
            'mapper': 'pwg-pmn',
            'name': 'lat20200120',
            'note': '''- This is a dummy test with a lat map
- A beam depends on this map'''
        },
        {
            'date_posted': GenericRepr('datetime.date(2020, 2, 1)'),
            'map_id': 1013,
            'mapper': 'pwg-pmn',
            'name': 'lat20200201',
            'note': '''- This is a dummy test with a lat map
- A beam depends on this map'''
        }
    ],
    'simulation_file_paths': [
        {
            'note': '',
            'path': 'nersc:/go/to/my/simulations',
            'simulation_file_path_id': 1,
            'simulation_id': 1001
        },
        {
            'note': '',
            'path': 'abcde:/path/to/the/simulations',
            'simulation_file_path_id': 2,
            'simulation_id': 1001
        }
    ],
    'simulations': [
        {
            'date_posted': GenericRepr('datetime.date(2019, 3, 15)'),
            'mapper': 'abc-def',
            'name': 'xyz-s1234-20200101',
            'note': '''- note 1
- note 2''',
            'simulation_id': 1001
        }
    ]
}
