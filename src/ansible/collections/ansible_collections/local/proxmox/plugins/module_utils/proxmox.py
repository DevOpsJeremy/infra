from ansible.module_utils.basic import env_fallback


def proxmox_auth_argument_spec():
    return dict(
        api_host=dict(
            type="str", required=True, fallback=(env_fallback, ["PROXMOX_HOST"])
        ),
        api_port=dict(type="int", fallback=(env_fallback, ["PROXMOX_PORT"])),
        api_user=dict(
            type="str", required=True, fallback=(env_fallback, ["PROXMOX_USER"])
        ),
        api_password=dict(
            type="str", no_log=True, fallback=(env_fallback, ["PROXMOX_PASSWORD"])
        ),
        api_token_id=dict(
            type="str", no_log=False, fallback=(env_fallback, ["PROXMOX_TOKEN_ID"])
        ),
        api_token_secret=dict(
            type="str", no_log=True, fallback=(env_fallback, ["PROXMOX_TOKEN_SECRET"])
        ),
        validate_certs=dict(
            type="bool",
            default=False,
            fallback=(env_fallback, ["PROXMOX_VALIDATE_CERTS"]),
        ),
    )
