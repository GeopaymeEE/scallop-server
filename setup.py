from setuptools import setup

setup(
    name="electrum-server",
    version="0.9",
    scripts=['run_electrum_server','electrum-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'scallopserver':'src'
        },
    py_modules=[
        'scallopserver.__init__',
        'scallopserver.utils',
        'scallopserver.storage',
        'scallopserver.deserialize',
        'scallopserver.networks',
        'scallopserver.blockchain_processor',
        'scallopserver.server_processor',
        'scallopserver.processor',
        'scallopserver.version',
        'scallopserver.ircthread',
        'scallopserver.stratum_tcp',
        'scallopserver.stratum_http'
    ],
    description="Bitcoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Electrum Lightweight Bitcoin Wallet"""
)


