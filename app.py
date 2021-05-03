"""
  主に flask xx コマンドから呼ばれる時用のモジュール
"""
from app_api import create_app


app = create_app()

# migrate = Migrate(app, db)

# app_cli.init_app(app)


def main():
    app.run(host='0.0.0.0')
