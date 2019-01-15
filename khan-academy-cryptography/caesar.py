msg1 = 'gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk'
msg2 = 'vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr'
msg3 = '''Klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn'''
train_msg = '''44541134541123335344541242
43424432514121231131135315
54425442444243443251415343
54324234411125513553341342
43225343114454345343225134
31421432513412533412155415
34513351444411225144425442
44441534512355154321345111
13112123514254315333214243
51445315341434512542531544
335154325341443'''
train_msg_2 = '43513544'

class CaesarCipher:
    _max = 26

    def __init__(self, shift):
        self.shift = shift
        self.base = ord('a')

    def encode(self, text):
        encoded_text = [self._transform(c, self.shift) for c in text]
        return "".join(encoded_text)

    def decode(self, text):
        decoded_text = [self._transform(c, -self.shift) for c in text]
        return "".join(decoded_text)

    def _transform(self, c, shift):
        if 'a' <= c <= 'z':
            idx = (ord(c) - self.base + shift) % self._max
            return chr(idx + self.base)
        return c


def test_one_letter():
    assert CaesarCipher(0).encode('foo') == 'foo'

def test_basic():
    assert CaesarCipher(10).encode('lol') == 'vyv'

def test_basic1():
    assert CaesarCipher(-10).encode('vyv') == 'lol'

english_frequency = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.0228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.0095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074
}


def test_frequency_sum():
    assert abs(sum(english_frequency.values()) - 1) < 0.01


def best_effort_caesar_decode(text):
    d = {}
    for c in text:
        if 'a' <= c <= 'z':
            d[c] = d.get(c, 0) + 1
    c, freq = max(d.items(), key=lambda v: v[1])
    diff = ord(c) - ord('e')
    return CaesarCipher(diff).decode(text)


def decode_vigenere(text, password):
    d = ''
    for i in range(len(text)):
        c = text[i]
        shift_idx = ord(password[i % len(password)]) - ord('a')
        new_letter_idx = (ord(c) - ord('a') - shift_idx) % 26
        new_letter = chr(ord('a') + new_letter_idx)
        d += new_letter
    return d

def polybius_decode(text):
    d = ''
    text = text.replace('\n','')
    print(text)
    for i in range(0, len(text), 2):
        if i + 1 == len(text):
            break
        c, k = int(text[i]), int(text[i+1])
        if c == 1:
            d += chr((k-1) + ord('a'))
        elif c == 2:
            if k == 4:
                d += '(i|j}'
            elif k == 5:
                d += 'k'
            else:
                d += chr(5*(c-1) + (k-1) + ord('a'))
        else:
            d+= chr(1 + (c-1)*5 + (k-1) + ord('a'))

    return d

def polybius_extended(text):
    d = ''
    text = text.replace('\n','')
    for i in range(0, len(text), 2):
        if i + 1 == len(text):
            break
        c, k = int(text[i]), int(text[i+1])
        if c < 5 or c == 5 and k <= 2:
            d += chr(ord('a') + (k-1) + 6*(c-1))
        elif c == 5:
            d += str(k-3)
        elif c == 6:
            d += str(k+3)
    return d

def polybius_no_z(text):
    d = ''
    text = text.replace('\n','')
    for i in range(0, len(text), 2):
        if i + 1 == len(text):
            break
        k, c = int(text[i]), int(text[i+1])
        d += chr(ord('a') + (c-1)*5 + (k-1))
    return d


sample = '''
wodryn sx grsmr okmr voddob sx dro zvksxdohd sc
bozvkmon li k voddob cywo pshon xewlob yp zycsdsyxc nygx dro kvzrklod. dro
wodryn sc xkwon kpdob tevsec mkockb, gry econ sd sx rsc zbsfkdo
mybboczyxnoxmo.
'''
print(best_effort_caesar_decode(msg1))
print(best_effort_caesar_decode(msg2))
print(decode_vigenere(msg3, 'sskkuullll'))
print()
print(polybius_no_z(train_msg))
print(polybius_no_z(train_msg_2))
