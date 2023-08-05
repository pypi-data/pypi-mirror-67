import getpass
import os
import dill
from dotenv import load_dotenv
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
from neo.libs import utils

GLOBAL_HOME = os.path.expanduser("~")
GLOBAL_AUTH_URL = "https://keystone.wjv-1.neo.id:443/v3"
GLOBAL_USER_DOMAIN_NAME = "neo.id"
GLOBAL_REGION = {
    "wjv": "https://keystone.wjv-1.neo.id:443/v3",
    "jkt": "https://keystone.jkt-1.neo.id:443/v3",
}
DEFAULT_REGION = "wjv"


def get_username():
    return input("username: ")


def get_password():
    return getpass.getpass("password: ")


def get_region():
    region = input("region (Default: wjv): ")
    try:
        if region == "":
            region = "wjv"
        print(GLOBAL_REGION[region])
        return GLOBAL_REGION[region]
    except KeyError:
        utils.log_err("Region not found, please check your region input")
        exit()


def generate_session(username, password, auth_url, user_domain_name, project_id=None):
    auth = v3.Password(
        username=username,
        password=password,
        project_id=project_id,
        auth_url=auth_url,
        user_domain_name=user_domain_name,
        reauthenticate=True,
        include_catalog=True,
    )
    sess = session.Session(auth=auth)
    dump_session(sess)
    return sess


def check_env():
    return os.path.isfile("{}/.neo.env".format(GLOBAL_HOME))


def create_env_file(username, password, project_id, auth_url, user_domain_name):
    try:
        env_file = open("{}/.neo.env".format(GLOBAL_HOME), "w+")
        env_file.write("OS_USERNAME=%s\n" % username)
        env_file.write("OS_PASSWORD=%s\n" % password)
        env_file.write("OS_AUTH_URL=%s\n" % auth_url)
        env_file.write("OS_PROJECT_ID=%s\n" % project_id)
        env_file.write("OS_USER_DOMAIN_NAME=%s\n" % user_domain_name)
        env_file.close()
        return True
    except Exception as e:
        utils.log_err(e)
        return False


def load_env_file():
    return load_dotenv("{}/.neo.env".format(GLOBAL_HOME), override=True)


def get_env_values():
    if check_env():
        load_env_file()
        neo_env = {}
        neo_env["username"] = os.environ.get("OS_USERNAME")
        neo_env["password"] = os.environ.get("OS_PASSWORD")
        neo_env["auth_url"] = os.environ.get("OS_AUTH_URL")
        neo_env["project_id"] = os.environ.get("OS_PROJECT_ID")
        neo_env["user_domain_name"] = os.environ.get("OS_USER_DOMAIN_NAME")
        return neo_env
    # else:
    #    utils.log_err("Can't find NEO environment configuration. Maybe you haven't login yet?")


def is_current_env(auth_url, user_domain_name, username):
    """ check if auth_url and user_domain_name differ from current .neo.env"""
    envs = get_env_values()
    if (
        envs["auth_url"] == auth_url
        and envs["user_domain_name"] == user_domain_name
        and envs["username"] == username
    ):
        return True
    else:
        return False


def get_project_id(username, password, auth_url, user_domain_name):
    sess = generate_session(
        username=username,
        password=password,
        auth_url=auth_url,
        user_domain_name=user_domain_name,
    )
    keystone = client.Client(session=sess)
    # project_list = [t.id for t in keystone.projects.list(user=sess.get_user_id())]
    enabled_project = []
    for project in keystone.projects.list(user=sess.get_user_id()):
        if project.enabled == True:
            enabled_project.append(project.id)

    if len(enabled_project) > 1:
        utils.log_err("Something wrong with your project. Please contact Support")
        exit()
    else:
        return enabled_project[0]


""" def do_fresh_login(auth_url=GLOBAL_AUTH_URL, user_domain_name=GLOBAL_USER_DOMAIN_NAME):
    try:
        username = get_username()
        password = get_password()
        # use default value for fresh login
        project_id = get_project_id(username, password, auth_url, user_domain_name)
        # generate fresh session
        generate_session(
            auth_url=auth_url,
            username=username,
            password=password,
            project_id=project_id,
            user_domain_name=user_domain_name,
        )
        # generate fresh neo.env
        create_env_file(username, password, project_id, auth_url, user_domain_name)
        utils.log_info("Login Success")
    except Exception as e:
        utils.log_err(e)
        utils.log_err("Login Failed") """


