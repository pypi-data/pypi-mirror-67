kind: manual

depends:
- base.bst

sources:
- kind: git
  url: https://gitlab.com/cs-shadow/dotfiles
  ref: 6a588e8dec143d4b2f8a191d98a80c222b535097

config:
  build-commands: [exit 1]
