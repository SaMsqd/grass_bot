MIN_PROXY_SCORE = 50

CLAIM_REWARDS_ONLY = False  # claim tiers rewards only (https://app.getgrass.io/dashboard/referral-program)

THREADS = 6  # for register account / claim rewards mode only

CHECK_POINTS = True  # show point for each account every nearly 10 minutes

STOP_ACCOUNTS_WHEN_SITE_IS_DOWN = True  # stop account for 20 minutes, to reduce proxy traffic usage

SHOW_LOGS_RARELY = False


# REGISTER PARAMETRS ONLY
REGISTER_ACCOUNT_ONLY = False
REGISTER_DELAY = (1, 3)

TWO_CAPTCHA_API_KEY = ""
ANTICAPTCHA_API_KEY = ""
CAPMONSTER_API_KEY = "677ed2a1ee8febdc34fb000a42d2309a"
CAPSOLVER_API_KEY = ""
CAPTCHAAI_API_KEY = ""

# Captcha params, left empty
CAPTCHA_PARAMS = {
    "captcha_type": "v2",
    "invisible_captcha": False,
    "sitekey": "6LdyCj0pAAAAAFvvSTRHYOzddUPMPcH232u7a9e0",
    "captcha_url": "https://app.getgrass.io/register"
}

########################################

ACCOUNTS_FILE_PATH = "data/accounts.txt"
PROXIES_FILE_PATH = "data/proxies.txt"

REF_CODE = 'HDPKrp21BhP-btP'
