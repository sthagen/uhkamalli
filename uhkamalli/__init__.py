# [[[fill git_describe()]]]
__version__ = '2023.10.22+parent.8d93fb85'
# [[[end]]] (checksum: 0266f11fb6403df290b631f426be17d5)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
