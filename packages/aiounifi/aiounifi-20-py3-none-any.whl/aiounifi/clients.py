"""Clients are devices on a UniFi network."""

from .api import APIItem, APIItems

URL = "/stat/sta"  # Active clients
URL_ALL = "/rest/user"  # All known and configured clients

URL_CLIENT_STATE_MANAGER = "/cmd/stamgr"


class Clients(APIItems):
    """Represents client network devices."""

    KEY = "mac"

    def __init__(self, raw, request):
        super().__init__(raw, request, URL, Client)

    async def async_block(self, mac):
        """Block client from controller."""
        data = {"mac": mac, "cmd": "block-sta"}
        await self._request("post", URL_CLIENT_STATE_MANAGER, json=data)

    async def async_unblock(self, mac):
        """Unblock client from controller."""
        data = {"mac": mac, "cmd": "unblock-sta"}
        await self._request("post", URL_CLIENT_STATE_MANAGER, json=data)


class ClientsAll(APIItems):
    """Represents all client network devices."""

    KEY = "mac"

    def __init__(self, raw, request):
        super().__init__(raw, request, URL_ALL, Client)


class Client(APIItem):
    """Represents a client network device."""

    @property
    def blocked(self):
        return self.raw.get("blocked", "")

    @property
    def essid(self):
        return self.raw.get("essid", "")

    @property
    def hostname(self):
        return self.raw.get("hostname", "")

    @property
    def ip(self):
        return self.raw.get("ip", "")

    @property
    def is_guest(self):
        return self.raw.get("is_guest", "")

    @property
    def is_wired(self):
        return self.raw.get("is_wired", "")

    @property
    def last_seen(self):
        return self.raw.get("last_seen", "")

    @property
    def mac(self):
        return self.raw.get("mac", "")

    @property
    def name(self):
        return self.raw.get("name", "")

    @property
    def oui(self):
        return self.raw.get("oui", "")

    @property
    def site_id(self):
        return self.raw.get("site_id", "")

    @property
    def sw_depth(self):
        return self.raw.get("sw_depth", "")

    @property
    def sw_mac(self):
        """MAC for switch client is connected to."""
        return self.raw.get("sw_mac", "")

    @property
    def sw_port(self):
        """Switch port client is connected to."""
        return self.raw.get("sw_port", "")

    @property
    def rx_bytes(self):
        """Bytes received over wireless connection."""
        return self.raw.get("rx_bytes", 0)

    @property
    def tx_bytes(self):
        """Bytes transferred over wireless connection."""
        return self.raw.get("tx_bytes", 0)

    @property
    def uptime(self):
        return self.raw.get("uptime", 0)

    @property
    def wired_rx_bytes(self):
        """Bytes received over wired connection."""
        return self.raw.get("wired-rx_bytes", 0)

    @property
    def wired_tx_bytes(self):
        """Bytes transferred over wired connection."""
        return self.raw.get("wired-tx_bytes", 0)

    def __repr__(self):
        """Return the representation."""
        name = self.name or self.hostname
        return f"<Client {name}: {self.mac} {self.raw}>"
