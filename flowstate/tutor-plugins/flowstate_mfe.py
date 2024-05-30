from tutor import hooks

hooks.Filters.ENV_PATCHES.add_items(
    [
        (
            "mfe-lms-development-settings",
            """
    MFE_CONFIG["LOGO_URL"] = "<URL>/logo.svg"
    MFE_CONFIG["LOGO_TRADEMARK_URL"] = "<URL>/logo-trademark.svg"
    MFE_CONFIG["LOGO_WHITE_URL"] = "<URL>/logo-white.svg"
    MFE_CONFIG["FAVICON_URL"] = "<URL>/favicon.ico"
    """
        ),
        (
            "mfe-lms-production-settings",
            """
    MFE_CONFIG["LOGO_URL"] = "<URL>/logo.svg"
    MFE_CONFIG["LOGO_TRADEMARK_URL"] = "<URL>/logo-trademark.svg"
    MFE_CONFIG["LOGO_WHITE_URL"] = "<URL>/logo-white.svg"
    MFE_CONFIG["FAVICON_URL"] = "<URL>/favicon.ico"
    """
        ),
    ]
)