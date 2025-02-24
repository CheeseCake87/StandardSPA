from flask_imp.config import FlaskConfig, ImpConfig, SQLiteDatabaseConfig

flask_config = FlaskConfig(
    secret_key="8163c469ec0182ff4d2ffce59a1488075098984883ca9cd6888",
)

imp_config = ImpConfig(
    database_main=SQLiteDatabaseConfig(),
    init_session={"auth": False}
)
