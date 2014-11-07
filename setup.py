from setuptools import setup

setup(
    name="electrum-vior-server",
    version="0.9",
    scripts=['run_electrum_vior_server','electrum-vior-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumviorserver':'src'
        },
    py_modules=[
        'electrumviorserver.__init__',
        'electrumviorserver.utils',
        'electrumviorserver.storage',
        'electrumviorserver.deserialize',
        'electrumviorserver.networks',
        'electrumviorserver.blockchain_processor',
        'electrumviorserver.server_processor',
        'electrumviorserver.processor',
        'electrumviorserver.version',
        'electrumviorserver.ircthread',
        'electrumviorserver.stratum_tcp',
        'electrumviorserver.stratum_http'
    ],
    description="ViorCoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/ROIV/ViorCoin-ElectrumServer/",
    long_description="""Server for the Electrum Lightweight ViorCoin Wallet"""
)


