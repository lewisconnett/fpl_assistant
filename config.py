# ==============================
# FPL API Endpoints
# ==============================
FPL_BASE_URL = 'https://fantasy.premierleague.com/api/'
BOOTSTRAP_STATIC = f'{FPL_BASE_URL}bootstrap-static/'
ELEMENT_SUMMARY = f'{FPL_BASE_URL}element-summary/{{player_id}}/'
TEAM_INFO = f'{FPL_BASE_URL}entry/{{team_id}}/'
SQUAD_PICKS = f'{FPL_BASE_URL}entry/{{team_id}}/event/{{gw}}/picks/'

# ==============================
# Captaincy Algorithm Weightings
# ==============================
CAPTAINCY_WEIGHTS = {
    'form': 0.40,          # How much recent form contributes to captain score
    'fixture': 0.30,       # How much next fixture difficulty contributes
    'availability': 0.15,  # Player fitness / minutes contribution
    'position': 0.15       # Positional multiplier contribution
}

POSITION_MULTIPLIERS = {
    '1': 0.6,
    '2': 0.8,
    '3': 1.0,
    '4': 1.4
}
POSITION_SCALE = 5  # Scaling factor to bring position score to comparable magnitude

# ==============================
# Purple Patch / Form Constants
# ==============================
PURPLE_PATCH_THRESHOLD = 1.3  # Threshold for recent form vs season average
PURPLE_PATCH_BONUS = 1.5      # Bonus multiplier if player is on purple patch
FORM_SCORE_SCALE = 1.5        # Scaling for form score normalization
FORM_RECENT_MATCHES = 3       # Number of recent matches to consider for form

# ==============================
# Player Positions & Availability
# ==============================
POSITIONS = {
    1: "GK",
    2: "DEF",
    3: "MID",
    4: "FWD"
}

AVAILABILITY_STATUSES = {
    "a": "Available",
    "d": "Doubtful",
    "i": "Injured",
    "s": "Suspended",
    "u": "Unavailable"
}

AVAILABILITY_MULTIPLIERS = {
    'a': 1.0,
    'd': 0.5,
    'i': 0.0,
    's': 0.0,
    'u': 0.0
}

AVAILABILITY_WEIGHTINGS = {
    'start_rate': 0.4,   # Weight for % of matches started
    'full_games': 0.3,   # Weight for % of matches played full 85+ minutes
    'minutes': 0.3       # Weight for average minutes played
}
RECENT_MATCHES_FOR_AVAILABILITY = 5
FULL_GAME_THRESHOLD = 85

# ==============================
# Captain Rating & Triple Captain Rules
# ==============================
CAPTAIN_RATING_THRESHOLDS = {
    8.5: "Platinum",
    7.5: "Gold",
    6.0: "Silver",
    4.0: "Bronze",
    0.0: "Avoid"
}

TRIPLE_CAPTAIN_RULES = [
    {"min_score": 8.5, "positions": ["FWD", "MID"], "recommendation": "Strong"},
    {"min_score": 7.0, "positions": ["FWD"], "recommendation": "Consider"},
]
DEFAULT_TRIPLE_CAPTAIN_RECOMMENDATION = 'Avoid'

# ==============================
# Fixture Difficulty
# ==============================
FIXTURE_DIFFICULTY_SCALING = 2          # Scale for fixture difficulty contribution
FPL_FIXTURE_DIFFICULTY_SCALE = 5        # FPL rates matches out of 5


# ==============================
# Fuzzy Search
# ==============================
FUZZY_MATCH_MIN_SCORE = 85.0
