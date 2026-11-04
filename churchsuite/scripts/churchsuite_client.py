#!/usr/bin/env python3
"""Minimal ChurchSuite API v2 client (client credentials grant).

Standard library only. Secrets come from environment variables:

    CHURCHSUITE_CLIENT_ID
    CHURCHSUITE_CLIENT_SECRET
    CHURCHSUITE_API_BASE   optional, defaults to https://api.churchsuite.com/v2
    CHURCHSUITE_TOKEN_URL  optional, defaults to https://login.churchsuite.com/oauth2/token
    CHURCHSUITE_SCOPE      required, space separated, for example "addressbook.read"
                           (full list: https://developer.churchsuite.com/auth)

Verified against developer.churchsuite.com in November 2026: token URL, client
credentials grant with HTTP Basic auth, scopes, default 50 and max 250 per page,
rate limit of 120 requests per 60 seconds (a 429 carries Retry-After).
Endpoints change often, so check the OpenAPI specs before production use.

Usage:

    CHURCHSUITE_SCOPE=addressbook.read python churchsuite_client.py addressbook/contacts per_page=100 status=active
"""
from __future__ import annotations

import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterator, Optional

DEFAULT_BASE = "https://api.churchsuite.com/v2"
DEFAULT_TOKEN_URL = "https://login.churchsuite.com/oauth2/token"


class ChurchSuiteError(RuntimeError):
    pass


class ChurchSuite:
    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        base_url: Optional[str] = None,
        token_url: Optional[str] = None,
        scope: Optional[str] = None,
        timeout: int = 30,
    ) -> None:
        self.client_id = client_id or os.environ.get("CHURCHSUITE_CLIENT_ID", "")
        self.client_secret = client_secret or os.environ.get("CHURCHSUITE_CLIENT_SECRET", "")
        if not self.client_id or not self.client_secret:
            raise ChurchSuiteError(
                "Set CHURCHSUITE_CLIENT_ID and CHURCHSUITE_CLIENT_SECRET in the environment."
            )
        self.base_url = (base_url or os.environ.get("CHURCHSUITE_API_BASE") or DEFAULT_BASE).rstrip("/")
        self.token_url = token_url or os.environ.get("CHURCHSUITE_TOKEN_URL") or DEFAULT_TOKEN_URL
        self.scope = scope or os.environ.get("CHURCHSUITE_SCOPE", "")
        if not self.scope:
            raise ChurchSuiteError(
                'Set CHURCHSUITE_SCOPE, for example "addressbook.read". A scope is required.'
            )
        self.timeout = timeout
        self._token: Optional[str] = None
        self._expires_at = 0.0

    # ---- auth -----------------------------------------------------------
    def _fetch_token(self) -> None:
        form = {"grant_type": "client_credentials"}
        if self.scope:
            form["scope"] = self.scope
        basic = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        req = urllib.request.Request(
            self.token_url,
            data=urllib.parse.urlencode(form).encode(),
            headers={
                "Authorization": f"Basic {basic}",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json",
            },
            method="POST",
        )
        payload = self._send(req)
        self._token = payload["access_token"]
        # refresh a minute early
        self._expires_at = time.time() + int(payload.get("expires_in", 3600)) - 60

    def _auth_header(self) -> Dict[str, str]:
        if not self._token or time.time() >= self._expires_at:
            self._fetch_token()
        return {"Authorization": f"Bearer {self._token}"}

    # ---- http -----------------------------------------------------------
    def _send(self, req: urllib.request.Request, _retries: int = 3) -> Any:
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                body = resp.read().decode("utf-8")
                return json.loads(body) if body else {}
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and _retries > 0:
                wait = exc.headers.get("Retry-After", "")
                time.sleep(min(int(wait) if wait.isdigit() else 5, 60))
                return self._send(req, _retries - 1)
            detail = exc.read().decode("utf-8", "replace")[:500]
            raise ChurchSuiteError(f"HTTP {exc.code} for {req.full_url}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise ChurchSuiteError(f"Network error for {req.full_url}: {exc.reason}") from exc

    def get(self, path: str, **params: Any) -> Any:
        query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None}, doseq=True)
        url = f"{self.base_url}/{path.lstrip('/')}" + (f"?{query}" if query else "")
        req = urllib.request.Request(
            url, headers={**self._auth_header(), "Accept": "application/json"}, method="GET"
        )
        return self._send(req)

    def paginate(self, path: str, per_page: int = 250, **params: Any) -> Iterator[Any]:
        """Yield items across pages (default 50, max 250 per page).

        Items are under 'data'. Stops when a page returns fewer than per_page items,
        so it does not depend on the exact shape of the pagination object.
        """
        page = 1
        while True:
            payload = self.get(path, page=page, per_page=per_page, **params)
            items = payload if isinstance(payload, list) else payload.get("data") or []
            for item in items:
                yield item
            if len(items) < per_page:
                return
            page += 1


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    path = argv[1]
    params = dict(arg.split("=", 1) for arg in argv[2:] if "=" in arg)
    try:
        client = ChurchSuite()
        for item in client.paginate(path, **params):
            print(json.dumps(item))
    except ChurchSuiteError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
