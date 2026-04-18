# Sourced all the patterns using AI
# Probably overkill but I thought 'you never know what you need in the future' lol

import regex as re

TLDS = (
    #
    r"com|net|org|edu|gov|mil|int|biz|info|name|pro|aero|coop|museum|mobi|tel|travel|jobs"
    #
    r"|ru|de|jp|uk|fr|br|it|es|pl|nl|au|cn|ca|in|eu|ch|at|kr|cz|mx"
    r"|be|se|tr|tw|ua|ir|vn|cl|sk|no|fi|us|pt|dk|ar|hu|ro|my|gr|il"
    r"|nz|sg|ee|th|bg|hk|rs|lt|ph|si|by|lv|hr|ng|kz|ae|is|sa|pe|za"
    #
    r"|tv|io|co|me|cc|to|ly|fm|la|ws|am|ms|ac|ag|bz|cx|dj|gs|gy|hn"
    r"|ht|im|je|ki|lc|md|mn|ms|mu|mv|mw|mx|nf|nr|nu|pn|ps|pw|sc|sl"
    r"|sm|sn|so|sr|st|su|sx|tc|tf|tl|tm|vc|ve|vg|vi|vu|wf|ws|yt|zm"
    #
    r"|xyz|top|online|shop|site|store|app|tech|club|info|news|live|pro"
    r"|dev|ai|link|wiki|tips|cat|mobi|jobs|biz|name|media|digital|web"
    r"|network|world|space|today|cloud|email|blog|design|studio|agency"
    r"|solutions|services|support|center|group|team|global|international"
    r"|systems|software|hosting|domains|marketing|consulting|training"
    r"|finance|capital|ventures|fund|holdings|partners|associates|legal"
    r"|health|care|clinic|dental|vision|fitness|yoga|spa|beauty|salon"
    r"|restaurant|cafe|bar|pub|pizza|food|kitchen|recipes|menu|delivery"
    r"|photography|photos|gallery|art|music|band|video|film|movie|tv"
    r"|games|game|play|casino|poker|bet|sport|football|soccer|golf|ski"
    r"|travel|tours|flights|hotel|rentals|properties|estate|realty|land"
    r"|school|academy|college|courses|education|degree|mba|phd"
    r"|church|faith|bible|charity|foundation|institute|university"
    r"|energy|solar|green|eco|bio|science|lab|research|engineering"
    r"|auto|cars|motors|parts|repair|garage|drive|bike|moto"
    r"|fashion|clothing|shoes|jewelry|watches|luxury|boutique"
    r"|accountant|tax|bank|insurance|loans|mortgage|money|cash|pay|trade"
)

