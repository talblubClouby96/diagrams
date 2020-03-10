# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _OnPrem


class _Security(_OnPrem):
    _type = "security"
    _icon_dir = "resources/onprem/security"


class Trivy(_Security):
    _icon = "trivy.png"


class Vault(_Security):
    _icon = "vault.png"


# Aliases
