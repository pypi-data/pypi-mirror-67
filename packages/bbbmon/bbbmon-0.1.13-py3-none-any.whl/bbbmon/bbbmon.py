#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import hashlib
from datetime import datetime, timedelta
import requests
import click
from xml.etree import cElementTree as ElementTree
from typing import NewType, Optional, Tuple, Iterable, List

# Local module imports
from bbbmon.xmldict import XmlListConfig, XmlDictConfig
from bbbmon.configuration import Config, Endpoint, SERVER_PROPERTIES_FILE, Url, Secret, get_user_config_path, init_config, new_config



FRIENDLY_KEYNAMES = {
    "participantCount"      : "Participants",
    "listenerCount"         : "only listening",
    "voiceParticipantCount" : "Mics on",
    "videoCount"            : "Webcams on",
    "moderatorCount"        : "Number of Moderators"
}

# Allow -h as help option as well
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])



class AliasedGroup(click.Group):
    """
    Subclass of Group to allow abbreviating commands like this:
    Instead of `bbbmon meetings` one could type `bbbmon m`
    """
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))


def generate_checksum(call_name: str, query_string: str, secret: Secret) -> str:
    """
    Generate Checksum for the request header (passed as value for `?checksum=`)
    """
    m = hashlib.sha1()
    m.update(call_name.encode('utf-8'))
    m.update(query_string.encode('utf-8'))
    m.update(secret.encode('utf-8'))
    return m.hexdigest()


def request_meetings(secret: Secret, bbb_url: Url, user_config_path: str) -> XmlDictConfig:
    """
    Make a getMeetings-API Call to the bbb instance and return a XmlDictConfig
    with the servers response
    """
    call_name = "getMeetings"
    checksum = generate_checksum(call_name, "", secret)
    url = "{}/api/{}?checksum={}".format(bbb_url, call_name, checksum)

    try:
        r = requests.get(url)
    except:
        click.echo("{} The URL \"{}\" is unreachable.\n       Check your network connection, and the URL and Secret of the endpoint.".format(click.style('Error:', fg='red', bold=True), url))
        print()
        time.sleep(1)
        if click.confirm(click.style('Do you want to open the config file at {} with your default editor?'.format(user_config_path), fg="yellow"), abort=True):
            click.edit(filename=user_config_path)
            exit()

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


def get_meetings(secret: Secret, bbb_url: Url, user_config_path: str) -> Iterable[XmlDictConfig]:
    """
    Request meetings and return a list of them. Sorted by biggest first
    """
    meetings = []
    d = request_meetings(secret, bbb_url, user_config_path)

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


def print_overview(config: Config, leaderboards: bool, participants: bool, presenter: bool, presenter_id: bool, show_meetings: bool, watch: int, fancy: bool):
    """
    For each endpoint in the configuration get the active meetings and print 
    out an overview of the current bbb-usage
    """

    # Request Meetings from API
    meetings = [get_meetings(e.secret, e.url, config.path) for e in config.endpoints]

    # Clear screen after request is done, and before printing new data to keep
    # blinking to a minimum
    if watch is not None:
        click.clear()


    for i, endpoint in enumerate(config.endpoints):
        meeting = meetings[i]

        # Print divider if there is more than one endpoint
        if i > 0:
            print()
            print("="*click.get_terminal_size()[0])
            print()

        # If there are no meetings, skip to next endpoint
        if len(meeting) == 0:
            if show_meetings:
                print_header(endpoint.name, "MEETINGS", fancy)
                print("   └─── Currently no active meetings.")
            continue

        n_running = len(meeting)
        n_recording = len([m for m in meeting if m["recording"] == "true"])
        n_participants = sum([int(m["participantCount"]) for m in meeting])
        n_listeners = sum([int(m["listenerCount"]) for m in meeting])
        n_voice = sum([int(m["voiceParticipantCount"]) for m in meeting])
        n_video = sum([int(m["videoCount"]) for m in meeting])
        n_moderator = sum([int(m["moderatorCount"]) for m in meeting])

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
            print_leaderboard(meeting, "participantCount", endpoint.name, presenter, presenter_id, fancy)
            print()
            print_leaderboard(meeting, "videoCount", endpoint.name, presenter, presenter_id, fancy)
            print()
            print_leaderboard(meeting, "voiceParticipantCount", endpoint.name, presenter, presenter_id, fancy)
            print()
            print_duration_leaderboard(meeting, endpoint.name, presenter, presenter_id, fancy)



@click.group(context_settings=CONTEXT_SETTINGS, cls=AliasedGroup)
def main():
    """BBBMON is a small CLI utility to monitor bbb usage

    \b
    Examples:  bbbmon config --edit
               bbbmon meetings --watch 20 --endpoint bbb

    Internally bbbmon relies on the offical bbb-API, which means you need to have the server's secret in order to create a valid request. Create a new configuration with: bbbmon config --new
    """
    pass 

@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.option('--endpoint', '-e', multiple=True, help="Filter by one or more endpoints as named in the user configuration (e.g. [servername]). Order is respected.")
@click.option('--watch', '-w', help="Run repeatedly with the given interval in seconds", type=click.IntRange(2, 2147483647, clamp=True))
@click.option('--leaderboards/--no-leaderboards', default=True, show_default=True, help="Hide or show the meeting leaderboards")
@click.option('--participants/--no-participants', default=True, show_default=True, help="Hide or show the participants")
@click.option('--meetings/--no-meetings', default=True, show_default=True, help="Hide or show the meetings")
@click.option('--presenter/--no-presenter', default=True, show_default=True, help="Hide or show the presenters")
@click.option('--presenter-id/--no-presenter-id', default=True, show_default=True, help="Hide or show the presenter IDs")
@click.option('--fancy/--no-fancy', default=True, show_default=True, help="Use fancy headers")
def meetings(ctx, leaderboards, participants, presenter, watch, presenter_id, meetings, endpoint, fancy):
    """View currently active meetings"""
    config = init_config()
    config.filter_endpoints(endpoint)
    if watch is not None:
        while watch is not None:
            print_overview(config, leaderboards, participants, presenter, presenter_id, meetings, watch, fancy)
            time.sleep(watch)
    else:
        print_overview(config, leaderboards, participants, presenter, presenter_id, meetings, watch, fancy)



@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.option('--new', is_flag=True, help="Create a new default config and open it in the default editor")
@click.option('--edit', is_flag=True, help="Open the config in the default editor")
@click.option('--print', 'print_', is_flag=True, help="Print the config to stdout")
@click.option('--path', is_flag=True, help="Print the path to the config")
def config(ctx, new, edit, path, print_):
    """Print, show or edit the config"""
    user_config_path = get_user_config_path()

    if edit:
        if os.path.isfile(user_config_path):
            click.edit(filename=user_config_path)
        else:
            new_config(user_config_path)
    elif path:
        print(get_user_config_path())
    elif print_:
        with open(get_user_config_path(), "r") as f:
            print(f.read())
    elif new:
        if os.path.isfile(user_config_path):
            click.echo("{} There is already a config file at {} !".format(click.style(" WARNING ", bg="bright_red", fg="black", bold=True), user_config_path))
            if click.confirm(click.style('Do you want to edit it with your default editor instead of overwriting it?', fg="yellow")):
                click.edit(filename=user_config_path)
            else:
                if click.confirm(click.style('Do you want to overwrite it with the default config instead?', fg="red"), abort=True):
                    new_config(user_config_path, skip_prompt=True)
        else:
            new_config(user_config_path)
    else:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())



if __name__ == "__main__":
    main()