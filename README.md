# harbour-ambience-template

A reworking of the ambience template originally provided by Jolla for
SailfishOS. The original was distributed in the Other Half Development Kit
(http://jolla.com/the-other-half-developer-kit), but doesn't build out of the
box and is a little unclear. This repository contains that code, cleaned up
and buildable. History of the transformation from that to this are included in
this git repository.

## Requirements

- The SailfishOS SDK Alpha 14.04 or later (https://sailfishos.org/develop.html)
- A SailfishOS device to install to

## Usage

First, git clone the repo. Launch the SDK, open the .pro file and configure the
project. The project should build out-of-the-box but that will leave you with 
an RPM named harbour-ambience-template-0.1.0-0.1.noarch.rpm, empty sounds and 
an ugly wallpaper. The personalisation steps involve:
- Changing harbour-ambience-template to harbour-ambience-yourcoolambiencename everywhere
- Adding your own wallpaper
- Adding and/or configuring your own sounds
- Correcting the RPM .spec file for your name, email address, description etc.

## Notes

- See the original README.Jolla for specifics on ambience behaviour
- Tested against the SDK, needs testing on OBS/Chum
- The translation skeleton is there but is completely untested
- I chose to rename the package/files generated to harbour-ambience-template as
they were initially confusing, to be broadly in line with harbour submission
guidelines and to try to impose a little structure as currently there is none. You can in principle name them anything.

## Ambiences and the Harbour

Currently the feasibility of accepting Ambiences to the Harbour and the Store
is under investigation by Jolla. Hopefully that investigation will have a
positive outcome but for the time being, ambiences based upon this template 
fail Harbour Validation with the following technical issues:

- Requires: ambienced is forbidden
- %post scripts are forbidden
- Packages that do not contain an ELF executable are forbidden

The first is trivial (if ugly) to remedy, the second is required for a good
user experience (i.e not requiring the user to reboot their device) but the
last is a blocker.
