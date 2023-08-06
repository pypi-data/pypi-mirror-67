from App.config import getConfiguration
from ftw.builder.testing import BUILDER_LAYER
from ftw.builder.testing import functional_session_factory
from ftw.builder.testing import set_builder_session_factory
from ftw.contentstats.logger import setup_logger
from ftw.testbrowser import REQUESTS_BROWSER_FIXTURE
from ftw.testing.layer import COMPONENT_REGISTRY_ISOLATION
from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from StringIO import StringIO
from zope.configuration import xmlconfig
import os
import pytz
import shutil
import tempfile
import ZConfig


IS_PLONE_5_OR_GREATER = get_distribution('Plone').version >= '5'


try:
    get_distribution('ftw.monitor')
    FTW_MONITOR_INSTALLED = True
except DistributionNotFound:
    FTW_MONITOR_INSTALLED = False


def get_log_path():
    """Get filesystem path to ftw.contentstats' logfile.
    """
    logger = setup_logger()
    log_path = logger.handlers[0].stream.name
    return log_path


class PatchedLogTZ(object):
    """Context manager that patches LOG_TZ to a given timezone.
    """

    def __init__(self, tzname):
        self.new_tz = pytz.timezone(tzname)

    def __enter__(self):
        from ftw.contentstats import logger
        self._original_log_tz = logger.LOG_TZ
        logger.LOG_TZ = self.new_tz
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        from ftw.contentstats import logger
        logger.LOG_TZ = self._original_log_tz


class ContentStatsLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, BUILDER_LAYER)

    def setUp(self):
        # Keep track of temporary files we create
        self.tempdir = None
        super(ContentStatsLayer, self).setUp()

    def tearDown(self):
        super(ContentStatsLayer, self).tearDown()

        # Clean up all temporary files we created
        shutil.rmtree(self.tempdir)

    def mktemp(self):
        """Create a temporary file to use as the path for the eventlog.
        We don't actually care about the contents of this file, we just need
        it to get a valid writable path to pass to the eventlog config, so
        ftw.contentstats can derive its own logfile path from it.

        We create this in a known tempdir so we can also clean up the
        contentstats.json file at layer teardown.
        """
        self.tempdir = tempfile.mkdtemp()
        f = open(os.path.join(self.tempdir, 'instance0.log'), 'w')
        f.close()
        return f.name

    def setup_eventlog(self):
        """Create an eventlog ZConfig configuration and patch it onto the
        global config, so it's present when ftw.contentstats attempts to read
        it to derive its own logfile path from the eventlog's logfile path.
        """
        schema = ZConfig.loadSchemaFile(StringIO("""
            <schema>
              <import package='ZConfig.components.logger'/>
              <section type='eventlog' name='*' attribute='eventlog'/>
            </schema>
        """))

        fn = self.mktemp()
        eventlog_conf, handler = ZConfig.loadConfigFile(schema, StringIO("""
            <eventlog>
              <logfile>
                path %s
                level debug
              </logfile>
            </eventlog>
        """ % fn))

        assert eventlog_conf.eventlog is not None
        getConfiguration().eventlog = eventlog_conf.eventlog

    def remove_eventlog(self):
        conf = getConfiguration()
        del conf.eventlog

    def setUpZope(self, app, configurationContext):
        # Set up the eventlog config before setup_logger is called
        self.setup_eventlog()

        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="z3c.autoinclude" file="meta.zcml" />'
            '  <includePlugins package="plone" />'
            '  <includePluginsOverrides package="plone" />'
            '</configure>',
            context=configurationContext)

        z2.installProduct(app, 'ftw.contentstats')

        if not IS_PLONE_5_OR_GREATER:
            # The tests will fail with a
            # `ValueError: Index of type DateRecurringIndex not found` unless
            # the product 'Products.DateRecurringIndex' is installed.
            z2.installProduct(app, 'Products.DateRecurringIndex')

    def tearDownZope(self, app):
        self.remove_eventlog()

    def testTearDown(self):
        # Isolation: truncate ftw.contentstats' logfile after each test
        with open(get_log_path(), 'w') as f:
            f.truncate()

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ftw.contentstats:default')
        if IS_PLONE_5_OR_GREATER:
            applyProfile(portal, 'plone.app.contenttypes:default')


CONTENTSTATS_FIXTURE = ContentStatsLayer()

CONTENTSTATS_FUNCTIONAL = FunctionalTesting(
    bases=(CONTENTSTATS_FIXTURE,
           COMPONENT_REGISTRY_ISOLATION,
           set_builder_session_factory(functional_session_factory)),
    name="ftw.contentstats:functional")

CONTENTSTATS_FUNCTIONAL_ZSERVER = FunctionalTesting(
    bases=(z2.ZSERVER_FIXTURE,
           REQUESTS_BROWSER_FIXTURE,
           CONTENTSTATS_FIXTURE,
           COMPONENT_REGISTRY_ISOLATION,
           set_builder_session_factory(functional_session_factory)),
    name="ftw.contentstats:functional:zserver")