PATTERNS = {
    # -------------------------------------------------------------------------
    # Web
    # -------------------------------------------------------------------------
    "email": re.compile(
        rf"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(?:{TLDS})\b",
        re.IGNORECASE,
    ),
    "url": re.compile(
        rf"\b(?:https?://|www\.)[^\s<>\"']+|[a-zA-Z0-9.-]+\.(?:{TLDS})\b",
        re.IGNORECASE,
    ),
    "user_agent": re.compile(r"Mozilla/\d+\.\d+\s*\([^)]+\)[^\n\"']*"),
    "html_tag": re.compile(
        r"</?[a-zA-Z][a-zA-Z0-9]*(?:\s+[^>]*)?\s*/?>",
    ),
    "html_comment": re.compile(r"<!--[\s\S]*?-->"),
    "css_color_hex": re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b"),
    "css_color_rgb": re.compile(
        r"rgba?\(\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*\d{1,3}(?:\s*,\s*[\d.]+)?\s*\)"
    ),
    # -------------------------------------------------------------------------
    # Network
    # -------------------------------------------------------------------------
    "ipv4": re.compile(
        r"(?<![/\d])(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
    ),
    "ipv6": re.compile(
        r"\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b"
        r"|\b(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}\b"
        r"|\b::(?:[0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4}\b"
        r"|\b::1\b"
        r"|\bfe80:(?::[0-9a-fA-F]{0,4}){0,4}\b"
    ),
    "cidr": re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)/(?:3[0-2]|[12]?\d)\b"
    ),
    "port": re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?):(\d{1,5})\b"
        r"|\blocalhost:(\d{1,5})\b"
    ),
    "mac_address": re.compile(r"\b(?:[0-9a-fA-F]{2}[:\-]){5}[0-9a-fA-F]{2}\b"),
    # -------------------------------------------------------------------------
    # Security & Secrets
    # -------------------------------------------------------------------------
    "jwt": re.compile(r"\beyJ[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+\b"),
    "bearer_token": re.compile(r"\bBearer\s+([a-zA-Z0-9_\-\.]+)\b"),
    "api_key": re.compile(
        r"\b(?:api[_\-]?key|apikey|access[_\-]?key|secret[_\-]?key)\s*[:=]\s*['\"]?([a-zA-Z0-9_\-]{16,64})['\"]?",
        re.IGNORECASE,
    ),
    "aws_key": re.compile(r"\b(AKIA[0-9A-Z]{16})\b"),
    "private_key_header": re.compile(
        r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"
    ),
    "base64": re.compile(
        r"\b(?:[A-Za-z0-9+/]{4}){8,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?\b"
    ),
    "password_in_url": re.compile(
        r"(?:https?|ftp|mongodb|postgresql|postgres|redis|mysql)://[^:@\s]+:([^@\s]+)@",
        re.IGNORECASE,
    ),
    "connection_string": re.compile(
        r"(?:mongodb|postgresql|postgres|mysql|redis|amqp|rabbitmq|sqlite)(?:\+\w+)?://[^\s\"']+",
        re.IGNORECASE,
    ),
    # -------------------------------------------------------------------------
    # Dev & Infrastructure
    # -------------------------------------------------------------------------
    "uuid": re.compile(
        r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
    ),
    "semver": re.compile(
        r"\bv\d+\.\d+\.\d+(?:-[a-zA-Z0-9.]+)?(?:\+[a-zA-Z0-9.]+)?\b"
        r"|(?<![.\d])(?:[0-9]|[1-9][0-9])\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[a-zA-Z0-9.]+)?(?:\+[a-zA-Z0-9.]+)?(?![.\d])\b",
    ),
    "git_commit": re.compile(
        r"(?:git\s+commits?|commits?|sha|hash|ref|full)\s*:?\s*([0-9a-f]{7,40})"
        r"|(?<=,\s)([0-9a-f]{7,40})\b(?=,|\s|$)",
        re.IGNORECASE,
    ),
    "docker_image": re.compile(
        r"\b(?:[a-z0-9\-]+\.)+[a-z]{2,}/[a-z0-9_\-]+/[a-z0-9_\-\.]+:[a-zA-Z0-9_\-\.]+\b"
        r"|\b(?<!\.)[a-z0-9_\-]+/[a-z0-9_\-\.]+:[a-zA-Z0-9_\-\.]+\b"
        r"|\b(?:nginx|postgres|redis|mysql|mongo|node|python|alpine|ubuntu|debian|centos):[a-zA-Z0-9_\-\.]+\b",
    ),
    "env_variable": re.compile(r"\b([A-Z][A-Z0-9_]{2,})\s*=\s*(.+)"),
    "filepath_unix": re.compile(r"(?:^|(?<=\s))/(?:[\w\-.]+/)*[\w\-.]*"),
    "filepath_windows": re.compile(r"\b[A-Za-z]:\\(?:[\w\s\-\.]+\\)*[\w\s\-\.]*"),
    "python_import": re.compile(
        r"^\s*import\s+([\w.]+(?:\s*,\s*[\w.]+)*)\s*$"
        r"|^\s*from\s+([\w.]+)\s+import\s+[\w.,\s*]+$",
        re.MULTILINE,
    ),
    "shebang": re.compile(
        r"^#!.+$",
        re.MULTILINE,
    ),
    "inline_comment": re.compile(
        r"(?<!:)(?<!\w)(?:#(?!!)(?![0-9a-fA-F]{3,8}\b)(?![^\s/])|\s#(?!!)"
        r"(?![0-9a-fA-F]{3,8}\b)|//(?!/))\s*.+$",
        re.MULTILINE,
    ),
    "json_key": re.compile(r'"([^"]+)"\s*:'),
    "xml_attribute": re.compile(r'\b(\w+)\s*=\s*"([^"]*)"'),
    # -------------------------------------------------------------------------
    # Date & Time
    # -------------------------------------------------------------------------
    "date": re.compile(
        r"(?<!\d\.)(?<!\d)"
        r"(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2}|\d{1,2}\.\d{1,2}\.\d{2,4})"
        r"(?![\d./])"
    ),
    "time": re.compile(
        r"(?<![0-9a-fA-F]:)(?<![0-9a-fA-F])\b(?:[01]?\d|2[0-3]):[0-5]\d(?::[0-5]\d)?(?:\s?[APap][Mm])?\b"
    ),
    "iso8601": re.compile(
        r"\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:?\d{2})?"
    ),
    "unix_timestamp": re.compile(r"\b1[0-9]{9}\b"),
    # -------------------------------------------------------------------------
    # Finance
    # -------------------------------------------------------------------------
    "credit_card": re.compile(
        r"\b(?:4\d{12}(?:\d{3})?|5[1-5]\d{14}|3[47]\d{13}|3(?:0[0-5]|[68]\d)\d{11}|6(?:011|5\d{2})\d{12})\b"
    ),
    "iban": re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}(?:[A-Z0-9]{0,16})?\b"),
    "btc_address": re.compile(r"\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b"),
    "eth_address": re.compile(r"\b0x[0-9a-fA-F]{40}\b"),
    "price": re.compile(
        r"(?:[$€£¥₹])\s?\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?"
        r"|(?<!\d)\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?[^\S\n]?(?:USD|EUR|GBP|JPY|INR|BTC|ETH)(?!\w)",
        re.IGNORECASE,
    ),
    # -------------------------------------------------------------------------
    # Identity & Documents
    # -------------------------------------------------------------------------
    "phone": re.compile(
        r"(?<!\d)"
        r"(?:"
        r"\+[\d\s\-.\(\)]{7,20}"
        r"|\(?\d{3}\)?[\s\-.]\d{3}[\s\-.]\d{4}"
        r")"
        r"(?!\d)",
    ),
    "ssn": re.compile(r"\b(?!000|666|9\d{2})\d{3}-(?!00)\d{2}-(?!0000)\d{4}\b"),
    "passport": re.compile(r"\b[A-Z]{1,2}[0-9]{6,9}\b"),
    "postal_code": re.compile(
        r"\b[A-Z]{1,2}\d[A-Z\d]?\s\d[A-Z]{2}\b"
        r"|\b\d{4}[A-Z]{2}\b"
        r"|\b[A-Z]\d[A-Z]\s?\d[A-Z]\d\b"
        r"|(?<![\d:])\b\d{5}(?:-\d{4})?(?!\d)\b",
    ),
    "coordinates": re.compile(
        r"(?<![.\d])[-+]?(?:[1-8]?\d(?:\.\d{2,})|90(?:\.0+))"
        r",\s*"
        r"[-+]?(?:180(?:\.0+)?|(?:1[0-7]\d|[1-9]?\d)(?:\.\d{2,}))(?![.\d])",
    ),
    # -------------------------------------------------------------------------
    # Social
    # -------------------------------------------------------------------------
    "hashtag": re.compile(
        r"(?<!\S)#(?![0-9a-fA-F]{3,8}\b)[a-zA-Z]\w+",
    ),
    "mention": re.compile(
        r"(?<!\S)@[a-zA-Z]\w+",
    ),
    # -------------------------------------------------------------------------
    # Logs & HTTP
    # -------------------------------------------------------------------------
    "log_level": re.compile(
        r"\b(DEBUG|INFO|WARNING|WARN|ERROR|CRITICAL|FATAL|TRACE|NOTICE)\b"
    ),
    "http_method": re.compile(
        r"\b(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|CONNECT|TRACE)\b"
    ),
    "http_status": re.compile(r"(?:(?:HTTP/[\d.]+|->)\s*)([1-5][0-9]{2})\b"),
    "log_timestamp": re.compile(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}(?:[.,]\d+)?"),
    "stack_trace": re.compile(
        r"(?:at\s+[\w.$]+\([\w./]+:\d+:\d+\)"
        r"|File \"[^\"]+\", line \d+(?:, in \w+)?)",
        re.MULTILINE,
    ),
}
