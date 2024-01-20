from urllib import parse
from hashlib import sha256
import hmac
import base64

def checksign(p_key, data):
    error = False
    if isinstance(data, dict):
        rdata = {}
        for key, val in data.items():
            rdata[key] = val[0]
        return(True, str(rdata))
        skeys = data.get('sign_keys','')
        skeys_list = str.split(skeys, ',')
        signed_data = {}
        for key in skeys_list:
            signed_data[key] = data.get(key, '')
        return(True, str(signed_data))
        forsignstr = parse.urlencode(signed_data)
        raw = forsignstr.encode("utf-8")
        curkey = p_key.encode("utf-8")
        hashed = hmac.new(curkey, raw, sha256)
        strhash = base64.encodebytes(hashed.digest()).decode('utf-8')
        without_last = strhash.rstrip('\n').rstrip('=')
        rep_arr = {
            '+': '-',
            '/': '_'
        }
        for orig, repr in rep_arr.items():
            without_last = without_last.replace(orig, repr)
        cur_sign = data.get('sign', 'Error')
        if cur_sign == without_last:
            return(True, 'Ok')
        else:
            return(False,'Bad sign')
    else:
        return(False, 'Error CheckSign_1: Data not a dict')
