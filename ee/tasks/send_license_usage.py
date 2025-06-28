import posthoganalytics
import requests
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.utils.timezone import now

from ee.models.license import License
from posthog.clickhouse.client import sync_execute
from posthog.models import User
from posthog.settings import SITE_URL


def send_license_usage():
    return
