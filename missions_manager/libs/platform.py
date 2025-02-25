import platform


def get_platform() -> tuple[str, str]:
    return platform.system(), platform.release()
