from huey import SqliteHuey, crontab
from websockets.sync.client import connect

from app.utilities.sys_print import sys_print_scheduler
from app.wsgi import create_app

main = create_app("scheduler")
huey = SqliteHuey(filename=main.instance_path + '/scheduler.sqlite')


@huey.task()
def manual_task():
    from app.wsgi.models.system_log import SystemLog

    with main.app_context():
        SystemLog.create(
            "scheduler",
            "sending websocket connection"
        )

    with connect("ws://127.0.0.1:5003") as websocket:
        websocket.send('Hello world!')
        sys_print_scheduler([
            "Sending websocket connection",
            "Sending: Hello world!",
        ])


@huey.periodic_task(crontab(minute='*/1'), expires=30)
def send_periodic():
    from app.wsgi.models.system_log import SystemLog

    with main.app_context():
        SystemLog.create(
            "scheduler",
            "periodic task"
        )

    with connect(f"ws://127.0.0.1:5003") as websocket:
        websocket.send('Hello world!')
        sys_print_scheduler([
            "Sending websocket connection",
            "Sending: Hello world!",
        ])
