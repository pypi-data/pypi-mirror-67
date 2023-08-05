#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import hashlib
from datetime import datetime, timedelta
import requests
import appdirs
from xml.etree import cElementTree as ElementTree
from typing import NewType, Optional, Tuple, Iterable, List

# Local module imports
from bbbmon.xmldict import XmlListConfig, XmlDictConfig
from bbbmon.configuration import Config, Endpoint, SERVER_PROPERTIES_FILE, Url, Secret



FRIENDLY_KEYNAMES = {
    "participantCount": "Participants",
    "listenerCount": "only listening",
    "voiceParticipantCount": "Mics on",
    "videoCount": "Webcams on",
    "moderatorCount": "Number of Moderators"
}


def generate_checksum(call_name: str, query_string: str, secret: Secret) -> str:
    """
    Generate Checksum for the request header (passed as value for `?checksum=`)
    """
    m = hashlib.sha1()
    m.update(call_name.encode('utf-8'))
    m.update(query_string.encode('utf-8'))
    m.update(secret.encode('utf-8'))
    return m.hexdigest()


def request_meetings(secret: Secret, bbb_url: Url) -> XmlDictConfig:
    """
    Make a getMeetings-API Call to the bbb instance and return a XmlDictConfig
    with the servers response
    """
    call_name = "getMeetings"
    checksum = generate_checksum(call_name, "", secret)
    url = "{}/api/{}?checksum={}".format(bbb_url, call_name, checksum)
    r = requests.get(url)
    root = ElementTree.XML(r.text)
    xmldict = XmlDictConfig(root)
    if "returncode" in xmldict.keys():
        if xmldict['returncode'] == "FAILED":
            print(xmldict)
            exit()
    else:
        print(r.text)
        exit()
    return xmldict


def get_meetings(secret: Secret, bbb_url: Url) -> Iterable[XmlDictConfig]:
    """
    Request meetings and return a list of them. Sorted by biggest first
    """
    meetings = []
    d = request_meetings(secret, bbb_url)

    if d["meetings"] is None:
        return []

    if type(d["meetings"]["meeting"]) is XmlListConfig:
        meetings = sorted([m for m in d["meetings"]["meeting"] if m["running"] == "true"], key=lambda x:int(x['participantCount']), reverse=True)
    elif type(d["meetings"]["meeting"]) is XmlDictConfig:
        meetings = [d["meetings"]["meeting"]]
    return meetings


def get_presenter(meeting: XmlDictConfig) -> Optional[XmlDictConfig]:
    """
    Get the presenter of a meeting (return None if there is none)
    """
    presenters = []
    if type(meeting["attendees"]["attendee"]) is XmlListConfig:
        presenters = [a for a in meeting["attendees"]["attendee"] if a["isPresenter"] == "true"]
    elif type(meeting["attendees"]["attendee"]) is XmlDictConfig:
        presenters = [meeting["attendees"]["attendee"]]
    
    if len(presenters) > 0:
        return presenters[0]
    else:
        return None


def get_duration(meeting: XmlDictConfig) -> timedelta:
    """
    Return the duration of a meeting
    """
    timestamp = int(meeting["startTime"][:-3])
    start_time = datetime.fromtimestamp(timestamp)
    duration = datetime.now() - start_time
    return duration


