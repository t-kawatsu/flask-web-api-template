"""
  主に flask xx コマンドから呼ばれる時用のモジュール
"""
from flask_web_api_template import create_app


app = create_app()

# migrate = Migrate(app, db)

# app_cli.init_app(app)
