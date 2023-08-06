#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
from datetime import datetime, timedelta
from typing import NewType, Optional, Tuple, Iterable, List

from bbbmon.xmldict import XmlListConfig, XmlDictConfig
import bbbmon.meetings




FRIENDLY_KEYNAMES = {
    "participantCount"      : "Participants",
    "listenerCount"         : "only listening",
    "voiceParticipantCount" : "Mics on",
    "videoCount"            : "Webcams on",
    "moderatorCount"        : "Number of Moderators"
}



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
    duration = bbbmon.meetings.get_duration(meeting)
    return strfdelta(duration)



def get_formated_presenter_name_id(meeting: XmlDictConfig) -> str:
    """
    Get the formated name of the presenter for a given meeting (with id)
    """
    presenter = bbbmon.meetings.get_presenter(meeting)
    if presenter is not None:
        return "{:<30} ({})".format(presenter["fullName"], presenter["userID"])
    else:
        return "no Presenter"

def get_formated_presenter_name(meeting: XmlDictConfig) -> str:
    """
    Get the formated name of the presenter for a given meeting
    """
    presenter = bbbmon.meetings.get_presenter(meeting)
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
    by_duration = sorted([m for m in meetings], key=lambda x:int(bbbmon.meetings.get_duration(x).total_seconds()), reverse=True)

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