import xbmcgui, xbmcaddon

languages = ("CS", "SK", "EN")

# new_dub_url = {"CS":
#                     {
#                         "CS":"DYQwdg5gvAxgzgMlJWi4HsBOAXKyIAiI2ApgIIAmFJFC2AngA4lQC26AbgJYkJbWYo1ODAQUQ9OFADMANgCsQA",
#                         "EN":"DYQwdg5gvAxgzgMlJKBTMC4HsBOAXKZCAERD1QEEATK1KhPATwAdUoBbLANwEtUFctHFFpwYCKiEZwoAZgBsAViA",
#                         "SK":"DYQwdg5gvAxgzgMlJKcDWC4HsBOAXKZCAERDwFMBBAE2vOoTwE8AHcqAWywDcBLchLjo4odODATUQTOFADMANgCsQA"

#                     },
#                "EN":
#                     {
#                         "CS":"DYQwdg5gvApmBkpJQMYGd5oPYCcAuUSEAIiHjAIIAmVMV8eAngA4xQC2WAbgJYzy5aOKLTQp4VEIzRQAzADYArEA",
#                         "EN":"DYQwdg5gvApmBkpKwQZwPYCcAuUkQBERsYBBAE3JnPmwE8AHGKAW3QDcBLGeLKzKFVQBjeORB1UUAMwA2AKxA",
#                         "SK":"DYQwdg5gvApmBkpJQM4Gt4oPYCcAuUSEAIiHjAIIAmVMV8eAngA4xQC2WAbgJYzy5aOKLRQBjeFRCMUUAMwA2AKxA"
#                     },
#                "SK":
#                     {
#                         "CS":"DYQwdg5gvAzg1gMlJKBjGCYHsBOAXKZCAERDwFMBBAE2vOoTwE8AHcqAWywDcBLchLjo4odGKgTUQTGFADMANgCsQA",
#                         "EN":"DYQwdg5gvAzg1gMlJKBTMCYHsBOAXKZCAERD1QEEATK1KhPATwAdUoBbLANwEtUFctHFFowAxgiohGMKAGYAbAFYgA",
#                         "SK":"DYQwdg5gvAzg1gMlJWiYHsBOAXKyIAiI2ApgIIAmFJFC2AngA4lQC26AbgJYkJbWYo1GAGMEFEPRhQAzADYArEA"
#                     }
#               }


addon = xbmcaddon.Addon("plugin.video.stream-cinema-2-release")

preferred_language = int(addon.getSetting("preferred_language"))
fallback_language = int(addon.getSetting("fallback_language"))

if fallback_language == 0:
    fallback_language = preferred_language
else:
    fallback_language = fallback_language - 1

preferred_language = languages[preferred_language]
fallback_language = languages[fallback_language]    

# xbmcgui.Window(10000).setProperty("SCC_new_dub_movies", "plugin://plugin.video.stream-cinema-2-release/get_media/?media_type=movie&amp;render_type=default&amp;url=%2fapi%2fmedia%2ffilter%2fnewsDubbed%3fquery%3d" + new_dub_url[preferred_language][fallback_language])
# xbmcgui.Window(10000).setProperty("SCC_new_dub_tvshows", "plugin://plugin.video.stream-cinema-2-release/get_media/?media_type=tvshow&amp;render_type=default&amp;url=%2fapi%2fmedia%2ffilter%2fnewsDubbed%3fquery%3d" + new_dub_url[preferred_language][fallback_language])
xbmcgui.Window(10000).setProperty("SCC_preferred_language", preferred_language)
xbmcgui.Window(10000).setProperty("SCC_fallback_language", fallback_language)

