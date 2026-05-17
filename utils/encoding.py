"""Base64 和 URL 编码解码工具"""
import base64
import binascii
from urllib.parse import quote, unquote


def b64encodes(s: str) -> str:
    """标准 Base64 编码"""
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')


def b64encodes_safe(s: str) -> str:
    """URL 安全的 Base64 编码"""
    return base64.urlsafe_b64encode(s.encode('utf-8')).decode('utf-8')


def b64decodes(s: str) -> str:
    """标准 Base64 解码"""
    ss = s + '=' * ((4 - len(s) % 4) % 4)
    try:
        return base64.b64decode(ss.encode('utf-8')).decode('utf-8')
    except UnicodeDecodeError:
        raise
    except binascii.Error:
        raise


def b64decodes_safe(s: str) -> str:
    """URL 安全的 Base64 解码"""
    ss = s + '=' * ((4 - len(s) % 4) % 4)
    try:
        return base64.urlsafe_b64decode(ss.encode('utf-8')).decode('utf-8')
    except UnicodeDecodeError:
        raise
    except binascii.Error:
        raise


def url_quote(s: str) -> str:
    """URL 编码"""
    return quote(s)


def url_unquote(s: str) -> str:
    """URL 解码"""
    return unquote(s)
