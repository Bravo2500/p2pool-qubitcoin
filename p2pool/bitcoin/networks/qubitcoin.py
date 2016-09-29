import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'fea503dd'.decode('hex')
P2P_PORT = 7788
ADDRESS_VERSION = 38
RPC_PORT = 7799
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'QubitCoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC=lambda height: 2048*100000000 >> (height + 1)//60480
BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('qubit_hash').getPoWHash(data))
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('qubit_hash').getPoWHash(data))
BLOCK_PERIOD=30
SYMBOL='Q2C'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Qubitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/QubitCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.QubitCoin'), 'QubitCoin.conf')
BLOCK_EXPLORER_URL_PREFIX='http://qubitxplorer.cf/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://qubitxplorer.cf/address/'
TX_EXPLORER_URL_PREFIX = 'http://qubitxplorer.cf/tx/'
SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1)
DUMB_SCRYPT_DIFF=1
DUST_THRESHOLD=0.001e8
