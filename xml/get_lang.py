import xbmcgui, xbmcaddon

languages = ("CS", "SK", "EN")
new_dub_url = {"CS":
                    {
                        "CS":"DYQwdg5gvAxgzgMlJWi4HsBOAXKATEbAUwEE88i8FsBPAByKgFt0A3ASyISws3yLgwEBGnCgBmAGwBWIA",
                        "EN":"DYQwdg5gvAxgzgMlJKBTMC4HsBOAXKAExD1QEFDDVCE8BPAB1SgFssA3AS1QVypyKo4MBMTpwoAZgBsAViA",
                        "SK":"DYQwdg5gvAxgzgMlJKcDWC4HsBOAXKAExDwFMBBQw0whPATwAdSoBbLANwEtSFdqcRUnBgJi9OFADMANgCsQA"
                    },
               "EN":
                    {
                        "CS":"DYQwdg5gvApmBkpJQMYGd5oPYCcAuUAJiHjAIKGEyHx4CeADjFALZYBuAljPLlTkRhoU8YnTRQAzADYArEA",
                        "EN":"DYQwdg5gvApmBkpKwQZwPYCcAuUAmI2MAgnnjHvNgJ4AOMUAtugG4CWM8W5m%2bMqAY3gFqqKAGYAbAFYgA",
                        "SK":"DYQwdg5gvApmBkpJQM4Gt4oPYCcAuUAJiHjAIKGEyHx4CeADjFALZYBuAljPLlTkRgoAxvGJ0UUAMwA2AKxA"
                    },
               "SK":
                    {
                        "CS":"DYQwdg5gvAzg1gMlJKBjGCYHsBOAXKAExDwFMBBQw0whPATwAdSoBbLANwEtSFdqcRUjFQJi9GFADMANgCsQA",
                        "EN":"DYQwdg5gvAzg1gMlJKBTMCYHsBOAXKAExD1QEFDDVCE8BPAB1SgFssA3AS1QVypyKoYAYwTE6MKAGYAbAFYgA",
                        "SK":"DYQwdg5gvAzg1gMlJWiYHsBOAXKATEbAUwEE88i8FsBPAByKgFt0A3ASyISws3yJgBjBARowoAZgBsAViA"
                    }
              }
        
addon = xbmcaddon.Addon("plugin.video.stream-cinema-2-release")

preferred_language = int(addon.getSetting("preferred_language"))
fallback_language = int(addon.getSetting("fallback_language"))

if fallback_language == 0:
    fallback_language = preferred_language
else:
    fallback_language = fallback_language - 1

preferred_language = languages[preferred_language]
fallback_language = languages[fallback_language]    

xbmcgui.Window(10000).setProperty("SCC_new_dub_movies", "plugin://plugin.video.stream-cinema-2-release/get_media/?media_type=movie&amp;render_type=default&amp;url=%2fapi%2fmedia%2ffilter%2fnewsDubbed%3fquery%3d" + new_dub_url[preferred_language][fallback_language])
xbmcgui.Window(10000).setProperty("SCC_fallback_language", "plugin://plugin.video.stream-cinema-2-release/get_media/?media_type=tvshow&amp;render_type=default&amp;url=%2fapi%2fmedia%2ffilter%2fnewsDubbed%3fquery%3d" + new_dub_url[preferred_language][fallback_language])

