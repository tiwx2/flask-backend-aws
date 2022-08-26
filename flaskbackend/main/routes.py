from flaskbackend.main import bp

# a simple page that says hello


@bp.route('/')
def hello():
    return 'Hello, World! in project format!'
