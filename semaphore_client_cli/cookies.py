

def http2time(text):
    """Returns time in seconds since epoch of time represented by a string.

    Return value is an integer.

    None is returned if the format of str is unrecognized, the time is outside
    the representable range, or the timezone string is not recognized.  If the
    string contains no timezone, UTC is assumed.

    The timezone in the string may be numerical (like "-0800" or "+0100") or a
    string timezone (like "UTC", "GMT", "BST" or "EST").  Currently, only the
    timezone strings equivalent to UTC (zero offset) are known to the function.

    The function loosely parses the following formats:

    Wed, 09 Feb 1994 22:23:32 GMT       -- HTTP format
    Tuesday, 08-Feb-94 14:15:29 GMT     -- old rfc850 HTTP format
    Tuesday, 08-Feb-1994 14:15:29 GMT   -- broken rfc850 HTTP format
    09 Feb 1994 22:23:32 GMT            -- HTTP format (no weekday)
    08-Feb-94 14:15:29 GMT              -- rfc850 format (no weekday)
    08-Feb-1994 14:15:29 GMT            -- broken rfc850 format (no weekday)

    The parser ignores leading and trailing whitespace.  The time may be
    absent.

    If the year is given with only 2 digits, the function will select the
    century that makes the year closest to the current date.

    """
    # fast exit for strictly conforming string
    m = STRICT_DATE_RE.search(text)
    if m:
        g = m.groups()
        mon = MONTHS_LOWER.index(g[1].lower()) + 1
        tt = (int(g[2]), mon, int(g[0]),
              int(g[3]), int(g[4]), float(g[5]))
        return _timegm(tt)

    # No, we need some messy parsing...

    # clean up
    text = text.lstrip()
    text = WEEKDAY_RE.sub("", text, 1)  # Useless weekday

    # tz is time zone specifier string
    day, mon, yr, hr, min, sec, tz = [None]*7

    # loose regexp parse
    m = LOOSE_HTTP_DATE_RE.search(text)
    if m is not None:
        day, mon, yr, hr, min, sec, tz = m.groups()
    else:
        return None  # bad format

    return _str2time(day, mon, yr, hr, min, sec, tz)

def strip_quotes(text):
    if text.startswith('"'):
        text = text[1:]
    if text.endswith('"'):
        text = text[:-1]
    return text

def parse_ns_headers(ns_headers):
    """Ad-hoc parser for Netscape protocol cookie-attributes.

    The old Netscape cookie format for Set-Cookie can for instance contain
    an unquoted "," in the expires field, so we have to use this ad-hoc
    parser instead of split_header_words.

    XXX This may not make the best possible effort to parse all the crap
    that Netscape Cookie headers contain.  Ronald Tschalar's HTTPClient
    parser is probably better, so could do worse than following that if
    this ever gives any trouble.

    Currently, this is also used for parsing RFC 2109 cookies.

    """
    known_attrs = ("expires", "domain", "path", "secure",
                # RFC 2109 attrs (may turn up in Netscape cookies, too)
                "version", "port", "max-age")

    result = []
    for ns_header in ns_headers:
        pairs = []
        version_set = False

        # XXX: The following does not strictly adhere to RFCs in that empty
        # names and values are legal (the former will only appear once and will
        # be overwritten if multiple occurrences are present). This is
        # mostly to deal with backwards compatibility.
        for ii, param in enumerate(ns_header.split(';')):
            param = param.strip()

            key, sep, val = param.partition('=')
            key = key.strip()

            if not key:
                if ii == 0:
                    break
                else:
                    continue

            # allow for a distinction between present and empty and missing
            # altogether
            val = val.strip() if sep else None

            if ii != 0:
                lc = key.lower()
                if lc in known_attrs:
                    key = lc

                if key == "version":
                    # This is an RFC 2109 cookie.
                    if val is not None:
                        val = strip_quotes(val)
                    version_set = True
                elif key == "expires":
                    # convert expires date to seconds since epoch
                    if val is not None:
                        val = http2time(strip_quotes(val))  # None if invalid
            pairs.append((key, val))

        if pairs:
            if not version_set:
                pairs.append(("version", "0"))
            result.append(pairs)

    return result