def strfdelta(duration: timedelta) -> str:
    """
    Helper function for datetime.timedelta formatting, use like this:
    strfdelta(delta_obj, "{days} days {hours}:{minutes}:{seconds}")
    """
    s = int(duration.total_seconds())

    return '{:02}:{:02}:{:02}'.format(s // 3600, s % 3600 // 60, s % 60)


def format_duration(meeting: XmlDictConfig) -> str:
    """
    Helper functions for duration
    """
    duration = get_duration(meeting)
    return strfdelta(duration)



def get_formated_presenter_name(meeting: XmlDictConfig) -> str:
    """
    Get the formated name of the presenter for a given meeting
    """
    presenter = get_presenter(meeting)
    if presenter is not None:
        return "{:<30} ({})".format(presenter["fullName"], presenter["userID"])
    else:
        return "no Presenter"


def print_leaderboard(meetings: Iterable[XmlDictConfig], key: str):
    """
    Print a leaderboard of all meetings sorted by a given key (e.g. 
    participantCount)
    """
    print("LEADERBOARD ({})".format(FRIENDLY_KEYNAMES[key]))
    sorted_by = sorted([m for m in meetings], key=lambda x:int(x[key]), reverse=True)
    for m in sorted_by:
        print("{:>5} {:<45} {}".format(m[key], m["meetingName"], get_formated_presenter_name(m))) 


def print_duration_leaderboard(meetings: Iterable[XmlDictConfig]):
    """
    Print a leaderboard of all meetings sorted by a given key (e.g. 
    participantCount)
    """
    print("LEADERBOARD (Duration)")
    by_duration = sorted([m for m in meetings], key=lambda x:int(get_duration(x).total_seconds()), reverse=True)

    for m in by_duration:
        print("{:>12} {:<45} {}".format(format_duration(m), m["meetingName"], get_formated_presenter_name(m))) 


def print_overview(config: Config):
    """
    For each endpoint in the configuration get the active meetings and print 
    out an overview of the current bbb-usage
    """
    for i, endpoint in enumerate(config.endpoints):
        meetings = get_meetings(endpoint.secret, endpoint.url)

        # Print divider if there is more than one endpoint
        if i > 0:
            print()
            print("="*80)
            print()

        # If there are no meetings, skip to next endpoint
        if len(meetings) == 0:
            print("MEETINGS on [{}]: None".format(endpoint.name))
            continue

        n_running = len(meetings)
        n_recording = len([m for m in meetings if m["recording"] == "true"])
        n_participants = sum([int(m["participantCount"]) for m in meetings])
        n_listeners = sum([int(m["listenerCount"]) for m in meetings])
        n_voice = sum([int(m["voiceParticipantCount"]) for m in meetings])
        n_video = sum([int(m["videoCount"]) for m in meetings])
        n_moderator = sum([int(m["moderatorCount"]) for m in meetings])

        print("MEETINGS on [{}]:".format(endpoint.name))
        print("   ├─── {:>4} running".format(n_running))
        print("   └─── {:>4} recording".format(n_recording))
        print()
        print("PARTICIPANTS across all {} rooms".format(n_running))
        print("   └─┬─ {:>4} total".format(n_participants))
        print("     ├─ {:>4} listening only".format(n_listeners))
        print("     ├─ {:>4} mic on".format(n_voice))
        print("     ├─ {:>4} video on".format(n_video))
        print("     └─ {:>4} moderators".format(n_moderator))

        print()
        print_leaderboard(meetings, "participantCount")
        print()
        print_leaderboard(meetings, "videoCount")
        print()
        print_leaderboard(meetings, "voiceParticipantCount")
        print()
        print_duration_leaderboard(meetings)


def init_config() -> Optional[Config]:
    """
    Read the config either from the servers bigbluebutton.properties-file or from
    the user config path. Display a message if neither of these files exist.
    """
    # Get OS dependend properties file
    user_config_path = appdirs.user_config_dir("bbbmon")
    user_config_path = "{}.properties".format(user_config_path)

    # Check if we are on the server and try to read that properties file first
    if os.path.isfile(SERVER_PROPERTIES_FILE):
        return Config().from_server()
    elif os.path.isfile(user_config_path):
        return Config().from_config(user_config_path)
    else:
        print("ERROR: There was no config file found. Make sure it exists and is readable:")
        print("[0] {}".format(SERVER_PROPERTIES_FILE))
        print("[1] {}".format(user_config_path))
        print()
        print("For now the file just needs to contain three lines:")
        print("[myservername]")
        print("securitySalt=YOURSUPERSECRETSECRET")
        print("bigbluebutton.web.serverURL=https://bbb.example.com/")
        print()
        print("(You can define multiple server-blocks however)")
        exit()



def main():
    Config = init_config()
    print_overview(Config)


if __name__ == "__main__":
    main()