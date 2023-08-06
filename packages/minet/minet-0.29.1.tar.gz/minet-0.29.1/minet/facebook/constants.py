# =============================================================================
# Minet Facebook Constants
# =============================================================================
#
# General constants used throughout the Facebook namespace.
#
from collections import OrderedDict


FACEBOOK_URL = 'https://www.facebook.com'
FACEBOOK_MOBILE_URL = 'https://m.facebook.com'

FACEBOOK_MOBILE_DEFAULT_THROTTLE = 0.5
FACEBOOK_WEB_DEFAULT_THROTTLE = 20.0

FACEBOOK_COMMENT_CSV_HEADERS = [
    'post_id',
    'comment_id',
    'user_id',
    'user_handle',
    'user_url',
    'user_label',
    'comment_text',
    'comment_html',
    'formatted_date',
    'date',
    'reactions',
    'replies',
    'in_reply_to'
]

FACEBOOK_POST_STATS_CSV_HEADERS = [
    'error',
    'canonical',
    'account_name',
    'timestamp',
    'time',
    'link',
    'aria_label',
    'text',
    'share_count',
    'comment_count',
    'reaction_count',
    'video_view_count'
]

FACEBOOK_REACTION_KEYS = OrderedDict({
    1: 'like',
    2: 'love',
    3: 'wow',
    4: 'haha',
    7: 'sad',
    8: 'angry',
    11: 'thankful',
    12: 'pride'
})
