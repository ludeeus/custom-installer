"""View for about."""
from componentstore.const import VERSION
from componentstore.server import REASON
import componentstore.resources.html as load


async def view():
    """View for about."""

    installed_version = VERSION
    if not installed_version:
        installed_version = 'dev'

    if REASON == 'versison':
        reason = "You need Home Assistant version 0.86 of newer to use this."
    elif REASON == 'no_path':
        reason = "Defined HA configuration path not found."
    elif REASON == 'ha_not_found':
        reason = "Home Assistant installation not found on the specified path."
    else:
        reason = "An unexpected error occurred."

    content = """
        <div class="row">
            <div class="col s12">
                <div class="card blue-grey darken-1">
                    <div class="card-content white-text">
                        <span class="card-title">Something went wrong</span>
                        <p>
                            {reason}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    """.format(reason=reason)

    html = load.TOP
    html += load.BASE.format(main=content)
    html += load.END

    return html