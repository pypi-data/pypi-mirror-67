#!/usr/bin/env python3

# Copyright (C) 2020 The btclib developers
#
# This file is part of btclib. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution.
#
# No part of btclib including this file, may be copied, modified, propagated,
# or distributed except according to the terms contained in the LICENSE file.

from typing import Optional, Tuple

from . import bip32
from .alias import BIP32Key, PrvKey, String
from .base58 import b58decode
from .curve import Curve
from .curves import secp256k1
from .network import NETWORKS, network_from_key_value, network_from_xprv
from .utils import bytes_from_octets


def _prvkey_info_from_wif(wif: String) -> Tuple[int, str, bool]:
    "Return (prvkey, compressed, network) info from WIF."

    if isinstance(wif, str):
        wif = wif.strip()

    payload = b58decode(wif)

    network = network_from_key_value('wif', payload[0:1])
    ec = NETWORKS[network]['curve']

    if len(payload) == ec.nsize + 2:       # compressed WIF
        compressed = True
        if payload[-1] != 0x01:            # must have a trailing 0x01
            raise ValueError("Not a compressed WIF: missing trailing 0x01")
        prvkey = payload[1:-1]
    elif len(payload) == ec.nsize + 1:     # uncompressed WIF
        compressed = False
        prvkey = payload[1:]
    else:
        raise ValueError(f"Wrong WIF size ({len(payload)})")

    q = int.from_bytes(prvkey, byteorder='big')
    if not 0 < q < ec.n:
        raise ValueError(f"Private key {hex(q)} not in [1, n-1]")

    return q, network, compressed


def _prvkey_info_from_xprv(xprv: BIP32Key) -> Tuple[int, str, bool]:
    "Return (prvkey, compressed, network) info from BIP32xprv."

    if not isinstance(xprv, dict):
        xprv = bip32.deserialize(xprv)
    if xprv['key'][0] != 0:
        m = f"Not a private key: {bip32.serialize(xprv).decode()}"
        raise ValueError(m)

    network = network_from_xprv(xprv['version'])
    q = int.from_bytes(xprv['key'][1:], byteorder='big')
    return q, network, True


def _prvkey_info_from_xprvwif(xprvwif: BIP32Key) -> Tuple[int, str, bool]:
    """Return (prvkey, compressed, network) info from WIF or BIP32xprv.

    Support WIF or BIP32 xprv.
    """

    if not isinstance(xprvwif, dict):
        try:
            return _prvkey_info_from_wif(xprvwif)
        except Exception:
            pass

    return _prvkey_info_from_xprv(xprvwif)


def prvkey_info_from_prvkey(prvkey: PrvKey, network: Optional[str] = None,
                            compressed: Optional[bool] = None) -> Tuple[int, str, bool]:

    compr = True if compressed is None else compressed
    net = 'mainnet' if network is None else network
    ec = NETWORKS[net]['curve']

    if isinstance(prvkey, int):
        q = prvkey
    elif isinstance(prvkey, dict):
        q, net, compr = _prvkey_info_from_xprv(prvkey)
        if compressed is not None and compr != compressed:
            m = "Compressed key provided, uncompressed key requested"
            raise ValueError(m)
        if network is not None and net != network:
            m = f"{net.capitalize()} key provided, {network} key requested"
            raise ValueError(m)
        return q, net, compr
    else:
        try:
            q, net, compr = _prvkey_info_from_xprvwif(prvkey)
        except Exception:
            pass
        else:
            if compressed is not None and compr != compressed:
                m = "Compression requirement mismatch"
                raise ValueError(m)
            if network is not None and net != network:
                m = f"{net.capitalize()} key provided, {network} key requested"
                raise ValueError(m)
            return q, net, compr

        prvkey = bytes_from_octets(prvkey, ec.nsize)
        q = int.from_bytes(prvkey, 'big')

    if not 0 < q < ec.n:
        raise ValueError(f"Private key {hex(q).upper()} not in [1, n-1]")

    return q, net, compr


def int_from_prvkey(prvkey: PrvKey, ec: Curve = secp256k1) -> int:
    """Return a verified-as-valid private key integer.

    It supports:

    - WIF (bytes or string)
    - BIP32 extended keys (bytes, string, or BIP32KeyDict)
    - SEC Octets (bytes or hex-string, with 02, 03, or 04 prefix)
    - integer (native int or hex-strin)
    """

    if isinstance(prvkey, int):
        q = prvkey
    elif isinstance(prvkey, dict):
        q, network, _ = _prvkey_info_from_xprvwif(prvkey)
        # q has been validated on the xprv/wif network
        ec2 = NETWORKS[network]['curve']
        assert ec == ec2, f"ec / network ({network}) mismatch"
        return q
    else:
        try:
            q, network, _ = _prvkey_info_from_xprvwif(prvkey)
        except Exception:
            pass
        else:
            # q has been validated on the xprv/wif network
            ec2 = NETWORKS[network]['curve']
            assert ec == ec2, f"ec / network ({network}) mismatch"
            return q

        prvkey = bytes_from_octets(prvkey, ec.nsize)
        q = int.from_bytes(prvkey, 'big')

    if not 0 < q < ec.n:
        raise ValueError(f"Private key {hex(q).upper()} not in [1, n-1]")

    return q
