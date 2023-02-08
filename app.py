from chalice import Chalice

app = Chalice(app_name='api_gateway_poc')


@app.route('/')
def index():
    return {'hello': 'world'}
