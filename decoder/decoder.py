import logging

from .msg import Msg
from .binrw import Buffer

"""
Replicate com.ankamagames.jerakine.network.CustomDataWrapper
"""

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("labot")

def readMsg(hex, from_client):
    data = Buffer(bytearray.fromhex(hex))
    return Msg.fromRaw(data, from_client).json()
