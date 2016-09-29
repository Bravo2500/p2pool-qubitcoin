from p2pool.bitcoin import networks

PARENT=networks.nets['qubitcoin']
SHARE_PERIOD=15 # seconds
NEW_SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=50 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD=30 # blocks
NEW_SPREAD=30 # blocks
IDENTIFIER='fc70135c7a81bc6f'.decode('hex')
PREFIX='9472ef181efcd37b'.decode('hex')
P2P_PORT=8371
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=9372
BOOTSTRAP_ADDRS='q2c1.ignorelist.com q2c2.ignorelist.com q2c3.ignorelist.com q2c4.ignorelist.com'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-q2c'
VERSION_CHECK=lambda v: True
VERSION_WARNING = lambda v: 'Upgrade QubitCoin to >= 0.8.4.3!' if v < 70001 else None
