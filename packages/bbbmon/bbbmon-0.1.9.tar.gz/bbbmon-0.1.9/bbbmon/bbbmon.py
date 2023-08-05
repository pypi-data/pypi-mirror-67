#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import hashlib
from datetime import datetime, timedelta
import requests
import click
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



def get_formated_presenter_name_id(meeting: XmlDictConfig) -> str:
    """
    Get the formated name of the presenter for a given meeting (with id)
    """
    presenter = get_presenter(meeting)
    if presenter is not None:
        return "{:<30} ({})".format(presenter["fullName"], presenter["userID"])
    else:
        return "no Presenter"

def get_formated_presenter_name(meeting: XmlDictConfig) -> str:
    """
    Get the formated name of the presenter for a given meeting
    """
    presenter = get_presenter(meeting)
    if presenter is not None:
        return "{:<30}".format(presenter["fullName"])
    else:
        return "no Presenter"


def print_leaderboard(meetings: Iterable[XmlDictConfig], key: str, endpoint_name: str, presenter: bool, presenter_id: bool, fancy: bool):
    """
    Print a leaderboard of all meetings sorted by a given key (e.g. 
    participantCount)
    """
    print_header(endpoint_name, "LEADERBOARD ({})".format(FRIENDLY_KEYNAMES[key]), fancy)
    sorted_by = sorted([m for m in meetings], key=lambda x:int(x[key]), reverse=True)
    for m in sorted_by:
        if presenter:
            if presenter_id:
                print("{:>5} {:<45} {}".format(m[key], m["meetingName"], get_formated_presenter_name_id(m))) 
            else:
                print("{:>5} {:<45} {}".format(m[key], m["meetingName"], get_formated_presenter_name(m))) 
        else:
            print("{:>5} {}".format(m[key], m["meetingName"]))

def print_duration_leaderboard(meetings: Iterable[XmlDictConfig], endpoint_name: str, presenter: bool, presenter_id: bool, fancy: bool):
    """
    Print a leaderboard of all meetings sorted by a given key (e.g. 
    participantCount)
    """
    print_header(endpoint_name, "LEADERBOARD (Duration)", fancy)
    by_duration = sorted([m for m in meetings], key=lambda x:int(get_duration(x).total_seconds()), reverse=True)

    for m in by_duration:
        if presenter:
            if presenter_id:
                print("{:>12} {:<38} {}".format(format_duration(m), m["meetingName"], get_formated_presenter_name_id(m))) 
            else:
                print("{:>12} {:<38} {}".format(format_duration(m), m["meetingName"], get_formated_presenter_name(m))) 
        else:
            print("{:>12} {}".format(format_duration(m), m["meetingName"]))

def print_header(endpoint_name: str, text: str, fancy=True):
    if fancy:
        click.echo(click.style("  [{}] {}  ".format(endpoint_name, text), fg='black', bg='white', bold=True))
    else:
        print("[{}] {}".format(endpoint_name, text))

def print_overview(config: Config, leaderboards: bool, participants: bool, presenter: bool, presenter_id: bool, show_meetings: bool, fancy: bool):
    """
    For each endpoint in the configuration get the active meetings and print 
    out an overview of the current bbb-usage
    """
    for i, endpoint in enumerate(config.endpoints):
        meetings = get_meetings(endpoint.secret, endpoint.url)

        # Print divider if there is more than one endpoint
        if i > 0:
            print()
            print("="*click.get_terminal_size()[0])
            print()

        # If there are no meetings, skip to next endpoint
        if len(meetings) == 0:
            if show_meetings:
                print_header(endpoint.name, "MEETINGS", fancy)
                print("   └─── Currently no active meetings.")
            continue

        n_running = len(meetings)
        n_recording = len([m for m in meetings if m["recording"] == "true"])
        n_participants = sum([int(m["participantCount"]) for m in meetings])
        n_listeners = sum([int(m["listenerCount"]) for m in meetings])
        n_voice = sum([int(m["voiceParticipantCount"]) for m in meetings])
        n_video = sum([int(m["videoCount"]) for m in meetings])
        n_moderator = sum([int(m["moderatorCount"]) for m in meetings])

        if show_meetings:
            print_header(endpoint.name, "MEETINGS", fancy)
            print("   ├─── {:>4} running".format(n_running))
            print("   └─── {:>4} recording".format(n_recording))
            print()

        if participants:
            print_header(endpoint.name, "PARTICIPANTS across all {} rooms".format(n_running), fancy)
            print("   └─┬─ {:>4} total".format(n_participants))
            print("     ├─ {:>4} listening only".format(n_listeners))
            print("     ├─ {:>4} mic on".format(n_voice))
            print("     ├─ {:>4} video on".format(n_video))
            print("     └─ {:>4} moderators".format(n_moderator))

        if leaderboards:
            print()
            print_leaderboard(meetings, "participantCount", endpoint.name, presenter, presenter_id, fancy)
            print()
            print_leaderboard(meetings, "videoCount", endpoint.name, presenter, presenter_id, fancy)
            print()
            print_leaderboard(meetings, "voiceParticipantCount", endpoint.name, presenter, presenter_id, fancy)
            print()
            print_duration_leaderboard(meetings, endpoint.name, presenter, presenter_id, fancy)


def init_config() -> Optional[Config]:
    """
    Read the config either from the servers bigbluebutton.properties-file or from
    the user config path. Display a message if neither of these files exist.
    """
    # Get OS dependend properties file
    user_config_path = click.get_app_dir("bbbmon")
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


@click.command()
@click.option('--endpoint', '-e', multiple=True, help="Filter by one or more endpoints as named in the user configuration. Order is respected.")
@click.option('--leaderboards/--no-leaderboards', default=True, show_default=True, help="Hide or show the meeting leaderboards")
@click.option('--participants/--no-participants', default=True, show_default=True, help="Hide or show the participants")
@click.option('--meetings/--no-meetings', default=True, show_default=True, help="Hide or show the meetings")
@click.option('--presenter/--no-presenter', default=True, show_default=True, help="Hide or show the presenters")
@click.option('--presenter-id/--no-presenter-id', default=True, show_default=True, help="Hide or show the presenter IDs")
@click.option('--fancy/--no-fancy', default=True, show_default=True, help="Use fancy headers")
def main(leaderboards, participants, presenter, presenter_id, meetings, endpoint, fancy):
    config = init_config()
    config.filter_endpoints(endpoint)
    print_overview(config, leaderboards, participants, presenter, presenter_id, meetings, fancy)


if __name__ == "__main__":
    main()