"""
A minimal startscript for the server. This can be used
as a quickstart module.
"""
import datetime
import logging
import os
import re
from logging.config import dictConfig  # pylint: disable=import-outside-toplevel

from importlib.resources import open_text
from typing import Optional
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, redirect, url_for, Response, request, Request, session
import yaml
from libgravatar import Gravatar
from markdown import markdown

from digicubes_common.exceptions import DigiCubeError
from digicubes_client.client.proxy import RightProxy, RoleProxy
from digicubes_flask import account_manager as accm, current_user
from digicubes_flask.email import MailCube
from digicubes_flask.web.modules import (
    account_blueprint,
    admin_blueprint,
    headmaster_blueprint,
    teacher_blueprint,
    student_blueprint,
)

from .account_manager import DigicubesAccountManager

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

digicubes: DigicubesAccountManager = accm

mail_cube = MailCube()
the_account_manager = DigicubesAccountManager()


def create_app():
    """
    Factory function to create the flask server.
    Flask will automatically detect the method
    on `flask run`.
    """

    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # TODO: Set via configuration

    @app.errorhandler(DigiCubeError)
    def handle_digicube_error(error):  # pylint: disable=unused-variable
        logger.exception("Error occurred. Going back to login page.")
        digicubes.logout()
        return redirect(url_for("account.login"))

    @app.errorhandler(404)
    def page_not_found(error):
        return redirect(url_for("account.login"))

    @app.template_filter()
    def gravatar(email: str) -> str:

        default = url_for("static", filename="image/digibot_profile_40.png", _external=True)
        if not email:
            return default

        gravatar: Gravatar = Gravatar(email)
        return gravatar.get_image(size=40, default="retro")

    @app.template_filter()
    def digidate(dtstr):  # pylint: disable=unused-variable
        if dtstr is None:
            return ""

        if isinstance(dtstr, (datetime.date, datetime.datetime)):
            date = datetime.datetime.fromisoformat(str(dtstr))
            return date.strftime("%d.%m.%Y")

        if isinstance(dtstr, str):
            date = datetime.datetime.fromisoformat(str(dtstr))
            return date.strftime("%d.%m.%Y")

        raise ValueError(f"Cannot convert given value. Unsupported type {type(dtstr)}")

    @app.template_filter()
    def md(txt: str) -> str:  # pylint: disable=unused-variable
        return markdown(txt)

    @app.template_filter()
    def digitime(dtstr):  # pylint: disable=unused-variable
        if dtstr is None:
            return ""

        if isinstance(dtstr, str):
            date = datetime.datetime.fromisoformat(str(dtstr))
            return date.strftime("%H:%M")

        if isinstance(dtstr, (datetime.date, datetime.datetime)):
            return date.strftime("%H:%M")

        raise ValueError(f"Cannot convert given value. Unsupported type {type(dtstr)}")

    @app.template_filter()
    def nonefilter(value):  # pylint: disable=unused-variable
        return value if value is not None else "-"

    @app.before_request
    def check_token():  # pylint: disable=unused-variable
        """
        Vor jedem Request das Token aktualisieren, damit das Zeitfenster
        der Gültigkeit des Tokens neu beginnt.

        Das wird somit eigentlich viel zu oft gemacht und frisst unnötig
        Ressourccen, ist aber der einfachste weg. Alternativ müsste der
        Client umgebaut werden, da der server bereits in jedem Response ein
        neues Token sendet. Villeicht kann man da noch mit Werkzeug locals
        arbeiten, so dass das neue token auch ermittelt werden kann, ohne
        die Methodensignatur ändern zu müssen.
        """
        if accm is not None:
            if accm.token is None:
                logger.debug("No user logged in. No new token will be generated.")
            else:
                # TODO: Den call könnte man asynchron machen, weil die
                # Aktuslisierung des Tokens für den aktuellen Request
                # nicht wichtig ist und der zusätzliche Call einen
                # minimalen Performance Verlust bedeutet.
                logger.debug("Refreshing token in 'at the end oth the request.")
                accm.refresh_token()
                # TODO: Hier sollte eigentlich der Fall abgefangen werden, dass das
                # alte Token abgelaufen ist.

                # TODO: ebenso könnte der UserProxy des eingeloggten users, sowie
                # seine Rechte geladen werden, um sie im g Objekt abzulegen. Allerdings
                # wäre das teuer, dies in jedem Request zu machen. Wir brauchen also
                # einen intelligenten cache für diese daten.
        else:
            logger.info("No account manager in app scope found. Maybe not an issue.")

    def parse_config(data=None, tag="!ENV"):
        """
        Add a new token to the yaml parser. If we have an !ENV ${xyz} string in the yaml file,
        xyz will be replaced by the corresonding environment variable if availabe or by the string
        xyz else.
        """
        pattern = re.compile(".*?\${(\w+)}.*?")  # pylint: disable=anomalous-backslash-in-string
        loader = yaml.SafeLoader
        loader.add_implicit_resolver(tag, pattern, None)

        def constructor_env_variables(loader, node):
            """
            Extracts the environment variable from the node's value
            :param yaml.Loader loader: the yaml loader
            :param node: the current node in the yaml
            :return: the parsed string that contains the value of the environment
            variable
            """
            value = loader.construct_scalar(node)
            match = pattern.findall(value)  # to find all env variables in line
            if match:
                full_value = value
                for g in match:
                    full_value = full_value.replace(f"${{{g}}}", os.environ.get(g, g))
                return full_value
            return value

        loader.add_constructor(tag, constructor_env_variables)
        return yaml.load(data, Loader=loader)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # C O N F I G U R A T I O N
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # First, load the .env file, wich adds environment variables to the
    # the program. Together with the pyaml parser extension these variables
    # can be used in the yaml configuration
    load_dotenv(verbose=False)

    # Load the default settings and then load the custom settings
    # The default settings are stored in this package and have to be loaded
    # as a ressource.
    with open_text("digicubes_flask.cfg", "default_configuration.yaml") as f:
        settings = parse_config(f)
        app.config.update(settings)

    # Loading the logging configuration. If no logging configuration
    # is found, it will fall back to logging.basicConfiguration
    logging.basicConfig(level=logging.DEBUG)
    """
    try:
        with open_text("digicubes_flask.cfg", "logging.yaml") as f:
            settings = yaml.safe_load(f)
            try:
                dictConfig(settings)
                logger.info("Configured logging")
            except ValueError:
                logging.basicConfig(level=logging.DEBUG)
                logger.fatal("Could not configure logging.", exc_info=True)
    except:
    """

    # Initalizes the account manager extension, wich is responsible for the the
    # login and logout procedure.
    the_account_manager.init_app(app)

    mail_cube.init_app(app)

    # ---------------------------
    # Now register the blueprints
    # ---------------------------

    # Account blueprint
    url_prefix = "/account"
    logger.debug("Register account blueprint at %s", url_prefix)
    app.register_blueprint(account_blueprint, url_prefix=url_prefix)

    # Admin blueprint
    url_prefix = "/dcad"
    logger.debug("Register admin blueprint at %s", url_prefix)
    app.register_blueprint(admin_blueprint, url_prefix=url_prefix)

    # Headmaster blueprint
    url_prefix = "/dchm"
    logger.debug("Register headmaster blueprint at %s", url_prefix)
    app.register_blueprint(headmaster_blueprint, url_prefix=url_prefix)

    # Teacher blueprint
    url_prefix = "/dcte"
    logger.debug("Register teacher blueprint at %s", url_prefix)
    app.register_blueprint(teacher_blueprint, url_prefix=url_prefix)

    url_prefix = "/dcst"
    logger.debug("Register student blueprint at %s", url_prefix)
    app.register_blueprint(student_blueprint, url_prefix=url_prefix)

    logger.info("Static folder is %s", app.static_folder)
    return app
