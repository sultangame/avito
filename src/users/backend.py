from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend


cookie_transport = CookieTransport(cookie_max_age=3600)


SECRET = "SECRET"


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(lifetime_seconds=3600, secret=SECRET)


auth_backend = AuthenticationBackend(
    name="jwt",
    get_strategy=get_jwt_strategy,
    transport=cookie_transport
)
