# -*- coding: utf-8 -*-
"""OSC adress pattern matching functions."""

__all__ = ('addr_match')


NON_ADDR_CHARS = ' #*,?[]{}'


def addrmatch(pat, s):
    """Match string s against OSC address pattern pat.

    Returns True if string matches, else False.

    """
    # DEBUG:
    #print("Pat:", pat, "Test:", s)
    spos = 0
    slen = len(s)
    plen = len(pat)
    state = group = None
    negate = False

    for ppos, p in enumerate(pat):
        if state == '[':
            if p == '-':
                # XXX
                pass
            elif p == '!':
                negate = True
            else:
                group.append(p)
        elif state and state[-1] == '{':
            pass
        elif p == '?':
            if spos == slen or s[spos] in NON_ADDR_CHARS:
                return False
        elif p == '*':
            while True:
                ppos += 1
                if ppos == plen:
                    return True
                if pat[ppos] != '*':
                    break

            while spos < slen:
                if addrmatch(pat[ppos:], s[spos:]):
                    return True
                spos += 1

            return False
        elif p == '[':
            state.append('[')
            continue
        elif p == '{':
            state.append('{')
            continue
        else:
            if p != s[spos]:
                return False

        spos += 1
    else:
        # pattern exhausted
        return spos == slen
