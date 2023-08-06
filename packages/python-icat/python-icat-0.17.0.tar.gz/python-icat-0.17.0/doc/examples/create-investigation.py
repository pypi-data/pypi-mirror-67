#! /usr/bin/python
#
# Create some sample investigations.
#
# This script should be run by the ICAT user useroffice.
#

from __future__ import print_function
import icat
import icat.config
import sys
import logging
import yaml

logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)

config = icat.config.Config()
config.add_variable('datafile', ("datafile",), 
                    dict(metavar="inputdata.yaml", 
                         help="name of the input datafile"))
config.add_variable('investigationname', ("investigationname",), 
                    dict(help="name of the investigation to add"))
client, conf = config.getconfig()
client.login(conf.auth, conf.credentials)


# ------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------

def initobj(obj, attrs):
    """Initialize an entity object from a dict of attributes."""
    for a in obj.InstAttr:
        if a != 'id' and a in attrs:
            setattr(obj, a, attrs[a])

def getUser(client, attrs):
    """Get the user, create it as needed.
    """
    try:
        return client.assertedSearch("User [name='%s']" % attrs['name'])[0]
    except icat.SearchResultError:
        user = client.new("user")
        initobj(user, attrs)
        user.create()
        return user

# ------------------------------------------------------------
# Read input data
# ------------------------------------------------------------

if conf.datafile == "-":
    f = sys.stdin
else:
    f = open(conf.datafile, 'r')
data = yaml.load(f)
f.close()

try:
    investigationdata = data['investigations'][conf.investigationname]
except KeyError:
    raise RuntimeError("unknown investigation '%s'" % conf.investigationname)


# ------------------------------------------------------------
# Get some objects from ICAT we need later on
# ------------------------------------------------------------

facilityname = data['facilities'][investigationdata['facility']]['name']
facility = client.assertedSearch("Facility[name='%s']" % facilityname)[0]
facility_const = "AND facility.id=%d" % facility.id

instrumentname = data['instruments'][investigationdata['instrument']]['name']
instrsearch = "Instrument[name='%s' %s]" % (instrumentname, facility_const)
instrument = client.assertedSearch(instrsearch)[0]

typename = data['investigation_types'][investigationdata['type']]['name']
typesearch = "InvestigationType[name='%s' %s]" % (typename, facility_const)
investigation_type = client.assertedSearch(typesearch)[0]


# ------------------------------------------------------------
# Create the investigation
# ------------------------------------------------------------

try:
    invsearch = "Investigation[name='%s']" % investigationdata['name']
    client.assertedSearch(invsearch, assertmax=None)
except icat.exception.SearchResultError:
    pass
else:
    raise RuntimeError("Investigation: '%s' already exists ..." 
                       % investigationdata['name'])

print("Investigation: creating '%s' ..." % investigationdata['name'])
investigation = client.new("investigation")
initobj(investigation, investigationdata)
investigation.facility = facility
investigation.type = investigation_type
if 'parameters' in investigationdata:
    for pdata in investigationdata['parameters']:
        ip = client.new('investigationParameter')
        initobj(ip, pdata)
        ptdata = data['parameter_types'][pdata['type']]
        query = ("ParameterType [name='%s' AND units='%s']"
                 % (ptdata['name'], ptdata['units']))
        ip.type = client.assertedSearch(query)[0]
        investigation.parameters.append(ip)
if 'shifts' in investigationdata:
    for sdata in investigationdata['shifts']:
        s = client.new('shift')
        initobj(s, sdata)
        if 'instrument' in s.InstRel:
            s.instrument = instrument
        investigation.shifts.append(s)
investigation.create()
investigation.addInstrument(instrument)
investigation.addKeywords(investigationdata['keywords'])


# ------------------------------------------------------------
# Add users and setup access groups
# ------------------------------------------------------------

investigationowner = []
investigationreader = []
investigationwriter = []

# Principal Investigator
user = data['users'][investigationdata['invpi']]
userpi = getUser(client, user)
investigation.addInvestigationUsers([userpi], role="Principal Investigator")
investigationowner.append(userpi)
investigationwriter.append(userpi)

# Additional Investigators
usercols = []
for u in investigationdata['invcol']:
    user = data['users'][u]
    usercols.append(getUser(client, user))
investigation.addInvestigationUsers(usercols)
investigationwriter.extend(usercols)

# More users that will get read permissions
for u in investigationdata['invguest']:
    user = data['users'][u]
    userguest = getUser(client, user)
    investigationreader.append(userguest)

owngroupname = "investigation_%s_owner" % investigation.name
writegroupname = "investigation_%s_writer" % investigation.name
readgroupname = "investigation_%s_reader" % investigation.name
owngroup = client.createGroup(owngroupname, investigationowner)
writegroup = client.createGroup(writegroupname, investigationwriter)
readgroup = client.createGroup(readgroupname, investigationreader)

# ------------------------------------------------------------
# Setup InvestigationGroups or permissions
# ------------------------------------------------------------

# InvestigationGroup have been introduced with ICAT 4.4.  If
# available, just create them.  Then we don't need to setup
# permissions, as the static rules created in init-icat.py apply.  For
# older versions of ICAT, we need to setup per investigation rules.

if client.apiversion > '4.3.99':

    investigation.addInvestigationGroup(owngroup, role="owner")
    investigation.addInvestigationGroup(writegroup, role="writer")
    investigation.addInvestigationGroup(readgroup, role="reader")

else:

    invcond = "Investigation[name='%s']" % investigation.name

    # Items that are considered to belong to the content of an
    # investigation, where %s represents the investigation itself.
    # The writer group will get CRUD permissions and the reader group
    # R permissions on these items.
    invwitems = [ "Sample <-> %s",
                  "Dataset <-> %s",
                  "Datafile <-> Dataset <-> %s",
                  "InvestigationParameter <-> %s",
                  "SampleParameter <-> Sample <-> %s",
                  "DatasetParameter <-> Dataset <-> %s",
                  "DatafileParameter <-> Datafile <-> Dataset <-> %s", ]

    # Items that we allow read only access for both readers and
    # writers, in particular the investigation itself.
    invritems = [ "%s",
                  "Shift <-> %s",
                  "Keyword <-> %s",
                  "Publication <-> %s", ]

    # set permissions for the writer group
    client.createRules("R", [ s % invcond for s in invritems ], writegroup)
    client.createRules("CRUD", [ s % invcond for s in invwitems ], writegroup)

    # set permissions for the reader group
    client.createRules("R", [ s % invcond for s in invritems ], readgroup)
    client.createRules("R", [ s % invcond for s in invwitems ], readgroup)

    # set owners permissions
    items = [ "UserGroup <-> Grouping[name='%s']" % (s) 
              for s in [ writegroupname, readgroupname ] ]
    client.createRules("CRUD", items, owngroup)
    items = [ "Grouping[name='%s']" % (s) 
              for s in [ writegroupname, readgroupname ] ]
    client.createRules("R", items, owngroup)

