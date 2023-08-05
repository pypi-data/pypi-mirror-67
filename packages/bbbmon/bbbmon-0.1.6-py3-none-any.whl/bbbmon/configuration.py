#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
from typing import NewType, Optional, Tuple, Iterable, List

# Default path
SERVER_PROPERTIES_FILE = "/usr/share/bbb-web/WEB-INF/classes/bigbluebutton.properties"


# Type definitions
Secret = NewType('Secret', str)
Url    = NewType('Url', str)


class Config():
    """
    Holds the Server Configurations for multiple endpoints
    """
    def __init__(self):
        self.endpoints = []

    def from_server(self, path: str=SERVER_PROPERTIES_FILE) -> 'Config':
        """
        If bbbmon is executed on the server, it uses this method to extract the
        Url (bigbluebutton.web.serverURL) and the Secret (securitySalt) from the
        server. Additionally this method is used as a legacy fallback for user
        configuration files that are not a valid ini with [section headers]
        """
        with open(path, "r") as f:
            lines = [l for l in f.readlines()]
            secret = Secret([l for l in lines if l.startswith("securitySalt=")][0].replace("securitySalt=", "")).strip()
            bbb_url = Url([l for l in lines if l.startswith("bigbluebutton.web.serverURL=")][0].replace("bigbluebutton.web.serverURL=", "")).strip()
            bbb_url = "{}/bigbluebutton".format(bbb_url.rstrip('/'))
            endpoint = Endpoint(url=bbb_url, secret=secret)
            self.endpoints.append(endpoint)
        return self

    def from_config(self, path: str) -> 'Config':
        """
        Read config from a given path. If the file has no section headers, try
        to use the .from_server(path) method instead
        """
        config = configparser.ConfigParser()
        try:
            config.read(path, encoding='utf-8')
            for section in config.sections():
                bbb_url = Url(config[section]["bigbluebutton.web.serverURL"])
                bbb_url = "{}/bigbluebutton".format(bbb_url.rstrip('/'))
                secret = Secret(config[section]["securitySalt"]).strip()
                endpoint = Endpoint(url=bbb_url, secret=secret, name=section)
                self.endpoints.append(endpoint)
            return self
        # Fallback for config files without sections
        except configparser.MissingSectionHeaderError:
            self = self.from_server(path)
            return self

    def __len__(self):
        """
        The length of a Config is represented by the number of endpoints
        """
        return len(self.endpoints)

    def __str__(self):
        """
        Allow a Config to be represented by a string quickly
        """
        l = ["Config"]
        for e in ["Endpoint[{}]: {}, SECRET OMITTED".format(e.name, e.url) for e in self.endpoints]:
            l.append(e)
        return "\n".join(l)




class Endpoint():
    """
    Objects of this class represent a single endpoint which runs a bigbluebutton
    instance. The relevant fields are the url and the secret, the name is either
    extracted from the section header of the user configuration file, or – as a
    fallback – from the URL
    """
    def __init__(self, url: Url, secret: Secret, name: str=None):
        self.url = url
        self.secret = secret
        if name is None:
            self.name = url.lower()\
                           .lstrip("http://")\
                           .lstrip("https://")\
                           .rstrip("/bigbluebutton")
        else:
            self.name = name