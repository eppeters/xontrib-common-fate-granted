from xonsh.built_ins import XonshSession


def _load_xontrib_(xsh: XonshSession, **_):
    # getting environment variable
    var = xsh.env.get("VAR", "default")

    print("Autoloading xontrib: xontrib-common-fate-granted")

    
    
    from .aliases import git_log
    xsh.aliases["gl"] = git_log
    