def do_fresh_login(username=None, auth_url=None):
    if username != None:
        username = username
        password = get_password()
        auth_url = auth_url
    else:
        username = get_username()
        password = get_password()
        if auth_url != None:
            auth_url = auth_url
        else:
            auth_url = get_region()

    try:
        project_id = get_project_id(
            username, password, auth_url, GLOBAL_USER_DOMAIN_NAME
        )
        generate_session(
            auth_url=auth_url,
            username=username,
            password=password,
            project_id=project_id,
            user_domain_name=GLOBAL_USER_DOMAIN_NAME,
        )
        # generate fresh neo.env
        create_env_file(
            username, password, project_id, auth_url, GLOBAL_USER_DOMAIN_NAME
        )
        utils.log_info("Login Success")
    except Exception as e:
        utils.log_err(e)
        utils.log_err("Login Failed")


def regenerate_sess():
    """ Regenerate session from old neo.env"""
    env_data = get_env_values()
    generate_session(
        auth_url=env_data["auth_url"],
        username=env_data["username"],
        password=env_data["password"],
        project_id=env_data["project_id"],
        user_domain_name=env_data["user_domain_name"],
    )


""" def do_login(auth_url=GLOBAL_AUTH_URL, user_domain_name=GLOBAL_USER_DOMAIN_NAME, **username):
    try:
        if check_env() and check_session():
            old_env_data = get_env_values()
            if is_current_env(
                auth_url, user_domain_name, username=old_env_data["username"]
            ):
                print("You are already logged.")
                print("  use 'neo login -D' to see your current account")
            else:
                print("Doing fresh login. You switched user account")
                do_fresh_login(auth_url=auth_url, user_domain_name=user_domain_name)
        elif check_env() and not check_session():
            print("Retrieving old login data ...")
            regenerate_sess()
            utils.log_info("Login Success")
        else:
            print("Doing fresh login. You don't have old login data")
            do_fresh_login(auth_url, user_domain_name)
    except Exception as e:
        utils.log_err(e)
        utils.log_err("Login Failed")
        return False """


def login_check(username=None, region=None):
    try:
        print("Connecting to region " + region + " at " + GLOBAL_REGION[region])
        auth_url = GLOBAL_REGION[region]
        old_env_data = get_env_values()
        if check_env() and check_session():
            if is_current_env(
                auth_url, GLOBAL_USER_DOMAIN_NAME, username=old_env_data["username"]
            ):
                print("You have logged in")
                print("You are already logged.")
                print("  use 'neo login -D' to see your current account")
            else:
                print("You have switch user or region, doing relogin")
                do_fresh_login(username, auth_url)
        elif check_env() and not check_session():
            print("Retrieving old login data ...")
            regenerate_sess()
            utils.log_info("Login Success")
        else:
            do_fresh_login(username, auth_url)
    except KeyError as e:
        utils.log_err("Region " + str(e) + " is  not found")


def do_login2(username=None, region=None):
    if region == None and username == None:
        do_fresh_login()
    elif region == None or username == None:
        if username == None:
            utils.log_err("You need to specify a username")
        elif region == None:
            login_check(username, DEFAULT_REGION)
    else:
        login_check(username, region)


def do_logout():
    if check_session():
        home = os.path.expanduser("~")
        os.remove("/tmp/session.pkl")
        os.remove(home + "/.neo.env")
        utils.log_info("Logout Success")


def dump_session(sess):
    try:
        with open("/tmp/session.pkl", "wb") as f:
            dill.dump(sess, f)
    except:
        utils.log_err("Dump session failed")


def load_dumped_session():
    try:
        if check_session():
            sess = None
            with open("/tmp/session.pkl", "rb") as f:
                sess = dill.load(f)
            return sess
        else:
            regenerate_sess()
            return load_dumped_session()
    except Exception as e:
        utils.log_err("Loading Session Failed")
        utils.log_err("Please login first")
        utils.log_err(e)


def check_session():
    return os.path.isfile("/tmp/session.pkl")
