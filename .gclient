solutions = [
  {
    "name"        : "src",
    "url"         : "https://chromium.googlesource.com/chromium/src.git",
    "deps_file"   : "DEPS",
    "managed"     : False,
    "custom_deps" : {},
    "custom_vars" : {},
    "custom_hooks": [{
      "name": "setup_gn",
      "pattern": ".",
      "action": [
        "python3",
        "src/ios/build/tools/setup-gn.py",
      ]
    }],
    "safesync_url": "",
  },
]
target_os = ["ios"]
target_os_only = True
